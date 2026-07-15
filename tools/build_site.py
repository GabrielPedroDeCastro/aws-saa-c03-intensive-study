#!/usr/bin/env python3
"""Build the study guide and the static GitHub Pages learning portal."""

from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPICS_SOURCE = ROOT / "content" / "topics.json"
QUIZ_SOURCE = ROOT / "quizzes" / "dia-01-10.json"
MARKDOWN = ROOT / "GUIA-DE-ESTUDOS.md"
SITE_SOURCE = ROOT / "site"
DOCS = ROOT / "docs"
REPOSITORY_URL = "https://github.com/GabrielPedroDeCastro/aws-saa-c03-intensive-study"
SITE_URL = "https://gabrielpedrodecastro.github.io/aws-saa-c03-intensive-study/"

LABS = [
    {
        "id": "lab-01",
        "number": "01",
        "title": "VPC multi-AZ + NAT",
        "domain": "D2",
        "minutes": 90,
        "cost": "Atenção",
        "summary": "Subnets públicas e privadas em duas AZs, rotas, NAT zonal e endpoint S3.",
        "diagram": "01-vpc-multi-az-nat.svg",
        "path": "labs/01-vpc-multi-az-nat/README.md",
    },
    {
        "id": "lab-02",
        "number": "02",
        "title": "ALB + Auto Scaling",
        "domain": "D2",
        "minutes": 75,
        "cost": "Baixo",
        "summary": "Aplicação stateless multi-AZ, health checks e target tracking.",
        "diagram": "02-alb-asg.svg",
        "path": "labs/02-alb-asg/README.md",
    },
    {
        "id": "lab-03",
        "number": "03",
        "title": "S3 + CloudFront + WAF",
        "domain": "D1",
        "minutes": 75,
        "cost": "Baixo",
        "summary": "Origem privada com OAC, distribuição global e proteção de camada 7.",
        "diagram": "03-s3-cloudfront-waf.svg",
        "path": "labs/03-s3-cloudfront-waf/README.md",
    },
    {
        "id": "lab-04",
        "number": "04",
        "title": "RDS Multi-AZ + réplica",
        "domain": "D2",
        "minutes": 90,
        "cost": "Atenção",
        "summary": "Alta disponibilidade, failover gerenciado e escala de leitura opcional.",
        "diagram": "04-rds-multi-az-replica.svg",
        "path": "labs/04-rds-multi-az-replica/README.md",
    },
    {
        "id": "lab-05",
        "number": "05",
        "title": "DynamoDB + DAX",
        "domain": "D3",
        "minutes": 75,
        "cost": "Opcional",
        "summary": "Modelagem de chaves, on-demand e cache DAX opt-in para comparar trade-offs.",
        "diagram": "05-dynamodb-dax.svg",
        "path": "labs/05-dynamodb-dax/README.md",
    },
    {
        "id": "lab-06",
        "number": "06",
        "title": "Lambda + API Gateway + IAM",
        "domain": "D1",
        "minutes": 70,
        "cost": "Muito baixo",
        "summary": "API serverless com permissões mínimas, logs e integração proxy.",
        "diagram": "06-lambda-api-gateway-iam.svg",
        "path": "labs/06-lambda-api-gateway-iam/README.md",
    },
    {
        "id": "lab-07",
        "number": "07",
        "title": "KMS e criptografia",
        "domain": "D1",
        "minutes": 60,
        "cost": "Baixo",
        "summary": "Envelope encryption, key policy, rotação e trilha de auditoria.",
        "diagram": "07-kms-encryption-at-rest.svg",
        "path": "labs/07-kms-encryption-at-rest/README.md",
    },
    {
        "id": "lab-08",
        "number": "08",
        "title": "Transit Gateway ou Peering",
        "domain": "D2",
        "minutes": 85,
        "cost": "Opt-in",
        "summary": "Conectividade entre VPCs e decisão por escala, transitividade e custo.",
        "diagram": "08-transit-gateway-peering.svg",
        "path": "labs/08-transit-gateway-peering/README.md",
    },
]

PLANS = [
    {
        "id": "4-semanas",
        "title": "4 semanas",
        "label": "Recomendado",
        "pace": "2–3 h por dia",
        "description": "Cobertura progressiva, oito labs, revisão espaçada e três simulados.",
        "days": 28,
    },
    {
        "id": "2-semanas",
        "title": "2 semanas",
        "label": "Intensivo",
        "pace": "4–6 h por dia",
        "description": "Mesma cobertura com blocos combinados de teoria, prática e correção.",
        "days": 14,
    },
    {
        "id": "bootcamp",
        "title": "3 fins de semana",
        "label": "Compacto",
        "pace": "Sábado + domingo",
        "description": "Seis dias longos para quem já trabalha com AWS e quer consolidar decisões.",
        "days": 6,
    },
]


def md_escape(value: str) -> str:
    return value.replace("|", "\\|")


def build_markdown(data: dict) -> str:
    lines = [
        f"# Guia por domínios - {data['exam']}",
        "",
        f"Verificado em **{data['version_checked']}**. {data['pricing_note']}",
        "",
        "## Mapa do exame",
        "",
        "| Domínio | Peso | Meta de estudo |",
        "|---|---:|---|",
    ]
    for domain in data["domains"]:
        lines.append(
            f"| [{domain['id']} - {domain['title']}](#{domain['id'].lower()}) | "
            f"{domain['weight']}% | {md_escape(domain['objective'])} |"
        )
    lines.extend(
        [
            "",
            "> Regra de prova: sublinhe requisito, restrição e palavra de decisão. Elimine respostas tecnicamente possíveis que não otimizam o requisito pedido.",
            "",
        ]
    )
    for domain in data["domains"]:
        lines.extend(
            [
                f'<a id="{domain["id"].lower()}"></a>',
                f"## {domain['id']} - {domain['title']} ({domain['weight']}%)",
                "",
                domain["objective"],
                "",
            ]
        )
        for topic in domain["topics"]:
            lines.extend(
                [
                    f"### {topic['title']}",
                    "",
                    f"**Técnico.** {topic['technical']}",
                    "",
                    f"**Como criança.** {topic['child']}",
                    "",
                    f"**Quando usar.** {topic['when']}",
                    "",
                    f"**Limitações.** {topic['limits']}",
                    "",
                    f"**Custo estimado.** {topic['cost']}",
                    "",
                    f"**Melhores práticas.** {topic['practices']}",
                    "",
                    f"**Pegadinhas de prova.** {topic['traps']}",
                    "",
                    "**Documentação oficial.** "
                    + " · ".join(f"[AWS {idx + 1}]({url})" for idx, url in enumerate(topic["links"])),
                    "",
                ]
            )
    lines.extend(
        [
            "## Como transformar leitura em decisão",
            "",
            "1. Explique o tópico sem siglas usando a analogia.",
            "2. Desenhe a menor arquitetura que atende o requisito.",
            "3. Nomeie uma limitação, uma cobrança e uma falha possível.",
            "4. Resolva cinco questões e registre por que descartou cada distrator.",
            "5. Execute o lab relacionado e comprove os checkpoints antes do cleanup.",
            "",
            f"Abra o [site de estudo]({SITE_URL}) ou volte ao [README](README.md).",
            "",
        ]
    )
    return "\n".join(lines)


def build_site_payload(topics: dict, quiz: dict) -> dict:
    return {
        "topics": topics,
        "quiz": quiz,
        "labs": [{**lab, "url": f"{REPOSITORY_URL}/blob/main/{lab['path']}"} for lab in LABS],
        "plans": PLANS,
        "repositoryUrl": REPOSITORY_URL,
        "siteUrl": SITE_URL,
        "stats": {
            "domains": 4,
            "topics": sum(len(domain["topics"]) for domain in topics["domains"]),
            "labs": len(LABS),
            "questions": 445,
            "flashcards": 240,
            "mockExams": 3,
        },
    }


def copy_site_assets() -> None:
    assets = DOCS / "assets"
    diagrams = DOCS / "diagrams"
    data_dir = DOCS / "data"
    assets.mkdir(parents=True, exist_ok=True)
    diagrams.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    for filename in ("styles.css", "app.js", "og.png"):
        shutil.copyfile(SITE_SOURCE / filename, assets / filename)
    for lab in LABS:
        shutil.copyfile(ROOT / "diagrams" / lab["diagram"], diagrams / lab["diagram"])
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")


def main() -> None:
    topics = json.loads(TOPICS_SOURCE.read_text(encoding="utf-8"))
    quiz = json.loads(QUIZ_SOURCE.read_text(encoding="utf-8"))
    payload = build_site_payload(topics, quiz)
    payload_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = (SITE_SOURCE / "index.template.html").read_text(encoding="utf-8")
    index = template.replace("__SITE_DATA__", payload_json)

    DOCS.mkdir(parents=True, exist_ok=True)
    copy_site_assets()
    MARKDOWN.write_text(build_markdown(topics), encoding="utf-8")
    (DOCS / "index.html").write_text(index, encoding="utf-8")
    (DOCS / "data" / "site-data.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    topic_count = payload["stats"]["topics"]
    print(f"Generated study guide and GitHub Pages portal from {topic_count} topics and {len(LABS)} labs.")


if __name__ == "__main__":
    main()
