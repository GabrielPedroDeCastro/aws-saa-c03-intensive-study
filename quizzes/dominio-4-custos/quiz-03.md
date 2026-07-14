# Mini-quiz 03 — Domínio 4 — Projetar arquiteturas otimizadas em custos

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Consolidated billing e compartilhamento de descontos

> **ID:** `QUIZ-D4-03-Q01` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A proptech janela está eliminando um ponto único de falha identificado em teste. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Uma empresa possui muitas contas AWS e quer uma fatura consolidada, visão central de custos e melhor aproveitamento agregado de descontos elegíveis. Qual recurso usar? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Compartilhar a senha do usuário raiz entre todas as equipes.
- **B)** Criar VPC peering entre contas para combinar as faturas.
- **C)** Gerenciar as contas com AWS Organizations e consolidated billing, estruturando OUs, tags e controles de compartilhamento de descontos.
- **D)** Duplicar os mesmos compromissos em cada conta sem analisar uso agregado.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

Organizations consolida cobrança e permite que uso agregado e compartilhamento elegível de descontos melhorem aproveitamento, além de centralizar relatórios.

Trade-off: Consolidar não elimina a necessidade de chargeback/showback. Savings Plans/RI sharing pode ser configurado e políticas organizacionais não concedem permissões automaticamente. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** A família junta todas as compras numa conta só e aproveita melhor o cartão de desconto do supermercado.

**Se acertou:** Acertou: Organizations consolida cobrança e permite que uso agregado e compartilhamento elegível de descontos melhorem aproveitamento, além de centralizar relatórios. Quando outra opção poderia valer: Consolidar não elimina a necessidade de chargeback/showback. Savings Plans/RI sharing pode ser configurado e políticas organizacionais não concedem permissões automaticamente. Mnemônica: associe “Consolidated billing e compartilhamento de descontos” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Isso é inseguro e não cria organização ou faturamento consolidado.
- **B:** Incorreta — Peering conecta redes e não consolida cobrança.
- **C:** Correta — Organizations consolida cobrança e permite que uso agregado e compartilhamento elegível de descontos melhorem aproveitamento, além de centralizar relatórios.
- **D:** Incorreta — Isso pode gerar excesso de compromisso e perde o benefício da visão consolidada.

**Referência oficial:** [https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)

**Referência prática:** ../labs/README.md — FinOps multi-conta e alocação de custos

**Exercício recomendado:** No lab FinOps multi-conta e alocação de custos, monte uma prova de conceito de Consolidated billing e compartilhamento de descontos; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. EFS lifecycle e Infrequent Access

> **ID:** `QUIZ-D4-03-Q02` · **Domínio:** D4 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

O marketplace beija-flor está preparando a arquitetura para a próxima campanha anual. A carga atende milhares de requisições por segundo em horários de pico. Um sistema EFS Regional contém muitos arquivos antigos raramente lidos, mas eles ainda precisam aparecer no mesmo namespace POSIX. Como reduzir o custo sem migração manual? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Criar um EFS novo para cada arquivo frio.
- **B)** Copiar manualmente arquivos para discos locais e apagar o EFS.
- **C)** Aumentar o throughput provisionado para reduzir armazenamento.
- **D)** Configurar EFS lifecycle management para mover arquivos não acessados a IA/Archive conforme elegibilidade e, se adequado, voltar ao Standard no primeiro acesso.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

EFS lifecycle move dados frios para classes mais baratas mantendo o mesmo sistema de arquivos e acesso transparente à aplicação.

Trade-off: Classes IA/Archive têm cobrança de acesso e são melhores para arquivos realmente frios. One Zone reduz custo adicional, mas muda a resiliência e não deve ser escolhido sem aceitar risco de AZ. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Os brinquedos esquecidos vão para uma prateleira barata, mas continuam no catálogo e voltam quando alguém pede.

**Se acertou:** Acertou: EFS lifecycle move dados frios para classes mais baratas mantendo o mesmo sistema de arquivos e acesso transparente à aplicação. Quando outra opção poderia valer: Classes IA/Archive têm cobrança de acesso e são melhores para arquivos realmente frios. One Zone reduz custo adicional, mas muda a resiliência e não deve ser escolhido sem aceitar risco de AZ. Mnemônica: associe “EFS lifecycle e Infrequent Access” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Isso aumenta complexidade e não usa o lifecycle transparente disponível.
- **B:** Incorreta — Isso perde compartilhamento, durabilidade e automação do namespace existente.
- **C:** Incorreta — Throughput e classe de armazenamento são dimensões diferentes; aumentar throughput pode elevar custo.
- **D:** Correta — EFS lifecycle move dados frios para classes mais baratas mantendo o mesmo sistema de arquivos e acesso transparente à aplicação.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)

**Referência prática:** ../labs/README.md — EFS, classes e custo

**Exercício recomendado:** No lab EFS, classes e custo, monte uma prova de conceito de EFS lifecycle e Infrequent Access; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. S3 Lifecycle

> **ID:** `QUIZ-D4-03-Q03` · **Domínio:** D4 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

O banco digital pioneiro opera com uma equipe pequena e quer reduzir tarefas manuais. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Logs são acessados diariamente por 30 dias, raramente até o primeiro ano e precisam ser retidos por sete anos. A equipe quer reduzir custo automaticamente sem scripts. Qual abordagem usar? Escolha a alternativa que atende diretamente ao requisito.

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

## 4. Savings Plans e Spot

> **ID:** `QUIZ-D4-03-Q04` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A universidade saber está eliminando um ponto único de falha identificado em teste. A carga atende milhares de requisições por segundo em horários de pico. Uma plataforma tem uma base de compute estável 24x7 e jobs batch tolerantes a interrupção durante a madrugada. Qual combinação tende a otimizar custo sem comprometer a base? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 5. RDS Reserved DB Instances

> **ID:** `QUIZ-D4-03-Q05` · **Domínio:** D4 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A proptech janela está preparando a arquitetura para a próxima campanha anual. Uma interrupção de poucos minutos gera impacto financeiro mensurável. Um banco RDS de produção possui classe e região estáveis, funciona continuamente e deve permanecer assim por pelo menos um ano. A empresa quer desconto sem redesenhar a aplicação. O que avaliar? Considere o principal trade-off operacional e escolha a melhor solução.

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
