#!/usr/bin/env python3
"""Validação estrutural e cruzada dos artefatos avaliativos materializados."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LETTERS = ["A", "B", "C", "D"]
REQUIRED = {
    "id", "tipo", "dominio", "codigo_dominio", "topico", "dificuldade",
    "tempo_sugerido_segundos", "pontos", "enunciado", "alternativas",
    "resposta_correta", "explicacao_tecnica", "explicacao_crianca",
    "feedback_acerto", "feedback_erro", "explicacao_alternativas",
    "referencia_oficial", "referencia_lab", "exercicio_recomendado", "origem",
}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_question(q, source):
    missing = REQUIRED - set(q)
    assert not missing, f"{source}: {q.get('id')} sem {sorted(missing)}"
    assert list(q["alternativas"]) == LETTERS, f"{q['id']}: alternativas"
    assert list(q["explicacao_alternativas"]) == LETTERS, f"{q['id']}: explicações A-D"
    assert q["resposta_correta"] in LETTERS, f"{q['id']}: gabarito"
    assert len(set(q["alternativas"].values())) == 4, f"{q['id']}: opções repetidas"
    assert q["dificuldade"] in {"fácil", "média", "difícil"}
    assert q["tempo_sugerido_segundos"] in {90, 110, 130}
    assert q["pontos"] in {1, 2, 3}
    assert "\n\n" in q["explicacao_tecnica"], f"{q['id']}: explicação técnica sem duas camadas"
    assert len(q["explicacao_crianca"]) >= 40, f"{q['id']}: analogia curta"
    assert q["referencia_oficial"].startswith("https://docs.aws.amazon.com/"), f"{q['id']}: referência não oficial"
    for field in ("feedback_acerto", "feedback_erro", "referencia_lab", "exercicio_recomendado"):
        assert str(q[field]).strip(), f"{q['id']}: {field} vazio"
    for letter in LETTERS:
        prefix = "Correta" if letter == q["resposta_correta"] else "Incorreta"
        assert q["explicacao_alternativas"][letter].startswith(prefix), f"{q['id']}: rótulo {letter}"


def check_assessment_pair(json_path, expected):
    md_path = json_path.with_suffix(".md")
    assert md_path.exists(), f"Markdown ausente para {json_path}"
    data = load(json_path)
    questions = data["questoes"]
    assert len(questions) == data["quantidade_questoes"] == expected, json_path
    md = md_path.read_text(encoding="utf-8")
    for q in questions:
        check_question(q, json_path)
        assert f"`{q['id']}`" in md, f"{q['id']} não aparece no Markdown"
    actual_answers = dict(sorted(Counter(q["resposta_correta"] for q in questions).items()))
    actual_domains = dict(sorted(Counter(q["codigo_dominio"] for q in questions).items()))
    assert actual_answers == data["distribuicao_gabarito"], json_path
    assert actual_domains == data["distribuicao_dominios"], json_path
    return data


def main():
    quizzes_root = ROOT / "quizzes"
    quiz_files = sorted(quizzes_root.glob("dominio-*/quiz-??.json"))
    assert len(quiz_files) == 40, f"mini-quizzes: {len(quiz_files)}"
    individual_questions = []
    for path in quiz_files:
        individual_questions.extend(check_assessment_pair(path, 5)["questoes"])
    assert len(individual_questions) == 200
    assert len({q["id"] for q in individual_questions}) == 200

    bank = check_assessment_pair(quizzes_root / "banco-200.json", 200)
    assert [q["id"] for q in bank["questoes"]] == [q["id"] for q in individual_questions]

    day1 = check_assessment_pair(quizzes_root / "dia-01-10.json", 10)
    assert {q["id"] for q in day1["questoes"]}.isdisjoint(q["id"] for q in individual_questions)

    diagnostic = check_assessment_pair(ROOT / "simulados" / "diagnostico-40.json", 40)
    assert diagnostic["distribuicao_dominios"] == {"D1": 12, "D2": 10, "D3": 10, "D4": 8}
    exams = []
    for number in range(1, 4):
        exam = check_assessment_pair(ROOT / "simulados" / f"simulado-{number:02d}-65.json", 65)
        assert exam["distribuicao_dominios"] == {"D1": 20, "D2": 17, "D3": 15, "D4": 13}
        counts = list(exam["distribuicao_gabarito"].values())
        assert max(counts) - min(counts) <= 1, f"simulado {number}: gabarito não balanceado"
        exams.append(exam)

    canonical = individual_questions + day1["questoes"] + diagnostic["questoes"]
    for exam in exams:
        canonical.extend(exam["questoes"])
    assert len(canonical) == 445
    assert len({q["id"] for q in canonical}) == 445
    assert len({q["enunciado"] for q in canonical}) == 445, "há enunciados idênticos"

    flash = load(ROOT / "flashcards" / "flashcards.json")
    assert flash["quantidade"] == len(flash["cards"]) >= 200
    assert len({c["id"] for c in flash["cards"]}) == len(flash["cards"])
    assert (ROOT / "flashcards" / "flashcards.md").exists()
    for card in flash["cards"]:
        for field in (
            "id", "dominio", "codigo_dominio", "topico", "frente", "verso_tecnico",
            "verso_crianca", "pegadinha_de_prova", "referencia_oficial", "referencia_lab",
        ):
            assert str(card[field]).strip(), f"{card.get('id')}: {field} vazio"

    answer_counts = dict(sorted(Counter(q["resposta_correta"] for q in canonical).items()))
    difficulty_counts = dict(sorted(Counter(q["dificuldade"] for q in canonical).items()))
    report = {
        "status": "OK",
        "arquivos_mini_quiz_json": 40,
        "arquivos_mini_quiz_markdown": 40,
        "questoes_mini_quizzes": 200,
        "questoes_dia_01": 10,
        "questoes_diagnostico": 40,
        "simulados_completos": 3,
        "questoes_simulados_completos": 195,
        "questoes_canonicas": len(canonical),
        "flashcards": len(flash["cards"]),
        "gabarito": answer_counts,
        "dificuldade": difficulty_counts,
        "enunciados_unicos": len({q["enunciado"] for q in canonical}),
        "ids_unicos": len({q["id"] for q in canonical}),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
