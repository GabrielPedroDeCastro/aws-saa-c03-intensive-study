# Mini-quiz 10 — Domínio 2 — Projetar arquiteturas resilientes

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. DynamoDB Global Tables

> **ID:** `QUIZ-D2-10-Q01` · **Domínio:** D2 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A empresa de geoprocessamento mapa vivo está migrando uma carga crítica para a AWS. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Usuários em duas regiões precisam ler e gravar em uma tabela DynamoDB com baixa latência local. A aplicação aceita consistência eventual entre regiões e deve continuar gravando se uma região falhar. Qual solução usar? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Criar uma tabela comum em uma única região e usar Multi-AZ manualmente.
- **B)** Adicionar DAX em duas regiões sem replicar a tabela.
- **C)** Fazer backup diário e restaurar em cada falha regional.
- **D)** Criar uma DynamoDB global table no modo de consistência eventual multi-região (MREC) e tornar a aplicação tolerante à resolução last-writer-wins.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

Global Tables em MREC fornecem replicação multi-active gerenciada, permitindo leitura e gravação locais nas regiões participantes.

Trade-off: No modo MREC, conflitos concorrentes usam last-writer-wins e a aplicação deve entender essa semântica. O modo MRSC oferece consistência forte multi-região com outra semântica, topologia e disponibilidade regional; a escolha depende do requisito de consistência. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** São dois cadernos mágicos: dá para escrever em qualquer cidade e as novidades aparecem no outro.

**Se acertou:** Acertou: Global Tables em MREC fornecem replicação multi-active gerenciada, permitindo leitura e gravação locais nas regiões participantes. Quando outra opção poderia valer: No modo MREC, conflitos concorrentes usam last-writer-wins e a aplicação deve entender essa semântica. O modo MRSC oferece consistência forte multi-região com outra semântica, topologia e disponibilidade regional; a escolha depende do requisito de consistência. Mnemônica: associe “DynamoDB Global Tables” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — DynamoDB já é multi-AZ na região, mas isso não fornece gravações locais em duas regiões.
- **B:** Incorreta — DAX é cache regional e não torna a tabela multi-region ou multi-active.
- **C:** Incorreta — Backup/restauração não atende baixa latência local nem continuidade de gravações com RTO curto.
- **D:** Correta — Global Tables em MREC fornecem replicação multi-active gerenciada, permitindo leitura e gravação locais nas regiões participantes.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html)

**Referência prática:** ../labs/README.md — DynamoDB, DAX e desenho de chaves

**Exercício recomendado:** No lab DynamoDB, DAX e desenho de chaves, monte uma prova de conceito de DynamoDB Global Tables; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. Falhas assíncronas do Lambda

> **ID:** `QUIZ-D2-10-Q02` · **Domínio:** D2 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A edtech farol deve manter a solução simples para a equipe de plantão. A carga atende milhares de requisições por segundo em horários de pico. Uma função Lambda é invocada de modo assíncrono por eventos. Após as tentativas automáticas, eventos malsucedidos devem ser preservados para investigação e reprocessamento, sem bloquear eventos saudáveis. O que configurar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Configurar uma on-failure destination para SQS/SNS/EventBridge ou uma DLQ compatível, além de alarmes e processamento idempotente.
- **B)** Reenviar o mesmo evento recursivamente dentro da função sem limite.
- **C)** Definir timeout infinito para garantir que toda execução termine.
- **D)** Desativar logs para impedir que falhas afetem o serviço.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Invocações assíncronas possuem fila e retries gerenciados; destinations entregam contexto do resultado após as tentativas, permitindo análise e reprocessamento desacoplado.

Trade-off: DLQ e destination têm formatos e capacidades diferentes; a equipe deve escolher um, observar idade máxima do evento e evitar loops de reprocessamento. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Cartinhas que o robô não consegue ler vão para uma caixa vermelha, sem parar a leitura das demais.

**Se acertou:** Acertou: Invocações assíncronas possuem fila e retries gerenciados; destinations entregam contexto do resultado após as tentativas, permitindo análise e reprocessamento desacoplado. Quando outra opção poderia valer: DLQ e destination têm formatos e capacidades diferentes; a equipe deve escolher um, observar idade máxima do evento e evitar loops de reprocessamento. Mnemônica: associe “Falhas assíncronas do Lambda” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Invocações assíncronas possuem fila e retries gerenciados; destinations entregam contexto do resultado após as tentativas, permitindo análise e reprocessamento desacoplado.
- **B:** Incorreta — Isso pode criar loop, duplicidade e custo sem isolar o evento defeituoso.
- **C:** Incorreta — Lambda tem limite de timeout e aumentar duração não resolve eventos permanentemente inválidos.
- **D:** Incorreta — Logs não causam a falha e removê-los prejudica diagnóstico e observabilidade.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html)

**Referência prática:** ../labs/README.md — Lambda, API Gateway e tratamento de erros

**Exercício recomendado:** No lab Lambda, API Gateway e tratamento de erros, monte uma prova de conceito de Falhas assíncronas do Lambda; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. Políticas centralizadas com AWS Backup

> **ID:** `QUIZ-D2-10-Q03` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A cooperativa campo vivo recebe picos imprevisíveis sem poder degradar o SLA. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Dezenas de contas precisam de backups consistentes de EBS, RDS e EFS, cópias entre regiões e proteção contra exclusão pela conta de origem. Segurança quer governança central. Qual abordagem usar? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 4. RDS Multi-AZ

> **ID:** `QUIZ-D2-10-Q04` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A companhia aérea ventos está migrando uma carga crítica para a AWS. A carga atende milhares de requisições por segundo em horários de pico. Um banco transacional RDS precisa recuperar automaticamente de falha de instância ou de AZ, preservando o mesmo endpoint. A carga de leitura não é o problema principal. Qual configuração atende ao requisito? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 5. ALB e Auto Scaling multi-AZ

> **ID:** `QUIZ-D2-10-Q05` · **Domínio:** D2 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A empresa de geoprocessamento mapa vivo deve manter a solução simples para a equipe de plantão. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Uma aplicação HTTP stateless precisa continuar disponível quando uma instância ou uma AZ falhar e deve ajustar capacidade conforme o volume de requisições. Qual arquitetura escolher? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

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
