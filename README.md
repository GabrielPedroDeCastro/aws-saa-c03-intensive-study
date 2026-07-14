# AWS SAA-C03 - projeto intensivo, prático e mensurável

Este repositório é um programa completo de preparação para a certificação **AWS Certified Solutions Architect - Associate (SAA-C03)**. O caminho padrão dura 4 semanas; também há uma trilha intensiva de 2 semanas e um bootcamp de 3 fins de semana. Todo conceito aparece em duas camadas: explicação técnica e analogia "como criança".

> **Segurança de custo:** nenhum comando de implantação é executado automaticamente. Use uma conta sandbox, um perfil AWS separado, alertas de orçamento e faça o cleanup ao terminar cada lab. NAT Gateway, DAX, WAF, Transit Gateway, RDS e outros recursos podem gerar cobrança mesmo com pouco tráfego.

## Comece aqui

1. Abra o [pacote inicial](PACOTE-INICIAL.md) para a orientação de entrega e o primeiro dia.
2. Leia o [guia por domínio](GUIA-DE-ESTUDOS.md).
3. Escolha um [cronograma](schedules/README.md).
4. Configure os [pré-requisitos e a conta sandbox](docs/SETUP.md).
5. Faça o [diagnóstico de 40 questões](simulados/diagnostico-40.md).
6. Corrija pelo terminal e gere seu primeiro relatório:

   ```powershell
   python tools/quiz_runner.py simulados/diagnostico-40.json
   ```

7. Comece o [Dia 1](schedules/DIA-01.md) e o lab de VPC multi-AZ.
8. Antes de qualquer deploy, rode a validação local:

   ```powershell
   python tools/validate_project.py
   ```

## O que está incluído

| Área | Conteúdo |
|---|---|
| Guia | 4 domínios oficiais, resumos técnicos, analogias, uso, limites, custo, boas práticas e pegadinhas |
| Hands-on | 8 labs, cada um com console, CLI, CloudFormation, Terraform, checkpoints e cleanup |
| Avaliação | diagnóstico de 40 questões, 40 mini-quizzes (200 questões) e 3 simulados de 65 questões |
| Memorização | 200+ flashcards e checklist de revisão |
| Métricas | relatório por domínio, tempo médio, erros conceituais e top 10 prioridades |
| Ritmos | 4 semanas, 2 semanas e 3 fins de semana |
| Automação | correção interativa, geração de relatório, validação de JSON/IaC e CI simples |

## Mapa do repositório

```text
.
|-- labs/          # roteiros hands-on completos
|-- iac/           # CloudFormation e Terraform por lab
|-- quizzes/       # 10 mini-quizzes por domínio, JSON + Markdown
|-- simulados/     # diagnóstico e 3 simulados completos
|-- diagrams/      # Mermaid e SVG por arquitetura
|-- flashcards/    # baralho em JSON e Markdown
|-- reports/       # relatórios gerados, modelo e checklist final
|-- schedules/     # planos de 4 semanas, 2 semanas e bootcamp
|-- references/    # fontes oficiais e avaliação de simulados externos
|-- tools/         # correção, relatório, validação e geradores
|-- scripts/       # utilitários de deploy/cleanup
|-- docs/          # setup, CI/CD e landing page HTML
`-- content/       # fonte estruturada do guia por domínio
```

## Uso rápido dos laboratórios

Cada pasta em `labs/` aponta para os dois sabores de IaC. O fluxo recomendado é:

```powershell
aws sts get-caller-identity --profile aws-saa-lab
# permaneça na raiz; escolha CloudFormation OU Terraform e siga:
# labs/01-vpc-multi-az-nat/README.md
```

Não implante os dois sabores ao mesmo tempo. Cada lab contém uma estimativa de custo, checkpoints objetivos e o comando de cleanup correspondente.

## Avaliações e feedback

As questões são autorais e seguem o estilo de decisão por cenário do exame. O corretor mostra:

- alternativa correta e justificativa técnica;
- analogia simples;
- motivo de cada alternativa estar certa ou errada;
- feedback diferente para acerto e erro;
- referência oficial ou lab recomendado;
- exercício de reforço, tempo sugerido e pontos.

Nos mini-quizzes e no quiz do Dia 1, o feedback aparece após cada resposta. No diagnóstico e nos simulados completos, ele é automaticamente adiado para o relatório final, evitando que uma explicação revele conceitos das questões seguintes.

Para responder sem modo interativo, copie [answers.example.json](reports/answers.example.json), preencha suas letras e rode:

```powershell
python tools/grade_answers.py `
  --exam simulados/diagnostico-40.json `
  --answers reports/answers.example.json `
  --output reports/meu-diagnostico.md
```

## Fontes e integridade

O [guia oficial SAA-C03](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) é a fonte de verdade para escopo e pesos. Os links pedidos, whitepapers, FAQs e a avaliação de simulados externos estão em [SOURCES.md](references/SOURCES.md).

Este projeto **não reproduz dumps nem questões reais sigilosas**. O PDF de terceiros fornecido é catalogado apenas como recurso não oficial e de alto risco pedagógico/ético; as questões deste repositório são originais.

## CI/CD simples

O workflow em `.github/workflows/validate.yml` valida JSON, contagens, links internos, sintaxe Python, CloudFormation e formatação Terraform quando as ferramentas estiverem disponíveis. Veja [CI-CD.md](docs/CI-CD.md).

## Definição de pronto

Rode `python tools/validate_project.py`. O comando só termina com sucesso quando encontra os 4 domínios, 8 labs com os dois IaCs, 40 questões diagnósticas, 3 simulados completos, 200 questões de mini-quizzes, 200 flashcards, cronogramas e os campos obrigatórios de feedback.

## Licença e responsabilidade

Material educacional independente, sem afiliação ou endosso da AWS. Nomes e marcas pertencem aos respectivos proprietários. Preços e recursos da nuvem mudam; confirme a região e a [página oficial de preços](https://aws.amazon.com/pricing/) antes de implantar.
