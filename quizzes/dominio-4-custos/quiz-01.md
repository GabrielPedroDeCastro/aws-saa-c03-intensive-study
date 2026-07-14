# Mini-quiz 01 — Domínio 4 — Projetar arquiteturas otimizadas em custos

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. S3 Lifecycle

> **ID:** `QUIZ-D4-01-Q01` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

O banco digital pioneiro precisa corrigir uma descoberta da revisão Well-Architected. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Logs são acessados diariamente por 30 dias, raramente até o primeiro ano e precisam ser retidos por sete anos. A equipe quer reduzir custo automaticamente sem scripts. Qual abordagem usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Criar S3 Lifecycle para transicionar objetos às classes adequadas ao padrão de acesso e expirá-los somente após o prazo regulatório.
- **B)** Excluir os logs aos 30 dias apesar da retenção de sete anos.
- **C)** Copiar os objetos diariamente para mais buckets Standard na mesma região.
- **D)** Manter tudo em S3 Standard para sempre porque todas as classes têm o mesmo preço.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

Lifecycle automatiza transições e expiração por idade; a seleção deve considerar duração mínima, custo de recuperação e latência de cada classe.

Trade-off: Glacier Flexible Retrieval/Deep Archive reduzem armazenamento, mas cobram recuperação e não servem a acesso imediato. Transições muito precoces podem gerar cobranças mínimas. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Caixas novas ficam na prateleira perto; depois vão ao depósito barato e, no prazo certo, são recicladas.

**Se acertou:** Acertou: Lifecycle automatiza transições e expiração por idade; a seleção deve considerar duração mínima, custo de recuperação e latência de cada classe. Quando outra opção poderia valer: Glacier Flexible Retrieval/Deep Archive reduzem armazenamento, mas cobram recuperação e não servem a acesso imediato. Transições muito precoces podem gerar cobranças mínimas. Mnemônica: associe “S3 Lifecycle” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — Lifecycle automatiza transições e expiração por idade; a seleção deve considerar duração mínima, custo de recuperação e latência de cada classe.
- **B:** Incorreta — Isso viola o requisito regulatório.
- **C:** Incorreta — Cópias adicionais aumentam armazenamento sem implementar uma política de arquivamento econômica.
- **D:** Incorreta — As classes têm preços e características diferentes; o padrão conhecido permite economizar.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

**Referência prática:** ../labs/README.md — S3, lifecycle e otimização de custos

**Exercício recomendado:** No lab S3, lifecycle e otimização de custos, monte uma prova de conceito de S3 Lifecycle; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. Savings Plans e Spot

> **ID:** `QUIZ-D4-01-Q02` · **Domínio:** D4 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A universidade saber está separando produção e desenvolvimento em contas distintas. A carga atende milhares de requisições por segundo em horários de pico. Uma plataforma tem uma base de compute estável 24x7 e jobs batch tolerantes a interrupção durante a madrugada. Qual combinação tende a otimizar custo sem comprometer a base? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Executar toda a base crítica apenas em uma única Spot Instance sem checkpoint.
- **B)** Cobrir a base previsível com Savings Plans e executar a capacidade batch flexível em Spot, com diversificação e tratamento de interrupções.
- **C)** Comprar compromisso para o pico máximo anual que dura uma hora.
- **D)** Usar Dedicated Hosts obrigatoriamente para qualquer job batch.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

Savings Plans descontam uso comprometido de compute; Spot aproveita capacidade excedente com grande desconto para workloads interrompíveis.

Trade-off: Não se deve comprometer acima da base bem conhecida. Spot precisa checkpoints, múltiplos tipos/AZs e resposta ao interruption notice. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Assinamos um passe barato para a viagem diária e compramos lugares promocionais para passeios que podem esperar.

**Se acertou:** Acertou: Savings Plans descontam uso comprometido de compute; Spot aproveita capacidade excedente com grande desconto para workloads interrompíveis. Quando outra opção poderia valer: Não se deve comprometer acima da base bem conhecida. Spot precisa checkpoints, múltiplos tipos/AZs e resposta ao interruption notice. Mnemônica: associe “Savings Plans e Spot” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Interrupções podem remover toda a capacidade crítica.
- **B:** Correta — Savings Plans descontam uso comprometido de compute; Spot aproveita capacidade excedente com grande desconto para workloads interrompíveis.
- **C:** Incorreta — Compromisso ocioso destrói a economia; ele deve mirar uso consistente.
- **D:** Incorreta — Dedicated Hosts costumam ter custo maior e só se justificam por licença/compliance específicos.

**Referência oficial:** [https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)

**Referência prática:** ../labs/README.md — Auto Scaling com On-Demand, Savings Plans e Spot

**Exercício recomendado:** No lab Auto Scaling com On-Demand, Savings Plans e Spot, monte uma prova de conceito de Savings Plans e Spot; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. RDS Reserved DB Instances

> **ID:** `QUIZ-D4-01-Q03` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A proptech janela precisa atender a uma auditoria sem redesenhar toda a aplicação. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Um banco RDS de produção possui classe e região estáveis, funciona continuamente e deve permanecer assim por pelo menos um ano. A empresa quer desconto sem redesenhar a aplicação. O que avaliar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Trocar para Multi-AZ exclusivamente para reduzir a fatura pela metade.
- **B)** Comprar Spot Instances para substituir diretamente a instância RDS gerenciada.
- **C)** Adquirir Reserved DB Instance para a configuração/família elegível após validar utilização, prazo e opção de pagamento.
- **D)** Criar uma read replica sem carga apenas para obter desconto.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Reserved DB Instances oferecem desconto de faturamento para uso RDS previsível; não são uma instância física separada e não alteram a arquitetura.

Trade-off: Reserva reduz compute do RDS, mas armazenamento, I/O, backup e transferência podem continuar cobrados. Rightsizing deve vir antes do compromisso. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** A mesma mesa é usada todo dia, então um plano anual sai mais barato que pagar diária.

**Se acertou:** Acertou: Reserved DB Instances oferecem desconto de faturamento para uso RDS previsível; não são uma instância física separada e não alteram a arquitetura. Quando outra opção poderia valer: Reserva reduz compute do RDS, mas armazenamento, I/O, backup e transferência podem continuar cobrados. Rightsizing deve vir antes do compromisso. Mnemônica: associe “RDS Reserved DB Instances” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Multi-AZ adiciona capacidade para alta disponibilidade e normalmente aumenta custo.
- **B:** Incorreta — RDS não oferece modelo Spot para a instância de banco gerenciada.
- **C:** Correta — Reserved DB Instances oferecem desconto de faturamento para uso RDS previsível; não são uma instância física separada e não alteram a arquitetura.
- **D:** Incorreta — A réplica acrescenta custo; não cria desconto de compromisso.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)

**Referência prática:** ../labs/README.md — RDS, capacidade e custo

**Exercício recomendado:** No lab RDS, capacidade e custo, monte uma prova de conceito de RDS Reserved DB Instances; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 4. Custo de NAT e VPC endpoints

> **ID:** `QUIZ-D4-01-Q04` · **Domínio:** D4 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

O marketplace beija-flor precisa corrigir uma descoberta da revisão Well-Architected. A carga atende milhares de requisições por segundo em horários de pico. Instâncias privadas baixam terabytes mensalmente do S3 através de NAT Gateways. A fatura mostra alto processamento de dados no NAT. Como reduzir o custo mantendo caminho privado? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

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

## 5. AWS Compute Optimizer

> **ID:** `QUIZ-D4-01-Q05` · **Domínio:** D4 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

O banco digital pioneiro está separando produção e desenvolvimento em contas distintas. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Centenas de instâncias EC2 têm baixa utilização, mas a equipe não sabe quais podem ser reduzidas sem risco de memória ou performance. Ela quer recomendações baseadas em métricas antes de mudar tamanhos. Qual serviço usar? Escolha a alternativa que atende diretamente ao requisito.

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
