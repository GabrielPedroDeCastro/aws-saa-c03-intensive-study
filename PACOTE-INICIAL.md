# Pacote Inicial - SAA-C03

Este índice reúne a primeira entrega pedida no briefing. O restante do repositório expande o mesmo padrão para as quatro semanas.

## 1. Dia 1 completo

- [Agenda intensiva, resumo técnico e versão "como criança"](schedules/DIA-01.md)
- [Lab 01 - VPC multi-AZ com NAT](labs/01-vpc-multi-az-nat/README.md)
- [CloudFormation do lab](iac/01-vpc-multi-az-nat/cloudformation/template.yaml)
- [Terraform do lab](iac/01-vpc-multi-az-nat/terraform/main.tf)
- [Quiz Dia 1 - 10 questões](quizzes/dia-01-10.md)
- [Quiz Dia 1 em JSON](quizzes/dia-01-10.json)

## 2. Diagnóstico de 40 questões

- [Versão Markdown](simulados/diagnostico-40.md)
- [Versão JSON](simulados/diagnostico-40.json)

Rodar preservando o baseline; o feedback detalhado aparece no relatório final:

```powershell
python tools/quiz_runner.py simulados/diagnostico-40.json --candidate "meu-apelido"
```

O relatório gerado contém acertos, erros, tempo médio por domínio e as dez maiores prioridades de revisão.

## 3. Estrutura inicial do repositório

```text
.
|-- README.md
|-- GUIA-DE-ESTUDOS.md
|-- labs/
|-- iac/
|-- quizzes/
|-- simulados/
|-- diagrams/
|-- flashcards/
|-- reports/
|-- schedules/
|-- references/
|-- scripts/
|-- tools/
`-- docs/
```

## 4. Usar localmente

Na pasta do projeto:

```powershell
python tools/validate_project.py
python tools/quiz_runner.py quizzes/dia-01-10.json
```

Para obter uma cópia portátil depois da inicialização Git:

```powershell
git archive --format=zip --output aws-saa-c03-study.zip HEAD
```

O [README principal](README.md) contém setup, mapa completo, critérios de aceitação e instruções de CI/CD.
