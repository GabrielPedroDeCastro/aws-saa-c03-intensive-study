#!/usr/bin/env python3
"""Interactive assessment runner with configurable detailed feedback."""

from __future__ import annotations

import argparse
import json
import random
import time
from datetime import datetime
from pathlib import Path

from assessment_lib import AnswerRecord, grade, load_exam, write_report


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Executa quiz/simulado com feedback imediato.")
    parser.add_argument("exam", type=Path, help="Arquivo JSON da avaliação.")
    parser.add_argument("--candidate", default="não informado", help="Nome ou apelido para o relatório.")
    parser.add_argument("--output", type=Path, help="Caminho do relatório Markdown.")
    parser.add_argument("--shuffle", action="store_true", help="Embaralha a ordem das questões.")
    feedback = parser.add_mutually_exclusive_group()
    feedback.add_argument("--immediate-feedback", dest="immediate_feedback", action="store_true", help="Mostra feedback após cada resposta.")
    feedback.add_argument("--no-immediate-feedback", dest="immediate_feedback", action="store_false", help="Oculta feedback até o relatório final.")
    parser.set_defaults(immediate_feedback=None)
    return parser.parse_args()


def ask(question: dict) -> AnswerRecord:
    print("\n" + "=" * 78)
    print(f"{question['id']} · {question['codigo_dominio']} · {question['dificuldade']} · "
          f"{question['tempo_sugerido_segundos']} s · {question['pontos']} ponto(s)")
    print("\n" + question["enunciado"] + "\n")
    for letter in ("A", "B", "C", "D"):
        print(f"  {letter}) {question['alternativas'][letter]}")
    started = time.monotonic()
    while True:
        value = input("\nResposta [A-D] ou P para pular: ").strip().upper()
        if value in {"A", "B", "C", "D"}:
            return AnswerRecord(value, round(time.monotonic() - started, 1))
        if value in {"P", "S", "SKIP", "PULAR", ""}:
            return AnswerRecord(None, round(time.monotonic() - started, 1))
        print("Digite A, B, C, D ou P.")


def show_feedback(question: dict, record: AnswerRecord) -> None:
    correct = question["resposta_correta"]
    hit = record.answer == correct
    print("\n" + ("✅ ACERTOU" if hit else f"❌ RESPOSTA CORRETA: {correct}"))
    print("\n" + (question["feedback_acerto"] if hit else question["feedback_erro"]))
    if record.answer:
        label = "Por que sua escolha funcionou" if hit else "Diagnóstico da sua escolha"
        print(f"\n{label}: você marcou {record.answer}: " + question["explicacao_alternativas"][record.answer])
    print("\nTécnico: " + question["explicacao_tecnica"])
    print("\nComo criança: " + question["explicacao_crianca"])
    print("\nPor alternativa:")
    for letter in ("A", "B", "C", "D"):
        print(f"  {letter}: {question['explicacao_alternativas'][letter]}")
    print("\nReferência: " + question["referencia_oficial"])
    print("Lab: " + question["referencia_lab"])
    print("Exercício: " + question["exercicio_recomendado"])


def main() -> None:
    args = arguments()
    exam = load_exam(args.exam)
    questions = list(exam["questoes"])
    immediate_feedback = args.immediate_feedback if args.immediate_feedback is not None else len(questions) <= 10
    if args.shuffle:
        random.SystemRandom().shuffle(questions)

    print(f"\n{exam.get('titulo', exam.get('id', 'Avaliação'))}")
    print(f"{len(questions)} questões · digite Ctrl+C para encerrar e salvar o progresso.")
    print("Feedback imediato " + ("ativado." if immediate_feedback else "adiado para preservar a medição; consulte o relatório final."))
    records: dict[str, AnswerRecord] = {}
    started = time.monotonic()
    try:
        for question in questions:
            record = ask(question)
            records[question["id"]] = record
            if immediate_feedback:
                show_feedback(question, record)
    except (KeyboardInterrupt, EOFError):
        print("\nAvaliação interrompida; o progresso respondido será salvo.")

    duration = round(time.monotonic() - started, 1)
    metadata = {"candidate": args.candidate, "wall_seconds": duration}
    report = grade(exam, records, metadata)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output = args.output or Path("reports") / f"{exam.get('id', 'assessment').lower()}-{stamp}.md"
    json_output = output.with_suffix(".json")
    write_report(report, output, json_output)

    answer_output = output.with_name(output.stem + "-answers.json")
    answer_output.write_text(
        json.dumps(
            {
                "candidate": args.candidate,
                "exam": exam.get("id"),
                "wall_seconds": duration,
                "answers": {
                    qid: {"answer": record.answer, "seconds": record.seconds}
                    for qid, record in records.items()
                },
            },
            ensure_ascii=False,
            indent=2,
            allow_nan=False,
        )
        + "\n",
        encoding="utf-8",
    )
    summary = report["summary"]
    print(f"\nResultado: {summary['correct']}/{summary['total']} ({summary['accuracy']}%).")
    print(f"Relatório: {output}\nRespostas: {answer_output}")


if __name__ == "__main__":
    main()
