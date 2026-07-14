# Cronograma padrão - 4 semanas

Carga sugerida: **2 a 4 horas por dia**, com uma pausa curta a cada 50 minutos. `Q-Dx-y` significa mini-quiz `y` do domínio `x`.

## Semana 1 - Segurança e networking

| Dia | Meta e teoria | Hands-on/desenho | Avaliação e evidência |
|---:|---|---|---|
| 1 | Setup, formato SAA-C03 e diagnóstico | Use apenas os blocos de setup/diagnóstico do [Dia 1 intensivo](DIA-01.md); deixe o lab para o dia 3 | Diagnóstico 40 + baseline por domínio (2-3 h) |
| 2 | IAM, STS, roles, Identity Center, Organizations e SCP | Desenhar acesso humano e workload cross-account | Q-D1-01; explicar `explicit deny` |
| 3 | SG, NACL, route tables, endpoints e DNS privado | Lab 01 VPC multi-AZ por um IaC; valide o segundo sem deploy simultâneo | Quiz Dia 1 + Q-D1-02; tabela SG x NACL |
| 4 | CloudFront, OAC, WAF, Shield e Route 53 | Lab 03 S3 + CloudFront + WAF | Q-D1-03; teste de origin privado |
| 5 | KMS, envelope encryption, key policy, ACM e secrets | Lab 07 KMS + criptografia em repouso | Q-D1-04; provar ciphertext/decrypt e cleanup |
| 6 | CloudTrail, Config, GuardDuty, Macie e CloudWatch | Threat-model de uma aplicação de três camadas | Q-D1-05 e Q-D1-06; mapa de sinais |
| 7 | Revisão espaçada D1 e pegadinhas | Redesenhar labs 01/03/07 de memória | Q-D1-07 a Q-D1-10; meta >= 75% |

## Semana 2 - Resiliência e desacoplamento

| Dia | Meta e teoria | Hands-on/desenho | Avaliação e evidência |
|---:|---|---|---|
| 8 | ELB, ASG, health checks, stateless e sessões | Lab 02 ALB + Auto Scaling | Q-D2-01; simular target unhealthy |
| 9 | SQS, SNS, EventBridge, DLQ e idempotência | Desenhar fanout e worker com retry | Q-D2-02; calcular visibility timeout |
| 10 | RDS Multi-AZ, replicas, Aurora e RDS Proxy | Lab 04 RDS Multi-AZ + read replica | Q-D2-03; identificar endpoints/failover |
| 11 | DynamoDB HA, PITR, Global Tables e backup | Tabela de RPO/RTO por serviço | Q-D2-04; restaurar raciocínio sem console |
| 12 | DR: backup/restore, pilot light, warm standby, active-active | Runbook de falha regional com dependências | Q-D2-05 e Q-D2-06; matriz custo x RTO/RPO |
| 13 | Peering, TGW, VPN e Direct Connect | Lab 08 peering/TGW | Q-D2-07; demonstrar não-transitividade |
| 14 | Revisão D2 e prova curta | Chaos checklist nos labs 02/04/08 | Q-D2-08 a Q-D2-10; revisão de erros |

## Semana 3 - Alto desempenho

| Dia | Meta e teoria | Hands-on/desenho | Avaliação e evidência |
|---:|---|---|---|
| 15 | EC2 families, placement, Lambda, ECS/EKS/Fargate | Lab 06 Lambda + API Gateway + IAM | Q-D3-01; medir cold/warm invocation |
| 16 | S3, EBS, EFS, FSx, throughput e IOPS | Matriz de storage por padrão de acesso | Q-D3-02; cálculo simples IOPS/throughput |
| 17 | RDS/Aurora performance, cache e connection pooling | Rever métricas do lab 04 | Q-D3-03; justificar cache-aside |
| 18 | DynamoDB keys, GSI/LSI, capacity, consistency e DAX | Lab 05 DynamoDB + DAX/alternativa barata | Q-D3-04; provar acesso sem scan |
| 19 | CloudFront x Global Accelerator x Route 53 | Desenhar três soluções globais e seus limites | Q-D3-05 e Q-D3-06 |
| 20 | Kinesis, Firehose, SQS, MSK e Glue | Pipeline streaming x batch no quadro | Q-D3-07; escolher partition key |
| 21 | Revisão D3 + simulado por tempo | Refazer checkpoint falho dos labs 05/06 | Q-D3-08 a Q-D3-10; meta >= 80% |

## Semana 4 - Custos, integração e prova

| Dia | Meta e teoria | Hands-on/desenho | Avaliação e evidência |
|---:|---|---|---|
| 22 | On-Demand, Spot, RI, Savings Plans, Graviton e S3 lifecycle | Otimizar labs 02/03 sem reduzir HA | Q-D4-01 a Q-D4-04 |
| 23 | Custos RDS/Aurora/DynamoDB e rede (NAT/endpoints/cross-AZ) | Right-sizing dos labs 04/05 e mapa de pedágios | Q-D4-05 a Q-D4-07 |
| 24 | Budgets, CUR, tags, Cost Explorer e Well-Architected | Plano FinOps e checklist de custo dos 8 labs | Q-D4-08 a Q-D4-10; D4 >= 75% |
| 25 | Simulado completo 1 em 130 minutos | Sem consulta; triagem inicial dos erros | Simulado 1 + top 10 fracos (3-4 h) |
| 26 | Correção profunda do simulado 1 | Checkpoint/lab curto nos cinco piores tópicos | Refazer erradas sem gabarito (2-4 h) |
| 27 | Simulado completo 2 em 130 minutos | Revisão dos distratores mais difíceis | Meta >= 80%, nenhum domínio < 72% (3-4 h) |
| 28 | Simulado completo 3 em 130 minutos | Relatório comparativo, checklist e descanso | Meta consistente; nenhum lab novo (3-4 h) |

## Gates de decisão

- **Fim da semana 1:** D1 >= 70%; caso contrário, repita IAM, rede privada e KMS.
- **Fim da semana 2:** D2 >= 75% e explicar RPO/RTO sem consulta.
- **Fim da semana 3:** D3 >= 75% e escolher storage/database a partir do access pattern.
- **Dia 28:** dois simulados consecutivos >= 80%, nenhum domínio abaixo de 72% e tempo médio <= 120 s.
