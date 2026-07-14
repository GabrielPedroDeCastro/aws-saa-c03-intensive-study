# Mini-quiz 04 — Domínio 4 — Projetar arquiteturas otimizadas em custos

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Custo de NAT e VPC endpoints

> **ID:** `QUIZ-D4-04-Q01` · **Domínio:** D4 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

O marketplace beija-flor precisa tomar uma decisão com base em desempenho, segurança e custo total. A carga atende milhares de requisições por segundo em horários de pico. Instâncias privadas baixam terabytes mensalmente do S3 através de NAT Gateways. A fatura mostra alto processamento de dados no NAT. Como reduzir o custo mantendo caminho privado? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Dar IP público às instâncias e remover todos os controles de saída.
- **B)** Mover objetos para EBS em uma única instância para evitar S3.
- **C)** Adicionar mais NAT Gateways e continuar roteando S3 por todos eles.
- **D)** Criar Gateway VPC Endpoint para S3, atualizar route tables/policies e manter o NAT apenas para destinos que realmente exigem internet.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

O endpoint de gateway para S3 evita o processamento pelo NAT e não possui cobrança por hora, reduzindo custo e simplificando o caminho privado.

Trade-off: Interface endpoints para outros serviços cobram por hora e dados, então seu custo deve ser comparado ao NAT e ao volume por AZ; alta disponibilidade do NAT também importa. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Abrimos uma porta direta e gratuita para o depósito, então os caminhões não pagam mais o pedágio da estrada geral.

**Se acertou:** Acertou: O endpoint de gateway para S3 evita o processamento pelo NAT e não possui cobrança por hora, reduzindo custo e simplificando o caminho privado. Quando outra opção poderia valer: Interface endpoints para outros serviços cobram por hora e dados, então seu custo deve ser comparado ao NAT e ao volume por AZ; alta disponibilidade do NAT também importa. Mnemônica: associe “Custo de NAT e VPC endpoints” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Isso altera a postura de segurança e não mantém o caminho privado.
- **B:** Incorreta — EBS não substitui armazenamento de objetos escalável e cria capacidade, disponibilidade e operação adicionais.
- **C:** Incorreta — Isso pode melhorar resiliência, mas não remove a cobrança de processamento responsável pelo custo.
- **D:** Correta — O endpoint de gateway para S3 evita o processamento pelo NAT e não possui cobrança por hora, reduzindo custo e simplificando o caminho privado.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Referência prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

**Exercício recomendado:** No lab VPC multi-AZ, NAT e endpoints, monte uma prova de conceito de Custo de NAT e VPC endpoints; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. AWS Compute Optimizer

> **ID:** `QUIZ-D4-04-Q02` · **Domínio:** D4 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

O banco digital pioneiro quer substituir um componente autogerenciado por um serviço gerenciado. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Centenas de instâncias EC2 têm baixa utilização, mas a equipe não sabe quais podem ser reduzidas sem risco de memória ou performance. Ela quer recomendações baseadas em métricas antes de mudar tamanhos. Qual serviço usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Ativar AWS Compute Optimizer, garantir métricas suficientes (incluindo memória com agente quando necessário) e testar as recomendações de rightsizing.
- **B)** Reduzir todas as instâncias para t3.micro sem medir.
- **C)** Comprar Reserved Instances para todos os tamanhos atuais antes do rightsizing.
- **D)** Usar AWS Budgets como ferramenta de benchmark de CPU e memória.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Compute Optimizer analisa métricas e oferece recomendações de tipo/tamanho e risco; a validação em carga real evita reduzir capacidade cegamente.

Trade-off: Cost Explorer Rightsizing também ajuda na visão de custo. Recomendações são insumo, não autorização automática: sazonalidade, licenças e limites de rede precisam ser considerados. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um treinador observa cada atleta e sugere um tênis do tamanho certo, em vez de comprar o maior para todos.

**Se acertou:** Acertou: Compute Optimizer analisa métricas e oferece recomendações de tipo/tamanho e risco; a validação em carga real evita reduzir capacidade cegamente. Quando outra opção poderia valer: Cost Explorer Rightsizing também ajuda na visão de custo. Recomendações são insumo, não autorização automática: sazonalidade, licenças e limites de rede precisam ser considerados. Mnemônica: associe “AWS Compute Optimizer” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Compute Optimizer analisa métricas e oferece recomendações de tipo/tamanho e risco; a validação em carga real evita reduzir capacidade cegamente.
- **B:** Incorreta — Uma regra única ignora CPU, memória, rede, burst e requisitos diferentes.
- **C:** Incorreta — Isso pode comprometer gasto em capacidade superdimensionada.
- **D:** Incorreta — Budgets alerta sobre custo/uso, mas não faz análise técnica de dimensionamento.

**Referência oficial:** [https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

**Referência prática:** ../labs/README.md — Observabilidade e rightsizing

**Exercício recomendado:** No lab Observabilidade e rightsizing, monte uma prova de conceito de AWS Compute Optimizer; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. Capacidade do DynamoDB

> **ID:** `QUIZ-D4-04-Q03` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A universidade saber vai lançar o serviço em três países. A carga atende milhares de requisições por segundo em horários de pico. Uma tabela nova tem tráfego imprevisível e pode ficar horas ociosa antes de picos abruptos. A equipe não conhece a capacidade necessária e quer evitar administração inicial. Qual modo escolher? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 4. Snapshots EBS com Data Lifecycle Manager

> **ID:** `QUIZ-D4-04-Q04` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A proptech janela precisa tomar uma decisão com base em desempenho, segurança e custo total. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Volumes EBS precisam de snapshots diários, retenção por 35 dias e exclusão automática dos antigos. O processo atual usa scripts em uma instância que frequentemente falha. Qual opção reduz operação e custo? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 5. AWS Budgets e Cost Explorer

> **ID:** `QUIZ-D4-04-Q05` · **Domínio:** D4 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

O marketplace beija-flor quer substituir um componente autogerenciado por um serviço gerenciado. A carga atende milhares de requisições por segundo em horários de pico. FinOps precisa alertar quando a previsão mensal ultrapassar o orçamento e depois investigar quais serviços e tags explicam a variação. Qual combinação usar? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

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
