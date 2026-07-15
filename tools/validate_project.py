#!/usr/bin/env python3
"""Validate the repository acceptance criteria without contacting AWS."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LETTERS = {"A", "B", "C", "D"}
DOMAIN_WEIGHTS = {"D1": 30, "D2": 26, "D3": 24, "D4": 20}
REQUIRED_DIRS = ["labs", "iac", "quizzes", "simulados", "diagrams", "flashcards", "reports"]
REQUIRED_QUESTION_FIELDS = {
    "id",
    "dominio",
    "codigo_dominio",
    "topico",
    "dificuldade",
    "tempo_sugerido_segundos",
    "pontos",
    "enunciado",
    "alternativas",
    "resposta_correta",
    "explicacao_tecnica",
    "explicacao_crianca",
    "feedback_acerto",
    "feedback_erro",
    "explicacao_alternativas",
    "referencia_oficial",
    "referencia_lab",
    "exercicio_recomendado",
}


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checks = 0

    def require(self, condition: bool, message: str) -> None:
        self.checks += 1
        if not condition:
            self.errors.append(message)

    def warn(self, condition: bool, message: str) -> None:
        if not condition:
            self.warnings.append(message)


def read_json(path: Path, validation: Validation) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - aggregate all validation failures
        validation.errors.append(f"JSON inválido em {path.relative_to(ROOT)}: {exc}")
        return {}


def validate_question(question: dict[str, Any], source: Path, validation: Validation) -> None:
    label = f"{source.relative_to(ROOT)}:{question.get('id', '?')}"
    missing = REQUIRED_QUESTION_FIELDS - set(question)
    validation.require(not missing, f"{label} sem campos: {sorted(missing)}")
    if missing:
        return
    alternatives = question["alternativas"]
    explanations = question["explicacao_alternativas"]
    validation.require(isinstance(alternatives, dict) and set(alternatives) == LETTERS, f"{label} deve ter A-D")
    validation.require(isinstance(explanations, dict) and set(explanations) == LETTERS, f"{label} sem explicações A-D")
    validation.require(question["resposta_correta"] in LETTERS, f"{label} com gabarito inválido")
    validation.require(question["codigo_dominio"] in DOMAIN_WEIGHTS, f"{label} com domínio inválido")
    validation.require(question["dificuldade"] in {"fácil", "média", "difícil"}, f"{label} com dificuldade inválida")
    validation.require(float(question["tempo_sugerido_segundos"]) > 0, f"{label} sem tempo positivo")
    validation.require(float(question["pontos"]) > 0, f"{label} sem pontos positivos")
    for field in (
        "enunciado",
        "explicacao_tecnica",
        "explicacao_crianca",
        "feedback_acerto",
        "feedback_erro",
        "referencia_oficial",
        "referencia_lab",
        "exercicio_recomendado",
    ):
        validation.require(bool(str(question[field]).strip()), f"{label} com '{field}' vazio")
    validation.require(
        str(question["referencia_oficial"]).startswith("https://"),
        f"{label} precisa de referência oficial HTTPS",
    )


def assessment(path: Path, expected_count: int, validation: Validation) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    payload = read_json(path, validation)
    questions = payload.get("questoes", [])
    validation.require(isinstance(questions, list), f"{path.relative_to(ROOT)} sem lista 'questoes'")
    if not isinstance(questions, list):
        return payload, []
    validation.require(len(questions) == expected_count, f"{path.relative_to(ROOT)}: esperado {expected_count}, obtido {len(questions)}")
    validation.require(payload.get("quantidade_questoes") == len(questions), f"{path.relative_to(ROOT)} com metadado de contagem incorreto")
    ids = [q.get("id") for q in questions]
    validation.require(len(ids) == len(set(ids)), f"{path.relative_to(ROOT)} contém IDs duplicados")
    for question in questions:
        validate_question(question, path, validation)
    answers = Counter(q.get("resposta_correta") for q in questions)
    if expected_count >= 10 and answers:
        validation.warn(max(answers.values()) - min(answers.values()) <= 2, f"Gabarito desequilibrado em {path.relative_to(ROOT)}: {dict(answers)}")
    validation.require(path.with_suffix(".md").exists(), f"Falta par Markdown de {path.relative_to(ROOT)}")
    return payload, questions


def validate_structure(validation: Validation) -> list[str]:
    validation.require((ROOT / "README.md").exists(), "README.md ausente")
    validation.require((ROOT / "GUIA-DE-ESTUDOS.md").exists(), "Guia Markdown ausente")
    validation.require((ROOT / "docs" / "index.html").exists(), "Landing page HTML ausente")
    for directory in REQUIRED_DIRS:
        validation.require((ROOT / directory).is_dir(), f"Diretório obrigatório ausente: {directory}")
    topics = read_json(ROOT / "content" / "topics.json", validation)
    domains = topics.get("domains", [])
    validation.require(len(domains) == 4, "topics.json deve conter quatro domínios")
    weights = {d.get("id"): d.get("weight") for d in domains}
    validation.require(weights == DOMAIN_WEIGHTS, f"Pesos de domínios incorretos: {weights}")
    topic_count = sum(len(d.get("topics", [])) for d in domains)
    validation.require(topic_count >= 20, f"Guia tem somente {topic_count} tópicos completos")
    for domain in domains:
        for topic in domain.get("topics", []):
            for field in ("technical", "child", "when", "limits", "cost", "practices", "traps", "links"):
                validation.require(bool(topic.get(field)), f"{domain.get('id')}/{topic.get('title')} sem {field}")
    return [d.get("id") for d in domains]


def validate_labs(validation: Validation) -> list[str]:
    labs = sorted(path for path in (ROOT / "labs").iterdir() if path.is_dir())
    validation.require(len(labs) >= 8, f"Esperados 8 labs; encontrados {len(labs)}")
    required_words = ["objetivo", "pré-requisitos", "custo", "console", "cli", "cloudformation", "terraform", "output", "checkpoint", "cleanup"]
    for lab in labs:
        readme = lab / "README.md"
        validation.require(readme.exists(), f"{lab.name} sem README.md")
        content = readme.read_text(encoding="utf-8").lower() if readme.exists() else ""
        for word in required_words:
            validation.require(word in content, f"{lab.name}/README.md não menciona '{word}'")
        iac_dir = ROOT / "iac" / lab.name
        cfn = list((iac_dir / "cloudformation").glob("*.y*ml")) if iac_dir.exists() else []
        terraform = list((iac_dir / "terraform").glob("*.tf")) if iac_dir.exists() else []
        validation.require(bool(cfn), f"{lab.name} sem CloudFormation YAML")
        validation.require(bool(terraform), f"{lab.name} sem Terraform HCL")
        for template in cfn:
            text = template.read_text(encoding="utf-8")
            validation.require("Resources:" in text, f"{template.relative_to(ROOT)} sem Resources")
            validation.require("Outputs:" in text, f"{template.relative_to(ROOT)} sem Outputs")
        for tf in terraform:
            text = tf.read_text(encoding="utf-8")
            validation.require("AKIA" not in text, f"Possível access key em {tf.relative_to(ROOT)}")
        diagram_candidates = list((ROOT / "diagrams").glob(f"{lab.name}*")) + list((ROOT / "diagrams" / lab.name).glob("*"))
        suffixes = {path.suffix.lower() for path in diagram_candidates if path.is_file()}
        validation.require(bool(suffixes & {".mmd", ".mermaid", ".md"}), f"{lab.name} sem diagrama como código")
        validation.require(bool(suffixes & {".svg", ".png"}), f"{lab.name} sem diagrama SVG/PNG")
    return [lab.name for lab in labs]


def validate_assessments(validation: Validation) -> dict[str, int]:
    canonical_ids: list[str] = []
    stems: list[str] = []
    quiz_files = sorted((ROOT / "quizzes").glob("dominio-*/quiz-??.json"))
    validation.require(len(quiz_files) == 40, f"Esperados 40 mini-quizzes; encontrados {len(quiz_files)}")
    quiz_domains = Counter()
    quiz_questions = 0
    for path in quiz_files:
        _, questions = assessment(path, 5, validation)
        quiz_questions += len(questions)
        if questions:
            quiz_domains[questions[0].get("codigo_dominio")] += 1
        canonical_ids.extend(q.get("id", "") for q in questions)
        stems.extend(q.get("enunciado", "") for q in questions)
    validation.require(quiz_questions >= 200, f"Banco de mini-quizzes tem {quiz_questions}, esperado >= 200")
    validation.require(quiz_domains == Counter({"D1": 10, "D2": 10, "D3": 10, "D4": 10}), f"Mini-quizzes por domínio: {dict(quiz_domains)}")

    _, day1 = assessment(ROOT / "quizzes" / "dia-01-10.json", 10, validation)
    _, diagnostic = assessment(ROOT / "simulados" / "diagnostico-40.json", 40, validation)
    canonical_ids.extend(q.get("id", "") for q in diagnostic)
    stems.extend(q.get("enunciado", "") for q in diagnostic)

    mock_files = sorted((ROOT / "simulados").glob("simulado-??-65.json"))
    validation.require(len(mock_files) == 3, f"Esperados 3 simulados completos; encontrados {len(mock_files)}")
    mock_questions = 0
    for path in mock_files:
        _, questions = assessment(path, 65, validation)
        mock_questions += len(questions)
        domains = Counter(q.get("codigo_dominio") for q in questions)
        validation.require(domains == Counter({"D1": 20, "D2": 17, "D3": 15, "D4": 13}), f"Distribuição incorreta em {path.name}: {dict(domains)}")
        canonical_ids.extend(q.get("id", "") for q in questions)
        stems.extend(q.get("enunciado", "") for q in questions)
    validation.require(len(canonical_ids) == len(set(canonical_ids)), "IDs duplicados entre avaliações canônicas")
    duplicates = len(stems) - len(set(stems))
    validation.warn(duplicates == 0, f"Há {duplicates} enunciados idênticos entre avaliações")

    flashcards = read_json(ROOT / "flashcards" / "flashcards.json", validation)
    cards = flashcards.get("cards", [])
    validation.require(len(cards) >= 200, f"Esperados >= 200 flashcards; encontrados {len(cards)}")
    validation.require(len({card.get('id') for card in cards}) == len(cards), "IDs de flashcards duplicados")
    for card in cards:
        for field in ("id", "codigo_dominio", "topico", "frente", "verso_tecnico", "verso_crianca", "pegadinha_de_prova", "referencia_oficial"):
            validation.require(bool(card.get(field)), f"Flashcard {card.get('id')} sem {field}")
    validation.require((ROOT / "flashcards" / "flashcards.md").exists(), "Flashcards Markdown ausentes")
    return {"mini_quizzes": quiz_questions, "day1": len(day1), "diagnostic": len(diagnostic), "mocks": mock_questions, "flashcards": len(cards)}


def validate_support(validation: Validation) -> None:
    for path in (
        "schedules/4-SEMANAS.md",
        "schedules/2-SEMANAS.md",
        "schedules/BOOTCAMP.md",
        "schedules/DIA-01.md",
        "reports/CHECKLIST-FINAL.md",
        "references/SOURCES.md",
        "tools/quiz_runner.py",
        "tools/grade_answers.py",
        "tools/test_assessment_lib.py",
        "tools/test_site.py",
        "site/index.template.html",
        "site/styles.css",
        "site/app.js",
        "site/og.png",
        "docs/assets/styles.css",
        "docs/assets/app.js",
        "docs/assets/og.png",
        "docs/data/site-data.json",
        "docs/.nojekyll",
        ".github/workflows/validate.yml",
        ".github/workflows/pages.yml",
    ):
        validation.require((ROOT / path).exists(), f"Arquivo obrigatório ausente: {path}")
    sources = (ROOT / "references" / "SOURCES.md").read_text(encoding="utf-8") if (ROOT / "references" / "SOURCES.md").exists() else ""
    provider_markers = ["Tutorials Dojo", "Udemy", "Digital Cloud", "MeasureUp", "ExamPro", "Pluralsight"]
    validation.require(sum(marker in sources for marker in provider_markers) >= 6, "SOURCES.md não avalia seis simulados externos")

    secret_patterns = [
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile(r"(?i)aws_secret_access_key\s*[=:]\s*['\"]?[A-Za-z0-9/+=]{30,}"),
    ]
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "tmp" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".tf", ".tfvars", ".example", ".py", ".ps1", ".sh", ".html"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in secret_patterns:
            validation.require(not pattern.search(text), f"Possível segredo em {path.relative_to(ROOT)}")


def validate_internal_links(validation: Validation) -> None:
    markdown_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    html_pattern = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
    for source in ROOT.rglob("*"):
        if not source.is_file() or ".git" in source.parts or "tmp" in source.parts:
            continue
        if source.suffix.lower() not in {".md", ".html"}:
            continue
        if source.name.endswith(".template.html"):
            # Template URLs are resolved relative to the generated docs/ output.
            continue
        text = source.read_text(encoding="utf-8")
        targets = markdown_pattern.findall(text) if source.suffix.lower() == ".md" else html_pattern.findall(text)
        for raw_target in targets:
            target = raw_target.strip().strip("<>")
            if not target or target.startswith("#"):
                continue
            if re.match(r"^(?:https?|mailto|data|javascript):", target, re.IGNORECASE):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (source.parent / unquote(target)).resolve()
            validation.require(
                resolved.exists(),
                f"Link interno quebrado em {source.relative_to(ROOT)}: {raw_target}",
            )


def main() -> None:
    validation = Validation()
    validate_structure(validation)
    labs = validate_labs(validation)
    counts = validate_assessments(validation)
    validate_support(validation)
    validate_internal_links(validation)

    print(f"Checks executados: {validation.checks}")
    print(f"Labs: {len(labs)} · mini-quizzes: {counts.get('mini_quizzes', 0)} · diagnóstico: {counts.get('diagnostic', 0)}")
    print(f"Simulados: {counts.get('mocks', 0)} questões · flashcards: {counts.get('flashcards', 0)}")
    if validation.warnings:
        print("\nAvisos:")
        for warning in validation.warnings:
            print(f"  - {warning}")
    if validation.errors:
        print("\nFalhas:")
        for error in validation.errors:
            print(f"  - {error}")
        raise SystemExit(1)
    print("\nVALIDAÇÃO OK — critérios de aceitação atendidos.")


if __name__ == "__main__":
    main()
