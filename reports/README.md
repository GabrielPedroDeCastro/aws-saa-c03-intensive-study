# Relatórios e métricas

Há duas formas de gerar um relatório:

```powershell
# modo interativo; diagnóstico adia feedback para preservar o baseline
python tools/quiz_runner.py simulados/diagnostico-40.json --candidate "meu-apelido"

# respostas já registradas em JSON
python tools/grade_answers.py `
  --exam simulados/diagnostico-40.json `
  --answers reports/answers.example.json `
  --output reports/meu-diagnostico.md
```

O Markdown e o resumo JSON incluem:

- acertos, erros, questões em branco e pontos;
- percentual e tempo médio por domínio;
- top 10 tópicos fracos ponderados por erro, lentidão e peso oficial;
- diagnóstico da alternativa escolhida;
- explicação técnica e versão "como criança";
- justificativa A-D, referência oficial, lab e exercício recomendado.

Use [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md) para acompanhamento manual e [CHECKLIST-FINAL.md](CHECKLIST-FINAL.md) na última semana. Relatórios pessoais `meu-*.md` e HTML não são versionados por padrão.
