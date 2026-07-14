# Scripts de deploy e cleanup

Os executáveis reutilizáveis ficam junto da infraestrutura em [`iac/scripts/`](../iac/scripts/):

| Motor | PowerShell | Bash |
|---|---|---|
| Deploy CloudFormation | [`deploy-cfn.ps1`](../iac/scripts/deploy-cfn.ps1) | [`deploy-cfn.sh`](../iac/scripts/deploy-cfn.sh) |
| Cleanup CloudFormation | [`cleanup-cfn.ps1`](../iac/scripts/cleanup-cfn.ps1) | [`cleanup-cfn.sh`](../iac/scripts/cleanup-cfn.sh) |
| Deploy Terraform | [`deploy-terraform.ps1`](../iac/scripts/deploy-terraform.ps1) | [`deploy-terraform.sh`](../iac/scripts/deploy-terraform.sh) |
| Cleanup Terraform | [`cleanup-terraform.ps1`](../iac/scripts/cleanup-terraform.ps1) | [`cleanup-terraform.sh`](../iac/scripts/cleanup-terraform.sh) |
| Esvaziar bucket S3 versionado | [`empty-versioned-bucket.ps1`](../iac/scripts/empty-versioned-bucket.ps1) | [`empty-versioned-bucket.sh`](../iac/scripts/empty-versioned-bucket.sh) |

Cada lab fornece o comando completo com diretório, stack e parâmetros. Os scripts exigem `-Profile`/`AWS_PROFILE`, mostram conta, ARN e região, pedem confirmação e interrompem em erro; nenhum deles cria credenciais ou escolhe uma conta silenciosamente.

Antes de usar:

```powershell
aws sts get-caller-identity --profile aws-saa-lab
python tools/validate_project.py
```
