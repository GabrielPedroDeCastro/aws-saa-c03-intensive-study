# Mini-quiz 09 — Domínio 2 — Projetar arquiteturas resilientes

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Fan-out com SNS e SQS

> **ID:** `QUIZ-D2-09-Q01` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A companhia aérea ventos precisa corrigir uma descoberta da revisão Well-Architected. A carga atende milhares de requisições por segundo em horários de pico. Cada evento de pedido deve ser processado independentemente por faturamento, estoque e analytics. Se um consumidor parar, os outros devem continuar e o backlog daquele consumidor deve ser preservado. Qual arquitetura é apropriada? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Guardar eventos em logs locais da instância produtora.
- **B)** Usar uma única fila SQS e fazer os três serviços competirem pela mesma mensagem.
- **C)** Publicar em uma SNS topic e criar uma fila SQS separada para cada consumidor, com subscriptions e DLQs próprias.
- **D)** Chamar os três serviços sequencialmente dentro do produtor.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

SNS replica cada mensagem para as filas assinantes; cada SQS mantém seu próprio backlog, ritmo e política de falhas, isolando consumidores.

Trade-off: Uma única fila com três consumidores distribuiria mensagens entre eles, em vez de entregar uma cópia a cada função de negócio. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um locutor anuncia a notícia para três caixas de correio; cada equipe abre a sua quando puder.

**Se acertou:** Acertou: SNS replica cada mensagem para as filas assinantes; cada SQS mantém seu próprio backlog, ritmo e política de falhas, isolando consumidores. Quando outra opção poderia valer: Uma única fila com três consumidores distribuiria mensagens entre eles, em vez de entregar uma cópia a cada função de negócio. Mnemônica: associe “Fan-out com SNS e SQS” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Logs locais não são um canal durável e consumível de integração.
- **B:** Incorreta — Consumidores concorrentes em uma fila recebem mensagens diferentes; não há fan-out por consumidor.
- **C:** Correta — SNS replica cada mensagem para as filas assinantes; cada SQS mantém seu próprio backlog, ritmo e política de falhas, isolando consumidores.
- **D:** Incorreta — A falha ou lentidão de um serviço afeta todos e acopla o produtor aos consumidores.

**Referência oficial:** [https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)

**Referência prática:** ../labs/README.md — Eventos, SNS, SQS e Lambda

**Exercício recomendado:** No lab Eventos, SNS, SQS e Lambda, monte uma prova de conceito de Fan-out com SNS e SQS; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. Estratégias de disaster recovery

> **ID:** `QUIZ-D2-09-Q02` · **Domínio:** D2 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A empresa de geoprocessamento mapa vivo está separando produção e desenvolvimento em contas distintas. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Um sistema regional exige RTO de 15 minutos e RPO de poucos minutos. A empresa aceita manter capacidade reduzida ativa na região de recuperação, mas não quer pagar por uma cópia em escala total. Qual estratégia se encaixa melhor? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Pilot light contendo somente dados, sem automação para subir a aplicação.
- **B)** Multi-site active-active em escala total obrigatoriamente.
- **C)** Backup and restore com backups semanais offline.
- **D)** Warm standby: manter uma versão funcional em escala reduzida na região secundária, replicar dados e escalar durante o failover.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

Warm standby já executa todos os componentes essenciais, reduzindo o RTO em comparação a pilot light sem manter capacidade integral como active-active.

Trade-off: Pilot light custa menos, mas precisa iniciar/implantar parte relevante da aplicação; multi-site active-active oferece RTO menor com maior custo e complexidade. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Há uma lojinha reserva já aberta com poucos caixas; numa emergência, ela chama reforços rapidamente.

**Se acertou:** Acertou: Warm standby já executa todos os componentes essenciais, reduzindo o RTO em comparação a pilot light sem manter capacidade integral como active-active. Quando outra opção poderia valer: Pilot light custa menos, mas precisa iniciar/implantar parte relevante da aplicação; multi-site active-active oferece RTO menor com maior custo e complexidade. Mnemônica: associe “Estratégias de disaster recovery” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — A ausência de componentes e automação torna o RTO incerto e provavelmente maior.
- **B:** Incorreta — Atenderia ou superaria o RTO, mas viola a intenção de evitar custo de capacidade integral quando warm standby basta.
- **C:** Incorreta — Em geral não atende RPO de minutos nem RTO de 15 minutos.
- **D:** Correta — Warm standby já executa todos os componentes essenciais, reduzindo o RTO em comparação a pilot light sem manter capacidade integral como active-active.

**Referência oficial:** [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

**Referência prática:** ../labs/README.md — Cenário de recuperação multi-região

**Exercício recomendado:** No lab Cenário de recuperação multi-região, monte uma prova de conceito de Estratégias de disaster recovery; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. Replicação S3 entre regiões

> **ID:** `QUIZ-D2-09-Q03` · **Domínio:** D2 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A edtech farol precisa atender a uma auditoria sem redesenhar toda a aplicação. A carga atende milhares de requisições por segundo em horários de pico. Objetos de um bucket precisam ser copiados automaticamente para outra região para recuperação. A empresa também quer preservar versões e impedir que uma exclusão acidental destrua imediatamente a cópia histórica. O que configurar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Habilitar versionamento nos buckets, configurar S3 Cross-Region Replication e definir cuidadosamente replicação de delete markers e retenção/Object Lock quando exigido.
- **B)** Usar lifecycle expiration no bucket de origem como mecanismo de cópia.
- **C)** Montar o bucket como EBS e fazer snapshot da instância.
- **D)** Desativar versionamento para reduzir o número de cópias.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

CRR requer versionamento e replica novos objetos conforme as regras. A política de delete markers e mecanismos de retenção determinam o comportamento diante de exclusões.

Trade-off: Replicação não é retroativa por padrão e não substitui toda estratégia de backup; S3 Batch Replication pode tratar objetos existentes. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Cada desenho ganha uma cópia em outra cidade e versões antigas ficam num fichário que uma borracha comum não apaga.

**Se acertou:** Acertou: CRR requer versionamento e replica novos objetos conforme as regras. A política de delete markers e mecanismos de retenção determinam o comportamento diante de exclusões. Quando outra opção poderia valer: Replicação não é retroativa por padrão e não substitui toda estratégia de backup; S3 Batch Replication pode tratar objetos existentes. Mnemônica: associe “Replicação S3 entre regiões” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — CRR requer versionamento e replica novos objetos conforme as regras. A política de delete markers e mecanismos de retenção determinam o comportamento diante de exclusões.
- **B:** Incorreta — Lifecycle gerencia transição/expiração e não replica objetos para outra região.
- **C:** Incorreta — S3 não é montado como volume EBS, e snapshot de EC2 não protege objetos do bucket.
- **D:** Incorreta — CRR exige versionamento e desativá-lo prejudica recuperação de alterações/exclusões.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

**Referência prática:** ../labs/README.md — S3 versionado e recuperação

**Exercício recomendado:** No lab S3 versionado e recuperação, monte uma prova de conceito de Replicação S3 entre regiões; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 4. Amazon EFS Regional

> **ID:** `QUIZ-D2-09-Q04` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A cooperativa campo vivo precisa corrigir uma descoberta da revisão Well-Architected. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Um conjunto de instâncias Linux em várias AZs precisa compartilhar arquivos POSIX. Os dados devem permanecer acessíveis quando uma instância ou uma AZ falhar, sem gerenciar servidores de arquivos. Qual armazenamento usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Hospedar um servidor NFS único em EC2 sem standby.
- **B)** Amazon EFS Regional montado pelos clientes nas diferentes AZs, com mount targets e security groups adequados.
- **C)** Usar um único volume EBS em uma AZ e anexá-lo simultaneamente a qualquer número de instâncias Linux.
- **D)** Usar instance store e copiar arquivos manualmente à noite.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

EFS Regional fornece sistema de arquivos gerenciado, elástico e multi-AZ, adequado ao compartilhamento simultâneo entre instâncias Linux.

Trade-off: EFS One Zone pode custar menos, mas não atende ao requisito de tolerância à perda de uma AZ. EBS é zonal e normalmente anexado a uma instância. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É uma estante compartilhada com portas em vários bairros; se uma porta fecha, as outras ainda chegam aos livros.

**Se acertou:** Acertou: EFS Regional fornece sistema de arquivos gerenciado, elástico e multi-AZ, adequado ao compartilhamento simultâneo entre instâncias Linux. Quando outra opção poderia valer: EFS One Zone pode custar menos, mas não atende ao requisito de tolerância à perda de uma AZ. EBS é zonal e normalmente anexado a uma instância. Mnemônica: associe “Amazon EFS Regional” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — O servidor seria ponto único de falha e exigiria administração.
- **B:** Correta — EFS Regional fornece sistema de arquivos gerenciado, elástico e multi-AZ, adequado ao compartilhamento simultâneo entre instâncias Linux.
- **C:** Incorreta — EBS é zonal e Multi-Attach possui tipos e cenários restritos; não vira um sistema de arquivos regional gerenciado.
- **D:** Incorreta — Instance store é efêmero e a cópia manual não dá consistência nem alta disponibilidade.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html)

**Referência prática:** ../labs/README.md — Armazenamento compartilhado multi-AZ

**Exercício recomendado:** No lab Armazenamento compartilhado multi-AZ, monte uma prova de conceito de Amazon EFS Regional; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 5. Aurora Global Database

> **ID:** `QUIZ-D2-09-Q05` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A companhia aérea ventos está separando produção e desenvolvimento em contas distintas. A carga atende milhares de requisições por segundo em horários de pico. Uma aplicação de leitura global baseada em Aurora precisa latência local em regiões secundárias e recuperação regional com replicação rápida. Escritas permanecem centralizadas durante operação normal. Qual recurso escolher? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Exportar snapshots manualmente uma vez por mês.
- **B)** Colocar o endpoint regional atrás de CloudFront para armazenar respostas SQL em cache.
- **C)** Usar Aurora Global Database com cluster primário gravável e clusters secundários de leitura nas regiões necessárias.
- **D)** Usar apenas Multi-AZ no cluster primário e esperar endpoints de leitura em outras regiões.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Aurora Global Database usa replicação dedicada entre regiões, oferece leituras locais e permite promover uma região secundária em um evento de recuperação.

Trade-off: A promoção e o roteamento da aplicação ainda precisam ser planejados. Multi-AZ protege dentro de uma região e não fornece, sozinho, leituras globais. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O livro mestre é escrito numa cidade, enquanto cópias quase instantâneas chegam às bibliotecas do mundo.

**Se acertou:** Acertou: Aurora Global Database usa replicação dedicada entre regiões, oferece leituras locais e permite promover uma região secundária em um evento de recuperação. Quando outra opção poderia valer: A promoção e o roteamento da aplicação ainda precisam ser planejados. Multi-AZ protege dentro de uma região e não fornece, sozinho, leituras globais. Mnemônica: associe “Aurora Global Database” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Snapshots mensais não oferecem replicação contínua nem RPO/RTO compatíveis.
- **B:** Incorreta — CloudFront não se conecta diretamente a um protocolo de banco e não cria réplicas do Aurora.
- **C:** Correta — Aurora Global Database usa replicação dedicada entre regiões, oferece leituras locais e permite promover uma região secundária em um evento de recuperação.
- **D:** Incorreta — Multi-AZ oferece resiliência regional, não clusters de leitura entre regiões.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

**Referência prática:** ../labs/README.md — RDS/Aurora, réplicas e failover

**Exercício recomendado:** No lab RDS/Aurora, réplicas e failover, monte uma prova de conceito de Aurora Global Database; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---
