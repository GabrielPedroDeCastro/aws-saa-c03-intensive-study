# Preparar o ambiente com segurança

## 1. Use uma conta sandbox

Não rode os labs em produção. O ideal é uma conta-membro exclusiva dentro do AWS Organizations, sem dados reais, com MFA no acesso humano e uma região padrão. Se isso não for possível, use ao menos um perfil separado, tags obrigatórias e faça o inventário antes/depois de cada lab.

Crie um orçamento e alertas pelo console em **Billing and Cost Management > Budgets** antes do primeiro deploy. O alerta avisa; ele não é um bloqueio rígido por padrão. Assine também alertas de anomalia de custos.

## 2. Ferramentas locais

- Python 3.10 ou superior;
- AWS CLI v2;
- Terraform 1.6 ou superior;
- Git;
- PowerShell 7+ no Windows ou Bash no Linux/macOS;
- conta AWS com permissão para os recursos do lab escolhido.

Instale pelas páginas oficiais, nesta ordem:

1. [Python](https://www.python.org/downloads/) — marque a opção de adicionar ao `PATH` no Windows.
2. [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) — use o instalador correspondente ao sistema.
3. [Terraform](https://developer.hashicorp.com/terraform/install) — extraia/instale o binário e adicione seu diretório ao `PATH`.
4. [Git](https://git-scm.com/downloads) — mantenha suporte a HTTPS e finais de linha do sistema.
5. [PowerShell 7](https://learn.microsoft.com/powershell/scripting/install/installing-powershell) no Windows; Bash já vem na maioria das distribuições Linux/macOS.

Feche e abra o terminal após as instalações. No Windows, se `python` abrir a Microsoft Store ou apontar só para `WindowsApps`, tente `py -3 --version`; você pode usar `py -3` no lugar de `python` nos comandos deste projeto. O corretor usa apenas a biblioteca padrão e não exige `pip install`.

Confira:

```powershell
python --version
py -3 --version  # alternativa no Windows
aws --version
terraform version
git --version
```

## 3. Perfil AWS separado

Configure credenciais temporárias/federadas sempre que possível. Para um perfil local:

```powershell
aws configure sso --profile aws-saa-lab
aws sso login --profile aws-saa-lab
aws sts get-caller-identity --profile aws-saa-lab
```

Se sua organização ainda não usa IAM Identity Center, siga a configuração aprovada pelo administrador. Não grave access keys no repositório, em arquivos `.tfvars` versionados ou em user data.

Defina a sessão atual:

```powershell
$env:AWS_PROFILE = "aws-saa-lab"
$env:AWS_REGION = "us-east-1"
aws sts get-caller-identity
```

Bash:

```bash
export AWS_PROFILE=aws-saa-lab
export AWS_REGION=us-east-1
aws sts get-caller-identity
```

## 4. Permissões

Os oito labs cobrem muitos serviços, portanto não existe uma policy curta que sirva a todos. Em uma conta sandbox sem dados reais, use um permission set temporário aprovado pelo responsável e remova-o ao encerrar o ciclo. Em ambientes compartilhados, prefira uma policy específica por lab a `AdministratorAccess`.

Todos os recursos recebem as tags:

- `Project=aws-saa-c03-intensive`
- `ManagedBy=cloudformation` ou `terraform`
- `Lab=<identificador>`
- `Owner=<seu-identificador>` quando solicitado

## 5. Validação local antes do deploy

```powershell
python tools/validate_project.py
aws cloudformation validate-template --template-body file://iac/01-vpc-multi-az-nat/cloudformation/template.yaml
terraform -chdir=iac/01-vpc-multi-az-nat/terraform init -backend=false
terraform -chdir=iac/01-vpc-multi-az-nat/terraform validate
```

`validate-template` comprova a estrutura CloudFormation, não permissões, quotas nem a disponibilidade de um tipo de instância na região.

## 6. Regras de custo

1. Leia a caixa de custo do lab e confira a região no [AWS Pricing Calculator](https://calculator.aws/).
2. Escolha CloudFormation **ou** Terraform; não implante os dois juntos.
3. Execute os checkpoints sem deixar o terminal.
4. Faça cleanup imediatamente.
5. Confirme que a stack sumiu ou que `terraform show` não contém recursos.
6. Verifique recursos tagueados e os consoles de EC2, VPC, RDS, DynamoDB, CloudFront, WAF e KMS.

Inventário por tag (a cobertura da API varia por tipo de recurso):

```powershell
aws resourcegroupstaggingapi get-resources `
  --tag-filters Key=Project,Values=aws-saa-c03-intensive `
  --query "ResourceTagMappingList[].ResourceARN" `
  --output table
```

## 7. Estado Terraform

O backend local serve apenas ao estudo individual. Não versionar `terraform.tfstate`, pois ele pode conter dados sensíveis. Para equipe, use S3 com versionamento, criptografia e locking compatível com a versão adotada, aplicando menor privilégio.

## Solução de problemas rápida

| Sintoma | Verifique primeiro |
|---|---|
| `ExpiredToken` | refaça login SSO e confirme `AWS_PROFILE` |
| `AccessDenied` | identidade ativa, permission set, SCP, permissions boundary e key policy |
| Terraform quer recriar tudo | diretório/state correto e mesma região/profile |
| Stack em rollback | primeiro evento com falha, quota, nome global e recurso dependente |
| Cleanup trava | bucket não vazio, ENI em uso, proteção contra exclusão ou dependência de rota |
| Conta continua cobrando | NAT, DAX, RDS, TGW, WAF, endpoints de interface e snapshots órfãos |
