# Mini-quiz 05 — Domínio 1 — Projetar arquiteturas seguras

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Autenticação de clientes com Amazon Cognito

> **ID:** `QUIZ-D1-05-Q01` · **Domínio:** D1 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

O marketplace beija-flor opera com uma equipe pequena e quer reduzir tarefas manuais. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Um aplicativo móvel voltado a milhões de consumidores precisa cadastro, login, recuperação de senha, MFA opcional e tokens para chamar uma API. A equipe não quer manter um diretório próprio. Qual serviço é indicado? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Usar somente uma API key do API Gateway compartilhada por todos.
- **B)** Usar um Amazon Cognito User Pool como diretório e emissor de tokens, integrando-o ao API Gateway; usar Identity Pool apenas se forem necessárias credenciais AWS temporárias.
- **C)** Criar um usuário IAM para cada consumidor do aplicativo.
- **D)** Salvar senhas em uma tabela DynamoDB sem hash e validar na Lambda.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

User Pools fornecem autenticação de usuários e tokens OIDC/OAuth; a API valida esses tokens sem a equipe operar o armazenamento de senhas.

Trade-off: IAM Identity Center atende principalmente força de trabalho; Cognito é adequado a identidades de clientes. Identity Pools cumprem outro papel: trocar identidades por credenciais AWS temporárias. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É uma portaria pronta que cadastra visitantes e entrega pulseiras válidas para entrar na festa.

**Se acertou:** Acertou: User Pools fornecem autenticação de usuários e tokens OIDC/OAuth; a API valida esses tokens sem a equipe operar o armazenamento de senhas. Quando outra opção poderia valer: IAM Identity Center atende principalmente força de trabalho; Cognito é adequado a identidades de clientes. Identity Pools cumprem outro papel: trocar identidades por credenciais AWS temporárias. Mnemônica: associe “Autenticação de clientes com Amazon Cognito” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — API keys ajudam em medição e planos de uso; não autenticam individualmente usuários finais.
- **B:** Correta — User Pools fornecem autenticação de usuários e tokens OIDC/OAuth; a API valida esses tokens sem a equipe operar o armazenamento de senhas.
- **C:** Incorreta — IAM users não são um diretório de clientes em escala e gerariam riscos e operação excessivos.
- **D:** Incorreta — Armazenamento de senhas em texto é inseguro e recria capacidades já gerenciadas pelo Cognito.

**Referência oficial:** [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)

**Referência prática:** ../labs/README.md — API Gateway, Lambda e autenticação

**Exercício recomendado:** No lab API Gateway, Lambda e autenticação, monte uma prova de conceito de Autenticação de clientes com Amazon Cognito; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. Proteção de camada 7 com AWS WAF

> **ID:** `QUIZ-D1-05-Q02` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

O banco digital pioneiro está eliminando um ponto único de falha identificado em teste. A solução atual funciona, mas não atende ao novo requisito não funcional. Uma API pública atrás de um ALB sofre credential stuffing e rajadas de um pequeno conjunto de endereços IP. É necessário bloquear padrões HTTP e limitar requisições por origem sem alterar a aplicação. O que fazer? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Usar apenas AWS Shield Standard para identificar senhas reutilizadas.
- **B)** Aumentar o número de instâncias do Auto Scaling sem filtrar as requisições.
- **C)** Associar um Web ACL do AWS WAF ao ALB, usando managed rules e uma rate-based rule ajustada ao tráfego legítimo.
- **D)** Editar a NACL para bloquear palavras presentes no corpo HTTP.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

WAF inspeciona atributos HTTP(S) e regras baseadas em taxa agregam requisições por chave, bloqueando ou desafiando origens abusivas na camada 7.

Trade-off: Shield Standard está incluído e lida com ataques DDoS comuns de rede e transporte; Shield Advanced acrescenta resposta e proteção de custo, mas não substitui regras HTTP do WAF. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** O porteiro reconhece truques nas cartas e manda quem bate vezes demais esperar do lado de fora.

**Se acertou:** Acertou: WAF inspeciona atributos HTTP(S) e regras baseadas em taxa agregam requisições por chave, bloqueando ou desafiando origens abusivas na camada 7. Quando outra opção poderia valer: Shield Standard está incluído e lida com ataques DDoS comuns de rede e transporte; Shield Advanced acrescenta resposta e proteção de custo, mas não substitui regras HTTP do WAF. Mnemônica: associe “Proteção de camada 7 com AWS WAF” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Shield não implementa lógica de credential stuffing baseada em campos e padrões HTTP.
- **B:** Incorreta — Escalar pode absorver carga, mas não bloqueia abuso e ainda amplia custo.
- **C:** Correta — WAF inspeciona atributos HTTP(S) e regras baseadas em taxa agregam requisições por chave, bloqueando ou desafiando origens abusivas na camada 7.
- **D:** Incorreta — NACLs operam em rede e não inspecionam conteúdo HTTP.

**Referência oficial:** [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)

**Referência prática:** ../labs/README.md — S3/CloudFront/WAF e proteção web

**Exercício recomendado:** No lab S3/CloudFront/WAF e proteção web, monte uma prova de conceito de Proteção de camada 7 com AWS WAF; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. S3 Block Public Access e políticas

> **ID:** `QUIZ-D1-05-Q03` · **Domínio:** D1 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A universidade saber está preparando a arquitetura para a próxima campanha anual. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Uma empresa armazena relatórios confidenciais em centenas de buckets. Ela precisa impedir exposição pública acidental em toda a organização e permitir acesso apenas por um VPC endpoint específico. Qual desenho é mais seguro? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Usar ACL public-read e esconder os nomes dos objetos.
- **B)** Associar um security group diretamente ao bucket.
- **C)** Criptografar os objetos, mas deixar leitura pública para qualquer principal.
- **D)** Ativar S3 Block Public Access no nível da organização/contas e aplicar bucket policies com condição aws:SourceVpce e negação fora do endpoint autorizado.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

Block Public Access neutraliza políticas e ACLs públicas; uma bucket policy com condição e Deny explícito restringe o caminho de acesso ao endpoint aprovado.

Trade-off: Ao usar condições de endpoint, é preciso preservar acessos administrativos e de serviços necessários para não bloquear operações legítimas de forma acidental. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Primeiro fechamos todas as janelas do prédio; depois damos uma chave que só funciona na passagem secreta certa.

**Se acertou:** Acertou: Block Public Access neutraliza políticas e ACLs públicas; uma bucket policy com condição e Deny explícito restringe o caminho de acesso ao endpoint aprovado. Quando outra opção poderia valer: Ao usar condições de endpoint, é preciso preservar acessos administrativos e de serviços necessários para não bloquear operações legítimas de forma acidental. Mnemônica: associe “S3 Block Public Access e políticas” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Obscuridade de nomes não é controle de acesso, e a ACL tornaria dados públicos.
- **B:** Incorreta — Buckets S3 não aceitam security groups.
- **C:** Incorreta — Criptografia em repouso não corrige uma autorização pública; serviços autorizados ainda descriptografariam dados.
- **D:** Correta — Block Public Access neutraliza políticas e ACLs públicas; uma bucket policy com condição e Deny explícito restringe o caminho de acesso ao endpoint aprovado.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

**Referência prática:** ../labs/README.md — S3 privado e endpoints VPC

**Exercício recomendado:** No lab S3 privado e endpoints VPC, monte uma prova de conceito de S3 Block Public Access e políticas; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 4. Permissions boundaries e delegação

> **ID:** `QUIZ-D1-05-Q04` · **Domínio:** D1 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A proptech janela opera com uma equipe pequena e quer reduzir tarefas manuais. A solução atual funciona, mas não atende ao novo requisito não funcional. Uma plataforma permite que times de produto criem suas próprias roles, mas segurança precisa garantir que nenhuma role criada ultrapasse um conjunto máximo de ações. Os times ainda devem escolher permissões dentro desse limite. Qual recurso usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Exigir uma permissions boundary nas roles criadas e controlar iam:PermissionsBoundary nas políticas do time.
- **B)** Criar somente tags sem nenhuma condição de IAM associada.
- **C)** Anexar AdministratorAccess e pedir que cada time não use ações perigosas.
- **D)** Usar uma NACL para limitar quais APIs IAM podem ser chamadas.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** A

**Explicação técnica**

A permissions boundary define o máximo que uma policy de identidade pode conceder, permitindo delegação sem entregar privilégios ilimitados.

Trade-off: Boundary não concede acesso por si só e precisa ser avaliada junto de policies de identidade, recurso, SCPs e negações explícitas. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** A criança escolhe onde brincar no quintal, mas a cerca define até onde ela pode ir.

**Se acertou:** Acertou: A permissions boundary define o máximo que uma policy de identidade pode conceder, permitindo delegação sem entregar privilégios ilimitados. Quando outra opção poderia valer: Boundary não concede acesso por si só e precisa ser avaliada junto de policies de identidade, recurso, SCPs e negações explícitas. Mnemônica: associe “Permissions boundaries e delegação” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é A. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Correta — A permissions boundary define o máximo que uma policy de identidade pode conceder, permitindo delegação sem entregar privilégios ilimitados.
- **B:** Incorreta — Tags isoladas são metadados; o controle exige policies que as avaliem.
- **C:** Incorreta — Confiança processual não impõe um limite técnico e AdministratorAccess viola privilégio mínimo.
- **D:** Incorreta — NACLs filtram pacotes e não avaliam ações IAM.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)

**Referência prática:** ../labs/README.md — IAM least privilege e roles

**Exercício recomendado:** No lab IAM least privilege e roles, monte uma prova de conceito de Permissions boundaries e delegação; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 5. Acesso entre contas com IAM Roles

> **ID:** `QUIZ-D1-05-Q05` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

O marketplace beija-flor está eliminando um ponto único de falha identificado em teste. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Uma aplicação na conta de produção precisa ler objetos de um bucket pertencente à conta de dados, sem armazenar chaves de acesso. O acesso deve ser temporário, auditável e seguir privilégio mínimo. Qual solução atende melhor? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Tornar o bucket público e restringir o endereço IP na aplicação.
- **B)** Criar uma IAM Role na conta de dados, confiar na role da aplicação e usar AWS STS AssumeRole com política limitada ao bucket.
- **C)** Compartilhar a senha do usuário raiz da conta de dados pelo Secrets Manager.
- **D)** Criar um usuário IAM na conta de dados e copiar access key e secret key para a instância.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

AssumeRole entrega credenciais temporárias e separa a política de confiança da política de permissões, permitindo acesso entre contas sem segredo de longa duração.

Trade-off: Uma bucket policy também participa do controle de acesso, mas a role com STS é a opção central quando a aplicação precisa de uma identidade temporária na outra conta. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É como dar um crachá de visitante que abre só uma sala e expira no fim da visita.

**Se acertou:** Acertou: AssumeRole entrega credenciais temporárias e separa a política de confiança da política de permissões, permitindo acesso entre contas sem segredo de longa duração. Quando outra opção poderia valer: Uma bucket policy também participa do controle de acesso, mas a role com STS é a opção central quando a aplicação precisa de uma identidade temporária na outra conta. Mnemônica: associe “Acesso entre contas com IAM Roles” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Exposição pública viola o requisito e endereço IP não substitui autenticação e autorização.
- **B:** Correta — AssumeRole entrega credenciais temporárias e separa a política de confiança da política de permissões, permitindo acesso entre contas sem segredo de longa duração.
- **C:** Incorreta — Credenciais do usuário raiz não devem ser usadas por aplicações, mesmo quando armazenadas em um cofre.
- **D:** Incorreta — Chaves de longa duração aumentam o risco de vazamento e exigem rotação; não são necessárias para workloads na AWS.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

**Referência prática:** ../labs/README.md — Lambda/API Gateway com IAM e acesso entre contas

**Exercício recomendado:** No lab Lambda/API Gateway com IAM e acesso entre contas, monte uma prova de conceito de Acesso entre contas com IAM Roles; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---
