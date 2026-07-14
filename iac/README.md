# Infraestrutura como código dos labs

Cada diretório numerado contém uma implementação equivalente em **CloudFormation** e **Terraform**. Implante apenas uma implementação por vez para não duplicar custos. A região padrão é `us-east-1`, mas todos os exemplos aceitam outra região.

Os arquivos `.terraform.lock.hcl` fixam as versões validadas dos providers. Mantenha-os no controle de versão; `terraform init` verifica seus hashes antes do uso.

## Scripts reutilizáveis

```powershell
$env:AWS_PROFILE = "aws-saa-lab"

# CloudFormation
./iac/scripts/deploy-cfn.ps1 -Template ./iac/01-vpc-multi-az-nat/cloudformation/template.yaml -StackName saa-lab-01
./iac/scripts/cleanup-cfn.ps1 -StackName saa-lab-01

# Terraform
./iac/scripts/deploy-terraform.ps1 -Directory ./iac/01-vpc-multi-az-nat/terraform
./iac/scripts/cleanup-terraform.ps1 -Directory ./iac/01-vpc-multi-az-nat/terraform
```

Em Bash, chame os scripts `.sh` equivalentes com `bash ./iac/scripts/NOME.sh`; isso não depende do bit executável preservado pelo download. **Defina `AWS_PROFILE` obrigatoriamente**; em PowerShell, use `-Profile` ou a mesma variável. Os scripts recusam o perfil implícito, exibem Account/ARN/região e exigem uma palavra de confirmação. Nunca grave chaves no repositório. Antes do deploy, confira a identidade com `aws sts get-caller-identity` e estime custos no [AWS Pricing Calculator](https://calculator.aws/).

Buckets S3 com versionamento precisam estar realmente vazios antes de uma stack CloudFormation ser excluída. Use `./iac/scripts/empty-versioned-bucket.ps1 -Bucket NOME` ou `bash ./iac/scripts/empty-versioned-bucket.sh NOME`; a ação **Empty** do Console S3 é a alternativa visual.

Os recursos recebem as tags `Project=saa-c03-intensive`, `Lab` e `ManagedBy` sempre que o serviço permite. Arquivos de estado Terraform, planos e variáveis locais estão ignorados pelo `.gitignore` principal do projeto.
