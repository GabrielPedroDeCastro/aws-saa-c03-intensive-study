# Simulados SAA-C03

Questões autorais, sem reprodução de dumps. O diagnóstico segue a proporção 12/10/10/8; cada simulado completo usa 20/17/15/13, aproximação inteira dos pesos oficiais 30%/26%/24%/20%.

| Arquivo | Questões | Tempo | D1/D2/D3/D4 | Gabarito A/B/C/D |
|---|---:|---:|---|---|
| [diagnostico-40.json](diagnostico-40.json) / [diagnostico-40.md](diagnostico-40.md) | 40 | 75 min | 12/10/10/8 | 10/10/10/10 |
| [simulado-01-65.json](simulado-01-65.json) / [simulado-01-65.md](simulado-01-65.md) | 65 | 130 min | 20/17/15/13 | 16/17/16/16 |
| [simulado-02-65.json](simulado-02-65.json) / [simulado-02-65.md](simulado-02-65.md) | 65 | 130 min | 20/17/15/13 | 16/16/17/16 |
| [simulado-03-65.json](simulado-03-65.json) / [simulado-03-65.md](simulado-03-65.md) | 65 | 130 min | 20/17/15/13 | 16/16/16/17 |

## Uso recomendado

1. Faça o diagnóstico no Dia 1 e registre domínio, tempo e tema de cada erro.
2. Faça os simulados completos sem consulta, em uma sessão de 130 minutos.
3. Para cada erro, leia A–D, realize o exercício recomendado e refaça a questão após 48 horas.
4. Não memorize letras: a ordem das alternativas foi deliberadamente balanceada.
5. `python tools/quiz_runner.py simulados/diagnostico-40.json` adia o feedback automaticamente em avaliações com mais de 10 questões, preservando o baseline. Use `--immediate-feedback` somente em revisão deliberada.
