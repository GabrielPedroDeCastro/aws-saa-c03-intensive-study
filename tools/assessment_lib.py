#!/usr/bin/env python3
"""Shared grading and report helpers for the SAA-C03 assessment files."""

from __future__ import annotations

import json
import math
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


DOMAIN_WEIGHTS = {"D1": 30, "D2": 26, "D3": 24, "D4": 20}
DOMAIN_SHORT_NAMES = {
    "D1": "Segurança",
    "D2": "Resiliência",
    "D3": "Alto desempenho",
    "D4": "Custos",
}
VALID_ANSWERS = {"A", "B", "C", "D"}


@dataclass
class AnswerRecord:
    answer: str | None
    seconds: float | None = None


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Arquivo não encontrado: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"JSON inválido em {path}: linha {exc.lineno}, coluna {exc.colno}") from exc


def load_exam(path: Path) -> dict[str, Any]:
    payload = load_json(path)
    questions = payload.get("questoes")
    if not isinstance(questions, list) or not questions:
        raise SystemExit(f"{path} não contém uma lista não vazia em 'questoes'.")
    return payload


def normalize_answer(value: Any) -> str | None:
    if value is None:
        return None
    answer = str(value).strip().upper()
    if answer in {"", "-", "?", "S", "SKIP", "PULAR"}:
        return None
    if answer not in VALID_ANSWERS:
        raise ValueError(f"Resposta '{value}' não é A, B, C ou D.")
    return answer


def parse_answer_payload(payload: dict[str, Any]) -> tuple[dict[str, AnswerRecord], dict[str, Any]]:
    raw_answers = payload.get("answers", payload.get("respostas", payload))
    if not isinstance(raw_answers, dict):
        raise SystemExit("O arquivo de respostas deve conter um objeto 'answers' ou 'respostas'.")

    records: dict[str, AnswerRecord] = {}
    metadata = {key: value for key, value in payload.items() if key not in {"answers", "respostas"}}
    for question_id, raw in raw_answers.items():
        try:
            if isinstance(raw, dict):
                answer = normalize_answer(raw.get("answer", raw.get("resposta")))
                seconds_raw = raw.get("seconds", raw.get("tempo_segundos"))
                seconds = float(seconds_raw) if seconds_raw is not None else None
            else:
                answer = normalize_answer(raw)
                seconds = None
            if seconds is not None and (not math.isfinite(seconds) or seconds < 0):
                raise ValueError("tempo deve ser um número finito maior ou igual a zero")
        except (TypeError, ValueError) as exc:
            raise SystemExit(f"Resposta inválida para {question_id}: {exc}") from exc
        records[str(question_id)] = AnswerRecord(answer=answer, seconds=seconds)
    return records, metadata


def grade(exam: dict[str, Any], records: dict[str, AnswerRecord], metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    metadata = metadata or {}
    question_ids = {q["id"] for q in exam["questoes"]}
    unknown = sorted(set(records) - question_ids)
    if unknown:
        raise SystemExit("IDs de resposta ausentes no exame: " + ", ".join(unknown[:10]))

    results: list[dict[str, Any]] = []
    domain_stats: dict[str, dict[str, Any]] = defaultdict(
        lambda: {"total": 0, "correct": 0, "wrong": 0, "unanswered": 0, "seconds": 0.0, "timed": 0, "points": 0, "earned": 0}
    )
    topic_stats: dict[tuple[str, str], dict[str, Any]] = defaultdict(
        lambda: {"total": 0, "correct": 0, "wrong": 0, "unanswered": 0, "slow": 0.0, "reference": "", "lab": ""}
    )

    for question in exam["questoes"]:
        qid = question["id"]
        record = records.get(qid, AnswerRecord(None, None))
        correct_answer = question["resposta_correta"].upper()
        is_correct = record.answer == correct_answer
        is_unanswered = record.answer is None
        domain = question["codigo_dominio"]
        topic = question["topico"]
        points = int(question.get("pontos", 1))
        suggested = float(question.get("tempo_sugerido_segundos", 120))
        elapsed = record.seconds

        domain_row = domain_stats[domain]
        domain_row["total"] += 1
        domain_row["points"] += points
        if is_correct:
            domain_row["correct"] += 1
            domain_row["earned"] += points
        elif is_unanswered:
            domain_row["unanswered"] += 1
        else:
            domain_row["wrong"] += 1
        if elapsed is not None:
            domain_row["seconds"] += elapsed
            domain_row["timed"] += 1

        topic_row = topic_stats[(domain, topic)]
        topic_row["total"] += 1
        topic_row["reference"] = question.get("referencia_oficial", "")
        topic_row["lab"] = question.get("referencia_lab", "")
        if is_correct:
            topic_row["correct"] += 1
        elif is_unanswered:
            topic_row["unanswered"] += 1
        else:
            topic_row["wrong"] += 1
        if elapsed is not None and elapsed > suggested:
            topic_row["slow"] += min((elapsed - suggested) / max(suggested, 1.0), 2.0)

        results.append(
            {
                "id": qid,
                "domain": domain,
                "topic": topic,
                "answer": record.answer,
                "correct_answer": correct_answer,
                "is_correct": is_correct,
                "is_unanswered": is_unanswered,
                "seconds": elapsed,
                "suggested_seconds": suggested,
                "points": points,
                "earned": points if is_correct else 0,
                "question": question,
            }
        )

    total = len(results)
    correct = sum(row["is_correct"] for row in results)
    unanswered = sum(row["is_unanswered"] for row in results)
    wrong = total - correct - unanswered
    total_points = sum(row["points"] for row in results)
    earned = sum(row["earned"] for row in results)
    timed = [row["seconds"] for row in results if row["seconds"] is not None]
    supplied_duration_raw = metadata.get("duration_seconds", metadata.get("duracao_segundos"))
    wall_duration_raw = metadata.get("wall_seconds", metadata.get("tempo_sessao_segundos"))

    def parse_duration(raw: Any, label: str) -> float | None:
        if raw is None:
            return None
        try:
            value = float(raw)
        except (TypeError, ValueError) as exc:
            raise SystemExit(f"{label} deve ser numérico.") from exc
        if not math.isfinite(value) or value < 0:
            raise SystemExit(f"{label} deve ser finito e maior ou igual a zero.")
        return value

    supplied_duration = parse_duration(supplied_duration_raw, "A duração total")
    wall_duration = parse_duration(wall_duration_raw, "O tempo total da sessão")
    if timed:
        total_seconds = sum(timed)
        timed_count = len(timed)
    elif supplied_duration is not None:
        total_seconds = supplied_duration
        timed_count = len(records)
    elif wall_duration is not None:
        total_seconds = wall_duration
        timed_count = len(records)
    else:
        total_seconds = 0.0
        timed_count = 0
    average_seconds = round(total_seconds / timed_count, 1) if timed_count else None
    session_seconds = wall_duration if wall_duration is not None else supplied_duration

    priorities = []
    for (domain, topic), row in topic_stats.items():
        accuracy = (row["correct"] / row["total"] * 100) if row["total"] else 0.0
        priority_score = (
            row["wrong"] * 5
            + row["unanswered"] * 6
            + row["slow"]
            + DOMAIN_WEIGHTS.get(domain, 0) / 20
            + (2 if accuracy < 60 else 0)
        )
        if row["wrong"] or row["unanswered"] or row["slow"] > 0:
            priorities.append(
                {
                    "domain": domain,
                    "topic": topic,
                    "accuracy": round(accuracy, 1),
                    "wrong": row["wrong"],
                    "unanswered": row["unanswered"],
                    "slow_penalty": round(row["slow"], 2),
                    "priority_score": round(priority_score, 2),
                    "reference": row["reference"],
                    "lab": row["lab"],
                }
            )
    priorities.sort(key=lambda row: (-row["priority_score"], row["accuracy"], row["domain"], row["topic"]))

    domains = {}
    for code in sorted(domain_stats):
        row = domain_stats[code]
        domains[code] = {
            **row,
            "accuracy": round(row["correct"] / row["total"] * 100, 1) if row["total"] else 0.0,
            "average_seconds": round(row["seconds"] / row["timed"], 1) if row["timed"] else None,
        }

    return {
        "exam_id": exam.get("id", "assessment"),
        "exam_title": exam.get("titulo", exam.get("id", "Avaliação")),
        "candidate": metadata.get("candidate", metadata.get("candidato", "não informado")),
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "summary": {
            "total": total,
            "correct": correct,
            "wrong": wrong,
            "unanswered": unanswered,
            "accuracy": round(correct / total * 100, 1),
            "points": earned,
            "total_points": total_points,
            "score_percent": round(earned / total_points * 100, 1) if total_points else 0.0,
            "total_seconds": round(total_seconds, 1),
            "average_seconds": average_seconds,
            "timed_count": timed_count,
            "wall_seconds": round(session_seconds, 1) if session_seconds is not None else None,
        },
        "domains": domains,
        "priorities": priorities[:10],
        "results": results,
    }


def _seconds(value: float | None) -> str:
    if value is None:
        return "não medido"
    minutes, seconds = divmod(int(round(value)), 60)
    return f"{minutes}m {seconds:02d}s" if minutes else f"{seconds}s"


def _safe_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_report(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        f"# Relatório - {report['exam_title']}",
        "",
        f"- **Candidato:** {report['candidate']}",
        f"- **Gerado em:** {report['generated_at']}",
        f"- **Resultado:** {summary['correct']}/{summary['total']} ({summary['accuracy']}%)",
        f"- **Pontos:** {summary['points']}/{summary['total_points']} ({summary['score_percent']}%)",
        f"- **Tempo de resposta registrado:** {_seconds(summary['total_seconds'])}; média {_seconds(summary['average_seconds'])} "
        f"em {summary['timed_count']} questão(ões) medida(s)",
        "",
        "> Este percentual é uma métrica de estudo, não uma conversão da escala oficial de 100 a 1.000 pontos.",
        "",
        "## Desempenho por domínio",
        "",
        "| Domínio | Peso | Acertos | Erros | Em branco | Percentual | Tempo médio |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    if summary.get("wall_seconds") is not None and summary["wall_seconds"] != summary["total_seconds"]:
        lines.insert(7, f"- **Tempo total da sessão:** {_seconds(summary['wall_seconds'])} (inclui leitura do feedback)")

    for code in ("D1", "D2", "D3", "D4"):
        row = report["domains"].get(
            code,
            {"total": 0, "correct": 0, "wrong": 0, "unanswered": 0, "accuracy": 0.0, "average_seconds": None},
        )
        lines.append(
            f"| {code} - {DOMAIN_SHORT_NAMES[code]} | {DOMAIN_WEIGHTS[code]}% | "
            f"{row['correct']}/{row['total']} | {row['wrong']} | {row['unanswered']} | "
            f"{row['accuracy']}% | {_seconds(row['average_seconds'])} |"
        )

    lines.extend(
        [
            "",
            "## Plano de revisão - top 10",
            "",
            "A prioridade combina erro, questão em branco, lentidão e peso oficial do domínio.",
            "",
            "| # | Domínio | Tópico | Acerto | Erros/brancos | Ação recomendada |",
            "|---:|---|---|---:|---:|---|",
        ]
    )
    if report["priorities"]:
        for index, item in enumerate(report["priorities"], start=1):
            action = item["lab"] or item["reference"] or "Revisar guia e resolver cinco novas questões."
            lines.append(
                f"| {index} | {item['domain']} | {_safe_cell(item['topic'])} | {item['accuracy']}% | "
                f"{item['wrong']}/{item['unanswered']} | {_safe_cell(action)} |"
            )
    else:
        lines.append("| - | - | Nenhuma fraqueza detectada nesta tentativa | - | - | Mantenha revisão espaçada |")

    lines.extend(["", "## Feedback por questão", ""])
    for result in report["results"]:
        question = result["question"]
        status = "✅ Acerto" if result["is_correct"] else ("⬜ Em branco" if result["is_unanswered"] else "❌ Erro")
        user_answer = result["answer"] or "não respondida"
        lines.extend(
            [
                f"### {result['id']} - {status}",
                "",
                f"**Tópico:** {question['topico']} · **Sua resposta:** {user_answer} · "
                f"**Correta:** {result['correct_answer']} · **Tempo:** {_seconds(result['seconds'])} "
                f"(sugerido: {_seconds(result['suggested_seconds'])})",
                "",
                f"**Pergunta.** {question['enunciado']}",
                "",
                question["feedback_acerto"] if result["is_correct"] else question["feedback_erro"],
                "",
            ]
        )
        if result["answer"]:
            choice_label = "Por que sua escolha funcionou" if result["is_correct"] else "Diagnóstico da sua escolha"
            lines.extend(
                [
                    f"**{choice_label}.** Você marcou {result['answer']}: "
                    f"{question['explicacao_alternativas'][result['answer']]}",
                    "",
                ]
            )
        lines.extend(
            [
                f"**Explicação técnica.** {question['explicacao_tecnica']}",
                "",
                f"**Como criança.** {question['explicacao_crianca']}",
                "",
                "**Alternativas.**",
                "",
            ]
        )
        for letter in ("A", "B", "C", "D"):
            lines.append(
                f"- **{letter}) {question['alternativas'][letter]}** — {question['explicacao_alternativas'][letter]}"
            )
        lines.extend(
            [
                "",
                f"**Referência oficial:** {question['referencia_oficial']}",
                "",
                f"**Lab relacionado:** {question['referencia_lab']}",
                "",
                f"**Exercício recomendado:** {question['exercicio_recomendado']}",
                "",
            ]
        )

    next_step = (
        "Refaça as questões erradas sem olhar o gabarito em D+1, execute o checkpoint do primeiro tópico prioritário e repita uma bateria curta em D+3 e D+7."
        if report["priorities"]
        else "Nenhuma fraqueza foi detectada nesta tentativa. Mantenha a revisão espaçada e confirme o desempenho com novas questões e outro simulado cronometrado."
    )
    lines.extend(["## Próximo passo", "", next_step, ""])
    return "\n".join(lines)


def serializable_report(report: dict[str, Any]) -> dict[str, Any]:
    """Return the full machine-readable report, including per-question feedback."""
    return report


def validate_output_paths(markdown_path: Path, json_path: Path) -> None:
    if markdown_path.suffix.lower() != ".md":
        raise SystemExit("O relatório principal deve usar extensão .md.")
    if json_path.suffix.lower() != ".json":
        raise SystemExit("O resumo estruturado deve usar extensão .json.")
    if markdown_path.resolve() == json_path.resolve():
        raise SystemExit("Os caminhos de saída Markdown e JSON precisam ser diferentes.")


def write_report(report: dict[str, Any], markdown_path: Path, json_path: Path | None = None) -> None:
    if json_path:
        validate_output_paths(markdown_path, json_path)
    elif markdown_path.suffix.lower() != ".md":
        raise SystemExit("O relatório principal deve usar extensão .md.")
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_report(report), encoding="utf-8")
    if json_path:
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(
            json.dumps(serializable_report(report), ensure_ascii=False, indent=2, allow_nan=False) + "\n",
            encoding="utf-8",
        )
