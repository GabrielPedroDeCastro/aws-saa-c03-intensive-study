# CI/CD simples

O workflow de validação não faz deploy na AWS e não precisa de credenciais. Em push ou pull request ele:

1. compila os scripts Python;
2. reconstrói a landing page a partir de `content/topics.json` e detecta diferença;
3. valida os contratos, contagens e JSON do projeto;
4. roda `cfn-lint` nos templates CloudFormation;
5. verifica `terraform fmt` e executa `terraform validate` com backend desabilitado em cada lab.

As versões do Terraform e do `cfn-lint` estão fixadas no workflow; cada lab mantém `.terraform.lock.hcl` para selecionar a mesma versão do provider validada neste commit.

Arquivo: [validate.yml](../.github/workflows/validate.yml).

## Fluxo sugerido de contribuição

```powershell
git switch -c conteudo/meu-topico
python tools/build_site.py
python tools/validate_project.py
git diff --check
git add .
git commit -m "docs: aprimora tópico de resiliência"
git push -u origin conteudo/meu-topico
```

O deploy de labs em CI não é recomendado para este projeto inicial: exigiria uma conta dedicada, OIDC, limites de custo, concorrência, cleanup mesmo após falha e aprovação manual. Se for adicionado, use GitHub OIDC para assumir uma role curta; nunca armazene access keys permanentes em secrets.

## Critérios para merge

- JSON válido e todos os campos de feedback preenchidos;
- alternativa correta existente entre A-D;
- explicação individual de A, B, C e D;
- link oficial ou lab de reforço;
- IaC formatado e sem credenciais;
- roteiro de cleanup atualizado quando o template muda;
- conteúdo autoral, sem dumps ou material de exame sigiloso.
