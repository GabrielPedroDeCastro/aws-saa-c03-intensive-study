# Mini-quiz 04 — Domínio 3 — Projetar arquiteturas de alto desempenho

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Read replicas para escalar leituras

> **ID:** `QUIZ-D3-04-Q01` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A plataforma de ingressos palco deve manter a solução simples para a equipe de plantão. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Um banco RDS atende relatórios pesados que disputam CPU e I/O com transações. Os relatórios toleram alguns segundos de defasagem e a alta disponibilidade já está coberta. O que fazer? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 2. Tipos de volume EBS

> **ID:** `QUIZ-D3-04-Q02` · **Domínio:** D3 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A rede hospitalar horizonte recebe picos imprevisíveis sem poder degradar o SLA. A solução atual funciona, mas não atende ao novo requisito não funcional. Um banco autogerenciado em EC2 exige latência de I/O consistente e dezenas de milhares de IOPS sustentadas. A performance deve ser previsível, mesmo que custe mais que uso geral. Qual volume escolher? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Usar st1 para milhões de pequenos I/Os aleatórios.
- **B)** Usar instance store sem replicação porque todo dado EBS é efêmero.
- **C)** Usar sc1 porque é o volume com menor latência para bancos críticos.
- **D)** Usar EBS io2, dimensionando IOPS e throughput conforme a instância e a carga, e validar limites ponta a ponta.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

io2 é SSD de Provisioned IOPS para workloads críticos que precisam de desempenho consistente e alta durabilidade.

Trade-off: gp3 é excelente padrão custo/desempenho e permite provisionar IOPS/throughput, mas io2 atende os requisitos mais rigorosos. st1/sc1 são HDD para acesso sequencial e não podem ser boot volume. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É uma pista expressa com número de faixas reservado, em vez de torcer para a rua comum estar vazia.

**Se acertou:** Acertou: io2 é SSD de Provisioned IOPS para workloads críticos que precisam de desempenho consistente e alta durabilidade. Quando outra opção poderia valer: gp3 é excelente padrão custo/desempenho e permite provisionar IOPS/throughput, mas io2 atende os requisitos mais rigorosos. st1/sc1 são HDD para acesso sequencial e não podem ser boot volume. Mnemônica: associe “Tipos de volume EBS” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — st1 é otimizado a throughput sequencial, não IOPS aleatórios de banco.
- **B:** Incorreta — EBS é persistente; instance store é que é efêmero e exigiria proteção adicional.
- **C:** Incorreta — sc1 é HDD de baixo custo para acesso pouco frequente e não oferece latência SSD.
- **D:** Correta — io2 é SSD de Provisioned IOPS para workloads críticos que precisam de desempenho consistente e alta durabilidade.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

**Referência prática:** ../labs/README.md — EC2, EBS e teste de I/O

**Exercício recomendado:** No lab EC2, EBS e teste de I/O, monte uma prova de conceito de Tipos de volume EBS; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. Transferência para Amazon S3

> **ID:** `QUIZ-D3-04-Q03` · **Domínio:** D3 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A empresa de logística rota certa está migrando uma carga crítica para a AWS. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Filiais globais enviam arquivos de 200 GB ao S3 por links de longa distância. A equipe quer paralelizar uploads, retomar partes com falha e melhorar o caminho pela rede AWS. Qual combinação usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Usar S3 multipart upload e avaliar S3 Transfer Acceleration para ingressar pela edge location mais próxima.
- **B)** Enviar cada arquivo em uma única requisição e reiniciar tudo em qualquer falha.
- **C)** Usar S3 Glacier restore antes de cada upload.
- **D)** Colocar um NAT Gateway na filial sem conexão com a AWS.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Multipart divide o objeto, permite upload paralelo e repetição de partes; Transfer Acceleration usa a rede global da AWS a partir da borda.

Trade-off: Transfer Acceleration tem custo adicional e benefício dependente da rota; deve ser testado. Para migração offline massiva, Snowball pode ser mais apropriado. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Um caminhão enorme vira várias caixas; se uma cai, reenviamos só aquela, e elas entram pela garagem mais próxima.

**Se acertou:** Acertou: Multipart divide o objeto, permite upload paralelo e repetição de partes; Transfer Acceleration usa a rede global da AWS a partir da borda. Quando outra opção poderia valer: Transfer Acceleration tem custo adicional e benefício dependente da rota; deve ser testado. Para migração offline massiva, Snowball pode ser mais apropriado. Mnemônica: associe “Transferência para Amazon S3” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Multipart divide o objeto, permite upload paralelo e repetição de partes; Transfer Acceleration usa a rede global da AWS a partir da borda.
- **B:** Incorreta — Isso perde paralelismo e torna falhas caras em objetos grandes.
- **C:** Incorreta — Restore recupera objetos arquivados e não acelera novos uploads.
- **D:** Incorreta — NAT Gateway é implantado em VPC e não melhora sozinho a rota WAN da filial.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

**Referência prática:** ../labs/README.md — S3, multipart e desempenho

**Exercício recomendado:** No lab S3, multipart e desempenho, monte uma prova de conceito de Transferência para Amazon S3; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 4. AWS Global Accelerator

> **ID:** `QUIZ-D3-04-Q04` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A empresa de jogos capivara deve manter a solução simples para a equipe de plantão. A solução atual funciona, mas não atende ao novo requisito não funcional. Um aplicativo de jogos usa TCP/UDP, possui endpoints em duas regiões e precisa de IPs anycast estáticos, failover rápido e tráfego pela rede global da AWS. O conteúdo não é cacheável. Qual serviço usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Criar Elastic IPs regionais e anunciar manualmente BGP pela internet.
- **B)** Usar AWS Global Accelerator com endpoint groups regionais e health checks.
- **C)** Usar CloudFront para armazenar pacotes UDP de sessão em cache.
- **D)** Usar apenas um registro DNS com TTL de 24 horas.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

Global Accelerator fornece IPs anycast estáticos, leva tráfego TCP/UDP pela borda à rede global e muda endpoints conforme saúde e políticas.

Trade-off: CloudFront é ideal para HTTP(S) cacheável e também pode acelerar conteúdo dinâmico, mas não fornece a mesma proposta para protocolos TCP/UDP genéricos e IPs anycast de entrada. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Todos usam o mesmo endereço de portão; por dentro, uma estrada rápida leva cada jogador ao parque saudável mais próximo.

**Se acertou:** Acertou: Global Accelerator fornece IPs anycast estáticos, leva tráfego TCP/UDP pela borda à rede global e muda endpoints conforme saúde e políticas. Quando outra opção poderia valer: CloudFront é ideal para HTTP(S) cacheável e também pode acelerar conteúdo dinâmico, mas não fornece a mesma proposta para protocolos TCP/UDP genéricos e IPs anycast de entrada. Mnemônica: associe “AWS Global Accelerator” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Elastic IP é regional e clientes não anunciam esse prefixo globalmente dessa forma.
- **B:** Correta — Global Accelerator fornece IPs anycast estáticos, leva tráfego TCP/UDP pela borda à rede global e muda endpoints conforme saúde e políticas.
- **C:** Incorreta — CloudFront não é cache genérico para UDP.
- **D:** Incorreta — DNS não fornece IPs anycast estáticos nem failover tão rápido, e TTL alto retarda mudança.

**Referência oficial:** [https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

**Referência prática:** ../labs/README.md — Roteamento global e failover

**Exercício recomendado:** No lab Roteamento global e failover, monte uma prova de conceito de AWS Global Accelerator; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 5. FSx for Lustre

> **ID:** `QUIZ-D3-04-Q05` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A plataforma de ingressos palco recebe picos imprevisíveis sem poder degradar o SLA. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Um workload HPC em milhares de vCPUs processa um dataset grande do S3 e precisa de sistema de arquivos paralelo com throughput muito alto. Ao final, os resultados devem voltar ao S3. Qual serviço usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Usar S3 Glacier Deep Archive como sistema de arquivos POSIX interativo.
- **B)** Executar um servidor SMB t3.micro como ponto central.
- **C)** Usar Amazon FSx for Lustre vinculado ao repositório de dados S3 e escolher deployment type/capacidade adequados.
- **D)** Usar um único volume gp2 pequeno compartilhado por todas as instâncias em regiões diferentes.

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

- **A:** Incorreta — Deep Archive exige restauração e não expõe semântica POSIX de baixa latência.
- **B:** Incorreta — O servidor seria gargalo e ponto único, além de protocolo inadequado ao padrão HPC descrito.
- **C:** Correta — FSx for Lustre é um sistema de arquivos paralelo de alto desempenho integrado ao S3, adequado a HPC, ML e processamento massivo.
- **D:** Incorreta — EBS é zonal, e esse desenho não fornece sistema de arquivos paralelo ou throughput agregado.

**Referência oficial:** [https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)

**Referência prática:** ../labs/README.md — Armazenamento de alto desempenho

**Exercício recomendado:** No lab Armazenamento de alto desempenho, monte uma prova de conceito de FSx for Lustre; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---
