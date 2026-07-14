# Mini-quiz 07 — Domínio 1 — Projetar arquiteturas seguras

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Trilha de auditoria organizacional

> **ID:** `QUIZ-D1-07-Q01` · **Domínio:** D1 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A universidade saber precisa corrigir uma descoberta da revisão Well-Architected. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Auditores exigem registro centralizado e resistente a adulteração das chamadas de API de todas as contas atuais e futuras. Também é preciso alertar quando alguém tentar apagar uma trilha. Qual arquitetura é adequada? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

- **A)** Usar VPC Flow Logs como substituto para chamadas de API.
- **B)** Habilitar logs de acesso do ALB para registrar alterações no IAM.
- **C)** Confiar apenas no Event history de 90 dias de cada conta.
- **D)** Criar uma organization trail no CloudTrail para bucket central dedicado, habilitar validação de integridade, restringir o bucket e monitorar eventos com EventBridge/CloudWatch.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** D

**Explicação técnica**

Uma organization trail cobre contas da organização de forma central; políticas do bucket e validação de logs protegem a evidência, e eventos permitem alertas rápidos.

Trade-off: CloudTrail Lake pode ajudar em consultas e retenção, mas não elimina a necessidade de definir proteção, governança e alertas coerentes para os registros. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** Todas as salas escrevem no mesmo diário lacrado; se alguém tentar arrancar uma página, um alarme toca.

**Se acertou:** Acertou: Uma organization trail cobre contas da organização de forma central; políticas do bucket e validação de logs protegem a evidência, e eventos permitem alertas rápidos. Quando outra opção poderia valer: CloudTrail Lake pode ajudar em consultas e retenção, mas não elimina a necessidade de definir proteção, governança e alertas coerentes para os registros. Mnemônica: associe “Trilha de auditoria organizacional” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é D. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Flow Logs registram metadados de fluxos de rede, não ações de controle executadas via APIs.
- **B:** Incorreta — Logs do ALB mostram requisições ao balanceador, não alterações administrativas em serviços AWS.
- **C:** Incorreta — O histórico é limitado, regionalmente consultado e não fornece sozinho retenção central protegida.
- **D:** Correta — Uma organization trail cobre contas da organização de forma central; políticas do bucket e validação de logs protegem a evidência, e eventos permitem alertas rápidos.

**Referência oficial:** [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

**Referência prática:** ../labs/README.md — Observabilidade, CloudTrail e alertas

**Exercício recomendado:** No lab Observabilidade, CloudTrail e alertas, monte uma prova de conceito de Trilha de auditoria organizacional; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 2. Security groups e network ACLs

> **ID:** `QUIZ-D1-07-Q02` · **Domínio:** D1 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A proptech janela está separando produção e desenvolvimento em contas distintas. A solução atual funciona, mas não atende ao novo requisito não funcional. Servidores web em subnets públicas aceitam HTTPS do mundo e acessam servidores de aplicação em subnets privadas. A equipe quer controles stateful por recurso e uma camada stateless de bloqueio explícito por CIDR na subnet. Qual combinação usar? Escolha a alternativa que atende diretamente ao requisito.

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

## 3. Autenticação de clientes com Amazon Cognito

> **ID:** `QUIZ-D1-07-Q03` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

O marketplace beija-flor precisa atender a uma auditoria sem redesenhar toda a aplicação. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Um aplicativo móvel voltado a milhões de consumidores precisa cadastro, login, recuperação de senha, MFA opcional e tokens para chamar uma API. A equipe não quer manter um diretório próprio. Qual serviço é indicado? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 4. Proteção de camada 7 com AWS WAF

> **ID:** `QUIZ-D1-07-Q04` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

O banco digital pioneiro precisa corrigir uma descoberta da revisão Well-Architected. A solução atual funciona, mas não atende ao novo requisito não funcional. Uma API pública atrás de um ALB sofre credential stuffing e rajadas de um pequeno conjunto de endereços IP. É necessário bloquear padrões HTTP e limitar requisições por origem sem alterar a aplicação. O que fazer? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 5. S3 Block Public Access e políticas

> **ID:** `QUIZ-D1-07-Q05` · **Domínio:** D1 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A universidade saber está separando produção e desenvolvimento em contas distintas. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Uma empresa armazena relatórios confidenciais em centenas de buckets. Ela precisa impedir exposição pública acidental em toda a organização e permitir acesso apenas por um VPC endpoint específico. Qual desenho é mais seguro? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

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
