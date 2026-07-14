# Mini-quiz 02 — Domínio 4 — Projetar arquiteturas otimizadas em custos

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Capacidade do DynamoDB

> **ID:** `QUIZ-D4-02-Q01` · **Domínio:** D4 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A universidade saber está migrando uma carga crítica para a AWS. A carga atende milhares de requisições por segundo em horários de pico. Uma tabela nova tem tráfego imprevisível e pode ficar horas ociosa antes de picos abruptos. A equipe não conhece a capacidade necessária e quer evitar administração inicial. Qual modo escolher? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Executar DynamoDB em uma EC2 Spot para pagar menos.
- **B)** Começar com DynamoDB on-demand e, quando o padrão se tornar previsível e sustentado, comparar com provisioned capacity e auto scaling.
- **C)** Provisionar imediatamente o pico teórico máximo 24x7 sem métricas.
- **D)** Escolher uma chave constante porque on-demand elimina hot partitions.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

On-demand cobra por requisição e ajusta capacidade automaticamente, sendo adequado a cargas novas, variáveis ou intermitentes sem planejamento de throughput.

Trade-off: Provisioned pode custar menos em uso estável e previsível, especialmente com auto scaling e reserved capacity elegível. Hot keys continuam sendo problema de modelagem. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Pagamos cada passeio quando alguém chega, sem manter um ônibus vazio esperando o dia inteiro.

**Se acertou:** Acertou: On-demand cobra por requisição e ajusta capacidade automaticamente, sendo adequado a cargas novas, variáveis ou intermitentes sem planejamento de throughput. Quando outra opção poderia valer: Provisioned pode custar menos em uso estável e previsível, especialmente com auto scaling e reserved capacity elegível. Hot keys continuam sendo problema de modelagem. Mnemônica: associe “Capacidade do DynamoDB” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — DynamoDB é serviço gerenciado e não é implantado pelo cliente em EC2.
- **B:** Correta — On-demand cobra por requisição e ajusta capacidade automaticamente, sendo adequado a cargas novas, variáveis ou intermitentes sem planejamento de throughput.
- **C:** Incorreta — Isso tende a pagar capacidade ociosa durante a maior parte do tempo.
- **D:** Incorreta — Modo de capacidade não corrige uma chave de partição mal distribuída.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)

**Referência prática:** ../labs/README.md — DynamoDB, DAX e capacidade

**Exercício recomendado:** No lab DynamoDB, DAX e capacidade, monte uma prova de conceito de Capacidade do DynamoDB; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. Snapshots EBS com Data Lifecycle Manager

> **ID:** `QUIZ-D4-02-Q02` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A proptech janela deve manter a solução simples para a equipe de plantão. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Volumes EBS precisam de snapshots diários, retenção por 35 dias e exclusão automática dos antigos. O processo atual usa scripts em uma instância que frequentemente falha. Qual opção reduz operação e custo? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Usar instance store como destino durável dos backups.
- **B)** Criar uma instância maior apenas para executar o cron de snapshots.
- **C)** Usar Amazon Data Lifecycle Manager com tags para criar e expirar snapshots segundo a política.
- **D)** Manter todos os snapshots para sempre porque snapshots incrementais não custam.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

DLM automatiza ciclo de vida de snapshots EBS e AMIs com seleção por tags, eliminando servidor de agendamento e acúmulo indefinido.

Trade-off: Snapshots são incrementais no armazenamento, mas cada snapshot aparece como ponto completo de restauração. A política precisa respeitar retenção e testes de restore. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um robô fotografa os cadernos todo dia e descarta sozinho as fotos que passaram do prazo.

**Se acertou:** Acertou: DLM automatiza ciclo de vida de snapshots EBS e AMIs com seleção por tags, eliminando servidor de agendamento e acúmulo indefinido. Quando outra opção poderia valer: Snapshots são incrementais no armazenamento, mas cada snapshot aparece como ponto completo de restauração. A política precisa respeitar retenção e testes de restore. Mnemônica: associe “Snapshots EBS com Data Lifecycle Manager” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Instance store é efêmero e não é serviço de backup.
- **B:** Incorreta — Isso aumenta custo e mantém uma automação desnecessariamente autogerenciada.
- **C:** Correta — DLM automatiza ciclo de vida de snapshots EBS e AMIs com seleção por tags, eliminando servidor de agendamento e acúmulo indefinido.
- **D:** Incorreta — Blocos exclusivos ainda ocupam armazenamento e retenção infinita gera custo.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)

**Referência prática:** ../labs/README.md — EBS, snapshots e recuperação

**Exercício recomendado:** No lab EBS, snapshots e recuperação, monte uma prova de conceito de Snapshots EBS com Data Lifecycle Manager; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. AWS Budgets e Cost Explorer

> **ID:** `QUIZ-D4-02-Q03` · **Domínio:** D4 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

O marketplace beija-flor recebe picos imprevisíveis sem poder degradar o SLA. A carga atende milhares de requisições por segundo em horários de pico. FinOps precisa alertar quando a previsão mensal ultrapassar o orçamento e depois investigar quais serviços e tags explicam a variação. Qual combinação usar? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Usar CloudTrail sozinho para calcular a previsão da fatura.
- **B)** Usar security groups para impedir qualquer recurso de gerar custo.
- **C)** Esperar a fatura fechar e analisar apenas uma vez por ano.
- **D)** Configurar AWS Budgets com alertas de custo previsto/real e usar Cost Explorer para analisar tendências, filtros, grupos e relatórios.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

Budgets compara gasto/uso com limites e envia alertas; Cost Explorer permite explorar a composição e a evolução dos custos.

Trade-off: Cost Anomaly Detection complementa com alertas de padrões incomuns. Tags precisam ser ativadas como cost allocation tags e a organização deve manter governança de marcação. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O alarme avisa que a mesada vai estourar, e a lupa mostra em quais brinquedos o dinheiro foi gasto.

**Se acertou:** Acertou: Budgets compara gasto/uso com limites e envia alertas; Cost Explorer permite explorar a composição e a evolução dos custos. Quando outra opção poderia valer: Cost Anomaly Detection complementa com alertas de padrões incomuns. Tags precisam ser ativadas como cost allocation tags e a organização deve manter governança de marcação. Mnemônica: associe “AWS Budgets e Cost Explorer” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — CloudTrail registra APIs e não é ferramenta de previsão e análise financeira.
- **B:** Incorreta — Security groups controlam rede e não funcionam como orçamento ou governança financeira.
- **C:** Incorreta — Isso elimina alerta precoce e capacidade de correção durante o período.
- **D:** Correta — Budgets compara gasto/uso com limites e envia alertas; Cost Explorer permite explorar a composição e a evolução dos custos.

**Referência oficial:** [https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)

**Referência prática:** ../labs/README.md — Budgets, tags e análise de custos

**Exercício recomendado:** No lab Budgets, tags e análise de custos, monte uma prova de conceito de AWS Budgets e Cost Explorer; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 4. S3 Intelligent-Tiering

> **ID:** `QUIZ-D4-02-Q04` · **Domínio:** D4 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

O banco digital pioneiro está migrando uma carga crítica para a AWS. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Milhões de objetos têm padrões de acesso desconhecidos e mudam ao longo do tempo. A aplicação exige acesso em milissegundos aos objetos ativos, e a equipe não quer criar regras por prefixo. Qual classe considerar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Usar S3 Intelligent-Tiering, habilitando tiers de archive opcionais apenas se a latência de recuperação for aceitável.
- **B)** Usar EBS io2 para armazenar todos os objetos desconhecidos.
- **C)** Colocar tudo diretamente em Glacier Deep Archive e exigir leitura imediata.
- **D)** Duplicar cada objeto em todas as classes de armazenamento.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Intelligent-Tiering monitora acesso e move objetos entre tiers automáticos sem cobrança de recuperação nos tiers de acesso frequente/infrequente, cobrando pequena taxa de monitoramento.

Trade-off: Objetos menores que 128 KB não são monitorados nem movidos automaticamente e permanecem no tier Frequent Access. Archive Access/Deep Archive Access têm recuperação assíncrona e devem ser habilitados conscientemente. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um bibliotecário observa quais livros são lidos e muda sozinho os pouco usados para estantes mais baratas.

**Se acertou:** Acertou: Intelligent-Tiering monitora acesso e move objetos entre tiers automáticos sem cobrança de recuperação nos tiers de acesso frequente/infrequente, cobrando pequena taxa de monitoramento. Quando outra opção poderia valer: Objetos menores que 128 KB não são monitorados nem movidos automaticamente e permanecem no tier Frequent Access. Archive Access/Deep Archive Access têm recuperação assíncrona e devem ser habilitados conscientemente. Mnemônica: associe “S3 Intelligent-Tiering” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Intelligent-Tiering monitora acesso e move objetos entre tiers automáticos sem cobrança de recuperação nos tiers de acesso frequente/infrequente, cobrando pequena taxa de monitoramento.
- **B:** Incorreta — EBS provisionado seria mais caro e não oferece a semântica/escala de armazenamento de objetos.
- **C:** Incorreta — Deep Archive não oferece recuperação em milissegundos.
- **D:** Incorreta — Isso multiplica custo e não automatiza seleção do tier apropriado.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)

**Referência prática:** ../labs/README.md — S3, lifecycle e classes de armazenamento

**Exercício recomendado:** No lab S3, lifecycle e classes de armazenamento, monte uma prova de conceito de S3 Intelligent-Tiering; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 5. Arquitetura serverless para carga esporádica

> **ID:** `QUIZ-D4-02-Q05` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A universidade saber deve manter a solução simples para a equipe de plantão. A carga atende milhares de requisições por segundo em horários de pico. Uma API recebe poucas chamadas na maior parte do dia e picos curtos imprevisíveis. Não mantém conexões longas nem estado local. A equipe quer pagar principalmente por uso e não administrar servidores. Qual arquitetura é adequada? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Usar Dedicated Hosts para cada requisição.
- **B)** API Gateway com Lambda e um armazenamento serverless apropriado, configurando limites, observabilidade e controle de concorrência.
- **C)** Executar a API em um NAT Gateway.
- **D)** Manter dez instâncias On-Demand grandes 24x7 para o pico raro.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

Serviços serverless escalam sob demanda e cobram por requisição/execução, evitando instâncias ociosas para uma carga esporádica.

Trade-off: Em carga alta e constante, contêineres/instâncias bem utilizados podem custar menos. Cold starts, limites de execução e dependências precisam ser avaliados. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** A barraca abre e chama ajudantes só quando chegam clientes, em vez de pagar uma equipe vazia o dia inteiro.

**Se acertou:** Acertou: Serviços serverless escalam sob demanda e cobram por requisição/execução, evitando instâncias ociosas para uma carga esporádica. Quando outra opção poderia valer: Em carga alta e constante, contêineres/instâncias bem utilizados podem custar menos. Cold starts, limites de execução e dependências precisam ser avaliados. Mnemônica: associe “Arquitetura serverless para carga esporádica” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Hosts dedicados são inadequados à granularidade e aumentariam drasticamente o custo.
- **B:** Correta — Serviços serverless escalam sob demanda e cobram por requisição/execução, evitando instâncias ociosas para uma carga esporádica.
- **C:** Incorreta — NAT Gateway é serviço de tradução de endereços, não runtime de aplicação.
- **D:** Incorreta — A maior parte da capacidade ficaria ociosa e paga.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html](https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html)

**Referência prática:** ../labs/README.md — Lambda, API Gateway e IAM roles

**Exercício recomendado:** No lab Lambda, API Gateway e IAM roles, monte uma prova de conceito de Arquitetura serverless para carga esporádica; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---
