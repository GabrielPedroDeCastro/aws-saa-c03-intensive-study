# Mini-quiz 02 — Domínio 3 — Projetar arquiteturas de alto desempenho

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Transferência para Amazon S3

> **ID:** `QUIZ-D3-02-Q01` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A empresa de logística rota certa precisa tomar uma decisão com base em desempenho, segurança e custo total. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Filiais globais enviam arquivos de 200 GB ao S3 por links de longa distância. A equipe quer paralelizar uploads, retomar partes com falha e melhorar o caminho pela rede AWS. Qual combinação usar? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 2. AWS Global Accelerator

> **ID:** `QUIZ-D3-02-Q02` · **Domínio:** D3 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A empresa de jogos capivara quer substituir um componente autogerenciado por um serviço gerenciado. A solução atual funciona, mas não atende ao novo requisito não funcional. Um aplicativo de jogos usa TCP/UDP, possui endpoints em duas regiões e precisa de IPs anycast estáticos, failover rápido e tráfego pela rede global da AWS. O conteúdo não é cacheável. Qual serviço usar? Escolha a alternativa que atende diretamente ao requisito.

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

## 3. FSx for Lustre

> **ID:** `QUIZ-D3-02-Q03` · **Domínio:** D3 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A plataforma de ingressos palco vai lançar o serviço em três países. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Um workload HPC em milhares de vCPUs processa um dataset grande do S3 e precisa de sistema de arquivos paralelo com throughput muito alto. Ao final, os resultados devem voltar ao S3. Qual serviço usar? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 4. Amazon Kinesis Data Streams

> **ID:** `QUIZ-D3-02-Q04` · **Domínio:** D3 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A rede hospitalar horizonte precisa tomar uma decisão com base em desempenho, segurança e custo total. A solução atual funciona, mas não atende ao novo requisito não funcional. Sensores enviam eventos continuamente e vários consumidores precisam processar o mesmo stream com baixa latência, preservando ordem por dispositivo e possibilidade de replay dentro da retenção. Qual serviço escolher? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Usar uma única fila SQS e esperar que todos os consumidores recebam cada evento e possam reler a sequência.
- **B)** Gravar eventos em arquivos locais e copiá-los semanalmente.
- **C)** Usar SNS sem assinantes duráveis nem retenção.
- **D)** Usar Kinesis Data Streams, com device ID como partition key, capacidade dimensionada/on-demand e consumidores apropriados.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

Kinesis mantém registros ordenados por shard/partition key, permite múltiplos consumidores e replay durante o período de retenção.

Trade-off: Uma partition key muito concentrada cria hot shard. SQS é excelente para filas de trabalho, mas normalmente cada mensagem é consumida como tarefa e não oferece o mesmo modelo de stream/replay. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Cada sensor põe bilhetes numa esteira própria; várias equipes podem reler a sequência enquanto ela ainda está guardada.

**Se acertou:** Acertou: Kinesis mantém registros ordenados por shard/partition key, permite múltiplos consumidores e replay durante o período de retenção. Quando outra opção poderia valer: Uma partition key muito concentrada cria hot shard. SQS é excelente para filas de trabalho, mas normalmente cada mensagem é consumida como tarefa e não oferece o mesmo modelo de stream/replay. Mnemônica: associe “Amazon Kinesis Data Streams” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Uma fila distribui trabalho; fan-out e replay ordenado exigiriam outro desenho.
- **B:** Incorreta — Isso não atende baixa latência, durabilidade gerenciada ou múltiplos consumidores.
- **C:** Incorreta — SNS faz push, mas sozinho não fornece retenção e replay do stream.
- **D:** Correta — Kinesis mantém registros ordenados por shard/partition key, permite múltiplos consumidores e replay durante o período de retenção.

**Referência oficial:** [https://docs.aws.amazon.com/streams/latest/dev/introduction.html](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

**Referência prática:** ../labs/README.md — Streaming e processamento de eventos

**Exercício recomendado:** No lab Streaming e processamento de eventos, monte uma prova de conceito de Amazon Kinesis Data Streams; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 5. Políticas de Auto Scaling

> **ID:** `QUIZ-D3-02-Q05` · **Domínio:** D3 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A empresa de logística rota certa quer substituir um componente autogerenciado por um serviço gerenciado. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Uma API em EC2 apresenta carga proporcional a requisições por target. A equipe quer manter cerca de 1.000 requisições por target, adicionando e removendo capacidade automaticamente. Qual política é mais simples? Escolha a alternativa que atende diretamente ao requisito.

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
