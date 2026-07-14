# Checklist final SAA-C03

Use na última semana e marque apenas quando conseguir justificar a decisão sem consultar material.

## Prontidão mensurável

- [ ] Dois simulados completos consecutivos com pelo menos 80%.
- [ ] Nenhum domínio abaixo de 72%.
- [ ] Tempo médio menor ou igual a 120 segundos por questão.
- [ ] Todas as erradas foram refeitas 24-72 h depois.
- [ ] Consigo explicar por que cada distrator recente estava errado.
- [ ] Top 10 tópicos fracos têm ação e nova data de teste.

## D1 - Segurança

- [ ] Identity policy, resource policy, permissions boundary, session policy e SCP.
- [ ] `explicit deny` prevalece; SCP não concede acesso.
- [ ] Role/STS e federação em vez de credencial longa.
- [ ] SG stateful x NACL stateless e portas efêmeras.
- [ ] Subnet pública, IGW, NAT Gateway e VPC endpoints.
- [ ] OAC, CloudFront, WAF, Shield e TLS/ACM.
- [ ] SSE-S3, SSE-KMS, client-side e envelope encryption.
- [ ] Key policy, grants, rotação e separação de funções.
- [ ] Secrets Manager x Parameter Store.
- [ ] CloudTrail x Config x CloudWatch x GuardDuty x Macie.

## D2 - Resiliência

- [ ] ALB/NLB/GWLB e health checks.
- [ ] Auto Scaling multi-AZ, grace period e stateless/session store.
- [ ] SQS Standard/FIFO, DLQ, visibility timeout e idempotência.
- [ ] SNS fanout e EventBridge routing.
- [ ] RDS Multi-AZ x read replica x Aurora replica.
- [ ] DynamoDB PITR, Global Tables e consistência.
- [ ] RPO/RTO e quatro estratégias de DR.
- [ ] Backup cross-account/Region e restore testado.
- [ ] Peering não transitivo x Transit Gateway.
- [ ] VPN x Direct Connect e redundância.

## D3 - Alto desempenho

- [ ] EC2 family, placement groups, Lambda e contêineres.
- [ ] S3 x EBS x EFS x FSx pelo access pattern.
- [ ] gp3/PIOPS, throughput e snapshots.
- [ ] Partition key DynamoDB sem hot partition; GSI/LSI.
- [ ] ElastiCache x DAX e estratégia de invalidação.
- [ ] CloudFront x Global Accelerator x Route 53.
- [ ] Kinesis Streams x Firehose x SQS x MSK.
- [ ] Read/write endpoints, connection pooling e RDS Proxy.
- [ ] Consistência forte/eventual e replica lag.
- [ ] Métrica de scaling correlacionada com demanda.

## D4 - Custos

- [ ] On-Demand x Spot x RI x Savings Plans.
- [ ] Right-sizing, Compute Optimizer e Graviton.
- [ ] S3 storage classes, duração mínima, retrieval e lifecycle.
- [ ] EBS gp3 e snapshots órfãos.
- [ ] DynamoDB on-demand x provisioned/auto scaling.
- [ ] Aurora Serverless v2 e custo de I/O/storage.
- [ ] NAT processing, cross-AZ/Region e endpoints.
- [ ] CloudFront como otimização de egress/origin.
- [ ] Tags, CUR, Cost Explorer, Budgets e anomalias.
- [ ] Menor custo **que ainda cumpre** segurança, RPO/RTO e desempenho.

## Estratégia de prova

- [ ] Sei reconhecer pergunta de única resposta e múltiplas respostas.
- [ ] Marco requisito, restrição e superlativo antes das alternativas.
- [ ] Elimino respostas que não cumprem uma restrição explícita.
- [ ] Não adiciono requisito imaginário ao cenário.
- [ ] Se duas funcionam, comparo operação, custo, RPO/RTO e serviço gerenciado.
- [ ] Marco questão longa para revisão e protejo o tempo.
- [ ] Reservei 15-20 minutos finais para marcadas e múltipla resposta.
- [ ] Documento, horário, ambiente e regras do provedor de prova confirmados.
- [ ] Dormir e comer bem fazem parte do plano; nenhum lab novo na véspera.
