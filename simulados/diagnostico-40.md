# Simulado diagnóstico — 40 questões

- **Tipo:** diagnóstico inicial
- **Questões:** 40
- **Tempo sugerido:** 75 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Acesso entre contas com IAM Roles

> **ID:** `DIAG-Q001` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

O banco digital pioneiro precisa corrigir uma descoberta da revisão Well-Architected. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Uma aplicação na conta de produção precisa ler objetos de um bucket pertencente à conta de dados, sem armazenar chaves de acesso. O acesso deve ser temporário, auditável e seguir privilégio mínimo. Qual solução atende melhor? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Criar uma IAM Role na conta de dados, confiar na role da aplicação e usar AWS STS AssumeRole com política limitada ao bucket.
- **B)** Tornar o bucket público e restringir o endereço IP na aplicação.
- **C)** Compartilhar a senha do usuário raiz da conta de dados pelo Secrets Manager.
- **D)** Criar um usuário IAM na conta de dados e copiar access key e secret key para a instância.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

AssumeRole entrega credenciais temporárias e separa a política de confiança da política de permissões, permitindo acesso entre contas sem segredo de longa duração.

Trade-off: Uma bucket policy também participa do controle de acesso, mas a role com STS é a opção central quando a aplicação precisa de uma identidade temporária na outra conta. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É como dar um crachá de visitante que abre só uma sala e expira no fim da visita.

**Se acertou:** Acertou: AssumeRole entrega credenciais temporárias e separa a política de confiança da política de permissões, permitindo acesso entre contas sem segredo de longa duração. Quando outra opção poderia valer: Uma bucket policy também participa do controle de acesso, mas a role com STS é a opção central quando a aplicação precisa de uma identidade temporária na outra conta. Mnemônica: associe “Acesso entre contas com IAM Roles” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — AssumeRole entrega credenciais temporárias e separa a política de confiança da política de permissões, permitindo acesso entre contas sem segredo de longa duração.
- **B:** Incorreta — Exposição pública viola o requisito e endereço IP não substitui autenticação e autorização.
- **C:** Incorreta — Credenciais do usuário raiz não devem ser usadas por aplicações, mesmo quando armazenadas em um cofre.
- **D:** Incorreta — Chaves de longa duração aumentam o risco de vazamento e exigem rotação; não são necessárias para workloads na AWS.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

**Referência prática:** ../labs/README.md — Lambda/API Gateway com IAM e acesso entre contas

**Exercício recomendado:** No lab Lambda/API Gateway com IAM e acesso entre contas, monte uma prova de conceito de Acesso entre contas com IAM Roles; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. Route 53 failover

> **ID:** `DIAG-Q002` · **Domínio:** D2 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A seguradora atlântico está separando produção e desenvolvimento em contas distintas. A equipe precisa provar a decisão com um teste pequeno e reversível. Uma aplicação possui um endpoint primário em uma região e um site de recuperação em outra. O DNS deve enviar tráfego ao secundário apenas quando o primário não estiver saudável. Qual política usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Usar geolocation apenas, pois localização detecta falha automaticamente.
- **B)** Criar registros Route 53 com failover routing, marcar primário/secundário e associar health check ao endpoint primário.
- **C)** Aumentar o TTL para 24 horas para acelerar a mudança.
- **D)** Usar simple routing com dois endereços e nenhum health check.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

A política de failover usa a saúde do recurso para responder com o secundário quando o primário falha, implementando active-passive no DNS.

Trade-off: TTL influencia quanto tempo resolvers mantêm respostas antigas; failover DNS não encerra conexões já abertas e deve ser combinado com um plano de dados consistente. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O mapa aponta para a loja principal; se a luz dela apaga, passa a apontar para a loja reserva.

**Se acertou:** Acertou: A política de failover usa a saúde do recurso para responder com o secundário quando o primário falha, implementando active-passive no DNS. Quando outra opção poderia valer: TTL influencia quanto tempo resolvers mantêm respostas antigas; failover DNS não encerra conexões já abertas e deve ser combinado com um plano de dados consistente. Mnemônica: associe “Route 53 failover” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Geolocation roteia pela origem do usuário; não é, por si só, política de recuperação por saúde.
- **B:** Correta — A política de failover usa a saúde do recurso para responder com o secundário quando o primário falha, implementando active-passive no DNS.
- **C:** Incorreta — TTL alto faz caches manterem a resposta anterior por mais tempo, retardando a convergência.
- **D:** Incorreta — Simple routing não fornece o comportamento primário/secundário orientado por saúde.

**Referência oficial:** [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)

**Referência prática:** ../labs/README.md — Failover multi-região e Route 53

**Exercício recomendado:** No lab Failover multi-região e Route 53, monte uma prova de conceito de Route 53 failover; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. Chave de partição do DynamoDB

> **ID:** `DIAG-Q003` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

O banco digital pioneiro precisa atender a uma auditoria sem redesenhar toda a aplicação. A carga atende milhares de requisições por segundo em horários de pico. Uma tabela DynamoDB recebe gravações intensas. A chave de partição atual usa apenas o código de um país, e um país concentra 80% do tráfego, causando throttling. Qual redesign é mais apropriado? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Adicionar apenas mais atributos sem alterar chaves ou índices.
- **B)** Manter o país como única chave e aumentar o tamanho de uma instância DynamoDB.
- **C)** Escolher uma chave de alta cardinalidade que distribua acessos, usando write sharding quando necessário, e manter padrões de consulta com índices adequados.
- **D)** Criar uma chave constante para garantir ordem global.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

DynamoDB distribui itens pela chave de partição; poucas chaves populares concentram capacidade. Alta cardinalidade e sharding espalham as requisições.

Trade-off: On-demand ajusta capacidade, mas não elimina todos os efeitos de uma hot partition. O modelo deve começar pelos padrões de acesso, não por normalização relacional. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Se todos entrarem pela mesma porta, forma fila; várias portas bem escolhidas distribuem a turma.

**Se acertou:** Acertou: DynamoDB distribui itens pela chave de partição; poucas chaves populares concentram capacidade. Alta cardinalidade e sharding espalham as requisições. Quando outra opção poderia valer: On-demand ajusta capacidade, mas não elimina todos os efeitos de uma hot partition. O modelo deve começar pelos padrões de acesso, não por normalização relacional. Mnemônica: associe “Chave de partição do DynamoDB” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Atributos extras não mudam a distribuição das requisições.
- **B:** Incorreta — DynamoDB é serverless e não expõe tamanho de instância; a chave quente continua problemática.
- **C:** Correta — DynamoDB distribui itens pela chave de partição; poucas chaves populares concentram capacidade. Alta cardinalidade e sharding espalham as requisições.
- **D:** Incorreta — Uma única chave concentra toda a carga em uma partição lógica.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)

**Referência prática:** ../labs/README.md — DynamoDB, DAX e modelagem de chaves

**Exercício recomendado:** No lab DynamoDB, DAX e modelagem de chaves, monte uma prova de conceito de Chave de partição do DynamoDB; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 4. RDS Reserved DB Instances

> **ID:** `DIAG-Q004` · **Domínio:** D4 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A healthtech pulso precisa corrigir uma descoberta da revisão Well-Architected. O orçamento é limitado e a operação manual deve ser mínima. Um banco RDS de produção possui classe e região estáveis, funciona continuamente e deve permanecer assim por pelo menos um ano. A empresa quer desconto sem redesenhar a aplicação. O que avaliar? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Comprar Spot Instances para substituir diretamente a instância RDS gerenciada.
- **B)** Criar uma read replica sem carga apenas para obter desconto.
- **C)** Trocar para Multi-AZ exclusivamente para reduzir a fatura pela metade.
- **D)** Adquirir Reserved DB Instance para a configuração/família elegível após validar utilização, prazo e opção de pagamento.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

Reserved DB Instances oferecem desconto de faturamento para uso RDS previsível; não são uma instância física separada e não alteram a arquitetura.

Trade-off: Reserva reduz compute do RDS, mas armazenamento, I/O, backup e transferência podem continuar cobrados. Rightsizing deve vir antes do compromisso. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** A mesma mesa é usada todo dia, então um plano anual sai mais barato que pagar diária.

**Se acertou:** Acertou: Reserved DB Instances oferecem desconto de faturamento para uso RDS previsível; não são uma instância física separada e não alteram a arquitetura. Quando outra opção poderia valer: Reserva reduz compute do RDS, mas armazenamento, I/O, backup e transferência podem continuar cobrados. Rightsizing deve vir antes do compromisso. Mnemônica: associe “RDS Reserved DB Instances” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — RDS não oferece modelo Spot para a instância de banco gerenciada.
- **B:** Incorreta — A réplica acrescenta custo; não cria desconto de compromisso.
- **C:** Incorreta — Multi-AZ adiciona capacidade para alta disponibilidade e normalmente aumenta custo.
- **D:** Correta — Reserved DB Instances oferecem desconto de faturamento para uso RDS previsível; não são uma instância física separada e não alteram a arquitetura.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)

**Referência prática:** ../labs/README.md — RDS, capacidade e custo

**Exercício recomendado:** No lab RDS, capacidade e custo, monte uma prova de conceito de RDS Reserved DB Instances; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 5. S3 privado atrás do CloudFront

> **ID:** `DIAG-Q005` · **Domínio:** D1 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A startup ipê digital está separando produção e desenvolvimento em contas distintas. Os dados incluem informações reguladas e devem permanecer auditáveis. Um site estático precisa ser distribuído globalmente. Os objetos do S3 não podem ser acessados diretamente pela internet, e a equipe quer aplicar regras contra requisições maliciosas na borda. O que deve ser configurado? Escolha a alternativa que atende diretamente ao requisito.

- **A)** CloudFront com Origin Access Control para o bucket privado, bucket policy restrita à distribuição e AWS WAF associado ao CloudFront.
- **B)** Habilitar website hosting público no S3 e filtrar acessos apenas com security groups.
- **C)** Colocar o bucket em uma subnet privada e anexar uma network ACL.
- **D)** Usar somente uma URL pré-assinada permanente para cada objeto.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

O OAC permite que somente a distribuição autorizada leia o bucket, enquanto o WAF inspeciona requisições HTTP(S) antes de elas alcançarem a origem.

Trade-off: Shield Standard já protege contra ataques DDoS comuns, mas WAF é o controle apropriado para padrões de camada 7 e o OAC evita bypass da distribuição. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O depósito fica trancado; um entregador com crachá busca os pacotes, e um porteiro barra visitantes perigosos.

**Se acertou:** Acertou: O OAC permite que somente a distribuição autorizada leia o bucket, enquanto o WAF inspeciona requisições HTTP(S) antes de elas alcançarem a origem. Quando outra opção poderia valer: Shield Standard já protege contra ataques DDoS comuns, mas WAF é o controle apropriado para padrões de camada 7 e o OAC evita bypass da distribuição. Mnemônica: associe “S3 privado atrás do CloudFront” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — O OAC permite que somente a distribuição autorizada leia o bucket, enquanto o WAF inspeciona requisições HTTP(S) antes de elas alcançarem a origem.
- **B:** Incorreta — Buckets S3 não usam security groups, e o endpoint de website exigiria exposição pública da origem.
- **C:** Incorreta — S3 é um serviço regional, não um recurso implantado dentro de subnets do cliente.
- **D:** Incorreta — URLs pré-assinadas expiram e não substituem uma arquitetura de distribuição, cache e proteção de borda.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

**Referência prática:** ../labs/README.md — S3, CloudFront e WAF

**Exercício recomendado:** No lab S3, CloudFront e WAF, monte uma prova de conceito de S3 privado atrás do CloudFront; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 6. Desacoplamento com SQS e DLQ

> **ID:** `DIAG-Q006` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A edtech farol precisa atender a uma auditoria sem redesenhar toda a aplicação. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Pedidos chegam em rajadas e o processador pode ficar temporariamente indisponível. Nenhum pedido pode ser perdido, falhas repetidas devem ser isoladas e o produtor não deve esperar o processamento. Qual desenho usar? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 7. Read replicas para escalar leituras

> **ID:** `DIAG-Q007` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A startup ipê digital precisa corrigir uma descoberta da revisão Well-Architected. A equipe precisa provar a decisão com um teste pequeno e reversível. Um banco RDS atende relatórios pesados que disputam CPU e I/O com transações. Os relatórios toleram alguns segundos de defasagem e a alta disponibilidade já está coberta. O que fazer? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Fazer snapshots a cada minuto e consultar os snapshots.
- **B)** Aumentar o TTL do Route 53 do endpoint do banco.
- **C)** Criar read replicas e direcionar consultas de relatório aos endpoints de leitura, monitorando replication lag.
- **D)** Usar o standby Multi-AZ diretamente para todas as consultas de relatório.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Read replicas usam replicação assíncrona para retirar consultas de leitura do primário; a tolerância a defasagem torna a solução adequada.

Trade-off: Read replica não substitui Multi-AZ para failover síncrono. A aplicação precisa separar endpoints e aceitar eventual consistency nas leituras. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Uma cópia recente do livro fica com a turma de relatórios, enquanto o original continua livre para registrar vendas.

**Se acertou:** Acertou: Read replicas usam replicação assíncrona para retirar consultas de leitura do primário; a tolerância a defasagem torna a solução adequada. Quando outra opção poderia valer: Read replica não substitui Multi-AZ para failover síncrono. A aplicação precisa separar endpoints e aceitar eventual consistency nas leituras. Mnemônica: associe “Read replicas para escalar leituras” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Snapshots não são uma interface de consulta e restaurações frequentes não servem a relatórios online.
- **B:** Incorreta — TTL DNS não reduz a carga de consultas no primário.
- **C:** Correta — Read replicas usam replicação assíncrona para retirar consultas de leitura do primário; a tolerância a defasagem torna a solução adequada.
- **D:** Incorreta — Na implantação Multi-AZ tradicional, o standby não é endpoint de leitura da aplicação.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

**Referência prática:** ../labs/README.md — RDS Multi-AZ e read replica

**Exercício recomendado:** No lab RDS Multi-AZ e read replica, monte uma prova de conceito de Read replicas para escalar leituras; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 8. Custo de NAT e VPC endpoints

> **ID:** `DIAG-Q008` · **Domínio:** D4 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A empresa de jogos capivara está separando produção e desenvolvimento em contas distintas. A carga atende milhares de requisições por segundo em horários de pico. Instâncias privadas baixam terabytes mensalmente do S3 através de NAT Gateways. A fatura mostra alto processamento de dados no NAT. Como reduzir o custo mantendo caminho privado? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Mover objetos para EBS em uma única instância para evitar S3.
- **B)** Adicionar mais NAT Gateways e continuar roteando S3 por todos eles.
- **C)** Dar IP público às instâncias e remover todos os controles de saída.
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

- **A:** Incorreta — EBS não substitui armazenamento de objetos escalável e cria capacidade, disponibilidade e operação adicionais.
- **B:** Incorreta — Isso pode melhorar resiliência, mas não remove a cobrança de processamento responsável pelo custo.
- **C:** Incorreta — Isso altera a postura de segurança e não mantém o caminho privado.
- **D:** Correta — O endpoint de gateway para S3 evita o processamento pelo NAT e não possui cobrança por hora, reduzindo custo e simplificando o caminho privado.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Referência prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

**Exercício recomendado:** No lab VPC multi-AZ, NAT e endpoints, monte uma prova de conceito de Custo de NAT e VPC endpoints; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 9. Criptografia com AWS KMS

> **ID:** `DIAG-Q009` · **Domínio:** D1 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

O marketplace beija-flor precisa atender a uma auditoria sem redesenhar toda a aplicação. A solução atual funciona, mas não atende ao novo requisito não funcional. Um banco RDS deve ser criptografado em repouso com uma chave controlada pela empresa. A segurança exige separação de funções, auditoria de uso da chave e rotação anual automática. Qual desenho é apropriado? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Criar uma chave simétrica gerenciada pelo cliente no AWS KMS, limitar key policy/grants, habilitar rotação e selecioná-la ao criar o RDS.
- **B)** Habilitar apenas TLS no endpoint do RDS.
- **C)** Usar uma chave gerenciada pela AWS e editar diretamente sua key policy para impor a separação de funções.
- **D)** Guardar uma senha AES em user data e criptografar manualmente cada página do banco.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Uma chave KMS gerenciada pelo cliente oferece controle de política, trilha de auditoria no CloudTrail e rotação automática compatível com a criptografia do RDS.

Trade-off: A chave gerenciada pela AWS reduz administração, porém não dá o mesmo nível de controle de política exigido; a escolha da chave ocorre na criação ou restauração criptografada. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É um cofre cuja chave mestra tem lista de convidados, diário de uso e troca automática de segredo.

**Se acertou:** Acertou: Uma chave KMS gerenciada pelo cliente oferece controle de política, trilha de auditoria no CloudTrail e rotação automática compatível com a criptografia do RDS. Quando outra opção poderia valer: A chave gerenciada pela AWS reduz administração, porém não dá o mesmo nível de controle de política exigido; a escolha da chave ocorre na criação ou restauração criptografada. Mnemônica: associe “Criptografia com AWS KMS” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Uma chave KMS gerenciada pelo cliente oferece controle de política, trilha de auditoria no CloudTrail e rotação automática compatível com a criptografia do RDS.
- **B:** Incorreta — TLS protege dados em trânsito; não satisfaz o requisito de criptografia em repouso.
- **C:** Incorreta — Key policies de chaves gerenciadas pela AWS não são editáveis pelo cliente como as de uma chave gerenciada pelo cliente.
- **D:** Incorreta — User data não é cofre de segredos e criptografia manual acrescenta risco e operação desnecessários.

**Referência oficial:** [https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)

**Referência prática:** ../labs/README.md — KMS e criptografia em repouso

**Exercício recomendado:** No lab KMS e criptografia em repouso, monte uma prova de conceito de Criptografia com AWS KMS; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 10. Fan-out com SNS e SQS

> **ID:** `DIAG-Q010` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A fintech aurora precisa corrigir uma descoberta da revisão Well-Architected. O tráfego normal é estável, mas cresce oito vezes em campanhas. Cada evento de pedido deve ser processado independentemente por faturamento, estoque e analytics. Se um consumidor parar, os outros devem continuar e o backlog daquele consumidor deve ser preservado. Qual arquitetura é apropriada? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Guardar eventos em logs locais da instância produtora.
- **B)** Publicar em uma SNS topic e criar uma fila SQS separada para cada consumidor, com subscriptions e DLQs próprias.
- **C)** Usar uma única fila SQS e fazer os três serviços competirem pela mesma mensagem.
- **D)** Chamar os três serviços sequencialmente dentro do produtor.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

SNS replica cada mensagem para as filas assinantes; cada SQS mantém seu próprio backlog, ritmo e política de falhas, isolando consumidores.

Trade-off: Uma única fila com três consumidores distribuiria mensagens entre eles, em vez de entregar uma cópia a cada função de negócio. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um locutor anuncia a notícia para três caixas de correio; cada equipe abre a sua quando puder.

**Se acertou:** Acertou: SNS replica cada mensagem para as filas assinantes; cada SQS mantém seu próprio backlog, ritmo e política de falhas, isolando consumidores. Quando outra opção poderia valer: Uma única fila com três consumidores distribuiria mensagens entre eles, em vez de entregar uma cópia a cada função de negócio. Mnemônica: associe “Fan-out com SNS e SQS” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Logs locais não são um canal durável e consumível de integração.
- **B:** Correta — SNS replica cada mensagem para as filas assinantes; cada SQS mantém seu próprio backlog, ritmo e política de falhas, isolando consumidores.
- **C:** Incorreta — Consumidores concorrentes em uma fila recebem mensagens diferentes; não há fan-out por consumidor.
- **D:** Incorreta — A falha ou lentidão de um serviço afeta todos e acopla o produtor aos consumidores.

**Referência oficial:** [https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)

**Referência prática:** ../labs/README.md — Eventos, SNS, SQS e Lambda

**Exercício recomendado:** No lab Eventos, SNS, SQS e Lambda, monte uma prova de conceito de Fan-out com SNS e SQS; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 11. Tipos de volume EBS

> **ID:** `DIAG-Q011` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

O marketplace beija-flor está separando produção e desenvolvimento em contas distintas. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Um banco autogerenciado em EC2 exige latência de I/O consistente e dezenas de milhares de IOPS sustentadas. A performance deve ser previsível, mesmo que custe mais que uso geral. Qual volume escolher? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Usar sc1 porque é o volume com menor latência para bancos críticos.
- **B)** Usar st1 para milhões de pequenos I/Os aleatórios.
- **C)** Usar EBS io2, dimensionando IOPS e throughput conforme a instância e a carga, e validar limites ponta a ponta.
- **D)** Usar instance store sem replicação porque todo dado EBS é efêmero.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

io2 é SSD de Provisioned IOPS para workloads críticos que precisam de desempenho consistente e alta durabilidade.

Trade-off: gp3 é excelente padrão custo/desempenho e permite provisionar IOPS/throughput, mas io2 atende os requisitos mais rigorosos. st1/sc1 são HDD para acesso sequencial e não podem ser boot volume. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É uma pista expressa com número de faixas reservado, em vez de torcer para a rua comum estar vazia.

**Se acertou:** Acertou: io2 é SSD de Provisioned IOPS para workloads críticos que precisam de desempenho consistente e alta durabilidade. Quando outra opção poderia valer: gp3 é excelente padrão custo/desempenho e permite provisionar IOPS/throughput, mas io2 atende os requisitos mais rigorosos. st1/sc1 são HDD para acesso sequencial e não podem ser boot volume. Mnemônica: associe “Tipos de volume EBS” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — sc1 é HDD de baixo custo para acesso pouco frequente e não oferece latência SSD.
- **B:** Incorreta — st1 é otimizado a throughput sequencial, não IOPS aleatórios de banco.
- **C:** Correta — io2 é SSD de Provisioned IOPS para workloads críticos que precisam de desempenho consistente e alta durabilidade.
- **D:** Incorreta — EBS é persistente; instance store é que é efêmero e exigiria proteção adicional.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

**Referência prática:** ../labs/README.md — EC2, EBS e teste de I/O

**Exercício recomendado:** No lab EC2, EBS e teste de I/O, monte uma prova de conceito de Tipos de volume EBS; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 12. AWS Compute Optimizer

> **ID:** `DIAG-Q012` · **Domínio:** D4 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A plataforma de mídia onda precisa atender a uma auditoria sem redesenhar toda a aplicação. A equipe precisa provar a decisão com um teste pequeno e reversível. Centenas de instâncias EC2 têm baixa utilização, mas a equipe não sabe quais podem ser reduzidas sem risco de memória ou performance. Ela quer recomendações baseadas em métricas antes de mudar tamanhos. Qual serviço usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Comprar Reserved Instances para todos os tamanhos atuais antes do rightsizing.
- **B)** Usar AWS Budgets como ferramenta de benchmark de CPU e memória.
- **C)** Reduzir todas as instâncias para t3.micro sem medir.
- **D)** Ativar AWS Compute Optimizer, garantir métricas suficientes (incluindo memória com agente quando necessário) e testar as recomendações de rightsizing.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

Compute Optimizer analisa métricas e oferece recomendações de tipo/tamanho e risco; a validação em carga real evita reduzir capacidade cegamente.

Trade-off: Cost Explorer Rightsizing também ajuda na visão de custo. Recomendações são insumo, não autorização automática: sazonalidade, licenças e limites de rede precisam ser considerados. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um treinador observa cada atleta e sugere um tênis do tamanho certo, em vez de comprar o maior para todos.

**Se acertou:** Acertou: Compute Optimizer analisa métricas e oferece recomendações de tipo/tamanho e risco; a validação em carga real evita reduzir capacidade cegamente. Quando outra opção poderia valer: Cost Explorer Rightsizing também ajuda na visão de custo. Recomendações são insumo, não autorização automática: sazonalidade, licenças e limites de rede precisam ser considerados. Mnemônica: associe “AWS Compute Optimizer” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Isso pode comprometer gasto em capacidade superdimensionada.
- **B:** Incorreta — Budgets alerta sobre custo/uso, mas não faz análise técnica de dimensionamento.
- **C:** Incorreta — Uma regra única ignora CPU, memória, rede, burst e requisitos diferentes.
- **D:** Correta — Compute Optimizer analisa métricas e oferece recomendações de tipo/tamanho e risco; a validação em carga real evita reduzir capacidade cegamente.

**Referência oficial:** [https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

**Referência prática:** ../labs/README.md — Observabilidade e rightsizing

**Exercício recomendado:** No lab Observabilidade e rightsizing, monte uma prova de conceito de AWS Compute Optimizer; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 13. Rotação de credenciais com Secrets Manager

> **ID:** `DIAG-Q013` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A varejista nuvem sul precisa corrigir uma descoberta da revisão Well-Architected. O orçamento é limitado e a operação manual deve ser mínima. Uma aplicação usa credenciais de um banco RDS. A senha precisa rotacionar automaticamente a cada 30 dias sem ser gravada no código ou na imagem do contêiner. Qual é a solução com menor esforço operacional? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Armazenar a credencial no AWS Secrets Manager, configurar rotação com Lambda e conceder à task role permissão de leitura do segredo.
- **B)** Guardar a senha em uma tag do recurso RDS protegida por IAM.
- **C)** Criar access keys para o usuário raiz e usá-las como senha do banco.
- **D)** Salvar a senha em uma variável de ambiente no Dockerfile e recriar a imagem mensalmente.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Secrets Manager armazena, versiona e integra a rotação de segredos; a role do workload elimina credenciais AWS embutidas no contêiner.

Trade-off: Parameter Store SecureString pode guardar valores sensíveis com KMS, mas a rotação gerenciada de credenciais de banco é a vantagem decisiva do Secrets Manager neste cenário. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** A senha mora num cofrinho que troca a combinação sozinho e só mostra a nova combinação ao robô autorizado.

**Se acertou:** Acertou: Secrets Manager armazena, versiona e integra a rotação de segredos; a role do workload elimina credenciais AWS embutidas no contêiner. Quando outra opção poderia valer: Parameter Store SecureString pode guardar valores sensíveis com KMS, mas a rotação gerenciada de credenciais de banco é a vantagem decisiva do Secrets Manager neste cenário. Mnemônica: associe “Rotação de credenciais com Secrets Manager” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Secrets Manager armazena, versiona e integra a rotação de segredos; a role do workload elimina credenciais AWS embutidas no contêiner.
- **B:** Incorreta — Tags não são um mecanismo de armazenamento seguro de segredos.
- **C:** Incorreta — Credenciais AWS não substituem credenciais do banco e o usuário raiz não deve ser usado por workloads.
- **D:** Incorreta — A imagem pode vazar a senha e a rotação permanece manual e acoplada ao deploy.

**Referência oficial:** [https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

**Referência prática:** ../labs/README.md — Lambda/API Gateway com IAM roles

**Exercício recomendado:** No lab Lambda/API Gateway com IAM roles, monte uma prova de conceito de Rotação de credenciais com Secrets Manager; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 14. Estratégias de disaster recovery

> **ID:** `DIAG-Q014` · **Domínio:** D2 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A empresa de geoprocessamento mapa vivo está separando produção e desenvolvimento em contas distintas. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Um sistema regional exige RTO de 15 minutos e RPO de poucos minutos. A empresa aceita manter capacidade reduzida ativa na região de recuperação, mas não quer pagar por uma cópia em escala total. Qual estratégia se encaixa melhor? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas. Para rastreabilidade, o comitê registrou este caso como DIAG-Q014.

- **A)** Pilot light contendo somente dados, sem automação para subir a aplicação.
- **B)** Warm standby: manter uma versão funcional em escala reduzida na região secundária, replicar dados e escalar durante o failover.
- **C)** Multi-site active-active em escala total obrigatoriamente.
- **D)** Backup and restore com backups semanais offline.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

Warm standby já executa todos os componentes essenciais, reduzindo o RTO em comparação a pilot light sem manter capacidade integral como active-active.

Trade-off: Pilot light custa menos, mas precisa iniciar/implantar parte relevante da aplicação; multi-site active-active oferece RTO menor com maior custo e complexidade. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Há uma lojinha reserva já aberta com poucos caixas; numa emergência, ela chama reforços rapidamente.

**Se acertou:** Acertou: Warm standby já executa todos os componentes essenciais, reduzindo o RTO em comparação a pilot light sem manter capacidade integral como active-active. Quando outra opção poderia valer: Pilot light custa menos, mas precisa iniciar/implantar parte relevante da aplicação; multi-site active-active oferece RTO menor com maior custo e complexidade. Mnemônica: associe “Estratégias de disaster recovery” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — A ausência de componentes e automação torna o RTO incerto e provavelmente maior.
- **B:** Correta — Warm standby já executa todos os componentes essenciais, reduzindo o RTO em comparação a pilot light sem manter capacidade integral como active-active.
- **C:** Incorreta — Atenderia ou superaria o RTO, mas viola a intenção de evitar custo de capacidade integral quando warm standby basta.
- **D:** Incorreta — Em geral não atende RPO de minutos nem RTO de 15 minutos.

**Referência oficial:** [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

**Referência prática:** ../labs/README.md — Cenário de recuperação multi-região

**Exercício recomendado:** No lab Cenário de recuperação multi-região, monte uma prova de conceito de Estratégias de disaster recovery; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 15. Transferência para Amazon S3

> **ID:** `DIAG-Q015` · **Domínio:** D3 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A varejista nuvem sul precisa atender a uma auditoria sem redesenhar toda a aplicação. O tráfego normal é estável, mas cresce oito vezes em campanhas. Filiais globais enviam arquivos de 200 GB ao S3 por links de longa distância. A equipe quer paralelizar uploads, retomar partes com falha e melhorar o caminho pela rede AWS. Qual combinação usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Colocar um NAT Gateway na filial sem conexão com a AWS.
- **B)** Enviar cada arquivo em uma única requisição e reiniciar tudo em qualquer falha.
- **C)** Usar S3 multipart upload e avaliar S3 Transfer Acceleration para ingressar pela edge location mais próxima.
- **D)** Usar S3 Glacier restore antes de cada upload.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Multipart divide o objeto, permite upload paralelo e repetição de partes; Transfer Acceleration usa a rede global da AWS a partir da borda.

Trade-off: Transfer Acceleration tem custo adicional e benefício dependente da rota; deve ser testado. Para migração offline massiva, Snowball pode ser mais apropriado. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um caminhão enorme vira várias caixas; se uma cai, reenviamos só aquela, e elas entram pela garagem mais próxima.

**Se acertou:** Acertou: Multipart divide o objeto, permite upload paralelo e repetição de partes; Transfer Acceleration usa a rede global da AWS a partir da borda. Quando outra opção poderia valer: Transfer Acceleration tem custo adicional e benefício dependente da rota; deve ser testado. Para migração offline massiva, Snowball pode ser mais apropriado. Mnemônica: associe “Transferência para Amazon S3” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — NAT Gateway é implantado em VPC e não melhora sozinho a rota WAN da filial.
- **B:** Incorreta — Isso perde paralelismo e torna falhas caras em objetos grandes.
- **C:** Correta — Multipart divide o objeto, permite upload paralelo e repetição de partes; Transfer Acceleration usa a rede global da AWS a partir da borda.
- **D:** Incorreta — Restore recupera objetos arquivados e não acelera novos uploads.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

**Referência prática:** ../labs/README.md — S3, multipart e desempenho

**Exercício recomendado:** No lab S3, multipart e desempenho, monte uma prova de conceito de Transferência para Amazon S3; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 16. Capacidade do DynamoDB

> **ID:** `DIAG-Q016` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A empresa de logística rota certa precisa corrigir uma descoberta da revisão Well-Architected. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Uma tabela nova tem tráfego imprevisível e pode ficar horas ociosa antes de picos abruptos. A equipe não conhece a capacidade necessária e quer evitar administração inicial. Qual modo escolher? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Provisionar imediatamente o pico teórico máximo 24x7 sem métricas.
- **B)** Escolher uma chave constante porque on-demand elimina hot partitions.
- **C)** Executar DynamoDB em uma EC2 Spot para pagar menos.
- **D)** Começar com DynamoDB on-demand e, quando o padrão se tornar previsível e sustentado, comparar com provisioned capacity e auto scaling.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

On-demand cobra por requisição e ajusta capacidade automaticamente, sendo adequado a cargas novas, variáveis ou intermitentes sem planejamento de throughput.

Trade-off: Provisioned pode custar menos em uso estável e previsível, especialmente com auto scaling e reserved capacity elegível. Hot keys continuam sendo problema de modelagem. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Pagamos cada passeio quando alguém chega, sem manter um ônibus vazio esperando o dia inteiro.

**Se acertou:** Acertou: On-demand cobra por requisição e ajusta capacidade automaticamente, sendo adequado a cargas novas, variáveis ou intermitentes sem planejamento de throughput. Quando outra opção poderia valer: Provisioned pode custar menos em uso estável e previsível, especialmente com auto scaling e reserved capacity elegível. Hot keys continuam sendo problema de modelagem. Mnemônica: associe “Capacidade do DynamoDB” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Isso tende a pagar capacidade ociosa durante a maior parte do tempo.
- **B:** Incorreta — Modo de capacidade não corrige uma chave de partição mal distribuída.
- **C:** Incorreta — DynamoDB é serviço gerenciado e não é implantado pelo cliente em EC2.
- **D:** Correta — On-demand cobra por requisição e ajusta capacidade automaticamente, sendo adequado a cargas novas, variáveis ou intermitentes sem planejamento de throughput.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)

**Referência prática:** ../labs/README.md — DynamoDB, DAX e capacidade

**Exercício recomendado:** No lab DynamoDB, DAX e capacidade, monte uma prova de conceito de Capacidade do DynamoDB; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 17. VPC Gateway Endpoint para S3

> **ID:** `DIAG-Q017` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A proptech janela está separando produção e desenvolvimento em contas distintas. A carga atende milhares de requisições por segundo em horários de pico. Instâncias EC2 em subnets privadas enviam grandes volumes ao S3. O tráfego não pode atravessar a internet e a solução deve evitar cobrança por hora de um componente de rede. Qual opção usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Criar um Gateway VPC Endpoint para S3, associá-lo às route tables privadas e restringir acesso com endpoint/bucket policies.
- **B)** Enviar o tráfego por um NAT Gateway em cada AZ.
- **C)** Criar um Interface Endpoint para qualquer serviço e esperar que ele seja sempre gratuito.
- **D)** Atribuir IPv4 público às instâncias e permitir saída 0.0.0.0/0.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Gateway endpoints para S3 adicionam rotas privadas ao serviço, não exigem NAT e não têm a cobrança por hora típica de interface endpoints.

Trade-off: Um NAT Gateway também permite chegar ao endpoint público do S3, mas adiciona custo por hora e por dados e não atende tão diretamente à exigência de caminho privado. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É uma estrada particular e gratuita do escritório até o armazém, sem sair para a avenida pública.

**Se acertou:** Acertou: Gateway endpoints para S3 adicionam rotas privadas ao serviço, não exigem NAT e não têm a cobrança por hora típica de interface endpoints. Quando outra opção poderia valer: Um NAT Gateway também permite chegar ao endpoint público do S3, mas adiciona custo por hora e por dados e não atende tão diretamente à exigência de caminho privado. Mnemônica: associe “VPC Gateway Endpoint para S3” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Gateway endpoints para S3 adicionam rotas privadas ao serviço, não exigem NAT e não têm a cobrança por hora típica de interface endpoints.
- **B:** Incorreta — O NAT adiciona custo e o caminho usa o endpoint público; é desnecessário quando há gateway endpoint para S3.
- **C:** Incorreta — Interface endpoints têm cobrança por hora e processamento de dados; a afirmação de gratuidade é incorreta.
- **D:** Incorreta — Isso expõe as instâncias a uma rota de internet e viola o requisito de tráfego privado.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Referência prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

**Exercício recomendado:** No lab VPC multi-AZ, NAT e endpoints, monte uma prova de conceito de VPC Gateway Endpoint para S3; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 18. Replicação S3 entre regiões

> **ID:** `DIAG-Q018` · **Domínio:** D2 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A empresa de energia raio precisa atender a uma auditoria sem redesenhar toda a aplicação. Os dados incluem informações reguladas e devem permanecer auditáveis. Objetos de um bucket precisam ser copiados automaticamente para outra região para recuperação. A empresa também quer preservar versões e impedir que uma exclusão acidental destrua imediatamente a cópia histórica. O que configurar? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Usar lifecycle expiration no bucket de origem como mecanismo de cópia.
- **B)** Habilitar versionamento nos buckets, configurar S3 Cross-Region Replication e definir cuidadosamente replicação de delete markers e retenção/Object Lock quando exigido.
- **C)** Montar o bucket como EBS e fazer snapshot da instância.
- **D)** Desativar versionamento para reduzir o número de cópias.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

CRR requer versionamento e replica novos objetos conforme as regras. A política de delete markers e mecanismos de retenção determinam o comportamento diante de exclusões.

Trade-off: Replicação não é retroativa por padrão e não substitui toda estratégia de backup; S3 Batch Replication pode tratar objetos existentes. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Cada desenho ganha uma cópia em outra cidade e versões antigas ficam num fichário que uma borracha comum não apaga.

**Se acertou:** Acertou: CRR requer versionamento e replica novos objetos conforme as regras. A política de delete markers e mecanismos de retenção determinam o comportamento diante de exclusões. Quando outra opção poderia valer: Replicação não é retroativa por padrão e não substitui toda estratégia de backup; S3 Batch Replication pode tratar objetos existentes. Mnemônica: associe “Replicação S3 entre regiões” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Lifecycle gerencia transição/expiração e não replica objetos para outra região.
- **B:** Correta — CRR requer versionamento e replica novos objetos conforme as regras. A política de delete markers e mecanismos de retenção determinam o comportamento diante de exclusões.
- **C:** Incorreta — S3 não é montado como volume EBS, e snapshot de EC2 não protege objetos do bucket.
- **D:** Incorreta — CRR exige versionamento e desativá-lo prejudica recuperação de alterações/exclusões.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

**Referência prática:** ../labs/README.md — S3 versionado e recuperação

**Exercício recomendado:** No lab S3 versionado e recuperação, monte uma prova de conceito de Replicação S3 entre regiões; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 19. AWS Global Accelerator

> **ID:** `DIAG-Q019` · **Domínio:** D3 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A proptech janela precisa corrigir uma descoberta da revisão Well-Architected. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Um aplicativo de jogos usa TCP/UDP, possui endpoints em duas regiões e precisa de IPs anycast estáticos, failover rápido e tráfego pela rede global da AWS. O conteúdo não é cacheável. Qual serviço usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Usar apenas um registro DNS com TTL de 24 horas.
- **B)** Criar Elastic IPs regionais e anunciar manualmente BGP pela internet.
- **C)** Usar AWS Global Accelerator com endpoint groups regionais e health checks.
- **D)** Usar CloudFront para armazenar pacotes UDP de sessão em cache.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Global Accelerator fornece IPs anycast estáticos, leva tráfego TCP/UDP pela borda à rede global e muda endpoints conforme saúde e políticas.

Trade-off: CloudFront é ideal para HTTP(S) cacheável e também pode acelerar conteúdo dinâmico, mas não fornece a mesma proposta para protocolos TCP/UDP genéricos e IPs anycast de entrada. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Todos usam o mesmo endereço de portão; por dentro, uma estrada rápida leva cada jogador ao parque saudável mais próximo.

**Se acertou:** Acertou: Global Accelerator fornece IPs anycast estáticos, leva tráfego TCP/UDP pela borda à rede global e muda endpoints conforme saúde e políticas. Quando outra opção poderia valer: CloudFront é ideal para HTTP(S) cacheável e também pode acelerar conteúdo dinâmico, mas não fornece a mesma proposta para protocolos TCP/UDP genéricos e IPs anycast de entrada. Mnemônica: associe “AWS Global Accelerator” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — DNS não fornece IPs anycast estáticos nem failover tão rápido, e TTL alto retarda mudança.
- **B:** Incorreta — Elastic IP é regional e clientes não anunciam esse prefixo globalmente dessa forma.
- **C:** Correta — Global Accelerator fornece IPs anycast estáticos, leva tráfego TCP/UDP pela borda à rede global e muda endpoints conforme saúde e políticas.
- **D:** Incorreta — CloudFront não é cache genérico para UDP.

**Referência oficial:** [https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

**Referência prática:** ../labs/README.md — Roteamento global e failover

**Exercício recomendado:** No lab Roteamento global e failover, monte uma prova de conceito de AWS Global Accelerator; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 20. Snapshots EBS com Data Lifecycle Manager

> **ID:** `DIAG-Q020` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A fabricante serra azul está separando produção e desenvolvimento em contas distintas. O tráfego normal é estável, mas cresce oito vezes em campanhas. Volumes EBS precisam de snapshots diários, retenção por 35 dias e exclusão automática dos antigos. O processo atual usa scripts em uma instância que frequentemente falha. Qual opção reduz operação e custo? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Criar uma instância maior apenas para executar o cron de snapshots.
- **B)** Manter todos os snapshots para sempre porque snapshots incrementais não custam.
- **C)** Usar instance store como destino durável dos backups.
- **D)** Usar Amazon Data Lifecycle Manager com tags para criar e expirar snapshots segundo a política.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

DLM automatiza ciclo de vida de snapshots EBS e AMIs com seleção por tags, eliminando servidor de agendamento e acúmulo indefinido.

Trade-off: Snapshots são incrementais no armazenamento, mas cada snapshot aparece como ponto completo de restauração. A política precisa respeitar retenção e testes de restore. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um robô fotografa os cadernos todo dia e descarta sozinho as fotos que passaram do prazo.

**Se acertou:** Acertou: DLM automatiza ciclo de vida de snapshots EBS e AMIs com seleção por tags, eliminando servidor de agendamento e acúmulo indefinido. Quando outra opção poderia valer: Snapshots são incrementais no armazenamento, mas cada snapshot aparece como ponto completo de restauração. A política precisa respeitar retenção e testes de restore. Mnemônica: associe “Snapshots EBS com Data Lifecycle Manager” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Isso aumenta custo e mantém uma automação desnecessariamente autogerenciada.
- **B:** Incorreta — Blocos exclusivos ainda ocupam armazenamento e retenção infinita gera custo.
- **C:** Incorreta — Instance store é efêmero e não é serviço de backup.
- **D:** Correta — DLM automatiza ciclo de vida de snapshots EBS e AMIs com seleção por tags, eliminando servidor de agendamento e acúmulo indefinido.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)

**Referência prática:** ../labs/README.md — EBS, snapshots e recuperação

**Exercício recomendado:** No lab EBS, snapshots e recuperação, monte uma prova de conceito de Snapshots EBS com Data Lifecycle Manager; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 21. SCP em AWS Organizations

> **ID:** `DIAG-Q021` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A indústria cedro precisa atender a uma auditoria sem redesenhar toda a aplicação. A equipe precisa provar a decisão com um teste pequeno e reversível. A organização quer impedir que qualquer conta membro desative o CloudTrail ou crie recursos fora de regiões aprovadas, inclusive quando um administrador local concede Allow. Qual controle deve formar o guardrail? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Aplicar Service Control Policies nas OUs, com exceções cuidadosamente definidas para serviços e funções indispensáveis.
- **B)** Criar uma tag chamada RegiãoPermitida e confiar que os serviços a aplicarão sozinhos.
- **C)** Adicionar uma IAM policy Allow a todos os administradores das contas.
- **D)** Usar somente security groups para bloquear chamadas de API fora da região.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

SCPs definem o teto de permissões de contas membros; um Allow local não consegue ultrapassar um Deny explícito aplicável da organização.

Trade-off: SCP não concede permissões e não substitui policies de identidade ou recurso; ele limita o conjunto máximo que esses mecanismos podem conceder. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É o muro do condomínio: cada morador escolhe as regras da casa, mas ninguém pode atravessar o muro externo.

**Se acertou:** Acertou: SCPs definem o teto de permissões de contas membros; um Allow local não consegue ultrapassar um Deny explícito aplicável da organização. Quando outra opção poderia valer: SCP não concede permissões e não substitui policies de identidade ou recurso; ele limita o conjunto máximo que esses mecanismos podem conceder. Mnemônica: associe “SCP em AWS Organizations” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — SCPs definem o teto de permissões de contas membros; um Allow local não consegue ultrapassar um Deny explícito aplicável da organização.
- **B:** Incorreta — Tags só têm efeito de autorização quando policies explicitamente as avaliam.
- **C:** Incorreta — Um Allow amplia permissões locais e não cria o guardrail organizacional solicitado.
- **D:** Incorreta — Security groups filtram tráfego de recursos e não governam permissões de APIs ou regiões.

**Referência oficial:** [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Referência prática:** ../labs/README.md — IAM, KMS e guardrails

**Exercício recomendado:** No lab IAM, KMS e guardrails, monte uma prova de conceito de SCP em AWS Organizations; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 22. Amazon EFS Regional

> **ID:** `DIAG-Q022` · **Domínio:** D2 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A companhia aérea ventos precisa corrigir uma descoberta da revisão Well-Architected. A solução atual funciona, mas não atende ao novo requisito não funcional. Um conjunto de instâncias Linux em várias AZs precisa compartilhar arquivos POSIX. Os dados devem permanecer acessíveis quando uma instância ou uma AZ falhar, sem gerenciar servidores de arquivos. Qual armazenamento usar? Escolha a alternativa que atende diretamente ao requisito.

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

## 23. FSx for Lustre

> **ID:** `DIAG-Q023` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A indústria cedro está separando produção e desenvolvimento em contas distintas. Os dados incluem informações reguladas e devem permanecer auditáveis. Um workload HPC em milhares de vCPUs processa um dataset grande do S3 e precisa de sistema de arquivos paralelo com throughput muito alto. Ao final, os resultados devem voltar ao S3. Qual serviço usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Usar um único volume gp2 pequeno compartilhado por todas as instâncias em regiões diferentes.
- **B)** Usar S3 Glacier Deep Archive como sistema de arquivos POSIX interativo.
- **C)** Usar Amazon FSx for Lustre vinculado ao repositório de dados S3 e escolher deployment type/capacidade adequados.
- **D)** Executar um servidor SMB t3.micro como ponto central.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

FSx for Lustre é um sistema de arquivos paralelo de alto desempenho integrado ao S3, adequado a HPC, ML e processamento massivo.

Trade-off: Scratch oferece custo menor para dados temporários sem replicação durável; Persistent atende workloads mais longos. O S3 continua sendo a fonte/repositório durável quando desenhado assim. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Mil cozinheiros abrem gavetas de uma despensa super-rápida ao mesmo tempo, e os pratos prontos voltam ao armazém.

**Se acertou:** Acertou: FSx for Lustre é um sistema de arquivos paralelo de alto desempenho integrado ao S3, adequado a HPC, ML e processamento massivo. Quando outra opção poderia valer: Scratch oferece custo menor para dados temporários sem replicação durável; Persistent atende workloads mais longos. O S3 continua sendo a fonte/repositório durável quando desenhado assim. Mnemônica: associe “FSx for Lustre” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — EBS é zonal, e esse desenho não fornece sistema de arquivos paralelo ou throughput agregado.
- **B:** Incorreta — Deep Archive exige restauração e não expõe semântica POSIX de baixa latência.
- **C:** Correta — FSx for Lustre é um sistema de arquivos paralelo de alto desempenho integrado ao S3, adequado a HPC, ML e processamento massivo.
- **D:** Incorreta — O servidor seria gargalo e ponto único, além de protocolo inadequado ao padrão HPC descrito.

**Referência oficial:** [https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)

**Referência prática:** ../labs/README.md — Armazenamento de alto desempenho

**Exercício recomendado:** No lab Armazenamento de alto desempenho, monte uma prova de conceito de FSx for Lustre; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 24. AWS Budgets e Cost Explorer

> **ID:** `DIAG-Q024` · **Domínio:** D4 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A rede hospitalar horizonte precisa atender a uma auditoria sem redesenhar toda a aplicação. Uma interrupção de poucos minutos gera impacto financeiro mensurável. FinOps precisa alertar quando a previsão mensal ultrapassar o orçamento e depois investigar quais serviços e tags explicam a variação. Qual combinação usar? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Usar security groups para impedir qualquer recurso de gerar custo.
- **B)** Esperar a fatura fechar e analisar apenas uma vez por ano.
- **C)** Usar CloudTrail sozinho para calcular a previsão da fatura.
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

- **A:** Incorreta — Security groups controlam rede e não funcionam como orçamento ou governança financeira.
- **B:** Incorreta — Isso elimina alerta precoce e capacidade de correção durante o período.
- **C:** Incorreta — CloudTrail registra APIs e não é ferramenta de previsão e análise financeira.
- **D:** Correta — Budgets compara gasto/uso com limites e envia alertas; Cost Explorer permite explorar a composição e a evolução dos custos.

**Referência oficial:** [https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)

**Referência prática:** ../labs/README.md — Budgets, tags e análise de custos

**Exercício recomendado:** No lab Budgets, tags e análise de custos, monte uma prova de conceito de AWS Budgets e Cost Explorer; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 25. Trilha de auditoria organizacional

> **ID:** `DIAG-Q025` · **Domínio:** D1 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A universidade saber precisa corrigir uma descoberta da revisão Well-Architected. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Auditores exigem registro centralizado e resistente a adulteração das chamadas de API de todas as contas atuais e futuras. Também é preciso alertar quando alguém tentar apagar uma trilha. Qual arquitetura é adequada? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Criar uma organization trail no CloudTrail para bucket central dedicado, habilitar validação de integridade, restringir o bucket e monitorar eventos com EventBridge/CloudWatch.
- **B)** Usar VPC Flow Logs como substituto para chamadas de API.
- **C)** Habilitar logs de acesso do ALB para registrar alterações no IAM.
- **D)** Confiar apenas no Event history de 90 dias de cada conta.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Uma organization trail cobre contas da organização de forma central; políticas do bucket e validação de logs protegem a evidência, e eventos permitem alertas rápidos.

Trade-off: CloudTrail Lake pode ajudar em consultas e retenção, mas não elimina a necessidade de definir proteção, governança e alertas coerentes para os registros. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Todas as salas escrevem no mesmo diário lacrado; se alguém tentar arrancar uma página, um alarme toca.

**Se acertou:** Acertou: Uma organization trail cobre contas da organização de forma central; políticas do bucket e validação de logs protegem a evidência, e eventos permitem alertas rápidos. Quando outra opção poderia valer: CloudTrail Lake pode ajudar em consultas e retenção, mas não elimina a necessidade de definir proteção, governança e alertas coerentes para os registros. Mnemônica: associe “Trilha de auditoria organizacional” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Uma organization trail cobre contas da organização de forma central; políticas do bucket e validação de logs protegem a evidência, e eventos permitem alertas rápidos.
- **B:** Incorreta — Flow Logs registram metadados de fluxos de rede, não ações de controle executadas via APIs.
- **C:** Incorreta — Logs do ALB mostram requisições ao balanceador, não alterações administrativas em serviços AWS.
- **D:** Incorreta — O histórico é limitado, regionalmente consultado e não fornece sozinho retenção central protegida.

**Referência oficial:** [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

**Referência prática:** ../labs/README.md — Observabilidade, CloudTrail e alertas

**Exercício recomendado:** No lab Observabilidade, CloudTrail e alertas, monte uma prova de conceito de Trilha de auditoria organizacional; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 26. Aurora Global Database

> **ID:** `DIAG-Q026` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A agência pública portal aberto está separando produção e desenvolvimento em contas distintas. O orçamento é limitado e a operação manual deve ser mínima. Uma aplicação de leitura global baseada em Aurora precisa latência local em regiões secundárias e recuperação regional com replicação rápida. Escritas permanecem centralizadas durante operação normal. Qual recurso escolher? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Exportar snapshots manualmente uma vez por mês.
- **B)** Usar Aurora Global Database com cluster primário gravável e clusters secundários de leitura nas regiões necessárias.
- **C)** Colocar o endpoint regional atrás de CloudFront para armazenar respostas SQL em cache.
- **D)** Usar apenas Multi-AZ no cluster primário e esperar endpoints de leitura em outras regiões.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

Aurora Global Database usa replicação dedicada entre regiões, oferece leituras locais e permite promover uma região secundária em um evento de recuperação.

Trade-off: A promoção e o roteamento da aplicação ainda precisam ser planejados. Multi-AZ protege dentro de uma região e não fornece, sozinho, leituras globais. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O livro mestre é escrito numa cidade, enquanto cópias quase instantâneas chegam às bibliotecas do mundo.

**Se acertou:** Acertou: Aurora Global Database usa replicação dedicada entre regiões, oferece leituras locais e permite promover uma região secundária em um evento de recuperação. Quando outra opção poderia valer: A promoção e o roteamento da aplicação ainda precisam ser planejados. Multi-AZ protege dentro de uma região e não fornece, sozinho, leituras globais. Mnemônica: associe “Aurora Global Database” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Snapshots mensais não oferecem replicação contínua nem RPO/RTO compatíveis.
- **B:** Correta — Aurora Global Database usa replicação dedicada entre regiões, oferece leituras locais e permite promover uma região secundária em um evento de recuperação.
- **C:** Incorreta — CloudFront não se conecta diretamente a um protocolo de banco e não cria réplicas do Aurora.
- **D:** Incorreta — Multi-AZ oferece resiliência regional, não clusters de leitura entre regiões.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

**Referência prática:** ../labs/README.md — RDS/Aurora, réplicas e failover

**Exercício recomendado:** No lab RDS/Aurora, réplicas e failover, monte uma prova de conceito de Aurora Global Database; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 27. Amazon Kinesis Data Streams

> **ID:** `DIAG-Q027` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A universidade saber precisa atender a uma auditoria sem redesenhar toda a aplicação. A solução atual funciona, mas não atende ao novo requisito não funcional. Sensores enviam eventos continuamente e vários consumidores precisam processar o mesmo stream com baixa latência, preservando ordem por dispositivo e possibilidade de replay dentro da retenção. Qual serviço escolher? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Usar SNS sem assinantes duráveis nem retenção.
- **B)** Usar uma única fila SQS e esperar que todos os consumidores recebam cada evento e possam reler a sequência.
- **C)** Usar Kinesis Data Streams, com device ID como partition key, capacidade dimensionada/on-demand e consumidores apropriados.
- **D)** Gravar eventos em arquivos locais e copiá-los semanalmente.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Kinesis mantém registros ordenados por shard/partition key, permite múltiplos consumidores e replay durante o período de retenção.

Trade-off: Uma partition key muito concentrada cria hot shard. SQS é excelente para filas de trabalho, mas normalmente cada mensagem é consumida como tarefa e não oferece o mesmo modelo de stream/replay. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Cada sensor põe bilhetes numa esteira própria; várias equipes podem reler a sequência enquanto ela ainda está guardada.

**Se acertou:** Acertou: Kinesis mantém registros ordenados por shard/partition key, permite múltiplos consumidores e replay durante o período de retenção. Quando outra opção poderia valer: Uma partition key muito concentrada cria hot shard. SQS é excelente para filas de trabalho, mas normalmente cada mensagem é consumida como tarefa e não oferece o mesmo modelo de stream/replay. Mnemônica: associe “Amazon Kinesis Data Streams” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — SNS faz push, mas sozinho não fornece retenção e replay do stream.
- **B:** Incorreta — Uma fila distribui trabalho; fan-out e replay ordenado exigiriam outro desenho.
- **C:** Correta — Kinesis mantém registros ordenados por shard/partition key, permite múltiplos consumidores e replay durante o período de retenção.
- **D:** Incorreta — Isso não atende baixa latência, durabilidade gerenciada ou múltiplos consumidores.

**Referência oficial:** [https://docs.aws.amazon.com/streams/latest/dev/introduction.html](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

**Referência prática:** ../labs/README.md — Streaming e processamento de eventos

**Exercício recomendado:** No lab Streaming e processamento de eventos, monte uma prova de conceito de Amazon Kinesis Data Streams; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 28. S3 Intelligent-Tiering

> **ID:** `DIAG-Q028` · **Domínio:** D4 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A foodtech panela precisa corrigir uma descoberta da revisão Well-Architected. Os dados incluem informações reguladas e devem permanecer auditáveis. Milhões de objetos têm padrões de acesso desconhecidos e mudam ao longo do tempo. A aplicação exige acesso em milissegundos aos objetos ativos, e a equipe não quer criar regras por prefixo. Qual classe considerar? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Colocar tudo diretamente em Glacier Deep Archive e exigir leitura imediata.
- **B)** Duplicar cada objeto em todas as classes de armazenamento.
- **C)** Usar EBS io2 para armazenar todos os objetos desconhecidos.
- **D)** Usar S3 Intelligent-Tiering, habilitando tiers de archive opcionais apenas se a latência de recuperação for aceitável.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

Intelligent-Tiering monitora acesso e move objetos entre tiers automáticos sem cobrança de recuperação nos tiers de acesso frequente/infrequente, cobrando pequena taxa de monitoramento.

Trade-off: Objetos menores que 128 KB não são monitorados nem movidos automaticamente e permanecem no tier Frequent Access. Archive Access/Deep Archive Access têm recuperação assíncrona e devem ser habilitados conscientemente. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um bibliotecário observa quais livros são lidos e muda sozinho os pouco usados para estantes mais baratas.

**Se acertou:** Acertou: Intelligent-Tiering monitora acesso e move objetos entre tiers automáticos sem cobrança de recuperação nos tiers de acesso frequente/infrequente, cobrando pequena taxa de monitoramento. Quando outra opção poderia valer: Objetos menores que 128 KB não são monitorados nem movidos automaticamente e permanecem no tier Frequent Access. Archive Access/Deep Archive Access têm recuperação assíncrona e devem ser habilitados conscientemente. Mnemônica: associe “S3 Intelligent-Tiering” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Deep Archive não oferece recuperação em milissegundos.
- **B:** Incorreta — Isso multiplica custo e não automatiza seleção do tier apropriado.
- **C:** Incorreta — EBS provisionado seria mais caro e não oferece a semântica/escala de armazenamento de objetos.
- **D:** Correta — Intelligent-Tiering monitora acesso e move objetos entre tiers automáticos sem cobrança de recuperação nos tiers de acesso frequente/infrequente, cobrando pequena taxa de monitoramento.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)

**Referência prática:** ../labs/README.md — S3, lifecycle e classes de armazenamento

**Exercício recomendado:** No lab S3, lifecycle e classes de armazenamento, monte uma prova de conceito de S3 Intelligent-Tiering; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 29. Security groups e network ACLs

> **ID:** `DIAG-Q029` · **Domínio:** D1 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A rede de hotéis brisa está separando produção e desenvolvimento em contas distintas. O tráfego normal é estável, mas cresce oito vezes em campanhas. Servidores web em subnets públicas aceitam HTTPS do mundo e acessam servidores de aplicação em subnets privadas. A equipe quer controles stateful por recurso e uma camada stateless de bloqueio explícito por CIDR na subnet. Qual combinação usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Security groups para permitir apenas os fluxos necessários entre tiers e network ACLs para regras stateless de allow/deny no limite das subnets.
- **B)** Usar apenas uma NACL, pois ela mantém estado das conexões automaticamente.
- **C)** Usar security group para negar explicitamente um CIDR malicioso.
- **D)** Associar uma NACL diretamente a cada instância EC2.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Security groups são stateful e associados a interfaces; NACLs são stateless, ordenadas e associadas a subnets, podendo negar CIDRs explicitamente.

Trade-off: Na maioria dos desenhos, security groups fazem o controle principal. NACLs são defesa adicional e exigem atenção às portas efêmeras nos dois sentidos. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O crachá lembra quem entrou e deixa a resposta voltar; a cancela da rua verifica ida e volta e pode barrar uma placa.

**Se acertou:** Acertou: Security groups são stateful e associados a interfaces; NACLs são stateless, ordenadas e associadas a subnets, podendo negar CIDRs explicitamente. Quando outra opção poderia valer: Na maioria dos desenhos, security groups fazem o controle principal. NACLs são defesa adicional e exigem atenção às portas efêmeras nos dois sentidos. Mnemônica: associe “Security groups e network ACLs” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Security groups são stateful e associados a interfaces; NACLs são stateless, ordenadas e associadas a subnets, podendo negar CIDRs explicitamente.
- **B:** Incorreta — NACLs são stateless e exigem regras correspondentes de entrada e saída.
- **C:** Incorreta — Security groups têm regras de allow, não regras de deny explícito.
- **D:** Incorreta — NACLs são associadas a subnets; security groups são associados às interfaces de rede.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

**Referência prática:** ../labs/README.md — VPC multi-AZ com SG e NACL

**Exercício recomendado:** No lab VPC multi-AZ com SG e NACL, monte uma prova de conceito de Security groups e network ACLs; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 30. DynamoDB Global Tables

> **ID:** `DIAG-Q030` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A cooperativa campo vivo precisa atender a uma auditoria sem redesenhar toda a aplicação. A carga atende milhares de requisições por segundo em horários de pico. Usuários em duas regiões precisam ler e gravar em uma tabela DynamoDB com baixa latência local. A aplicação aceita consistência eventual entre regiões e deve continuar gravando se uma região falhar. Qual solução usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Criar uma tabela comum em uma única região e usar Multi-AZ manualmente.
- **B)** Criar uma DynamoDB global table no modo de consistência eventual multi-região (MREC) e tornar a aplicação tolerante à resolução last-writer-wins.
- **C)** Adicionar DAX em duas regiões sem replicar a tabela.
- **D)** Fazer backup diário e restaurar em cada falha regional.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

Global Tables em MREC fornecem replicação multi-active gerenciada, permitindo leitura e gravação locais nas regiões participantes.

Trade-off: No modo MREC, conflitos concorrentes usam last-writer-wins e a aplicação deve entender essa semântica. O modo MRSC oferece consistência forte multi-região com outra semântica, topologia e disponibilidade regional; a escolha depende do requisito de consistência. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** São dois cadernos mágicos: dá para escrever em qualquer cidade e as novidades aparecem no outro.

**Se acertou:** Acertou: Global Tables em MREC fornecem replicação multi-active gerenciada, permitindo leitura e gravação locais nas regiões participantes. Quando outra opção poderia valer: No modo MREC, conflitos concorrentes usam last-writer-wins e a aplicação deve entender essa semântica. O modo MRSC oferece consistência forte multi-região com outra semântica, topologia e disponibilidade regional; a escolha depende do requisito de consistência. Mnemônica: associe “DynamoDB Global Tables” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — DynamoDB já é multi-AZ na região, mas isso não fornece gravações locais em duas regiões.
- **B:** Correta — Global Tables em MREC fornecem replicação multi-active gerenciada, permitindo leitura e gravação locais nas regiões participantes.
- **C:** Incorreta — DAX é cache regional e não torna a tabela multi-region ou multi-active.
- **D:** Incorreta — Backup/restauração não atende baixa latência local nem continuidade de gravações com RTO curto.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html)

**Referência prática:** ../labs/README.md — DynamoDB, DAX e desenho de chaves

**Exercício recomendado:** No lab DynamoDB, DAX e desenho de chaves, monte uma prova de conceito de DynamoDB Global Tables; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 31. Políticas de Auto Scaling

> **ID:** `DIAG-Q031` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A rede de hotéis brisa precisa corrigir uma descoberta da revisão Well-Architected. O orçamento é limitado e a operação manual deve ser mínima. Uma API em EC2 apresenta carga proporcional a requisições por target. A equipe quer manter cerca de 1.000 requisições por target, adicionando e removendo capacidade automaticamente. Qual política é mais simples? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Criar uma instância por usuário autenticado.
- **B)** Desabilitar health checks para evitar substituições durante picos.
- **C)** Usar target tracking no Auto Scaling com ALBRequestCountPerTarget definido para o valor desejado e warmup apropriado.
- **D)** Usar somente scheduled scaling para uma carga totalmente imprevisível.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Target tracking ajusta capacidade para manter a métrica perto do alvo e gerencia os alarmes subjacentes, reduzindo lógica manual.

Trade-off: Step scaling é útil quando a resposta precisa variar por faixas; scheduled/predictive scaling ajuda cargas previsíveis. Cooldown e warmup evitam oscilações. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O gerente abre caixas até cada caixa ter mais ou menos a fila combinada e fecha os extras quando o movimento cai.

**Se acertou:** Acertou: Target tracking ajusta capacidade para manter a métrica perto do alvo e gerencia os alarmes subjacentes, reduzindo lógica manual. Quando outra opção poderia valer: Step scaling é útil quando a resposta precisa variar por faixas; scheduled/predictive scaling ajuda cargas previsíveis. Cooldown e warmup evitam oscilações. Mnemônica: associe “Políticas de Auto Scaling” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — A relação não é operacionalmente adequada e ignora utilização agregada e limites.
- **B:** Incorreta — Isso mantém instâncias defeituosas e prejudica disponibilidade e desempenho.
- **C:** Correta — Target tracking ajusta capacidade para manter a métrica perto do alvo e gerencia os alarmes subjacentes, reduzindo lógica manual.
- **D:** Incorreta — Agendamento depende de horários conhecidos e não reage bem a rajadas imprevisíveis.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)

**Referência prática:** ../labs/README.md — ALB, Auto Scaling e health checks

**Exercício recomendado:** No lab ALB, Auto Scaling e health checks, monte uma prova de conceito de Políticas de Auto Scaling; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 32. Arquitetura serverless para carga esporádica

> **ID:** `DIAG-Q032` · **Domínio:** D4 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A plataforma de ingressos palco está separando produção e desenvolvimento em contas distintas. A solução atual funciona, mas não atende ao novo requisito não funcional. Uma API recebe poucas chamadas na maior parte do dia e picos curtos imprevisíveis. Não mantém conexões longas nem estado local. A equipe quer pagar principalmente por uso e não administrar servidores. Qual arquitetura é adequada? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Executar a API em um NAT Gateway.
- **B)** Manter dez instâncias On-Demand grandes 24x7 para o pico raro.
- **C)** Usar Dedicated Hosts para cada requisição.
- **D)** API Gateway com Lambda e um armazenamento serverless apropriado, configurando limites, observabilidade e controle de concorrência.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

Serviços serverless escalam sob demanda e cobram por requisição/execução, evitando instâncias ociosas para uma carga esporádica.

Trade-off: Em carga alta e constante, contêineres/instâncias bem utilizados podem custar menos. Cold starts, limites de execução e dependências precisam ser avaliados. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** A barraca abre e chama ajudantes só quando chegam clientes, em vez de pagar uma equipe vazia o dia inteiro.

**Se acertou:** Acertou: Serviços serverless escalam sob demanda e cobram por requisição/execução, evitando instâncias ociosas para uma carga esporádica. Quando outra opção poderia valer: Em carga alta e constante, contêineres/instâncias bem utilizados podem custar menos. Cold starts, limites de execução e dependências precisam ser avaliados. Mnemônica: associe “Arquitetura serverless para carga esporádica” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — NAT Gateway é serviço de tradução de endereços, não runtime de aplicação.
- **B:** Incorreta — A maior parte da capacidade ficaria ociosa e paga.
- **C:** Incorreta — Hosts dedicados são inadequados à granularidade e aumentariam drasticamente o custo.
- **D:** Correta — Serviços serverless escalam sob demanda e cobram por requisição/execução, evitando instâncias ociosas para uma carga esporádica.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html](https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html)

**Referência prática:** ../labs/README.md — Lambda, API Gateway e IAM roles

**Exercício recomendado:** No lab Lambda, API Gateway e IAM roles, monte uma prova de conceito de Arquitetura serverless para carga esporádica; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 33. Autenticação de clientes com Amazon Cognito

> **ID:** `DIAG-Q033` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

O banco digital pioneiro precisa atender a uma auditoria sem redesenhar toda a aplicação. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Um aplicativo móvel voltado a milhões de consumidores precisa cadastro, login, recuperação de senha, MFA opcional e tokens para chamar uma API. A equipe não quer manter um diretório próprio. Qual serviço é indicado? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Usar um Amazon Cognito User Pool como diretório e emissor de tokens, integrando-o ao API Gateway; usar Identity Pool apenas se forem necessárias credenciais AWS temporárias.
- **B)** Usar somente uma API key do API Gateway compartilhada por todos.
- **C)** Criar um usuário IAM para cada consumidor do aplicativo.
- **D)** Salvar senhas em uma tabela DynamoDB sem hash e validar na Lambda.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

User Pools fornecem autenticação de usuários e tokens OIDC/OAuth; a API valida esses tokens sem a equipe operar o armazenamento de senhas.

Trade-off: IAM Identity Center atende principalmente força de trabalho; Cognito é adequado a identidades de clientes. Identity Pools cumprem outro papel: trocar identidades por credenciais AWS temporárias. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É uma portaria pronta que cadastra visitantes e entrega pulseiras válidas para entrar na festa.

**Se acertou:** Acertou: User Pools fornecem autenticação de usuários e tokens OIDC/OAuth; a API valida esses tokens sem a equipe operar o armazenamento de senhas. Quando outra opção poderia valer: IAM Identity Center atende principalmente força de trabalho; Cognito é adequado a identidades de clientes. Identity Pools cumprem outro papel: trocar identidades por credenciais AWS temporárias. Mnemônica: associe “Autenticação de clientes com Amazon Cognito” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — User Pools fornecem autenticação de usuários e tokens OIDC/OAuth; a API valida esses tokens sem a equipe operar o armazenamento de senhas.
- **B:** Incorreta — API keys ajudam em medição e planos de uso; não autenticam individualmente usuários finais.
- **C:** Incorreta — IAM users não são um diretório de clientes em escala e gerariam riscos e operação excessivos.
- **D:** Incorreta — Armazenamento de senhas em texto é inseguro e recria capacidades já gerenciadas pelo Cognito.

**Referência oficial:** [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)

**Referência prática:** ../labs/README.md — API Gateway, Lambda e autenticação

**Exercício recomendado:** No lab API Gateway, Lambda e autenticação, monte uma prova de conceito de Autenticação de clientes com Amazon Cognito; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 34. Falhas assíncronas do Lambda

> **ID:** `DIAG-Q034` · **Domínio:** D2 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A seguradora atlântico precisa corrigir uma descoberta da revisão Well-Architected. A equipe precisa provar a decisão com um teste pequeno e reversível. Uma função Lambda é invocada de modo assíncrono por eventos. Após as tentativas automáticas, eventos malsucedidos devem ser preservados para investigação e reprocessamento, sem bloquear eventos saudáveis. O que configurar? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Reenviar o mesmo evento recursivamente dentro da função sem limite.
- **B)** Configurar uma on-failure destination para SQS/SNS/EventBridge ou uma DLQ compatível, além de alarmes e processamento idempotente.
- **C)** Definir timeout infinito para garantir que toda execução termine.
- **D)** Desativar logs para impedir que falhas afetem o serviço.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

Invocações assíncronas possuem fila e retries gerenciados; destinations entregam contexto do resultado após as tentativas, permitindo análise e reprocessamento desacoplado.

Trade-off: DLQ e destination têm formatos e capacidades diferentes; a equipe deve escolher um, observar idade máxima do evento e evitar loops de reprocessamento. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Cartinhas que o robô não consegue ler vão para uma caixa vermelha, sem parar a leitura das demais.

**Se acertou:** Acertou: Invocações assíncronas possuem fila e retries gerenciados; destinations entregam contexto do resultado após as tentativas, permitindo análise e reprocessamento desacoplado. Quando outra opção poderia valer: DLQ e destination têm formatos e capacidades diferentes; a equipe deve escolher um, observar idade máxima do evento e evitar loops de reprocessamento. Mnemônica: associe “Falhas assíncronas do Lambda” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Isso pode criar loop, duplicidade e custo sem isolar o evento defeituoso.
- **B:** Correta — Invocações assíncronas possuem fila e retries gerenciados; destinations entregam contexto do resultado após as tentativas, permitindo análise e reprocessamento desacoplado.
- **C:** Incorreta — Lambda tem limite de timeout e aumentar duração não resolve eventos permanentemente inválidos.
- **D:** Incorreta — Logs não causam a falha e removê-los prejudica diagnóstico e observabilidade.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html)

**Referência prática:** ../labs/README.md — Lambda, API Gateway e tratamento de erros

**Exercício recomendado:** No lab Lambda, API Gateway e tratamento de erros, monte uma prova de conceito de Falhas assíncronas do Lambda; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 35. Lambda provisioned concurrency

> **ID:** `DIAG-Q035` · **Domínio:** D3 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

O banco digital pioneiro está separando produção e desenvolvimento em contas distintas. A carga atende milhares de requisições por segundo em horários de pico. Uma função Lambda síncrona atende uma API sensível à latência. Após períodos ociosos, cold starts ultrapassam o SLA; o volume do horário comercial é previsível. Qual recurso reduz essa variação? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Aumentar o timeout e assumir que isso inicializa a função antes da chamada.
- **B)** Usar reserved concurrency como sinônimo de ambientes sempre aquecidos.
- **C)** Configurar provisioned concurrency no alias/versão e, se adequado, escalá-la por agenda ou Application Auto Scaling.
- **D)** Colocar respostas da função em um volume instance store.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Provisioned concurrency mantém ambientes inicializados e prontos, reduzindo cold starts para invocações atendidas pela capacidade provisionada.

Trade-off: Provisioned concurrency gera custo enquanto alocada; para cargas tolerantes a cold start, memória maior, código otimizado ou SnapStart em runtimes compatíveis podem ser melhores. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Os cozinheiros ficam de avental e panela quente antes do primeiro pedido, em vez de abrir a cozinha do zero.

**Se acertou:** Acertou: Provisioned concurrency mantém ambientes inicializados e prontos, reduzindo cold starts para invocações atendidas pela capacidade provisionada. Quando outra opção poderia valer: Provisioned concurrency gera custo enquanto alocada; para cargas tolerantes a cold start, memória maior, código otimizado ou SnapStart em runtimes compatíveis podem ser melhores. Mnemônica: associe “Lambda provisioned concurrency” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Timeout limita duração após invocação; não pré-inicializa ambientes.
- **B:** Incorreta — Reserved concurrency protege/limita capacidade, mas não inicializa ambientes como provisioned concurrency.
- **C:** Correta — Provisioned concurrency mantém ambientes inicializados e prontos, reduzindo cold starts para invocações atendidas pela capacidade provisionada.
- **D:** Incorreta — Lambda não fornece instance store persistente dessa forma e isso não elimina inicialização.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

**Referência prática:** ../labs/README.md — Lambda, API Gateway e desempenho

**Exercício recomendado:** No lab Lambda, API Gateway e desempenho, monte uma prova de conceito de Lambda provisioned concurrency; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 36. Proteção de camada 7 com AWS WAF

> **ID:** `DIAG-Q036` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A edtech farol precisa atender a uma auditoria sem redesenhar toda a aplicação. A solução atual funciona, mas não atende ao novo requisito não funcional. Uma API pública atrás de um ALB sofre credential stuffing e rajadas de um pequeno conjunto de endereços IP. É necessário bloquear padrões HTTP e limitar requisições por origem sem alterar a aplicação. O que fazer? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Editar a NACL para bloquear palavras presentes no corpo HTTP.
- **B)** Usar apenas AWS Shield Standard para identificar senhas reutilizadas.
- **C)** Aumentar o número de instâncias do Auto Scaling sem filtrar as requisições.
- **D)** Associar um Web ACL do AWS WAF ao ALB, usando managed rules e uma rate-based rule ajustada ao tráfego legítimo.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

WAF inspeciona atributos HTTP(S) e regras baseadas em taxa agregam requisições por chave, bloqueando ou desafiando origens abusivas na camada 7.

Trade-off: Shield Standard está incluído e lida com ataques DDoS comuns de rede e transporte; Shield Advanced acrescenta resposta e proteção de custo, mas não substitui regras HTTP do WAF. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O porteiro reconhece truques nas cartas e manda quem bate vezes demais esperar do lado de fora.

**Se acertou:** Acertou: WAF inspeciona atributos HTTP(S) e regras baseadas em taxa agregam requisições por chave, bloqueando ou desafiando origens abusivas na camada 7. Quando outra opção poderia valer: Shield Standard está incluído e lida com ataques DDoS comuns de rede e transporte; Shield Advanced acrescenta resposta e proteção de custo, mas não substitui regras HTTP do WAF. Mnemônica: associe “Proteção de camada 7 com AWS WAF” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — NACLs operam em rede e não inspecionam conteúdo HTTP.
- **B:** Incorreta — Shield não implementa lógica de credential stuffing baseada em campos e padrões HTTP.
- **C:** Incorreta — Escalar pode absorver carga, mas não bloqueia abuso e ainda amplia custo.
- **D:** Correta — WAF inspeciona atributos HTTP(S) e regras baseadas em taxa agregam requisições por chave, bloqueando ou desafiando origens abusivas na camada 7.

**Referência oficial:** [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)

**Referência prática:** ../labs/README.md — S3/CloudFront/WAF e proteção web

**Exercício recomendado:** No lab S3/CloudFront/WAF e proteção web, monte uma prova de conceito de Proteção de camada 7 com AWS WAF; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 37. Políticas centralizadas com AWS Backup

> **ID:** `DIAG-Q037` · **Domínio:** D2 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A foodtech panela precisa corrigir uma descoberta da revisão Well-Architected. O tráfego normal é estável, mas cresce oito vezes em campanhas. Dezenas de contas precisam de backups consistentes de EBS, RDS e EFS, cópias entre regiões e proteção contra exclusão pela conta de origem. Segurança quer governança central. Qual abordagem usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Usar AWS Backup com backup policies da organização, cofre central/cross-account, cópia cross-region e Vault Lock quando a imutabilidade for requerida.
- **B)** Pedir que cada desenvolvedor crie snapshots manuais quando lembrar.
- **C)** Usar apenas RDS Multi-AZ como backup histórico.
- **D)** Copiar arquivos para o disco local de uma instância na mesma conta.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

AWS Backup centraliza planos, seleção, retenção e cópias entre serviços e contas; Vault Lock ajuda a impor retenção WORM contra alterações indevidas.

Trade-off: Backup só é confiável quando restaurações são testadas e métricas de RPO/RTO são verificadas; replicação e alta disponibilidade não substituem backups protegidos. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um bibliotecário central faz cópias de todos os livros, guarda outra caixa em outra cidade e lacra as caixas pelo prazo certo.

**Se acertou:** Acertou: AWS Backup centraliza planos, seleção, retenção e cópias entre serviços e contas; Vault Lock ajuda a impor retenção WORM contra alterações indevidas. Quando outra opção poderia valer: Backup só é confiável quando restaurações são testadas e métricas de RPO/RTO são verificadas; replicação e alta disponibilidade não substituem backups protegidos. Mnemônica: associe “Políticas centralizadas com AWS Backup” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — AWS Backup centraliza planos, seleção, retenção e cópias entre serviços e contas; Vault Lock ajuda a impor retenção WORM contra alterações indevidas.
- **B:** Incorreta — O processo não é consistente, auditável nem centralmente imposto.
- **C:** Incorreta — Multi-AZ é alta disponibilidade e replica também erros lógicos; não é retenção histórica independente.
- **D:** Incorreta — A cópia permanece vulnerável a falhas e exclusões na mesma fronteira administrativa.

**Referência oficial:** [https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html)

**Referência prática:** ../labs/README.md — Backup, restore e testes de recuperação

**Exercício recomendado:** No lab Backup, restore e testes de recuperação, monte uma prova de conceito de Políticas centralizadas com AWS Backup; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 38. Athena, partições e formato colunar

> **ID:** `DIAG-Q038` · **Domínio:** D3 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A edtech farol está separando produção e desenvolvimento em contas distintas. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Consultas Athena leem logs no S3 particionados apenas em arquivos JSON grandes e escaneiam terabytes para filtrar um único dia e região. Como reduzir tempo e bytes processados? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Usar SELECT * em todas as consultas para aumentar o cache.
- **B)** Converter dados para Parquet/ORC comprimido, particionar por campos usados em filtros e garantir partition pruning/projection nas consultas.
- **C)** Mover logs para S3 Glacier Deep Archive e consultá-los diretamente a cada minuto.
- **D)** Renomear JSON para .parquet sem transformar o conteúdo.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

Formatos colunares leem apenas colunas necessárias; partições permitem ignorar diretórios inteiros, reduzindo I/O, latência e custo por dados examinados.

Trade-off: Partições demais e arquivos minúsculos também prejudicam desempenho. Compactação e tamanho de arquivo devem ser equilibrados com paralelismo. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Em vez de ler todos os cadernos, organizamos gavetas por dia e guardamos cada assunto em colunas fáceis de pegar.

**Se acertou:** Acertou: Formatos colunares leem apenas colunas necessárias; partições permitem ignorar diretórios inteiros, reduzindo I/O, latência e custo por dados examinados. Quando outra opção poderia valer: Partições demais e arquivos minúsculos também prejudicam desempenho. Compactação e tamanho de arquivo devem ser equilibrados com paralelismo. Mnemônica: associe “Athena, partições e formato colunar” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Ler todas as colunas aumenta dados examinados e normalmente piora custo e latência.
- **B:** Correta — Formatos colunares leem apenas colunas necessárias; partições permitem ignorar diretórios inteiros, reduzindo I/O, latência e custo por dados examinados.
- **C:** Incorreta — Objetos arquivados exigem restauração e não são adequados a consultas interativas contínuas.
- **D:** Incorreta — A extensão não muda o formato físico nem habilita leitura colunar.

**Referência oficial:** [https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html)

**Referência prática:** ../labs/README.md — Data lake no S3 e consultas Athena

**Exercício recomendado:** No lab Data lake no S3 e consultas Athena, monte uma prova de conceito de Athena, partições e formato colunar; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 39. S3 Block Public Access e políticas

> **ID:** `DIAG-Q039` · **Domínio:** D1 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A plataforma de ingressos palco precisa atender a uma auditoria sem redesenhar toda a aplicação. A carga atende milhares de requisições por segundo em horários de pico. Uma empresa armazena relatórios confidenciais em centenas de buckets. Ela precisa impedir exposição pública acidental em toda a organização e permitir acesso apenas por um VPC endpoint específico. Qual desenho é mais seguro? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Associar um security group diretamente ao bucket.
- **B)** Criptografar os objetos, mas deixar leitura pública para qualquer principal.
- **C)** Ativar S3 Block Public Access no nível da organização/contas e aplicar bucket policies com condição aws:SourceVpce e negação fora do endpoint autorizado.
- **D)** Usar ACL public-read e esconder os nomes dos objetos.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Block Public Access neutraliza políticas e ACLs públicas; uma bucket policy com condição e Deny explícito restringe o caminho de acesso ao endpoint aprovado.

Trade-off: Ao usar condições de endpoint, é preciso preservar acessos administrativos e de serviços necessários para não bloquear operações legítimas de forma acidental. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Primeiro fechamos todas as janelas do prédio; depois damos uma chave que só funciona na passagem secreta certa.

**Se acertou:** Acertou: Block Public Access neutraliza políticas e ACLs públicas; uma bucket policy com condição e Deny explícito restringe o caminho de acesso ao endpoint aprovado. Quando outra opção poderia valer: Ao usar condições de endpoint, é preciso preservar acessos administrativos e de serviços necessários para não bloquear operações legítimas de forma acidental. Mnemônica: associe “S3 Block Public Access e políticas” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Buckets S3 não aceitam security groups.
- **B:** Incorreta — Criptografia em repouso não corrige uma autorização pública; serviços autorizados ainda descriptografariam dados.
- **C:** Correta — Block Public Access neutraliza políticas e ACLs públicas; uma bucket policy com condição e Deny explícito restringe o caminho de acesso ao endpoint aprovado.
- **D:** Incorreta — Obscuridade de nomes não é controle de acesso, e a ACL tornaria dados públicos.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

**Referência prática:** ../labs/README.md — S3 privado e endpoints VPC

**Exercício recomendado:** No lab S3 privado e endpoints VPC, monte uma prova de conceito de S3 Block Public Access e políticas; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 40. Permissions boundaries e delegação

> **ID:** `DIAG-Q040` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A rede hospitalar horizonte precisa corrigir uma descoberta da revisão Well-Architected. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Uma plataforma permite que times de produto criem suas próprias roles, mas segurança precisa garantir que nenhuma role criada ultrapasse um conjunto máximo de ações. Os times ainda devem escolher permissões dentro desse limite. Qual recurso usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Anexar AdministratorAccess e pedir que cada time não use ações perigosas.
- **B)** Usar uma NACL para limitar quais APIs IAM podem ser chamadas.
- **C)** Criar somente tags sem nenhuma condição de IAM associada.
- **D)** Exigir uma permissions boundary nas roles criadas e controlar iam:PermissionsBoundary nas políticas do time.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

A permissions boundary define o máximo que uma policy de identidade pode conceder, permitindo delegação sem entregar privilégios ilimitados.

Trade-off: Boundary não concede acesso por si só e precisa ser avaliada junto de policies de identidade, recurso, SCPs e negações explícitas. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** A criança escolhe onde brincar no quintal, mas a cerca define até onde ela pode ir.

**Se acertou:** Acertou: A permissions boundary define o máximo que uma policy de identidade pode conceder, permitindo delegação sem entregar privilégios ilimitados. Quando outra opção poderia valer: Boundary não concede acesso por si só e precisa ser avaliada junto de policies de identidade, recurso, SCPs e negações explícitas. Mnemônica: associe “Permissions boundaries e delegação” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Confiança processual não impõe um limite técnico e AdministratorAccess viola privilégio mínimo.
- **B:** Incorreta — NACLs filtram pacotes e não avaliam ações IAM.
- **C:** Incorreta — Tags isoladas são metadados; o controle exige policies que as avaliem.
- **D:** Correta — A permissions boundary define o máximo que uma policy de identidade pode conceder, permitindo delegação sem entregar privilégios ilimitados.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)

**Referência prática:** ../labs/README.md — IAM least privilege e roles

**Exercício recomendado:** No lab IAM least privilege e roles, monte uma prova de conceito de Permissions boundaries e delegação; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---
