# Mini-quiz 08 — Domínio 3 — Projetar arquiteturas de alto desempenho

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Athena, partições e formato colunar

> **ID:** `QUIZ-D3-08-Q01` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A plataforma de ingressos palco recebe picos imprevisíveis sem poder degradar o SLA. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Consultas Athena leem logs no S3 particionados apenas em arquivos JSON grandes e escaneiam terabytes para filtrar um único dia e região. Como reduzir tempo e bytes processados? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Renomear JSON para .parquet sem transformar o conteúdo.
- **B)** Usar SELECT * em todas as consultas para aumentar o cache.
- **C)** Converter dados para Parquet/ORC comprimido, particionar por campos usados em filtros e garantir partition pruning/projection nas consultas.
- **D)** Mover logs para S3 Glacier Deep Archive e consultá-los diretamente a cada minuto.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Formatos colunares leem apenas colunas necessárias; partições permitem ignorar diretórios inteiros, reduzindo I/O, latência e custo por dados examinados.

Trade-off: Partições demais e arquivos minúsculos também prejudicam desempenho. Compactação e tamanho de arquivo devem ser equilibrados com paralelismo. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Em vez de ler todos os cadernos, organizamos gavetas por dia e guardamos cada assunto em colunas fáceis de pegar.

**Se acertou:** Acertou: Formatos colunares leem apenas colunas necessárias; partições permitem ignorar diretórios inteiros, reduzindo I/O, latência e custo por dados examinados. Quando outra opção poderia valer: Partições demais e arquivos minúsculos também prejudicam desempenho. Compactação e tamanho de arquivo devem ser equilibrados com paralelismo. Mnemônica: associe “Athena, partições e formato colunar” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — A extensão não muda o formato físico nem habilita leitura colunar.
- **B:** Incorreta — Ler todas as colunas aumenta dados examinados e normalmente piora custo e latência.
- **C:** Correta — Formatos colunares leem apenas colunas necessárias; partições permitem ignorar diretórios inteiros, reduzindo I/O, latência e custo por dados examinados.
- **D:** Incorreta — Objetos arquivados exigem restauração e não são adequados a consultas interativas contínuas.

**Referência oficial:** [https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html)

**Referência prática:** ../labs/README.md — Data lake no S3 e consultas Athena

**Exercício recomendado:** No lab Data lake no S3 e consultas Athena, monte uma prova de conceito de Athena, partições e formato colunar; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. Cache global com CloudFront

> **ID:** `QUIZ-D3-08-Q02` · **Domínio:** D3 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A rede hospitalar horizonte está migrando uma carga crítica para a AWS. A solução atual funciona, mas não atende ao novo requisito não funcional. Um portal entrega imagens e arquivos estáticos do S3 a usuários globais. A origem recebe leituras repetidas e usuários distantes observam alta latência. Qual mudança melhora desempenho com menor operação? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Usar Route 53 weighted routing para armazenar objetos em cache.
- **B)** Aumentar o tamanho do bucket S3.
- **C)** Copiar manualmente todos os objetos para volumes EBS em cada região.
- **D)** Distribuir o conteúdo com CloudFront, definir cache policies/TTLs adequados, compressão e OAC para a origem S3 privada.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

CloudFront guarda objetos em edge locations próximas aos usuários, reduzindo latência e carga na origem; políticas de cache controlam a chave e a validade.

Trade-off: TTL longo aumenta hit ratio, mas atrasa atualizações; versionar nomes de objetos é geralmente mais previsível que invalidar grandes volumes. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Em vez de buscar cada brinquedo na fábrica distante, pequenas lojas perto das crianças guardam os mais pedidos.

**Se acertou:** Acertou: CloudFront guarda objetos em edge locations próximas aos usuários, reduzindo latência e carga na origem; políticas de cache controlam a chave e a validade. Quando outra opção poderia valer: TTL longo aumenta hit ratio, mas atrasa atualizações; versionar nomes de objetos é geralmente mais previsível que invalidar grandes volumes. Mnemônica: associe “Cache global com CloudFront” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Route 53 responde DNS; ele não armazena nem entrega o conteúdo.
- **B:** Incorreta — S3 não precisa de provisionamento de capacidade do bucket e isso não aproxima conteúdo do usuário.
- **C:** Incorreta — Isso cria operação, inconsistência e não fornece uma rede de borda global.
- **D:** Correta — CloudFront guarda objetos em edge locations próximas aos usuários, reduzindo latência e carga na origem; políticas de cache controlam a chave e a validade.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html)

**Referência prática:** ../labs/README.md — S3, CloudFront e WAF

**Exercício recomendado:** No lab S3, CloudFront e WAF, monte uma prova de conceito de Cache global com CloudFront; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. ElastiCache for Redis

> **ID:** `QUIZ-D3-08-Q03` · **Domínio:** D3 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A empresa de logística rota certa deve manter a solução simples para a equipe de plantão. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Uma API lê repetidamente os mesmos registros de sessão e catálogo em um banco relacional. O banco está no limite de CPU, e dados em cache podem expirar em minutos. Qual solução reduz a latência? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Adicionar ElastiCache for Redis e aplicar cache-aside com TTL, tratamento de cache miss e invalidação coerente.
- **B)** Aumentar indefinidamente o TTL de DNS do banco.
- **C)** Mover registros de sessão para S3 Glacier Deep Archive.
- **D)** Criar uma read replica e gravar sessões diretamente nela.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Redis oferece acesso em memória de baixa latência e remove leituras repetitivas do banco; cache-aside mantém o banco como fonte de verdade.

Trade-off: Cache introduz risco de dados obsoletos e stampede. TTL, jitter, réplicas e comportamento quando o cache falha devem ser desenhados. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** As respostas mais usadas ficam em post-its na mesa, em vez de procurar o livro inteiro a cada pergunta.

**Se acertou:** Acertou: Redis oferece acesso em memória de baixa latência e remove leituras repetitivas do banco; cache-aside mantém o banco como fonte de verdade. Quando outra opção poderia valer: Cache introduz risco de dados obsoletos e stampede. TTL, jitter, réplicas e comportamento quando o cache falha devem ser desenhados. Mnemônica: associe “ElastiCache for Redis” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Redis oferece acesso em memória de baixa latência e remove leituras repetitivas do banco; cache-aside mantém o banco como fonte de verdade.
- **B:** Incorreta — Cache DNS não armazena resultados de consulta nem reduz CPU de execução SQL.
- **C:** Incorreta — A classe tem recuperação lenta e não serve a acesso interativo de baixa latência.
- **D:** Incorreta — Read replicas relacionais normalmente são somente leitura e não são ideais como armazenamento de sessão volátil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html)

**Referência prática:** ../labs/README.md — Cache, banco e observabilidade

**Exercício recomendado:** No lab Cache, banco e observabilidade, monte uma prova de conceito de ElastiCache for Redis; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 4. Chave de partição do DynamoDB

> **ID:** `QUIZ-D3-08-Q04` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A empresa de jogos capivara recebe picos imprevisíveis sem poder degradar o SLA. A solução atual funciona, mas não atende ao novo requisito não funcional. Uma tabela DynamoDB recebe gravações intensas. A chave de partição atual usa apenas o código de um país, e um país concentra 80% do tráfego, causando throttling. Qual redesign é mais apropriado? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Manter o país como única chave e aumentar o tamanho de uma instância DynamoDB.
- **B)** Escolher uma chave de alta cardinalidade que distribua acessos, usando write sharding quando necessário, e manter padrões de consulta com índices adequados.
- **C)** Criar uma chave constante para garantir ordem global.
- **D)** Adicionar apenas mais atributos sem alterar chaves ou índices.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

DynamoDB distribui itens pela chave de partição; poucas chaves populares concentram capacidade. Alta cardinalidade e sharding espalham as requisições.

Trade-off: On-demand ajusta capacidade, mas não elimina todos os efeitos de uma hot partition. O modelo deve começar pelos padrões de acesso, não por normalização relacional. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Se todos entrarem pela mesma porta, forma fila; várias portas bem escolhidas distribuem a turma.

**Se acertou:** Acertou: DynamoDB distribui itens pela chave de partição; poucas chaves populares concentram capacidade. Alta cardinalidade e sharding espalham as requisições. Quando outra opção poderia valer: On-demand ajusta capacidade, mas não elimina todos os efeitos de uma hot partition. O modelo deve começar pelos padrões de acesso, não por normalização relacional. Mnemônica: associe “Chave de partição do DynamoDB” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — DynamoDB é serverless e não expõe tamanho de instância; a chave quente continua problemática.
- **B:** Correta — DynamoDB distribui itens pela chave de partição; poucas chaves populares concentram capacidade. Alta cardinalidade e sharding espalham as requisições.
- **C:** Incorreta — Uma única chave concentra toda a carga em uma partição lógica.
- **D:** Incorreta — Atributos extras não mudam a distribuição das requisições.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)

**Referência prática:** ../labs/README.md — DynamoDB, DAX e modelagem de chaves

**Exercício recomendado:** No lab DynamoDB, DAX e modelagem de chaves, monte uma prova de conceito de Chave de partição do DynamoDB; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 5. Read replicas para escalar leituras

> **ID:** `QUIZ-D3-08-Q05` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A plataforma de ingressos palco está migrando uma carga crítica para a AWS. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Um banco RDS atende relatórios pesados que disputam CPU e I/O com transações. Os relatórios toleram alguns segundos de defasagem e a alta disponibilidade já está coberta. O que fazer? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Aumentar o TTL do Route 53 do endpoint do banco.
- **B)** Usar o standby Multi-AZ diretamente para todas as consultas de relatório.
- **C)** Criar read replicas e direcionar consultas de relatório aos endpoints de leitura, monitorando replication lag.
- **D)** Fazer snapshots a cada minuto e consultar os snapshots.

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

- **A:** Incorreta — TTL DNS não reduz a carga de consultas no primário.
- **B:** Incorreta — Na implantação Multi-AZ tradicional, o standby não é endpoint de leitura da aplicação.
- **C:** Correta — Read replicas usam replicação assíncrona para retirar consultas de leitura do primário; a tolerância a defasagem torna a solução adequada.
- **D:** Incorreta — Snapshots não são uma interface de consulta e restaurações frequentes não servem a relatórios online.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

**Referência prática:** ../labs/README.md — RDS Multi-AZ e read replica

**Exercício recomendado:** No lab RDS Multi-AZ e read replica, monte uma prova de conceito de Read replicas para escalar leituras; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---
