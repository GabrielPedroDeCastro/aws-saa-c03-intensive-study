#!/usr/bin/env python3
"""Grade a JSON answer file and generate domain-level Markdown/JSON reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from assessment_lib import grade, load_exam, load_json, parse_answer_payload, write_report


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Corrige respostas e gera relatório por domínio.")
    parser.add_argument("--exam", required=True, type=Path, help="Avaliação JSON em simulados/ ou quizzes/.")
    parser.add_argument("--answers", required=True, type=Path, help="JSON com objeto answers/respostas.")
    parser.add_argument("--output", required=True, type=Path, help="Relatório Markdown de saída.")
    parser.add_argument("--json-output", type=Path, help="Resumo JSON; padrão: mesmo nome do Markdown.")
    return parser.parse_args()


def main() -> None:
    args = arguments()
    exam = load_exam(args.exam)
    answers_payload = load_json(args.answers)
    records, metadata = parse_answer_payload(answers_payload)
    report = grade(exam, records, metadata)
    json_output = args.json_output or args.output.with_suffix(".json")
    write_report(report, args.output, json_output)
    summary = report["summary"]
    print(
        f"Resultado: {summary['correct']}/{summary['total']} ({summary['accuracy']}%). "
        f"Relatórios: {args.output} e {json_output}"
    )


if __name__ == "__main__":
    main()
