# Cronograma intensivo - 2 semanas

Carga sugerida: **10 a 12 horas por dia incluindo questões e labs**, nunca 12 horas contínuas. Use blocos de 50/10, almoço de pelo menos 60 minutos, caminhada e sono de 7-8 horas. Reduza a carga se a precisão cair: fadiga ensina respostas erradas.

| Dia | Manhã (3-4 h) | Tarde (4 h) | Noite (2-3 h) | Gate |
|---:|---|---|---|---|
| 1 | Setup, diagnóstico 40, VPC e routing | Lab 01 CloudFormation **ou** Terraform, checkpoints e cleanup | 10 questões, relatório inicial e flashcards | [Roteiro completo](DIA-01.md) |
| 2 | IAM, STS, Identity Center, Organizations/SCP | Lab mental cross-account + SG/NACL/endpoints | Q-D1-01 a 04 e revisão dos erros | D1 parcial >= 70% |
| 3 | CloudFront, WAF, Shield, Route 53, TLS | Lab 03; comparar OAC e website endpoint | Q-D1-05 a 07 + 30 flashcards | Origin não público |
| 4 | KMS, secrets, CloudTrail, Config, GuardDuty/Macie | Lab 07 + threat model e cleanup | Q-D1-08 a 10 + revisão D1 | D1 >= 78% |
| 5 | ELB, ASG, health, sessões, SQS/SNS/EventBridge | Lab 02 + desenho fanout/DLQ | Q-D2-01 a 04 | Explicar idempotência |
| 6 | RDS/Aurora, replicas, DynamoDB HA, backup/PITR | Lab 04 e teste de endpoints | Q-D2-05 a 07 | Multi-AZ x replica sem erro |
| 7 | RPO/RTO, DR e conectividade híbrida | Lab 08, peering e alternativa TGW | Q-D2-08 a 10 + prova de 40 | D2 >= 78% |
| 8 | Compute: EC2/Lambda/ECS/EKS/Fargate | Lab 06 API serverless | Q-D3-01 a 03 + cold-start review | Escolha por restrição |
| 9 | S3/EBS/EFS/FSx e banco/cache | Lab 05 DynamoDB/DAX barato | Q-D3-04 a 06 | Sem scan e chave uniforme |
| 10 | Rede global, Kinesis/Firehose/MSK/Glue | Redesenhar pipelines e caching | Q-D3-07 a 10 + 40 flashcards | D3 >= 78% |
| 11 | Spot/RI/Savings Plans/Graviton e storage lifecycle | Otimizar labs 02/03 com mesma HA | Q-D4-01 a 04 | Explicar compromisso x risco |
| 12 | Custo de DB/rede, NAT/endpoints, CUR/Budgets | Mapa de custos dos 8 labs + checklist cleanup | Q-D4-05 a 10 | D4 >= 78% |
| 13 | Simulado 1 (130 min) e correção profunda | Reforço dos 5 piores tópicos + checkpoints | Simulado 2 (130 min) | Geral >= 78%; domínio >= 70% |
| 14 | Reforço dos 5 tópicos restantes | Simulado 3 (130 min) e relatório final | Checklist, revisão leve e descanso | Dois resultados >= 80% |

## Ordem fixa de um dia intensivo

1. Recall sem consulta (20 min).
2. Teoria focada (2 blocos).
3. Questões de descoberta (1 bloco).
4. Lab/desenho e checkpoints (3-4 blocos).
5. Cleanup e evidência (1 bloco).
6. Questões cronometradas (2 blocos).
7. Correção dos distratores e flashcards (2 blocos).
8. Relatório e plano de amanhã (20 min).
