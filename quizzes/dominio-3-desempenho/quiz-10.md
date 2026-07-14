# Mini-quiz 10 — Domínio 3 — Projetar arquiteturas de alto desempenho

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Políticas de Auto Scaling

> **ID:** `QUIZ-D3-10-Q01` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A empresa de logística rota certa vai lançar o serviço em três países. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Uma API em EC2 apresenta carga proporcional a requisições por target. A equipe quer manter cerca de 1.000 requisições por target, adicionando e removendo capacidade automaticamente. Qual política é mais simples? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Usar target tracking no Auto Scaling com ALBRequestCountPerTarget definido para o valor desejado e warmup apropriado.
- **B)** Desabilitar health checks para evitar substituições durante picos.
- **C)** Usar somente scheduled scaling para uma carga totalmente imprevisível.
- **D)** Criar uma instância por usuário autenticado.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Target tracking ajusta capacidade para manter a métrica perto do alvo e gerencia os alarmes subjacentes, reduzindo lógica manual.

Trade-off: Step scaling é útil quando a resposta precisa variar por faixas; scheduled/predictive scaling ajuda cargas previsíveis. Cooldown e warmup evitam oscilações. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O gerente abre caixas até cada caixa ter mais ou menos a fila combinada e fecha os extras quando o movimento cai.

**Se acertou:** Acertou: Target tracking ajusta capacidade para manter a métrica perto do alvo e gerencia os alarmes subjacentes, reduzindo lógica manual. Quando outra opção poderia valer: Step scaling é útil quando a resposta precisa variar por faixas; scheduled/predictive scaling ajuda cargas previsíveis. Cooldown e warmup evitam oscilações. Mnemônica: associe “Políticas de Auto Scaling” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Target tracking ajusta capacidade para manter a métrica perto do alvo e gerencia os alarmes subjacentes, reduzindo lógica manual.
- **B:** Incorreta — Isso mantém instâncias defeituosas e prejudica disponibilidade e desempenho.
- **C:** Incorreta — Agendamento depende de horários conhecidos e não reage bem a rajadas imprevisíveis.
- **D:** Incorreta — A relação não é operacionalmente adequada e ignora utilização agregada e limites.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)

**Referência prática:** ../labs/README.md — ALB, Auto Scaling e health checks

**Exercício recomendado:** No lab ALB, Auto Scaling e health checks, monte uma prova de conceito de Políticas de Auto Scaling; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. Lambda provisioned concurrency

> **ID:** `QUIZ-D3-10-Q02` · **Domínio:** D3 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A empresa de jogos capivara precisa tomar uma decisão com base em desempenho, segurança e custo total. A solução atual funciona, mas não atende ao novo requisito não funcional. Uma função Lambda síncrona atende uma API sensível à latência. Após períodos ociosos, cold starts ultrapassam o SLA; o volume do horário comercial é previsível. Qual recurso reduz essa variação? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Usar reserved concurrency como sinônimo de ambientes sempre aquecidos.
- **B)** Configurar provisioned concurrency no alias/versão e, se adequado, escalá-la por agenda ou Application Auto Scaling.
- **C)** Colocar respostas da função em um volume instance store.
- **D)** Aumentar o timeout e assumir que isso inicializa a função antes da chamada.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

Provisioned concurrency mantém ambientes inicializados e prontos, reduzindo cold starts para invocações atendidas pela capacidade provisionada.

Trade-off: Provisioned concurrency gera custo enquanto alocada; para cargas tolerantes a cold start, memória maior, código otimizado ou SnapStart em runtimes compatíveis podem ser melhores. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Os cozinheiros ficam de avental e panela quente antes do primeiro pedido, em vez de abrir a cozinha do zero.

**Se acertou:** Acertou: Provisioned concurrency mantém ambientes inicializados e prontos, reduzindo cold starts para invocações atendidas pela capacidade provisionada. Quando outra opção poderia valer: Provisioned concurrency gera custo enquanto alocada; para cargas tolerantes a cold start, memória maior, código otimizado ou SnapStart em runtimes compatíveis podem ser melhores. Mnemônica: associe “Lambda provisioned concurrency” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Reserved concurrency protege/limita capacidade, mas não inicializa ambientes como provisioned concurrency.
- **B:** Correta — Provisioned concurrency mantém ambientes inicializados e prontos, reduzindo cold starts para invocações atendidas pela capacidade provisionada.
- **C:** Incorreta — Lambda não fornece instance store persistente dessa forma e isso não elimina inicialização.
- **D:** Incorreta — Timeout limita duração após invocação; não pré-inicializa ambientes.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

**Referência prática:** ../labs/README.md — Lambda, API Gateway e desempenho

**Exercício recomendado:** No lab Lambda, API Gateway e desempenho, monte uma prova de conceito de Lambda provisioned concurrency; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. Athena, partições e formato colunar

> **ID:** `QUIZ-D3-10-Q03` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A plataforma de ingressos palco quer substituir um componente autogerenciado por um serviço gerenciado. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Consultas Athena leem logs no S3 particionados apenas em arquivos JSON grandes e escaneiam terabytes para filtrar um único dia e região. Como reduzir tempo e bytes processados? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 4. Cache global com CloudFront

> **ID:** `QUIZ-D3-10-Q04` · **Domínio:** D3 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A rede hospitalar horizonte vai lançar o serviço em três países. A solução atual funciona, mas não atende ao novo requisito não funcional. Um portal entrega imagens e arquivos estáticos do S3 a usuários globais. A origem recebe leituras repetidas e usuários distantes observam alta latência. Qual mudança melhora desempenho com menor operação? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

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

## 5. ElastiCache for Redis

> **ID:** `QUIZ-D3-10-Q05` · **Domínio:** D3 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A empresa de logística rota certa precisa tomar uma decisão com base em desempenho, segurança e custo total. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Uma API lê repetidamente os mesmos registros de sessão e catálogo em um banco relacional. O banco está no limite de CPU, e dados em cache podem expirar em minutos. Qual solução reduz a latência? Escolha a alternativa que atende diretamente ao requisito.

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
