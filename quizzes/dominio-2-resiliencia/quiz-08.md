# Mini-quiz 08 — Domínio 2 — Projetar arquiteturas resilientes

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Políticas centralizadas com AWS Backup

> **ID:** `QUIZ-D2-08-Q01` · **Domínio:** D2 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A cooperativa campo vivo vai lançar o serviço em três países. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Dezenas de contas precisam de backups consistentes de EBS, RDS e EFS, cópias entre regiões e proteção contra exclusão pela conta de origem. Segurança quer governança central. Qual abordagem usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Usar apenas RDS Multi-AZ como backup histórico.
- **B)** Usar AWS Backup com backup policies da organização, cofre central/cross-account, cópia cross-region e Vault Lock quando a imutabilidade for requerida.
- **C)** Copiar arquivos para o disco local de uma instância na mesma conta.
- **D)** Pedir que cada desenvolvedor crie snapshots manuais quando lembrar.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

AWS Backup centraliza planos, seleção, retenção e cópias entre serviços e contas; Vault Lock ajuda a impor retenção WORM contra alterações indevidas.

Trade-off: Backup só é confiável quando restaurações são testadas e métricas de RPO/RTO são verificadas; replicação e alta disponibilidade não substituem backups protegidos. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um bibliotecário central faz cópias de todos os livros, guarda outra caixa em outra cidade e lacra as caixas pelo prazo certo.

**Se acertou:** Acertou: AWS Backup centraliza planos, seleção, retenção e cópias entre serviços e contas; Vault Lock ajuda a impor retenção WORM contra alterações indevidas. Quando outra opção poderia valer: Backup só é confiável quando restaurações são testadas e métricas de RPO/RTO são verificadas; replicação e alta disponibilidade não substituem backups protegidos. Mnemônica: associe “Políticas centralizadas com AWS Backup” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Multi-AZ é alta disponibilidade e replica também erros lógicos; não é retenção histórica independente.
- **B:** Correta — AWS Backup centraliza planos, seleção, retenção e cópias entre serviços e contas; Vault Lock ajuda a impor retenção WORM contra alterações indevidas.
- **C:** Incorreta — A cópia permanece vulnerável a falhas e exclusões na mesma fronteira administrativa.
- **D:** Incorreta — O processo não é consistente, auditável nem centralmente imposto.

**Referência oficial:** [https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html)

**Referência prática:** ../labs/README.md — Backup, restore e testes de recuperação

**Exercício recomendado:** No lab Backup, restore e testes de recuperação, monte uma prova de conceito de Políticas centralizadas com AWS Backup; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. RDS Multi-AZ

> **ID:** `QUIZ-D2-08-Q02` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A companhia aérea ventos precisa tomar uma decisão com base em desempenho, segurança e custo total. A carga atende milhares de requisições por segundo em horários de pico. Um banco transacional RDS precisa recuperar automaticamente de falha de instância ou de AZ, preservando o mesmo endpoint. A carga de leitura não é o problema principal. Qual configuração atende ao requisito? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Criar uma read replica na mesma AZ e usá-la como standby síncrono automático.
- **B)** Fazer snapshot manual uma vez por semana.
- **C)** Habilitar uma implantação RDS Multi-AZ com standby síncrono e failover gerenciado.
- **D)** Aumentar a classe da instância sem criar réplica.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

RDS Multi-AZ replica de forma síncrona para outra AZ e executa failover do endpoint, sendo uma solução de alta disponibilidade e não de escalabilidade de leitura.

Trade-off: Read replicas são assíncronas e adequadas para escalar leituras; podem ser promovidas, mas isso não equivale ao failover automático de Multi-AZ. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Há uma loja gêmea pronta em outro bairro; se a primeira fecha, a placa aponta sozinha para a segunda.

**Se acertou:** Acertou: RDS Multi-AZ replica de forma síncrona para outra AZ e executa failover do endpoint, sendo uma solução de alta disponibilidade e não de escalabilidade de leitura. Quando outra opção poderia valer: Read replicas são assíncronas e adequadas para escalar leituras; podem ser promovidas, mas isso não equivale ao failover automático de Multi-AZ. Mnemônica: associe “RDS Multi-AZ” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Read replicas usam replicação assíncrona e não fornecem o mesmo mecanismo de failover Multi-AZ.
- **B:** Incorreta — Snapshots ajudam em restauração, mas não fornecem failover rápido nem RPO próximo de zero.
- **C:** Correta — RDS Multi-AZ replica de forma síncrona para outra AZ e executa failover do endpoint, sendo uma solução de alta disponibilidade e não de escalabilidade de leitura.
- **D:** Incorreta — Uma instância maior continua sendo um ponto único de falha.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

**Referência prática:** ../labs/README.md — RDS Multi-AZ e read replica

**Exercício recomendado:** No lab RDS Multi-AZ e read replica, monte uma prova de conceito de RDS Multi-AZ; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. ALB e Auto Scaling multi-AZ

> **ID:** `QUIZ-D2-08-Q03` · **Domínio:** D2 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A empresa de geoprocessamento mapa vivo quer substituir um componente autogerenciado por um serviço gerenciado. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Uma aplicação HTTP stateless precisa continuar disponível quando uma instância ou uma AZ falhar e deve ajustar capacidade conforme o volume de requisições. Qual arquitetura escolher? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Usar somente DNS round-robin com endereços fixos e sem Auto Scaling.
- **B)** Executar uma única instância grande e reiniciá-la com um cron job.
- **C)** Colocar duas instâncias na mesma AZ sem health check.
- **D)** ALB em pelo menos duas AZs, Auto Scaling group distribuído nessas AZs e target tracking baseado em uma métrica apropriada.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

O ALB encaminha apenas para targets saudáveis e o Auto Scaling substitui capacidade e distribui instâncias entre AZs, eliminando pontos únicos no tier web.

Trade-off: Sessões devem ficar fora das instâncias ou usar um armazenamento compartilhado; sticky sessions podem ajudar temporariamente, mas reduzem flexibilidade e não substituem estado externo. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Vários caixas trabalham em lojas de bairros diferentes; um organizador manda clientes só aos caixas abertos e chama reforço quando a fila cresce.

**Se acertou:** Acertou: O ALB encaminha apenas para targets saudáveis e o Auto Scaling substitui capacidade e distribui instâncias entre AZs, eliminando pontos únicos no tier web. Quando outra opção poderia valer: Sessões devem ficar fora das instâncias ou usar um armazenamento compartilhado; sticky sessions podem ajudar temporariamente, mas reduzem flexibilidade e não substituem estado externo. Mnemônica: associe “ALB e Auto Scaling multi-AZ” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — DNS não substitui health checks do balanceador nem reposição e ajuste automático de capacidade.
- **B:** Incorreta — Ainda há ponto único de falha e recuperação dependente de automação frágil.
- **C:** Incorreta — Uma falha da AZ afeta ambas, e sem health check o tráfego pode chegar a targets defeituosos.
- **D:** Correta — O ALB encaminha apenas para targets saudáveis e o Auto Scaling substitui capacidade e distribui instâncias entre AZs, eliminando pontos únicos no tier web.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html)

**Referência prática:** ../labs/README.md — ALB, Auto Scaling e health checks

**Exercício recomendado:** No lab ALB, Auto Scaling e health checks, monte uma prova de conceito de ALB e Auto Scaling multi-AZ; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 4. Route 53 failover

> **ID:** `QUIZ-D2-08-Q04` · **Domínio:** D2 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A edtech farol vai lançar o serviço em três países. A carga atende milhares de requisições por segundo em horários de pico. Uma aplicação possui um endpoint primário em uma região e um site de recuperação em outra. O DNS deve enviar tráfego ao secundário apenas quando o primário não estiver saudável. Qual política usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Criar registros Route 53 com failover routing, marcar primário/secundário e associar health check ao endpoint primário.
- **B)** Usar geolocation apenas, pois localização detecta falha automaticamente.
- **C)** Aumentar o TTL para 24 horas para acelerar a mudança.
- **D)** Usar simple routing com dois endereços e nenhum health check.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

A política de failover usa a saúde do recurso para responder com o secundário quando o primário falha, implementando active-passive no DNS.

Trade-off: TTL influencia quanto tempo resolvers mantêm respostas antigas; failover DNS não encerra conexões já abertas e deve ser combinado com um plano de dados consistente. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O mapa aponta para a loja principal; se a luz dela apaga, passa a apontar para a loja reserva.

**Se acertou:** Acertou: A política de failover usa a saúde do recurso para responder com o secundário quando o primário falha, implementando active-passive no DNS. Quando outra opção poderia valer: TTL influencia quanto tempo resolvers mantêm respostas antigas; failover DNS não encerra conexões já abertas e deve ser combinado com um plano de dados consistente. Mnemônica: associe “Route 53 failover” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — A política de failover usa a saúde do recurso para responder com o secundário quando o primário falha, implementando active-passive no DNS.
- **B:** Incorreta — Geolocation roteia pela origem do usuário; não é, por si só, política de recuperação por saúde.
- **C:** Incorreta — TTL alto faz caches manterem a resposta anterior por mais tempo, retardando a convergência.
- **D:** Incorreta — Simple routing não fornece o comportamento primário/secundário orientado por saúde.

**Referência oficial:** [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)

**Referência prática:** ../labs/README.md — Failover multi-região e Route 53

**Exercício recomendado:** No lab Failover multi-região e Route 53, monte uma prova de conceito de Route 53 failover; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 5. Desacoplamento com SQS e DLQ

> **ID:** `QUIZ-D2-08-Q05` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A cooperativa campo vivo precisa tomar uma decisão com base em desempenho, segurança e custo total. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Pedidos chegam em rajadas e o processador pode ficar temporariamente indisponível. Nenhum pedido pode ser perdido, falhas repetidas devem ser isoladas e o produtor não deve esperar o processamento. Qual desenho usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Fazer o produtor chamar o processador de forma síncrona com retries infinitos.
- **B)** Enviar pedidos para uma fila SQS, processar com consumidores idempotentes, configurar visibility timeout e redrive para uma DLQ.
- **C)** Publicar somente em uma SNS topic sem qualquer assinatura durável.
- **D)** Gravar pedidos em instance store de uma única EC2.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

SQS armazena mensagens de forma durável e desacopla ritmos; visibility timeout evita processamento concorrente imediato e a DLQ isola mensagens após tentativas definidas.

Trade-off: Standard queues entregam ao menos uma vez e podem duplicar; idempotência é essencial. FIFO deve ser usada apenas quando ordenação estrita/deduplicação justificarem suas restrições. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Os pedidos entram numa caixa de correio; o cozinheiro pega um, e pedidos problemáticos vão para uma bandeja de investigação.

**Se acertou:** Acertou: SQS armazena mensagens de forma durável e desacopla ritmos; visibility timeout evita processamento concorrente imediato e a DLQ isola mensagens após tentativas definidas. Quando outra opção poderia valer: Standard queues entregam ao menos uma vez e podem duplicar; idempotência é essencial. FIFO deve ser usada apenas quando ordenação estrita/deduplicação justificarem suas restrições. Mnemônica: associe “Desacoplamento com SQS e DLQ” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Isso acopla os componentes, prende recursos e pode criar tempestades de retries.
- **B:** Correta — SQS armazena mensagens de forma durável e desacopla ritmos; visibility timeout evita processamento concorrente imediato e a DLQ isola mensagens após tentativas definidas.
- **C:** Incorreta — SNS sozinho não mantém backlog para um consumidor indisponível; uma assinatura SQS adicionaria durabilidade.
- **D:** Incorreta — Instance store é efêmero e a instância continua sendo ponto único de falha.

**Referência oficial:** [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

**Referência prática:** ../labs/README.md — Lambda, filas e tratamento de falhas

**Exercício recomendado:** No lab Lambda, filas e tratamento de falhas, monte uma prova de conceito de Desacoplamento com SQS e DLQ; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---
