# Laboratórios hands-on

Execute **um lab e um motor de IaC por vez**. Todos têm rota pelo console para observação, comandos CLI, CloudFormation, Terraform, outputs, checkpoints, troubleshooting e cleanup.

> Mantenha o terminal na **raiz do repositório** em todos os comandos (`./iac/...`). Não execute depois de entrar na pasta de um lab.

| # | Laboratório | Custo relativo | Modo econômico padrão | IaC |
|---:|---|---|---|---|
| 01 | [VPC multi-AZ + NAT](01-vpc-multi-az-nat/README.md) | moderado | um NAT zonal; compare com um por AZ e Regional NAT Gateway | [CFN](../iac/01-vpc-multi-az-nat/cloudformation/template.yaml) · [TF](../iac/01-vpc-multi-az-nat/terraform/) |
| 02 | [ALB + Auto Scaling](02-alb-asg/README.md) | moderado | instâncias pequenas e capacidade mínima | [CFN](../iac/02-alb-asg/cloudformation/template.yaml) · [TF](../iac/02-alb-asg/terraform/) |
| 03 | [S3 + CloudFront + WAF](03-s3-cloudfront-waf/README.md) | baixo/moderado | conteúdo mínimo, sem tráfego de carga | [CFN](../iac/03-s3-cloudfront-waf/cloudformation/template.yaml) · [TF](../iac/03-s3-cloudfront-waf/terraform/) |
| 04 | [RDS Multi-AZ + read replica](04-rds-multi-az-replica/README.md) | alto | toggles permitem estudar recursos caros separadamente | [CFN](../iac/04-rds-multi-az-replica/cloudformation/template.yaml) · [TF](../iac/04-rds-multi-az-replica/terraform/) |
| 05 | [DynamoDB + DAX](05-dynamodb-dax/README.md) | baixo/alto | DAX desligado por padrão | [CFN](../iac/05-dynamodb-dax/cloudformation/template.yaml) · [TF](../iac/05-dynamodb-dax/terraform/) |
| 06 | [Lambda + API Gateway + IAM](06-lambda-api-gateway-iam/README.md) | baixo | serverless com poucas invocações | [CFN](../iac/06-lambda-api-gateway-iam/cloudformation/template.yaml) · [TF](../iac/06-lambda-api-gateway-iam/terraform/) |
| 07 | [KMS + criptografia em repouso](07-kms-encryption-at-rest/README.md) | baixo | poucos objetos/chamadas | [CFN](../iac/07-kms-encryption-at-rest/cloudformation/template.yaml) · [TF](../iac/07-kms-encryption-at-rest/terraform/) |
| 08 | [Transit Gateway x Peering](08-transit-gateway-peering/README.md) | baixo/alto | peering por padrão; TGW opt-in | [CFN](../iac/08-transit-gateway-peering/cloudformation/template.yaml) · [TF](../iac/08-transit-gateway-peering/terraform/) |

## Método de execução

1. Leia objetivo, custo e cleanup antes do deploy.
2. Desenhe a arquitetura de memória e compare com o SVG.
3. Confirme identidade, perfil e região.
4. Implante CloudFormation **ou** Terraform.
5. Rode comandos de validação e marque checkpoints.
6. Explique o trade-off técnico e pela analogia infantil.
7. Faça cleanup e confirme que recursos cobrados desapareceram.

Os scripts reutilizáveis estão em [`iac/scripts/`](../iac/scripts/). O [setup seguro](../docs/SETUP.md) explica perfil separado, estado Terraform e inventário por tags.

## Bash no Linux/macOS/WSL

Chame os arquivos com `bash`; assim o fluxo funciona mesmo se o ZIP foi baixado sem preservar o bit executável. Substitua `SLUG` e `STACK` pela linha desejada da tabela.

| Lab | `SLUG` | `STACK` |
|---:|---|---|
| 01 | `01-vpc-multi-az-nat` | `saa-lab-01` |
| 02 | `02-alb-asg` | `saa-lab-02` |
| 03 | `03-s3-cloudfront-waf` | `saa-lab-03` |
| 04 | `04-rds-multi-az-replica` | `saa-lab-04` |
| 05 | `05-dynamodb-dax` | `saa-lab-05` |
| 06 | `06-lambda-api-gateway-iam` | `saa-lab-06` |
| 07 | `07-kms-encryption-at-rest` | `saa-lab-07` |
| 08 | `08-transit-gateway-peering` | `saa-lab-08` |

```bash
# Execute da raiz do repositório
SLUG=02-alb-asg
STACK=saa-lab-02
REGION=us-east-1
export AWS_PROFILE=aws-saa-lab

# CloudFormation: deploy; valide o lab; depois cleanup
bash ./iac/scripts/deploy-cfn.sh "./iac/$SLUG/cloudformation/template.yaml" "$STACK" "$REGION"
bash ./iac/scripts/cleanup-cfn.sh "$STACK" "$REGION"

# Terraform alternativo: deploy; valide o lab; depois cleanup
cp "./iac/$SLUG/terraform/terraform.tfvars.example" "./iac/$SLUG/terraform/terraform.tfvars"
bash ./iac/scripts/deploy-terraform.sh "./iac/$SLUG/terraform" "$REGION"
bash ./iac/scripts/cleanup-terraform.sh "./iac/$SLUG/terraform" "$REGION"
```

Parâmetros CloudFormation opcionais vêm depois da região, por exemplo `EnableDax=true DaxReplicationFactor=1`. No Terraform, altere apenas a cópia local `terraform.tfvars`.

Os scripts mostram conta, ARN, região e perfil antes de agir e pedem que você digite `DEPLOY`, `DESTROY` ou `EMPTY`. Em automação isolada, `LAB_AUTO_APPROVE=1` remove somente essa confirmação; use apenas após validar o alvo explicitamente.
