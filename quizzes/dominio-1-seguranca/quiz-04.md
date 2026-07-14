# Mini-quiz 04 — Domínio 1 — Projetar arquiteturas seguras

- **Tipo:** mini-quiz por domínio
- **Questões:** 5
- **Tempo sugerido:** 10 minutos
- **Autoria:** Conteúdo original deste projeto; não reproduz questões reais nem dumps.

## Instruções

- Marque uma única alternativa (A, B, C ou D) por questão.
- Faça a primeira tentativa sem consultar o gabarito.
- Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.

---

## 1. Rotação de credenciais com Secrets Manager

> **ID:** `QUIZ-D1-04-Q01` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

A proptech janela recebe picos imprevisíveis sem poder degradar o SLA. A solução atual funciona, mas não atende ao novo requisito não funcional. Uma aplicação usa credenciais de um banco RDS. A senha precisa rotacionar automaticamente a cada 30 dias sem ser gravada no código ou na imagem do contêiner. Qual é a solução com menor esforço operacional? Considere o principal trade-off operacional e escolha a melhor solução.

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

## 2. VPC Gateway Endpoint para S3

> **ID:** `QUIZ-D1-04-Q02` · **Domínio:** D1 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

O marketplace beija-flor está migrando uma carga crítica para a AWS. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Instâncias EC2 em subnets privadas enviam grandes volumes ao S3. O tráfego não pode atravessar a internet e a solução deve evitar cobrança por hora de um componente de rede. Qual opção usar? Escolha a alternativa que atende diretamente ao requisito.

- **A)** Enviar o tráfego por um NAT Gateway em cada AZ.
- **B)** Criar um Gateway VPC Endpoint para S3, associá-lo às route tables privadas e restringir acesso com endpoint/bucket policies.
- **C)** Criar um Interface Endpoint para qualquer serviço e esperar que ele seja sempre gratuito.
- **D)** Atribuir IPv4 público às instâncias e permitir saída 0.0.0.0/0.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** B

**Explicação técnica**

Gateway endpoints para S3 adicionam rotas privadas ao serviço, não exigem NAT e não têm a cobrança por hora típica de interface endpoints.

Trade-off: Um NAT Gateway também permite chegar ao endpoint público do S3, mas adiciona custo por hora e por dados e não atende tão diretamente à exigência de caminho privado. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É uma estrada particular e gratuita do escritório até o armazém, sem sair para a avenida pública.

**Se acertou:** Acertou: Gateway endpoints para S3 adicionam rotas privadas ao serviço, não exigem NAT e não têm a cobrança por hora típica de interface endpoints. Quando outra opção poderia valer: Um NAT Gateway também permite chegar ao endpoint público do S3, mas adiciona custo por hora e por dados e não atende tão diretamente à exigência de caminho privado. Mnemônica: associe “VPC Gateway Endpoint para S3” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é B. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — O NAT adiciona custo e o caminho usa o endpoint público; é desnecessário quando há gateway endpoint para S3.
- **B:** Correta — Gateway endpoints para S3 adicionam rotas privadas ao serviço, não exigem NAT e não têm a cobrança por hora típica de interface endpoints.
- **C:** Incorreta — Interface endpoints têm cobrança por hora e processamento de dados; a afirmação de gratuidade é incorreta.
- **D:** Incorreta — Isso expõe as instâncias a uma rota de internet e viola o requisito de tráfego privado.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Referência prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

**Exercício recomendado:** No lab VPC multi-AZ, NAT e endpoints, monte uma prova de conceito de VPC Gateway Endpoint para S3; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 3. SCP em AWS Organizations

> **ID:** `QUIZ-D1-04-Q03` · **Domínio:** D1 · **Dificuldade:** média · **Tempo:** 110 s · **Pontos:** 2

O banco digital pioneiro deve manter a solução simples para a equipe de plantão. A solução atual funciona, mas não atende ao novo requisito não funcional. A organização quer impedir que qualquer conta membro desative o CloudTrail ou crie recursos fora de regiões aprovadas, inclusive quando um administrador local concede Allow. Qual controle deve formar o guardrail? Considere o principal trade-off operacional e escolha a melhor solução.

- **A)** Criar uma tag chamada RegiãoPermitida e confiar que os serviços a aplicarão sozinhos.
- **B)** Adicionar uma IAM policy Allow a todos os administradores das contas.
- **C)** Aplicar Service Control Policies nas OUs, com exceções cuidadosamente definidas para serviços e funções indispensáveis.
- **D)** Usar somente security groups para bloquear chamadas de API fora da região.

<details>
<summary>Gabarito e feedback detalhado</summary>

**Resposta correta:** C

**Explicação técnica**

SCPs definem o teto de permissões de contas membros; um Allow local não consegue ultrapassar um Deny explícito aplicável da organização.

Trade-off: SCP não concede permissões e não substitui policies de identidade ou recurso; ele limita o conjunto máximo que esses mecanismos podem conceder. A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado.

**Como se fosse para uma criança:** É o muro do condomínio: cada morador escolhe as regras da casa, mas ninguém pode atravessar o muro externo.

**Se acertou:** Acertou: SCPs definem o teto de permissões de contas membros; um Allow local não consegue ultrapassar um Deny explícito aplicável da organização. Quando outra opção poderia valer: SCP não concede permissões e não substitui policies de identidade ou recurso; ele limita o conjunto máximo que esses mecanismos podem conceder. Mnemônica: associe “SCP em AWS Organizations” ao requisito decisivo destacado no cenário.

**Se errou:** A resposta correta é C. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado.

**Por que cada alternativa está certa ou errada**

- **A:** Incorreta — Tags só têm efeito de autorização quando policies explicitamente as avaliam.
- **B:** Incorreta — Um Allow amplia permissões locais e não cria o guardrail organizacional solicitado.
- **C:** Correta — SCPs definem o teto de permissões de contas membros; um Allow local não consegue ultrapassar um Deny explícito aplicável da organização.
- **D:** Incorreta — Security groups filtram tráfego de recursos e não governam permissões de APIs ou regiões.

**Referência oficial:** [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Referência prática:** ../labs/README.md — IAM, KMS e guardrails

**Exercício recomendado:** No lab IAM, KMS e guardrails, monte uma prova de conceito de SCP em AWS Organizations; registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende.

</details>

---

## 4. Trilha de auditoria organizacional

> **ID:** `QUIZ-D1-04-Q04` · **Domínio:** D1 · **Dificuldade:** difícil · **Tempo:** 130 s · **Pontos:** 3

A universidade saber recebe picos imprevisíveis sem poder degradar o SLA. A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio. Auditores exigem registro centralizado e resistente a adulteração das chamadas de API de todas as contas atuais e futuras. Também é preciso alertar quando alguém tentar apagar uma trilha. Qual arquitetura é adequada? Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.

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

## 5. Security groups e network ACLs

> **ID:** `QUIZ-D1-04-Q05` · **Domínio:** D1 · **Dificuldade:** fácil · **Tempo:** 90 s · **Pontos:** 1

A proptech janela está migrando uma carga crítica para a AWS. A solução atual funciona, mas não atende ao novo requisito não funcional. Servidores web em subnets públicas aceitam HTTPS do mundo e acessam servidores de aplicação em subnets privadas. A equipe quer controles stateful por recurso e uma camada stateless de bloqueio explícito por CIDR na subnet. Qual combinação usar? Escolha a alternativa que atende diretamente ao requisito.

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
