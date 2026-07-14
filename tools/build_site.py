#!/usr/bin/env python3
"""Build the Markdown and self-contained HTML landing pages from structured topics."""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "topics.json"
MARKDOWN = ROOT / "GUIA-DE-ESTUDOS.md"
HTML = ROOT / "docs" / "index.html"


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
            "> Regra de prova: sublinhe requisito, restrição e palavra de decisão (mais resiliente, menor custo, menor esforço operacional ou maior desempenho). Elimine respostas tecnicamente possíveis que não otimizam o requisito pedido.",
            "",
        ]
    )
    for domain in data["domains"]:
        lines.extend(
            [
                f"<a id=\"{domain['id'].lower()}\"></a>",
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
            "Volte ao [README](README.md), escolha um [cronograma](schedules/README.md) ou abra a [landing page HTML](docs/index.html).",
            "",
        ]
    )
    return "\n".join(lines)


def build_html(data: dict) -> str:
    nav = "".join(
        f'<a href="#{d["id"].lower()}">{html.escape(d["id"])} · {d["weight"]}%</a>'
        for d in data["domains"]
    )
    sections = []
    for domain in data["domains"]:
        cards = []
        for topic in domain["topics"]:
            links = " · ".join(
                f'<a href="{html.escape(url)}" target="_blank" rel="noreferrer">AWS {i + 1}</a>'
                for i, url in enumerate(topic["links"])
            )
            cards.append(
                f'''<article class="card">
<h3>{html.escape(topic['title'])}</h3>
<p><b>Técnico.</b> {html.escape(topic['technical'])}</p>
<p class="kid"><b>🧒 Como criança.</b> {html.escape(topic['child'])}</p>
<dl>
<dt>Quando usar</dt><dd>{html.escape(topic['when'])}</dd>
<dt>Limitações</dt><dd>{html.escape(topic['limits'])}</dd>
<dt>Custo estimado</dt><dd>{html.escape(topic['cost'])}</dd>
<dt>Melhores práticas</dt><dd>{html.escape(topic['practices'])}</dd>
<dt>Pegadinhas</dt><dd>{html.escape(topic['traps'])}</dd>
</dl><p class="links">{links}</p></article>'''
            )
        sections.append(
            f'''<section id="{domain['id'].lower()}">
<header><span>{html.escape(domain['id'])}</span><h2>{html.escape(domain['title'])}</h2><strong>{domain['weight']}%</strong></header>
<p class="objective">{html.escape(domain['objective'])}</p>
<div class="grid">{"".join(cards)}</div></section>'''
        )
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Guia intensivo AWS SAA-C03</title>
<style>
:root{{--ink:#172033;--muted:#536078;--bg:#f5f7fb;--card:#fff;--aws:#ff9900;--blue:#146eb4;--line:#dfe5ef;--kid:#fff6de}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,Segoe UI,sans-serif}}
.hero{{padding:4.5rem max(6vw,1rem);background:linear-gradient(135deg,#101827,#243b64);color:white}}.eyebrow{{color:#ffc65c;text-transform:uppercase;letter-spacing:.12em;font-weight:800}}
h1{{font-size:clamp(2.2rem,6vw,4.7rem);line-height:1.02;max-width:900px;margin:.3rem 0 1rem}}.hero p{{max-width:760px;color:#dce6f7;font-size:1.15rem}}
nav{{display:flex;gap:.7rem;flex-wrap:wrap;margin-top:1.6rem}}nav a{{color:white;text-decoration:none;border:1px solid #ffffff55;border-radius:999px;padding:.5rem .9rem}}nav a:hover{{background:#ffffff18}}
main{{width:min(1200px,94vw);margin:auto}}section{{padding:4rem 0 1rem;scroll-margin-top:1rem}}section>header{{display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:1rem}}
section>header span{{background:var(--aws);font-weight:900;border-radius:.6rem;padding:.45rem .7rem}}h2{{font-size:clamp(1.6rem,3vw,2.6rem);margin:0}}section>header strong{{font-size:1.4rem;color:var(--blue)}}.objective{{color:var(--muted);max-width:800px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:1rem}}.card{{background:var(--card);border:1px solid var(--line);border-radius:1rem;padding:1.25rem;box-shadow:0 5px 20px #20304a0b}}h3{{margin-top:0;line-height:1.25}}.kid{{background:var(--kid);padding:.75rem;border-radius:.7rem}}
dl{{display:grid;grid-template-columns:8.2rem 1fr;gap:.45rem .7rem;margin-bottom:.8rem}}dt{{font-weight:800}}dd{{margin:0;color:var(--muted)}}a{{color:#075b9b}}.links{{margin-bottom:0}}footer{{padding:4rem max(3vw,1rem);text-align:center;color:var(--muted)}}
@media(max-width:560px){{dl{{grid-template-columns:1fr}}section>header{{grid-template-columns:auto 1fr}}section>header strong{{grid-column:2}}}}
</style></head><body>
<header class="hero"><div class="eyebrow">Projeto hands-on · SAA-C03</div><h1>Aprenda a decidir como arquiteto.</h1>
<p>Quatro domínios, duas camadas de explicação e um foco: transformar requisitos, restrições, custo e falhas em escolhas arquiteturais defensáveis.</p><nav>{nav}</nav></header>
<main>{''.join(sections)}</main><footer>Conteúdo verificado em {html.escape(data['version_checked'])}. Preços são relativos; confirme no AWS Pricing Calculator. <a href="../README.md">Abrir README</a>.</footer>
</body></html>'''


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    MARKDOWN.write_text(build_markdown(data), encoding="utf-8")
    HTML.write_text(build_html(data), encoding="utf-8")
    topic_count = sum(len(domain["topics"]) for domain in data["domains"])
    print(f"Generated {MARKDOWN.name} and {HTML.relative_to(ROOT)} from {topic_count} topics.")


if __name__ == "__main__":
    main()
