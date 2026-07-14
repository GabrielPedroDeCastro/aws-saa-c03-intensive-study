# 240 flashcards SAA-C03

> Use repetição espaçada. Diga a resposta em voz alta antes de abrir o verso e sempre conecte a decisão a um requisito do cenário.

**Distribuição:** {'D1': 60, 'D2': 60, 'D3': 60, 'D4': 60}

---

## FC-001 — Acesso entre contas com IAM Roles

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito Acesso entre contas com IAM Roles costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** AssumeRole entrega credenciais temporárias e separa a política de confiança da política de permissões, permitindo acesso entre contas sem segredo de longa duração.

**Como criança:** É como dar um crachá de visitante que abre só uma sala e expira no fim da visita.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Uma bucket policy também participa do controle de acesso, mas a role com STS é a opção central quando a aplicação precisa de uma identidade temporária na outra conta.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

**Prática:** ../labs/README.md — Lambda/API Gateway com IAM e acesso entre contas

</details>

---

## FC-002 — Acesso entre contas com IAM Roles

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente Acesso entre contas com IAM Roles?

<details>
<summary>Ver verso</summary>

**Técnico:** Criar uma IAM Role na conta de dados, confiar na role da aplicação e usar AWS STS AssumeRole com política limitada ao bucket.

**Como criança:** É como dar um crachá de visitante que abre só uma sala e expira no fim da visita.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

**Prática:** ../labs/README.md — Lambda/API Gateway com IAM e acesso entre contas

</details>

---

## FC-003 — Acesso entre contas com IAM Roles

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar Acesso entre contas com IAM Roles?

<details>
<summary>Ver verso</summary>

**Técnico:** Uma bucket policy também participa do controle de acesso, mas a role com STS é a opção central quando a aplicação precisa de uma identidade temporária na outra conta.

**Como criança:** É como dar um crachá de visitante que abre só uma sala e expira no fim da visita.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

**Prática:** ../labs/README.md — Lambda/API Gateway com IAM e acesso entre contas

</details>

---

## FC-004 — Acesso entre contas com IAM Roles

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve Acesso entre contas com IAM Roles: “Criar um usuário IAM na conta de dados e copiar access key e secret key para a instância.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Chaves de longa duração aumentam o risco de vazamento e exigem rotação; não são necessárias para workloads na AWS.

**Como criança:** É como dar um crachá de visitante que abre só uma sala e expira no fim da visita.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

**Prática:** ../labs/README.md — Lambda/API Gateway com IAM e acesso entre contas

</details>

---

## FC-005 — Acesso entre contas com IAM Roles

> **Domínio:** D1

**Frente:** Ensine — Explique Acesso entre contas com IAM Roles em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** AssumeRole entrega credenciais temporárias e separa a política de confiança da política de permissões, permitindo acesso entre contas sem segredo de longa duração.

**Como criança:** É como dar um crachá de visitante que abre só uma sala e expira no fim da visita.

**Pegadinha:** Mnemônica: conecte “Acesso entre contas com IAM Roles” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

**Prática:** ../labs/README.md — Lambda/API Gateway com IAM e acesso entre contas

</details>

---

## FC-006 — S3 privado atrás do CloudFront

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito S3 privado atrás do CloudFront costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** O OAC permite que somente a distribuição autorizada leia o bucket, enquanto o WAF inspeciona requisições HTTP(S) antes de elas alcançarem a origem.

**Como criança:** O depósito fica trancado; um entregador com crachá busca os pacotes, e um porteiro barra visitantes perigosos.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Shield Standard já protege contra ataques DDoS comuns, mas WAF é o controle apropriado para padrões de camada 7 e o OAC evita bypass da distribuição.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

**Prática:** ../labs/README.md — S3, CloudFront e WAF

</details>

---

## FC-007 — S3 privado atrás do CloudFront

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente S3 privado atrás do CloudFront?

<details>
<summary>Ver verso</summary>

**Técnico:** CloudFront com Origin Access Control para o bucket privado, bucket policy restrita à distribuição e AWS WAF associado ao CloudFront.

**Como criança:** O depósito fica trancado; um entregador com crachá busca os pacotes, e um porteiro barra visitantes perigosos.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

**Prática:** ../labs/README.md — S3, CloudFront e WAF

</details>

---

## FC-008 — S3 privado atrás do CloudFront

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar S3 privado atrás do CloudFront?

<details>
<summary>Ver verso</summary>

**Técnico:** Shield Standard já protege contra ataques DDoS comuns, mas WAF é o controle apropriado para padrões de camada 7 e o OAC evita bypass da distribuição.

**Como criança:** O depósito fica trancado; um entregador com crachá busca os pacotes, e um porteiro barra visitantes perigosos.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

**Prática:** ../labs/README.md — S3, CloudFront e WAF

</details>

---

## FC-009 — S3 privado atrás do CloudFront

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve S3 privado atrás do CloudFront: “Habilitar website hosting público no S3 e filtrar acessos apenas com security groups.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Buckets S3 não usam security groups, e o endpoint de website exigiria exposição pública da origem.

**Como criança:** O depósito fica trancado; um entregador com crachá busca os pacotes, e um porteiro barra visitantes perigosos.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

**Prática:** ../labs/README.md — S3, CloudFront e WAF

</details>

---

## FC-010 — S3 privado atrás do CloudFront

> **Domínio:** D1

**Frente:** Ensine — Explique S3 privado atrás do CloudFront em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** O OAC permite que somente a distribuição autorizada leia o bucket, enquanto o WAF inspeciona requisições HTTP(S) antes de elas alcançarem a origem.

**Como criança:** O depósito fica trancado; um entregador com crachá busca os pacotes, e um porteiro barra visitantes perigosos.

**Pegadinha:** Mnemônica: conecte “S3 privado atrás do CloudFront” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

**Prática:** ../labs/README.md — S3, CloudFront e WAF

</details>

---

## FC-011 — Criptografia com AWS KMS

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito Criptografia com AWS KMS costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Uma chave KMS gerenciada pelo cliente oferece controle de política, trilha de auditoria no CloudTrail e rotação automática compatível com a criptografia do RDS.

**Como criança:** É um cofre cuja chave mestra tem lista de convidados, diário de uso e troca automática de segredo.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. A chave gerenciada pela AWS reduz administração, porém não dá o mesmo nível de controle de política exigido; a escolha da chave ocorre na criação ou restauração criptografada.

**Referência oficial:** [https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)

**Prática:** ../labs/README.md — KMS e criptografia em repouso

</details>

---

## FC-012 — Criptografia com AWS KMS

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente Criptografia com AWS KMS?

<details>
<summary>Ver verso</summary>

**Técnico:** Criar uma chave simétrica gerenciada pelo cliente no AWS KMS, limitar key policy/grants, habilitar rotação e selecioná-la ao criar o RDS.

**Como criança:** É um cofre cuja chave mestra tem lista de convidados, diário de uso e troca automática de segredo.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)

**Prática:** ../labs/README.md — KMS e criptografia em repouso

</details>

---

## FC-013 — Criptografia com AWS KMS

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar Criptografia com AWS KMS?

<details>
<summary>Ver verso</summary>

**Técnico:** A chave gerenciada pela AWS reduz administração, porém não dá o mesmo nível de controle de política exigido; a escolha da chave ocorre na criação ou restauração criptografada.

**Como criança:** É um cofre cuja chave mestra tem lista de convidados, diário de uso e troca automática de segredo.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)

**Prática:** ../labs/README.md — KMS e criptografia em repouso

</details>

---

## FC-014 — Criptografia com AWS KMS

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve Criptografia com AWS KMS: “Usar uma chave gerenciada pela AWS e editar diretamente sua key policy para impor a separação de funções.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Key policies de chaves gerenciadas pela AWS não são editáveis pelo cliente como as de uma chave gerenciada pelo cliente.

**Como criança:** É um cofre cuja chave mestra tem lista de convidados, diário de uso e troca automática de segredo.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)

**Prática:** ../labs/README.md — KMS e criptografia em repouso

</details>

---

## FC-015 — Criptografia com AWS KMS

> **Domínio:** D1

**Frente:** Ensine — Explique Criptografia com AWS KMS em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Uma chave KMS gerenciada pelo cliente oferece controle de política, trilha de auditoria no CloudTrail e rotação automática compatível com a criptografia do RDS.

**Como criança:** É um cofre cuja chave mestra tem lista de convidados, diário de uso e troca automática de segredo.

**Pegadinha:** Mnemônica: conecte “Criptografia com AWS KMS” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)

**Prática:** ../labs/README.md — KMS e criptografia em repouso

</details>

---

## FC-016 — Rotação de credenciais com Secrets Manager

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito Rotação de credenciais com Secrets Manager costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Secrets Manager armazena, versiona e integra a rotação de segredos; a role do workload elimina credenciais AWS embutidas no contêiner.

**Como criança:** A senha mora num cofrinho que troca a combinação sozinho e só mostra a nova combinação ao robô autorizado.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Parameter Store SecureString pode guardar valores sensíveis com KMS, mas a rotação gerenciada de credenciais de banco é a vantagem decisiva do Secrets Manager neste cenário.

**Referência oficial:** [https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

**Prática:** ../labs/README.md — Lambda/API Gateway com IAM roles

</details>

---

## FC-017 — Rotação de credenciais com Secrets Manager

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente Rotação de credenciais com Secrets Manager?

<details>
<summary>Ver verso</summary>

**Técnico:** Armazenar a credencial no AWS Secrets Manager, configurar rotação com Lambda e conceder à task role permissão de leitura do segredo.

**Como criança:** A senha mora num cofrinho que troca a combinação sozinho e só mostra a nova combinação ao robô autorizado.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

**Prática:** ../labs/README.md — Lambda/API Gateway com IAM roles

</details>

---

## FC-018 — Rotação de credenciais com Secrets Manager

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar Rotação de credenciais com Secrets Manager?

<details>
<summary>Ver verso</summary>

**Técnico:** Parameter Store SecureString pode guardar valores sensíveis com KMS, mas a rotação gerenciada de credenciais de banco é a vantagem decisiva do Secrets Manager neste cenário.

**Como criança:** A senha mora num cofrinho que troca a combinação sozinho e só mostra a nova combinação ao robô autorizado.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

**Prática:** ../labs/README.md — Lambda/API Gateway com IAM roles

</details>

---

## FC-019 — Rotação de credenciais com Secrets Manager

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve Rotação de credenciais com Secrets Manager: “Salvar a senha em uma variável de ambiente no Dockerfile e recriar a imagem mensalmente.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** A imagem pode vazar a senha e a rotação permanece manual e acoplada ao deploy.

**Como criança:** A senha mora num cofrinho que troca a combinação sozinho e só mostra a nova combinação ao robô autorizado.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

**Prática:** ../labs/README.md — Lambda/API Gateway com IAM roles

</details>

---

## FC-020 — Rotação de credenciais com Secrets Manager

> **Domínio:** D1

**Frente:** Ensine — Explique Rotação de credenciais com Secrets Manager em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Secrets Manager armazena, versiona e integra a rotação de segredos; a role do workload elimina credenciais AWS embutidas no contêiner.

**Como criança:** A senha mora num cofrinho que troca a combinação sozinho e só mostra a nova combinação ao robô autorizado.

**Pegadinha:** Mnemônica: conecte “Rotação de credenciais com Secrets Manager” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

**Prática:** ../labs/README.md — Lambda/API Gateway com IAM roles

</details>

---

## FC-021 — VPC Gateway Endpoint para S3

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito VPC Gateway Endpoint para S3 costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Gateway endpoints para S3 adicionam rotas privadas ao serviço, não exigem NAT e não têm a cobrança por hora típica de interface endpoints.

**Como criança:** É uma estrada particular e gratuita do escritório até o armazém, sem sair para a avenida pública.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Um NAT Gateway também permite chegar ao endpoint público do S3, mas adiciona custo por hora e por dados e não atende tão diretamente à exigência de caminho privado.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

</details>

---

## FC-022 — VPC Gateway Endpoint para S3

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente VPC Gateway Endpoint para S3?

<details>
<summary>Ver verso</summary>

**Técnico:** Criar um Gateway VPC Endpoint para S3, associá-lo às route tables privadas e restringir acesso com endpoint/bucket policies.

**Como criança:** É uma estrada particular e gratuita do escritório até o armazém, sem sair para a avenida pública.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

</details>

---

## FC-023 — VPC Gateway Endpoint para S3

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar VPC Gateway Endpoint para S3?

<details>
<summary>Ver verso</summary>

**Técnico:** Um NAT Gateway também permite chegar ao endpoint público do S3, mas adiciona custo por hora e por dados e não atende tão diretamente à exigência de caminho privado.

**Como criança:** É uma estrada particular e gratuita do escritório até o armazém, sem sair para a avenida pública.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

</details>

---

## FC-024 — VPC Gateway Endpoint para S3

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve VPC Gateway Endpoint para S3: “Enviar o tráfego por um NAT Gateway em cada AZ.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** O NAT adiciona custo e o caminho usa o endpoint público; é desnecessário quando há gateway endpoint para S3.

**Como criança:** É uma estrada particular e gratuita do escritório até o armazém, sem sair para a avenida pública.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

</details>

---

## FC-025 — VPC Gateway Endpoint para S3

> **Domínio:** D1

**Frente:** Ensine — Explique VPC Gateway Endpoint para S3 em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Gateway endpoints para S3 adicionam rotas privadas ao serviço, não exigem NAT e não têm a cobrança por hora típica de interface endpoints.

**Como criança:** É uma estrada particular e gratuita do escritório até o armazém, sem sair para a avenida pública.

**Pegadinha:** Mnemônica: conecte “VPC Gateway Endpoint para S3” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

</details>

---

## FC-026 — SCP em AWS Organizations

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito SCP em AWS Organizations costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** SCPs definem o teto de permissões de contas membros; um Allow local não consegue ultrapassar um Deny explícito aplicável da organização.

**Como criança:** É o muro do condomínio: cada morador escolhe as regras da casa, mas ninguém pode atravessar o muro externo.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. SCP não concede permissões e não substitui policies de identidade ou recurso; ele limita o conjunto máximo que esses mecanismos podem conceder.

**Referência oficial:** [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Prática:** ../labs/README.md — IAM, KMS e guardrails

</details>

---

## FC-027 — SCP em AWS Organizations

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente SCP em AWS Organizations?

<details>
<summary>Ver verso</summary>

**Técnico:** Aplicar Service Control Policies nas OUs, com exceções cuidadosamente definidas para serviços e funções indispensáveis.

**Como criança:** É o muro do condomínio: cada morador escolhe as regras da casa, mas ninguém pode atravessar o muro externo.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Prática:** ../labs/README.md — IAM, KMS e guardrails

</details>

---

## FC-028 — SCP em AWS Organizations

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar SCP em AWS Organizations?

<details>
<summary>Ver verso</summary>

**Técnico:** SCP não concede permissões e não substitui policies de identidade ou recurso; ele limita o conjunto máximo que esses mecanismos podem conceder.

**Como criança:** É o muro do condomínio: cada morador escolhe as regras da casa, mas ninguém pode atravessar o muro externo.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Prática:** ../labs/README.md — IAM, KMS e guardrails

</details>

---

## FC-029 — SCP em AWS Organizations

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve SCP em AWS Organizations: “Adicionar uma IAM policy Allow a todos os administradores das contas.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Um Allow amplia permissões locais e não cria o guardrail organizacional solicitado.

**Como criança:** É o muro do condomínio: cada morador escolhe as regras da casa, mas ninguém pode atravessar o muro externo.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Prática:** ../labs/README.md — IAM, KMS e guardrails

</details>

---

## FC-030 — SCP em AWS Organizations

> **Domínio:** D1

**Frente:** Ensine — Explique SCP em AWS Organizations em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** SCPs definem o teto de permissões de contas membros; um Allow local não consegue ultrapassar um Deny explícito aplicável da organização.

**Como criança:** É o muro do condomínio: cada morador escolhe as regras da casa, mas ninguém pode atravessar o muro externo.

**Pegadinha:** Mnemônica: conecte “SCP em AWS Organizations” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Prática:** ../labs/README.md — IAM, KMS e guardrails

</details>

---

## FC-031 — Trilha de auditoria organizacional

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito Trilha de auditoria organizacional costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Uma organization trail cobre contas da organização de forma central; políticas do bucket e validação de logs protegem a evidência, e eventos permitem alertas rápidos.

**Como criança:** Todas as salas escrevem no mesmo diário lacrado; se alguém tentar arrancar uma página, um alarme toca.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. CloudTrail Lake pode ajudar em consultas e retenção, mas não elimina a necessidade de definir proteção, governança e alertas coerentes para os registros.

**Referência oficial:** [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

**Prática:** ../labs/README.md — Observabilidade, CloudTrail e alertas

</details>

---

## FC-032 — Trilha de auditoria organizacional

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente Trilha de auditoria organizacional?

<details>
<summary>Ver verso</summary>

**Técnico:** Criar uma organization trail no CloudTrail para bucket central dedicado, habilitar validação de integridade, restringir o bucket e monitorar eventos com EventBridge/CloudWatch.

**Como criança:** Todas as salas escrevem no mesmo diário lacrado; se alguém tentar arrancar uma página, um alarme toca.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

**Prática:** ../labs/README.md — Observabilidade, CloudTrail e alertas

</details>

---

## FC-033 — Trilha de auditoria organizacional

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar Trilha de auditoria organizacional?

<details>
<summary>Ver verso</summary>

**Técnico:** CloudTrail Lake pode ajudar em consultas e retenção, mas não elimina a necessidade de definir proteção, governança e alertas coerentes para os registros.

**Como criança:** Todas as salas escrevem no mesmo diário lacrado; se alguém tentar arrancar uma página, um alarme toca.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

**Prática:** ../labs/README.md — Observabilidade, CloudTrail e alertas

</details>

---

## FC-034 — Trilha de auditoria organizacional

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve Trilha de auditoria organizacional: “Confiar apenas no Event history de 90 dias de cada conta.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** O histórico é limitado, regionalmente consultado e não fornece sozinho retenção central protegida.

**Como criança:** Todas as salas escrevem no mesmo diário lacrado; se alguém tentar arrancar uma página, um alarme toca.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

**Prática:** ../labs/README.md — Observabilidade, CloudTrail e alertas

</details>

---

## FC-035 — Trilha de auditoria organizacional

> **Domínio:** D1

**Frente:** Ensine — Explique Trilha de auditoria organizacional em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Uma organization trail cobre contas da organização de forma central; políticas do bucket e validação de logs protegem a evidência, e eventos permitem alertas rápidos.

**Como criança:** Todas as salas escrevem no mesmo diário lacrado; se alguém tentar arrancar uma página, um alarme toca.

**Pegadinha:** Mnemônica: conecte “Trilha de auditoria organizacional” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

**Prática:** ../labs/README.md — Observabilidade, CloudTrail e alertas

</details>

---

## FC-036 — Security groups e network ACLs

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito Security groups e network ACLs costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Security groups são stateful e associados a interfaces; NACLs são stateless, ordenadas e associadas a subnets, podendo negar CIDRs explicitamente.

**Como criança:** O crachá lembra quem entrou e deixa a resposta voltar; a cancela da rua verifica ida e volta e pode barrar uma placa.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Na maioria dos desenhos, security groups fazem o controle principal. NACLs são defesa adicional e exigem atenção às portas efêmeras nos dois sentidos.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

**Prática:** ../labs/README.md — VPC multi-AZ com SG e NACL

</details>

---

## FC-037 — Security groups e network ACLs

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente Security groups e network ACLs?

<details>
<summary>Ver verso</summary>

**Técnico:** Security groups para permitir apenas os fluxos necessários entre tiers e network ACLs para regras stateless de allow/deny no limite das subnets.

**Como criança:** O crachá lembra quem entrou e deixa a resposta voltar; a cancela da rua verifica ida e volta e pode barrar uma placa.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

**Prática:** ../labs/README.md — VPC multi-AZ com SG e NACL

</details>

---

## FC-038 — Security groups e network ACLs

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar Security groups e network ACLs?

<details>
<summary>Ver verso</summary>

**Técnico:** Na maioria dos desenhos, security groups fazem o controle principal. NACLs são defesa adicional e exigem atenção às portas efêmeras nos dois sentidos.

**Como criança:** O crachá lembra quem entrou e deixa a resposta voltar; a cancela da rua verifica ida e volta e pode barrar uma placa.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

**Prática:** ../labs/README.md — VPC multi-AZ com SG e NACL

</details>

---

## FC-039 — Security groups e network ACLs

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve Security groups e network ACLs: “Usar apenas uma NACL, pois ela mantém estado das conexões automaticamente.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** NACLs são stateless e exigem regras correspondentes de entrada e saída.

**Como criança:** O crachá lembra quem entrou e deixa a resposta voltar; a cancela da rua verifica ida e volta e pode barrar uma placa.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

**Prática:** ../labs/README.md — VPC multi-AZ com SG e NACL

</details>

---

## FC-040 — Security groups e network ACLs

> **Domínio:** D1

**Frente:** Ensine — Explique Security groups e network ACLs em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Security groups são stateful e associados a interfaces; NACLs são stateless, ordenadas e associadas a subnets, podendo negar CIDRs explicitamente.

**Como criança:** O crachá lembra quem entrou e deixa a resposta voltar; a cancela da rua verifica ida e volta e pode barrar uma placa.

**Pegadinha:** Mnemônica: conecte “Security groups e network ACLs” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

**Prática:** ../labs/README.md — VPC multi-AZ com SG e NACL

</details>

---

## FC-041 — Autenticação de clientes com Amazon Cognito

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito Autenticação de clientes com Amazon Cognito costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** User Pools fornecem autenticação de usuários e tokens OIDC/OAuth; a API valida esses tokens sem a equipe operar o armazenamento de senhas.

**Como criança:** É uma portaria pronta que cadastra visitantes e entrega pulseiras válidas para entrar na festa.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. IAM Identity Center atende principalmente força de trabalho; Cognito é adequado a identidades de clientes. Identity Pools cumprem outro papel: trocar identidades por credenciais AWS temporárias.

**Referência oficial:** [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)

**Prática:** ../labs/README.md — API Gateway, Lambda e autenticação

</details>

---

## FC-042 — Autenticação de clientes com Amazon Cognito

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente Autenticação de clientes com Amazon Cognito?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar um Amazon Cognito User Pool como diretório e emissor de tokens, integrando-o ao API Gateway; usar Identity Pool apenas se forem necessárias credenciais AWS temporárias.

**Como criança:** É uma portaria pronta que cadastra visitantes e entrega pulseiras válidas para entrar na festa.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)

**Prática:** ../labs/README.md — API Gateway, Lambda e autenticação

</details>

---

## FC-043 — Autenticação de clientes com Amazon Cognito

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar Autenticação de clientes com Amazon Cognito?

<details>
<summary>Ver verso</summary>

**Técnico:** IAM Identity Center atende principalmente força de trabalho; Cognito é adequado a identidades de clientes. Identity Pools cumprem outro papel: trocar identidades por credenciais AWS temporárias.

**Como criança:** É uma portaria pronta que cadastra visitantes e entrega pulseiras válidas para entrar na festa.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)

**Prática:** ../labs/README.md — API Gateway, Lambda e autenticação

</details>

---

## FC-044 — Autenticação de clientes com Amazon Cognito

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve Autenticação de clientes com Amazon Cognito: “Criar um usuário IAM para cada consumidor do aplicativo.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** IAM users não são um diretório de clientes em escala e gerariam riscos e operação excessivos.

**Como criança:** É uma portaria pronta que cadastra visitantes e entrega pulseiras válidas para entrar na festa.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)

**Prática:** ../labs/README.md — API Gateway, Lambda e autenticação

</details>

---

## FC-045 — Autenticação de clientes com Amazon Cognito

> **Domínio:** D1

**Frente:** Ensine — Explique Autenticação de clientes com Amazon Cognito em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** User Pools fornecem autenticação de usuários e tokens OIDC/OAuth; a API valida esses tokens sem a equipe operar o armazenamento de senhas.

**Como criança:** É uma portaria pronta que cadastra visitantes e entrega pulseiras válidas para entrar na festa.

**Pegadinha:** Mnemônica: conecte “Autenticação de clientes com Amazon Cognito” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)

**Prática:** ../labs/README.md — API Gateway, Lambda e autenticação

</details>

---

## FC-046 — Proteção de camada 7 com AWS WAF

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito Proteção de camada 7 com AWS WAF costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** WAF inspeciona atributos HTTP(S) e regras baseadas em taxa agregam requisições por chave, bloqueando ou desafiando origens abusivas na camada 7.

**Como criança:** O porteiro reconhece truques nas cartas e manda quem bate vezes demais esperar do lado de fora.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Shield Standard está incluído e lida com ataques DDoS comuns de rede e transporte; Shield Advanced acrescenta resposta e proteção de custo, mas não substitui regras HTTP do WAF.

**Referência oficial:** [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)

**Prática:** ../labs/README.md — S3/CloudFront/WAF e proteção web

</details>

---

## FC-047 — Proteção de camada 7 com AWS WAF

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente Proteção de camada 7 com AWS WAF?

<details>
<summary>Ver verso</summary>

**Técnico:** Associar um Web ACL do AWS WAF ao ALB, usando managed rules e uma rate-based rule ajustada ao tráfego legítimo.

**Como criança:** O porteiro reconhece truques nas cartas e manda quem bate vezes demais esperar do lado de fora.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)

**Prática:** ../labs/README.md — S3/CloudFront/WAF e proteção web

</details>

---

## FC-048 — Proteção de camada 7 com AWS WAF

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar Proteção de camada 7 com AWS WAF?

<details>
<summary>Ver verso</summary>

**Técnico:** Shield Standard está incluído e lida com ataques DDoS comuns de rede e transporte; Shield Advanced acrescenta resposta e proteção de custo, mas não substitui regras HTTP do WAF.

**Como criança:** O porteiro reconhece truques nas cartas e manda quem bate vezes demais esperar do lado de fora.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)

**Prática:** ../labs/README.md — S3/CloudFront/WAF e proteção web

</details>

---

## FC-049 — Proteção de camada 7 com AWS WAF

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve Proteção de camada 7 com AWS WAF: “Editar a NACL para bloquear palavras presentes no corpo HTTP.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** NACLs operam em rede e não inspecionam conteúdo HTTP.

**Como criança:** O porteiro reconhece truques nas cartas e manda quem bate vezes demais esperar do lado de fora.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)

**Prática:** ../labs/README.md — S3/CloudFront/WAF e proteção web

</details>

---

## FC-050 — Proteção de camada 7 com AWS WAF

> **Domínio:** D1

**Frente:** Ensine — Explique Proteção de camada 7 com AWS WAF em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** WAF inspeciona atributos HTTP(S) e regras baseadas em taxa agregam requisições por chave, bloqueando ou desafiando origens abusivas na camada 7.

**Como criança:** O porteiro reconhece truques nas cartas e manda quem bate vezes demais esperar do lado de fora.

**Pegadinha:** Mnemônica: conecte “Proteção de camada 7 com AWS WAF” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)

**Prática:** ../labs/README.md — S3/CloudFront/WAF e proteção web

</details>

---

## FC-051 — S3 Block Public Access e políticas

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito S3 Block Public Access e políticas costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Block Public Access neutraliza políticas e ACLs públicas; uma bucket policy com condição e Deny explícito restringe o caminho de acesso ao endpoint aprovado.

**Como criança:** Primeiro fechamos todas as janelas do prédio; depois damos uma chave que só funciona na passagem secreta certa.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Ao usar condições de endpoint, é preciso preservar acessos administrativos e de serviços necessários para não bloquear operações legítimas de forma acidental.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

**Prática:** ../labs/README.md — S3 privado e endpoints VPC

</details>

---

## FC-052 — S3 Block Public Access e políticas

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente S3 Block Public Access e políticas?

<details>
<summary>Ver verso</summary>

**Técnico:** Ativar S3 Block Public Access no nível da organização/contas e aplicar bucket policies com condição aws:SourceVpce e negação fora do endpoint autorizado.

**Como criança:** Primeiro fechamos todas as janelas do prédio; depois damos uma chave que só funciona na passagem secreta certa.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

**Prática:** ../labs/README.md — S3 privado e endpoints VPC

</details>

---

## FC-053 — S3 Block Public Access e políticas

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar S3 Block Public Access e políticas?

<details>
<summary>Ver verso</summary>

**Técnico:** Ao usar condições de endpoint, é preciso preservar acessos administrativos e de serviços necessários para não bloquear operações legítimas de forma acidental.

**Como criança:** Primeiro fechamos todas as janelas do prédio; depois damos uma chave que só funciona na passagem secreta certa.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

**Prática:** ../labs/README.md — S3 privado e endpoints VPC

</details>

---

## FC-054 — S3 Block Public Access e políticas

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve S3 Block Public Access e políticas: “Usar ACL public-read e esconder os nomes dos objetos.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Obscuridade de nomes não é controle de acesso, e a ACL tornaria dados públicos.

**Como criança:** Primeiro fechamos todas as janelas do prédio; depois damos uma chave que só funciona na passagem secreta certa.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

**Prática:** ../labs/README.md — S3 privado e endpoints VPC

</details>

---

## FC-055 — S3 Block Public Access e políticas

> **Domínio:** D1

**Frente:** Ensine — Explique S3 Block Public Access e políticas em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Block Public Access neutraliza políticas e ACLs públicas; uma bucket policy com condição e Deny explícito restringe o caminho de acesso ao endpoint aprovado.

**Como criança:** Primeiro fechamos todas as janelas do prédio; depois damos uma chave que só funciona na passagem secreta certa.

**Pegadinha:** Mnemônica: conecte “S3 Block Public Access e políticas” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

**Prática:** ../labs/README.md — S3 privado e endpoints VPC

</details>

---

## FC-056 — Permissions boundaries e delegação

> **Domínio:** D1

**Frente:** Decisão — Em qual requisito Permissions boundaries e delegação costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** A permissions boundary define o máximo que uma policy de identidade pode conceder, permitindo delegação sem entregar privilégios ilimitados.

**Como criança:** A criança escolhe onde brincar no quintal, mas a cerca define até onde ela pode ir.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Boundary não concede acesso por si só e precisa ser avaliada junto de policies de identidade, recurso, SCPs e negações explícitas.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)

**Prática:** ../labs/README.md — IAM least privilege e roles

</details>

---

## FC-057 — Permissions boundaries e delegação

> **Domínio:** D1

**Frente:** Solução — Qual implementação resume corretamente Permissions boundaries e delegação?

<details>
<summary>Ver verso</summary>

**Técnico:** Exigir uma permissions boundary nas roles criadas e controlar iam:PermissionsBoundary nas políticas do time.

**Como criança:** A criança escolhe onde brincar no quintal, mas a cerca define até onde ela pode ir.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)

**Prática:** ../labs/README.md — IAM least privilege e roles

</details>

---

## FC-058 — Permissions boundaries e delegação

> **Domínio:** D1

**Frente:** Trade-off — O que precisa ser lembrado ao usar Permissions boundaries e delegação?

<details>
<summary>Ver verso</summary>

**Técnico:** Boundary não concede acesso por si só e precisa ser avaliada junto de policies de identidade, recurso, SCPs e negações explícitas.

**Como criança:** A criança escolhe onde brincar no quintal, mas a cerca define até onde ela pode ir.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)

**Prática:** ../labs/README.md — IAM least privilege e roles

</details>

---

## FC-059 — Permissions boundaries e delegação

> **Domínio:** D1

**Frente:** Pegadinha — Por que esta alternativa não resolve Permissions boundaries e delegação: “Anexar AdministratorAccess e pedir que cada time não use ações perigosas.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Confiança processual não impõe um limite técnico e AdministratorAccess viola privilégio mínimo.

**Como criança:** A criança escolhe onde brincar no quintal, mas a cerca define até onde ela pode ir.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)

**Prática:** ../labs/README.md — IAM least privilege e roles

</details>

---

## FC-060 — Permissions boundaries e delegação

> **Domínio:** D1

**Frente:** Ensine — Explique Permissions boundaries e delegação em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** A permissions boundary define o máximo que uma policy de identidade pode conceder, permitindo delegação sem entregar privilégios ilimitados.

**Como criança:** A criança escolhe onde brincar no quintal, mas a cerca define até onde ela pode ir.

**Pegadinha:** Mnemônica: conecte “Permissions boundaries e delegação” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)

**Prática:** ../labs/README.md — IAM least privilege e roles

</details>

---

## FC-061 — RDS Multi-AZ

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito RDS Multi-AZ costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** RDS Multi-AZ replica de forma síncrona para outra AZ e executa failover do endpoint, sendo uma solução de alta disponibilidade e não de escalabilidade de leitura.

**Como criança:** Há uma loja gêmea pronta em outro bairro; se a primeira fecha, a placa aponta sozinha para a segunda.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Read replicas são assíncronas e adequadas para escalar leituras; podem ser promovidas, mas isso não equivale ao failover automático de Multi-AZ.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

**Prática:** ../labs/README.md — RDS Multi-AZ e read replica

</details>

---

## FC-062 — RDS Multi-AZ

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente RDS Multi-AZ?

<details>
<summary>Ver verso</summary>

**Técnico:** Habilitar uma implantação RDS Multi-AZ com standby síncrono e failover gerenciado.

**Como criança:** Há uma loja gêmea pronta em outro bairro; se a primeira fecha, a placa aponta sozinha para a segunda.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

**Prática:** ../labs/README.md — RDS Multi-AZ e read replica

</details>

---

## FC-063 — RDS Multi-AZ

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar RDS Multi-AZ?

<details>
<summary>Ver verso</summary>

**Técnico:** Read replicas são assíncronas e adequadas para escalar leituras; podem ser promovidas, mas isso não equivale ao failover automático de Multi-AZ.

**Como criança:** Há uma loja gêmea pronta em outro bairro; se a primeira fecha, a placa aponta sozinha para a segunda.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

**Prática:** ../labs/README.md — RDS Multi-AZ e read replica

</details>

---

## FC-064 — RDS Multi-AZ

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve RDS Multi-AZ: “Criar uma read replica na mesma AZ e usá-la como standby síncrono automático.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Read replicas usam replicação assíncrona e não fornecem o mesmo mecanismo de failover Multi-AZ.

**Como criança:** Há uma loja gêmea pronta em outro bairro; se a primeira fecha, a placa aponta sozinha para a segunda.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

**Prática:** ../labs/README.md — RDS Multi-AZ e read replica

</details>

---

## FC-065 — RDS Multi-AZ

> **Domínio:** D2

**Frente:** Ensine — Explique RDS Multi-AZ em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** RDS Multi-AZ replica de forma síncrona para outra AZ e executa failover do endpoint, sendo uma solução de alta disponibilidade e não de escalabilidade de leitura.

**Como criança:** Há uma loja gêmea pronta em outro bairro; se a primeira fecha, a placa aponta sozinha para a segunda.

**Pegadinha:** Mnemônica: conecte “RDS Multi-AZ” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

**Prática:** ../labs/README.md — RDS Multi-AZ e read replica

</details>

---

## FC-066 — ALB e Auto Scaling multi-AZ

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito ALB e Auto Scaling multi-AZ costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** O ALB encaminha apenas para targets saudáveis e o Auto Scaling substitui capacidade e distribui instâncias entre AZs, eliminando pontos únicos no tier web.

**Como criança:** Vários caixas trabalham em lojas de bairros diferentes; um organizador manda clientes só aos caixas abertos e chama reforço quando a fila cresce.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Sessões devem ficar fora das instâncias ou usar um armazenamento compartilhado; sticky sessions podem ajudar temporariamente, mas reduzem flexibilidade e não substituem estado externo.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html)

**Prática:** ../labs/README.md — ALB, Auto Scaling e health checks

</details>

---

## FC-067 — ALB e Auto Scaling multi-AZ

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente ALB e Auto Scaling multi-AZ?

<details>
<summary>Ver verso</summary>

**Técnico:** ALB em pelo menos duas AZs, Auto Scaling group distribuído nessas AZs e target tracking baseado em uma métrica apropriada.

**Como criança:** Vários caixas trabalham em lojas de bairros diferentes; um organizador manda clientes só aos caixas abertos e chama reforço quando a fila cresce.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html)

**Prática:** ../labs/README.md — ALB, Auto Scaling e health checks

</details>

---

## FC-068 — ALB e Auto Scaling multi-AZ

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar ALB e Auto Scaling multi-AZ?

<details>
<summary>Ver verso</summary>

**Técnico:** Sessões devem ficar fora das instâncias ou usar um armazenamento compartilhado; sticky sessions podem ajudar temporariamente, mas reduzem flexibilidade e não substituem estado externo.

**Como criança:** Vários caixas trabalham em lojas de bairros diferentes; um organizador manda clientes só aos caixas abertos e chama reforço quando a fila cresce.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html)

**Prática:** ../labs/README.md — ALB, Auto Scaling e health checks

</details>

---

## FC-069 — ALB e Auto Scaling multi-AZ

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve ALB e Auto Scaling multi-AZ: “Executar uma única instância grande e reiniciá-la com um cron job.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Ainda há ponto único de falha e recuperação dependente de automação frágil.

**Como criança:** Vários caixas trabalham em lojas de bairros diferentes; um organizador manda clientes só aos caixas abertos e chama reforço quando a fila cresce.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html)

**Prática:** ../labs/README.md — ALB, Auto Scaling e health checks

</details>

---

## FC-070 — ALB e Auto Scaling multi-AZ

> **Domínio:** D2

**Frente:** Ensine — Explique ALB e Auto Scaling multi-AZ em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** O ALB encaminha apenas para targets saudáveis e o Auto Scaling substitui capacidade e distribui instâncias entre AZs, eliminando pontos únicos no tier web.

**Como criança:** Vários caixas trabalham em lojas de bairros diferentes; um organizador manda clientes só aos caixas abertos e chama reforço quando a fila cresce.

**Pegadinha:** Mnemônica: conecte “ALB e Auto Scaling multi-AZ” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html)

**Prática:** ../labs/README.md — ALB, Auto Scaling e health checks

</details>

---

## FC-071 — Route 53 failover

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito Route 53 failover costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** A política de failover usa a saúde do recurso para responder com o secundário quando o primário falha, implementando active-passive no DNS.

**Como criança:** O mapa aponta para a loja principal; se a luz dela apaga, passa a apontar para a loja reserva.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. TTL influencia quanto tempo resolvers mantêm respostas antigas; failover DNS não encerra conexões já abertas e deve ser combinado com um plano de dados consistente.

**Referência oficial:** [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)

**Prática:** ../labs/README.md — Failover multi-região e Route 53

</details>

---

## FC-072 — Route 53 failover

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente Route 53 failover?

<details>
<summary>Ver verso</summary>

**Técnico:** Criar registros Route 53 com failover routing, marcar primário/secundário e associar health check ao endpoint primário.

**Como criança:** O mapa aponta para a loja principal; se a luz dela apaga, passa a apontar para a loja reserva.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)

**Prática:** ../labs/README.md — Failover multi-região e Route 53

</details>

---

## FC-073 — Route 53 failover

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar Route 53 failover?

<details>
<summary>Ver verso</summary>

**Técnico:** TTL influencia quanto tempo resolvers mantêm respostas antigas; failover DNS não encerra conexões já abertas e deve ser combinado com um plano de dados consistente.

**Como criança:** O mapa aponta para a loja principal; se a luz dela apaga, passa a apontar para a loja reserva.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)

**Prática:** ../labs/README.md — Failover multi-região e Route 53

</details>

---

## FC-074 — Route 53 failover

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve Route 53 failover: “Usar simple routing com dois endereços e nenhum health check.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Simple routing não fornece o comportamento primário/secundário orientado por saúde.

**Como criança:** O mapa aponta para a loja principal; se a luz dela apaga, passa a apontar para a loja reserva.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)

**Prática:** ../labs/README.md — Failover multi-região e Route 53

</details>

---

## FC-075 — Route 53 failover

> **Domínio:** D2

**Frente:** Ensine — Explique Route 53 failover em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** A política de failover usa a saúde do recurso para responder com o secundário quando o primário falha, implementando active-passive no DNS.

**Como criança:** O mapa aponta para a loja principal; se a luz dela apaga, passa a apontar para a loja reserva.

**Pegadinha:** Mnemônica: conecte “Route 53 failover” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)

**Prática:** ../labs/README.md — Failover multi-região e Route 53

</details>

---

## FC-076 — Desacoplamento com SQS e DLQ

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito Desacoplamento com SQS e DLQ costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** SQS armazena mensagens de forma durável e desacopla ritmos; visibility timeout evita processamento concorrente imediato e a DLQ isola mensagens após tentativas definidas.

**Como criança:** Os pedidos entram numa caixa de correio; o cozinheiro pega um, e pedidos problemáticos vão para uma bandeja de investigação.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Standard queues entregam ao menos uma vez e podem duplicar; idempotência é essencial. FIFO deve ser usada apenas quando ordenação estrita/deduplicação justificarem suas restrições.

**Referência oficial:** [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

**Prática:** ../labs/README.md — Lambda, filas e tratamento de falhas

</details>

---

## FC-077 — Desacoplamento com SQS e DLQ

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente Desacoplamento com SQS e DLQ?

<details>
<summary>Ver verso</summary>

**Técnico:** Enviar pedidos para uma fila SQS, processar com consumidores idempotentes, configurar visibility timeout e redrive para uma DLQ.

**Como criança:** Os pedidos entram numa caixa de correio; o cozinheiro pega um, e pedidos problemáticos vão para uma bandeja de investigação.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

**Prática:** ../labs/README.md — Lambda, filas e tratamento de falhas

</details>

---

## FC-078 — Desacoplamento com SQS e DLQ

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar Desacoplamento com SQS e DLQ?

<details>
<summary>Ver verso</summary>

**Técnico:** Standard queues entregam ao menos uma vez e podem duplicar; idempotência é essencial. FIFO deve ser usada apenas quando ordenação estrita/deduplicação justificarem suas restrições.

**Como criança:** Os pedidos entram numa caixa de correio; o cozinheiro pega um, e pedidos problemáticos vão para uma bandeja de investigação.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

**Prática:** ../labs/README.md — Lambda, filas e tratamento de falhas

</details>

---

## FC-079 — Desacoplamento com SQS e DLQ

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve Desacoplamento com SQS e DLQ: “Fazer o produtor chamar o processador de forma síncrona com retries infinitos.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Isso acopla os componentes, prende recursos e pode criar tempestades de retries.

**Como criança:** Os pedidos entram numa caixa de correio; o cozinheiro pega um, e pedidos problemáticos vão para uma bandeja de investigação.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

**Prática:** ../labs/README.md — Lambda, filas e tratamento de falhas

</details>

---

## FC-080 — Desacoplamento com SQS e DLQ

> **Domínio:** D2

**Frente:** Ensine — Explique Desacoplamento com SQS e DLQ em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** SQS armazena mensagens de forma durável e desacopla ritmos; visibility timeout evita processamento concorrente imediato e a DLQ isola mensagens após tentativas definidas.

**Como criança:** Os pedidos entram numa caixa de correio; o cozinheiro pega um, e pedidos problemáticos vão para uma bandeja de investigação.

**Pegadinha:** Mnemônica: conecte “Desacoplamento com SQS e DLQ” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

**Prática:** ../labs/README.md — Lambda, filas e tratamento de falhas

</details>

---

## FC-081 — Fan-out com SNS e SQS

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito Fan-out com SNS e SQS costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** SNS replica cada mensagem para as filas assinantes; cada SQS mantém seu próprio backlog, ritmo e política de falhas, isolando consumidores.

**Como criança:** Um locutor anuncia a notícia para três caixas de correio; cada equipe abre a sua quando puder.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Uma única fila com três consumidores distribuiria mensagens entre eles, em vez de entregar uma cópia a cada função de negócio.

**Referência oficial:** [https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)

**Prática:** ../labs/README.md — Eventos, SNS, SQS e Lambda

</details>

---

## FC-082 — Fan-out com SNS e SQS

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente Fan-out com SNS e SQS?

<details>
<summary>Ver verso</summary>

**Técnico:** Publicar em uma SNS topic e criar uma fila SQS separada para cada consumidor, com subscriptions e DLQs próprias.

**Como criança:** Um locutor anuncia a notícia para três caixas de correio; cada equipe abre a sua quando puder.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)

**Prática:** ../labs/README.md — Eventos, SNS, SQS e Lambda

</details>

---

## FC-083 — Fan-out com SNS e SQS

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar Fan-out com SNS e SQS?

<details>
<summary>Ver verso</summary>

**Técnico:** Uma única fila com três consumidores distribuiria mensagens entre eles, em vez de entregar uma cópia a cada função de negócio.

**Como criança:** Um locutor anuncia a notícia para três caixas de correio; cada equipe abre a sua quando puder.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)

**Prática:** ../labs/README.md — Eventos, SNS, SQS e Lambda

</details>

---

## FC-084 — Fan-out com SNS e SQS

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve Fan-out com SNS e SQS: “Usar uma única fila SQS e fazer os três serviços competirem pela mesma mensagem.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Consumidores concorrentes em uma fila recebem mensagens diferentes; não há fan-out por consumidor.

**Como criança:** Um locutor anuncia a notícia para três caixas de correio; cada equipe abre a sua quando puder.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)

**Prática:** ../labs/README.md — Eventos, SNS, SQS e Lambda

</details>

---

## FC-085 — Fan-out com SNS e SQS

> **Domínio:** D2

**Frente:** Ensine — Explique Fan-out com SNS e SQS em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** SNS replica cada mensagem para as filas assinantes; cada SQS mantém seu próprio backlog, ritmo e política de falhas, isolando consumidores.

**Como criança:** Um locutor anuncia a notícia para três caixas de correio; cada equipe abre a sua quando puder.

**Pegadinha:** Mnemônica: conecte “Fan-out com SNS e SQS” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)

**Prática:** ../labs/README.md — Eventos, SNS, SQS e Lambda

</details>

---

## FC-086 — Estratégias de disaster recovery

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito Estratégias de disaster recovery costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Warm standby já executa todos os componentes essenciais, reduzindo o RTO em comparação a pilot light sem manter capacidade integral como active-active.

**Como criança:** Há uma lojinha reserva já aberta com poucos caixas; numa emergência, ela chama reforços rapidamente.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Pilot light custa menos, mas precisa iniciar/implantar parte relevante da aplicação; multi-site active-active oferece RTO menor com maior custo e complexidade.

**Referência oficial:** [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

**Prática:** ../labs/README.md — Cenário de recuperação multi-região

</details>

---

## FC-087 — Estratégias de disaster recovery

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente Estratégias de disaster recovery?

<details>
<summary>Ver verso</summary>

**Técnico:** Warm standby: manter uma versão funcional em escala reduzida na região secundária, replicar dados e escalar durante o failover.

**Como criança:** Há uma lojinha reserva já aberta com poucos caixas; numa emergência, ela chama reforços rapidamente.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

**Prática:** ../labs/README.md — Cenário de recuperação multi-região

</details>

---

## FC-088 — Estratégias de disaster recovery

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar Estratégias de disaster recovery?

<details>
<summary>Ver verso</summary>

**Técnico:** Pilot light custa menos, mas precisa iniciar/implantar parte relevante da aplicação; multi-site active-active oferece RTO menor com maior custo e complexidade.

**Como criança:** Há uma lojinha reserva já aberta com poucos caixas; numa emergência, ela chama reforços rapidamente.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

**Prática:** ../labs/README.md — Cenário de recuperação multi-região

</details>

---

## FC-089 — Estratégias de disaster recovery

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve Estratégias de disaster recovery: “Backup and restore com backups semanais offline.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Em geral não atende RPO de minutos nem RTO de 15 minutos.

**Como criança:** Há uma lojinha reserva já aberta com poucos caixas; numa emergência, ela chama reforços rapidamente.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

**Prática:** ../labs/README.md — Cenário de recuperação multi-região

</details>

---

## FC-090 — Estratégias de disaster recovery

> **Domínio:** D2

**Frente:** Ensine — Explique Estratégias de disaster recovery em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Warm standby já executa todos os componentes essenciais, reduzindo o RTO em comparação a pilot light sem manter capacidade integral como active-active.

**Como criança:** Há uma lojinha reserva já aberta com poucos caixas; numa emergência, ela chama reforços rapidamente.

**Pegadinha:** Mnemônica: conecte “Estratégias de disaster recovery” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

**Prática:** ../labs/README.md — Cenário de recuperação multi-região

</details>

---

## FC-091 — Replicação S3 entre regiões

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito Replicação S3 entre regiões costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** CRR requer versionamento e replica novos objetos conforme as regras. A política de delete markers e mecanismos de retenção determinam o comportamento diante de exclusões.

**Como criança:** Cada desenho ganha uma cópia em outra cidade e versões antigas ficam num fichário que uma borracha comum não apaga.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Replicação não é retroativa por padrão e não substitui toda estratégia de backup; S3 Batch Replication pode tratar objetos existentes.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

**Prática:** ../labs/README.md — S3 versionado e recuperação

</details>

---

## FC-092 — Replicação S3 entre regiões

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente Replicação S3 entre regiões?

<details>
<summary>Ver verso</summary>

**Técnico:** Habilitar versionamento nos buckets, configurar S3 Cross-Region Replication e definir cuidadosamente replicação de delete markers e retenção/Object Lock quando exigido.

**Como criança:** Cada desenho ganha uma cópia em outra cidade e versões antigas ficam num fichário que uma borracha comum não apaga.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

**Prática:** ../labs/README.md — S3 versionado e recuperação

</details>

---

## FC-093 — Replicação S3 entre regiões

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar Replicação S3 entre regiões?

<details>
<summary>Ver verso</summary>

**Técnico:** Replicação não é retroativa por padrão e não substitui toda estratégia de backup; S3 Batch Replication pode tratar objetos existentes.

**Como criança:** Cada desenho ganha uma cópia em outra cidade e versões antigas ficam num fichário que uma borracha comum não apaga.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

**Prática:** ../labs/README.md — S3 versionado e recuperação

</details>

---

## FC-094 — Replicação S3 entre regiões

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve Replicação S3 entre regiões: “Usar lifecycle expiration no bucket de origem como mecanismo de cópia.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Lifecycle gerencia transição/expiração e não replica objetos para outra região.

**Como criança:** Cada desenho ganha uma cópia em outra cidade e versões antigas ficam num fichário que uma borracha comum não apaga.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

**Prática:** ../labs/README.md — S3 versionado e recuperação

</details>

---

## FC-095 — Replicação S3 entre regiões

> **Domínio:** D2

**Frente:** Ensine — Explique Replicação S3 entre regiões em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** CRR requer versionamento e replica novos objetos conforme as regras. A política de delete markers e mecanismos de retenção determinam o comportamento diante de exclusões.

**Como criança:** Cada desenho ganha uma cópia em outra cidade e versões antigas ficam num fichário que uma borracha comum não apaga.

**Pegadinha:** Mnemônica: conecte “Replicação S3 entre regiões” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

**Prática:** ../labs/README.md — S3 versionado e recuperação

</details>

---

## FC-096 — Amazon EFS Regional

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito Amazon EFS Regional costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** EFS Regional fornece sistema de arquivos gerenciado, elástico e multi-AZ, adequado ao compartilhamento simultâneo entre instâncias Linux.

**Como criança:** É uma estante compartilhada com portas em vários bairros; se uma porta fecha, as outras ainda chegam aos livros.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. EFS One Zone pode custar menos, mas não atende ao requisito de tolerância à perda de uma AZ. EBS é zonal e normalmente anexado a uma instância.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html)

**Prática:** ../labs/README.md — Armazenamento compartilhado multi-AZ

</details>

---

## FC-097 — Amazon EFS Regional

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente Amazon EFS Regional?

<details>
<summary>Ver verso</summary>

**Técnico:** Amazon EFS Regional montado pelos clientes nas diferentes AZs, com mount targets e security groups adequados.

**Como criança:** É uma estante compartilhada com portas em vários bairros; se uma porta fecha, as outras ainda chegam aos livros.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html)

**Prática:** ../labs/README.md — Armazenamento compartilhado multi-AZ

</details>

---

## FC-098 — Amazon EFS Regional

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar Amazon EFS Regional?

<details>
<summary>Ver verso</summary>

**Técnico:** EFS One Zone pode custar menos, mas não atende ao requisito de tolerância à perda de uma AZ. EBS é zonal e normalmente anexado a uma instância.

**Como criança:** É uma estante compartilhada com portas em vários bairros; se uma porta fecha, as outras ainda chegam aos livros.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html)

**Prática:** ../labs/README.md — Armazenamento compartilhado multi-AZ

</details>

---

## FC-099 — Amazon EFS Regional

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve Amazon EFS Regional: “Usar um único volume EBS em uma AZ e anexá-lo simultaneamente a qualquer número de instâncias Linux.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** EBS é zonal e Multi-Attach possui tipos e cenários restritos; não vira um sistema de arquivos regional gerenciado.

**Como criança:** É uma estante compartilhada com portas em vários bairros; se uma porta fecha, as outras ainda chegam aos livros.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html)

**Prática:** ../labs/README.md — Armazenamento compartilhado multi-AZ

</details>

---

## FC-100 — Amazon EFS Regional

> **Domínio:** D2

**Frente:** Ensine — Explique Amazon EFS Regional em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** EFS Regional fornece sistema de arquivos gerenciado, elástico e multi-AZ, adequado ao compartilhamento simultâneo entre instâncias Linux.

**Como criança:** É uma estante compartilhada com portas em vários bairros; se uma porta fecha, as outras ainda chegam aos livros.

**Pegadinha:** Mnemônica: conecte “Amazon EFS Regional” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html)

**Prática:** ../labs/README.md — Armazenamento compartilhado multi-AZ

</details>

---

## FC-101 — Aurora Global Database

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito Aurora Global Database costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Aurora Global Database usa replicação dedicada entre regiões, oferece leituras locais e permite promover uma região secundária em um evento de recuperação.

**Como criança:** O livro mestre é escrito numa cidade, enquanto cópias quase instantâneas chegam às bibliotecas do mundo.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. A promoção e o roteamento da aplicação ainda precisam ser planejados. Multi-AZ protege dentro de uma região e não fornece, sozinho, leituras globais.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

**Prática:** ../labs/README.md — RDS/Aurora, réplicas e failover

</details>

---

## FC-102 — Aurora Global Database

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente Aurora Global Database?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar Aurora Global Database com cluster primário gravável e clusters secundários de leitura nas regiões necessárias.

**Como criança:** O livro mestre é escrito numa cidade, enquanto cópias quase instantâneas chegam às bibliotecas do mundo.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

**Prática:** ../labs/README.md — RDS/Aurora, réplicas e failover

</details>

---

## FC-103 — Aurora Global Database

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar Aurora Global Database?

<details>
<summary>Ver verso</summary>

**Técnico:** A promoção e o roteamento da aplicação ainda precisam ser planejados. Multi-AZ protege dentro de uma região e não fornece, sozinho, leituras globais.

**Como criança:** O livro mestre é escrito numa cidade, enquanto cópias quase instantâneas chegam às bibliotecas do mundo.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

**Prática:** ../labs/README.md — RDS/Aurora, réplicas e failover

</details>

---

## FC-104 — Aurora Global Database

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve Aurora Global Database: “Usar apenas Multi-AZ no cluster primário e esperar endpoints de leitura em outras regiões.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Multi-AZ oferece resiliência regional, não clusters de leitura entre regiões.

**Como criança:** O livro mestre é escrito numa cidade, enquanto cópias quase instantâneas chegam às bibliotecas do mundo.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

**Prática:** ../labs/README.md — RDS/Aurora, réplicas e failover

</details>

---

## FC-105 — Aurora Global Database

> **Domínio:** D2

**Frente:** Ensine — Explique Aurora Global Database em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Aurora Global Database usa replicação dedicada entre regiões, oferece leituras locais e permite promover uma região secundária em um evento de recuperação.

**Como criança:** O livro mestre é escrito numa cidade, enquanto cópias quase instantâneas chegam às bibliotecas do mundo.

**Pegadinha:** Mnemônica: conecte “Aurora Global Database” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

**Prática:** ../labs/README.md — RDS/Aurora, réplicas e failover

</details>

---

## FC-106 — DynamoDB Global Tables

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito DynamoDB Global Tables costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Global Tables em MREC fornecem replicação multi-active gerenciada, permitindo leitura e gravação locais nas regiões participantes.

**Como criança:** São dois cadernos mágicos: dá para escrever em qualquer cidade e as novidades aparecem no outro.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. No modo MREC, conflitos concorrentes usam last-writer-wins e a aplicação deve entender essa semântica. O modo MRSC oferece consistência forte multi-região com outra semântica, topologia e disponibilidade regional; a escolha depende do requisito de consistência.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e desenho de chaves

</details>

---

## FC-107 — DynamoDB Global Tables

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente DynamoDB Global Tables?

<details>
<summary>Ver verso</summary>

**Técnico:** Criar uma DynamoDB global table no modo de consistência eventual multi-região (MREC) e tornar a aplicação tolerante à resolução last-writer-wins.

**Como criança:** São dois cadernos mágicos: dá para escrever em qualquer cidade e as novidades aparecem no outro.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e desenho de chaves

</details>

---

## FC-108 — DynamoDB Global Tables

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar DynamoDB Global Tables?

<details>
<summary>Ver verso</summary>

**Técnico:** No modo MREC, conflitos concorrentes usam last-writer-wins e a aplicação deve entender essa semântica. O modo MRSC oferece consistência forte multi-região com outra semântica, topologia e disponibilidade regional; a escolha depende do requisito de consistência.

**Como criança:** São dois cadernos mágicos: dá para escrever em qualquer cidade e as novidades aparecem no outro.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e desenho de chaves

</details>

---

## FC-109 — DynamoDB Global Tables

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve DynamoDB Global Tables: “Criar uma tabela comum em uma única região e usar Multi-AZ manualmente.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** DynamoDB já é multi-AZ na região, mas isso não fornece gravações locais em duas regiões.

**Como criança:** São dois cadernos mágicos: dá para escrever em qualquer cidade e as novidades aparecem no outro.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e desenho de chaves

</details>

---

## FC-110 — DynamoDB Global Tables

> **Domínio:** D2

**Frente:** Ensine — Explique DynamoDB Global Tables em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Global Tables em MREC fornecem replicação multi-active gerenciada, permitindo leitura e gravação locais nas regiões participantes.

**Como criança:** São dois cadernos mágicos: dá para escrever em qualquer cidade e as novidades aparecem no outro.

**Pegadinha:** Mnemônica: conecte “DynamoDB Global Tables” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e desenho de chaves

</details>

---

## FC-111 — Falhas assíncronas do Lambda

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito Falhas assíncronas do Lambda costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Invocações assíncronas possuem fila e retries gerenciados; destinations entregam contexto do resultado após as tentativas, permitindo análise e reprocessamento desacoplado.

**Como criança:** Cartinhas que o robô não consegue ler vão para uma caixa vermelha, sem parar a leitura das demais.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. DLQ e destination têm formatos e capacidades diferentes; a equipe deve escolher um, observar idade máxima do evento e evitar loops de reprocessamento.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e tratamento de erros

</details>

---

## FC-112 — Falhas assíncronas do Lambda

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente Falhas assíncronas do Lambda?

<details>
<summary>Ver verso</summary>

**Técnico:** Configurar uma on-failure destination para SQS/SNS/EventBridge ou uma DLQ compatível, além de alarmes e processamento idempotente.

**Como criança:** Cartinhas que o robô não consegue ler vão para uma caixa vermelha, sem parar a leitura das demais.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e tratamento de erros

</details>

---

## FC-113 — Falhas assíncronas do Lambda

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar Falhas assíncronas do Lambda?

<details>
<summary>Ver verso</summary>

**Técnico:** DLQ e destination têm formatos e capacidades diferentes; a equipe deve escolher um, observar idade máxima do evento e evitar loops de reprocessamento.

**Como criança:** Cartinhas que o robô não consegue ler vão para uma caixa vermelha, sem parar a leitura das demais.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e tratamento de erros

</details>

---

## FC-114 — Falhas assíncronas do Lambda

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve Falhas assíncronas do Lambda: “Definir timeout infinito para garantir que toda execução termine.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Lambda tem limite de timeout e aumentar duração não resolve eventos permanentemente inválidos.

**Como criança:** Cartinhas que o robô não consegue ler vão para uma caixa vermelha, sem parar a leitura das demais.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e tratamento de erros

</details>

---

## FC-115 — Falhas assíncronas do Lambda

> **Domínio:** D2

**Frente:** Ensine — Explique Falhas assíncronas do Lambda em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Invocações assíncronas possuem fila e retries gerenciados; destinations entregam contexto do resultado após as tentativas, permitindo análise e reprocessamento desacoplado.

**Como criança:** Cartinhas que o robô não consegue ler vão para uma caixa vermelha, sem parar a leitura das demais.

**Pegadinha:** Mnemônica: conecte “Falhas assíncronas do Lambda” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e tratamento de erros

</details>

---

## FC-116 — Políticas centralizadas com AWS Backup

> **Domínio:** D2

**Frente:** Decisão — Em qual requisito Políticas centralizadas com AWS Backup costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** AWS Backup centraliza planos, seleção, retenção e cópias entre serviços e contas; Vault Lock ajuda a impor retenção WORM contra alterações indevidas.

**Como criança:** Um bibliotecário central faz cópias de todos os livros, guarda outra caixa em outra cidade e lacra as caixas pelo prazo certo.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Backup só é confiável quando restaurações são testadas e métricas de RPO/RTO são verificadas; replicação e alta disponibilidade não substituem backups protegidos.

**Referência oficial:** [https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html)

**Prática:** ../labs/README.md — Backup, restore e testes de recuperação

</details>

---

## FC-117 — Políticas centralizadas com AWS Backup

> **Domínio:** D2

**Frente:** Solução — Qual implementação resume corretamente Políticas centralizadas com AWS Backup?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar AWS Backup com backup policies da organização, cofre central/cross-account, cópia cross-region e Vault Lock quando a imutabilidade for requerida.

**Como criança:** Um bibliotecário central faz cópias de todos os livros, guarda outra caixa em outra cidade e lacra as caixas pelo prazo certo.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html)

**Prática:** ../labs/README.md — Backup, restore e testes de recuperação

</details>

---

## FC-118 — Políticas centralizadas com AWS Backup

> **Domínio:** D2

**Frente:** Trade-off — O que precisa ser lembrado ao usar Políticas centralizadas com AWS Backup?

<details>
<summary>Ver verso</summary>

**Técnico:** Backup só é confiável quando restaurações são testadas e métricas de RPO/RTO são verificadas; replicação e alta disponibilidade não substituem backups protegidos.

**Como criança:** Um bibliotecário central faz cópias de todos os livros, guarda outra caixa em outra cidade e lacra as caixas pelo prazo certo.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html)

**Prática:** ../labs/README.md — Backup, restore e testes de recuperação

</details>

---

## FC-119 — Políticas centralizadas com AWS Backup

> **Domínio:** D2

**Frente:** Pegadinha — Por que esta alternativa não resolve Políticas centralizadas com AWS Backup: “Pedir que cada desenvolvedor crie snapshots manuais quando lembrar.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** O processo não é consistente, auditável nem centralmente imposto.

**Como criança:** Um bibliotecário central faz cópias de todos os livros, guarda outra caixa em outra cidade e lacra as caixas pelo prazo certo.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html)

**Prática:** ../labs/README.md — Backup, restore e testes de recuperação

</details>

---

## FC-120 — Políticas centralizadas com AWS Backup

> **Domínio:** D2

**Frente:** Ensine — Explique Políticas centralizadas com AWS Backup em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** AWS Backup centraliza planos, seleção, retenção e cópias entre serviços e contas; Vault Lock ajuda a impor retenção WORM contra alterações indevidas.

**Como criança:** Um bibliotecário central faz cópias de todos os livros, guarda outra caixa em outra cidade e lacra as caixas pelo prazo certo.

**Pegadinha:** Mnemônica: conecte “Políticas centralizadas com AWS Backup” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html)

**Prática:** ../labs/README.md — Backup, restore e testes de recuperação

</details>

---

## FC-121 — Cache global com CloudFront

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito Cache global com CloudFront costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** CloudFront guarda objetos em edge locations próximas aos usuários, reduzindo latência e carga na origem; políticas de cache controlam a chave e a validade.

**Como criança:** Em vez de buscar cada brinquedo na fábrica distante, pequenas lojas perto das crianças guardam os mais pedidos.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. TTL longo aumenta hit ratio, mas atrasa atualizações; versionar nomes de objetos é geralmente mais previsível que invalidar grandes volumes.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html)

**Prática:** ../labs/README.md — S3, CloudFront e WAF

</details>

---

## FC-122 — Cache global com CloudFront

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente Cache global com CloudFront?

<details>
<summary>Ver verso</summary>

**Técnico:** Distribuir o conteúdo com CloudFront, definir cache policies/TTLs adequados, compressão e OAC para a origem S3 privada.

**Como criança:** Em vez de buscar cada brinquedo na fábrica distante, pequenas lojas perto das crianças guardam os mais pedidos.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html)

**Prática:** ../labs/README.md — S3, CloudFront e WAF

</details>

---

## FC-123 — Cache global com CloudFront

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar Cache global com CloudFront?

<details>
<summary>Ver verso</summary>

**Técnico:** TTL longo aumenta hit ratio, mas atrasa atualizações; versionar nomes de objetos é geralmente mais previsível que invalidar grandes volumes.

**Como criança:** Em vez de buscar cada brinquedo na fábrica distante, pequenas lojas perto das crianças guardam os mais pedidos.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html)

**Prática:** ../labs/README.md — S3, CloudFront e WAF

</details>

---

## FC-124 — Cache global com CloudFront

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve Cache global com CloudFront: “Aumentar o tamanho do bucket S3.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** S3 não precisa de provisionamento de capacidade do bucket e isso não aproxima conteúdo do usuário.

**Como criança:** Em vez de buscar cada brinquedo na fábrica distante, pequenas lojas perto das crianças guardam os mais pedidos.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html)

**Prática:** ../labs/README.md — S3, CloudFront e WAF

</details>

---

## FC-125 — Cache global com CloudFront

> **Domínio:** D3

**Frente:** Ensine — Explique Cache global com CloudFront em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** CloudFront guarda objetos em edge locations próximas aos usuários, reduzindo latência e carga na origem; políticas de cache controlam a chave e a validade.

**Como criança:** Em vez de buscar cada brinquedo na fábrica distante, pequenas lojas perto das crianças guardam os mais pedidos.

**Pegadinha:** Mnemônica: conecte “Cache global com CloudFront” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html)

**Prática:** ../labs/README.md — S3, CloudFront e WAF

</details>

---

## FC-126 — ElastiCache for Redis

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito ElastiCache for Redis costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Redis oferece acesso em memória de baixa latência e remove leituras repetitivas do banco; cache-aside mantém o banco como fonte de verdade.

**Como criança:** As respostas mais usadas ficam em post-its na mesa, em vez de procurar o livro inteiro a cada pergunta.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Cache introduz risco de dados obsoletos e stampede. TTL, jitter, réplicas e comportamento quando o cache falha devem ser desenhados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html)

**Prática:** ../labs/README.md — Cache, banco e observabilidade

</details>

---

## FC-127 — ElastiCache for Redis

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente ElastiCache for Redis?

<details>
<summary>Ver verso</summary>

**Técnico:** Adicionar ElastiCache for Redis e aplicar cache-aside com TTL, tratamento de cache miss e invalidação coerente.

**Como criança:** As respostas mais usadas ficam em post-its na mesa, em vez de procurar o livro inteiro a cada pergunta.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html)

**Prática:** ../labs/README.md — Cache, banco e observabilidade

</details>

---

## FC-128 — ElastiCache for Redis

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar ElastiCache for Redis?

<details>
<summary>Ver verso</summary>

**Técnico:** Cache introduz risco de dados obsoletos e stampede. TTL, jitter, réplicas e comportamento quando o cache falha devem ser desenhados.

**Como criança:** As respostas mais usadas ficam em post-its na mesa, em vez de procurar o livro inteiro a cada pergunta.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html)

**Prática:** ../labs/README.md — Cache, banco e observabilidade

</details>

---

## FC-129 — ElastiCache for Redis

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve ElastiCache for Redis: “Criar uma read replica e gravar sessões diretamente nela.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Read replicas relacionais normalmente são somente leitura e não são ideais como armazenamento de sessão volátil.

**Como criança:** As respostas mais usadas ficam em post-its na mesa, em vez de procurar o livro inteiro a cada pergunta.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html)

**Prática:** ../labs/README.md — Cache, banco e observabilidade

</details>

---

## FC-130 — ElastiCache for Redis

> **Domínio:** D3

**Frente:** Ensine — Explique ElastiCache for Redis em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Redis oferece acesso em memória de baixa latência e remove leituras repetitivas do banco; cache-aside mantém o banco como fonte de verdade.

**Como criança:** As respostas mais usadas ficam em post-its na mesa, em vez de procurar o livro inteiro a cada pergunta.

**Pegadinha:** Mnemônica: conecte “ElastiCache for Redis” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html)

**Prática:** ../labs/README.md — Cache, banco e observabilidade

</details>

---

## FC-131 — Chave de partição do DynamoDB

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito Chave de partição do DynamoDB costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** DynamoDB distribui itens pela chave de partição; poucas chaves populares concentram capacidade. Alta cardinalidade e sharding espalham as requisições.

**Como criança:** Se todos entrarem pela mesma porta, forma fila; várias portas bem escolhidas distribuem a turma.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. On-demand ajusta capacidade, mas não elimina todos os efeitos de uma hot partition. O modelo deve começar pelos padrões de acesso, não por normalização relacional.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e modelagem de chaves

</details>

---

## FC-132 — Chave de partição do DynamoDB

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente Chave de partição do DynamoDB?

<details>
<summary>Ver verso</summary>

**Técnico:** Escolher uma chave de alta cardinalidade que distribua acessos, usando write sharding quando necessário, e manter padrões de consulta com índices adequados.

**Como criança:** Se todos entrarem pela mesma porta, forma fila; várias portas bem escolhidas distribuem a turma.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e modelagem de chaves

</details>

---

## FC-133 — Chave de partição do DynamoDB

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar Chave de partição do DynamoDB?

<details>
<summary>Ver verso</summary>

**Técnico:** On-demand ajusta capacidade, mas não elimina todos os efeitos de uma hot partition. O modelo deve começar pelos padrões de acesso, não por normalização relacional.

**Como criança:** Se todos entrarem pela mesma porta, forma fila; várias portas bem escolhidas distribuem a turma.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e modelagem de chaves

</details>

---

## FC-134 — Chave de partição do DynamoDB

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve Chave de partição do DynamoDB: “Manter o país como única chave e aumentar o tamanho de uma instância DynamoDB.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** DynamoDB é serverless e não expõe tamanho de instância; a chave quente continua problemática.

**Como criança:** Se todos entrarem pela mesma porta, forma fila; várias portas bem escolhidas distribuem a turma.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e modelagem de chaves

</details>

---

## FC-135 — Chave de partição do DynamoDB

> **Domínio:** D3

**Frente:** Ensine — Explique Chave de partição do DynamoDB em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** DynamoDB distribui itens pela chave de partição; poucas chaves populares concentram capacidade. Alta cardinalidade e sharding espalham as requisições.

**Como criança:** Se todos entrarem pela mesma porta, forma fila; várias portas bem escolhidas distribuem a turma.

**Pegadinha:** Mnemônica: conecte “Chave de partição do DynamoDB” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e modelagem de chaves

</details>

---

## FC-136 — Read replicas para escalar leituras

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito Read replicas para escalar leituras costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Read replicas usam replicação assíncrona para retirar consultas de leitura do primário; a tolerância a defasagem torna a solução adequada.

**Como criança:** Uma cópia recente do livro fica com a turma de relatórios, enquanto o original continua livre para registrar vendas.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Read replica não substitui Multi-AZ para failover síncrono. A aplicação precisa separar endpoints e aceitar eventual consistency nas leituras.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

**Prática:** ../labs/README.md — RDS Multi-AZ e read replica

</details>

---

## FC-137 — Read replicas para escalar leituras

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente Read replicas para escalar leituras?

<details>
<summary>Ver verso</summary>

**Técnico:** Criar read replicas e direcionar consultas de relatório aos endpoints de leitura, monitorando replication lag.

**Como criança:** Uma cópia recente do livro fica com a turma de relatórios, enquanto o original continua livre para registrar vendas.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

**Prática:** ../labs/README.md — RDS Multi-AZ e read replica

</details>

---

## FC-138 — Read replicas para escalar leituras

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar Read replicas para escalar leituras?

<details>
<summary>Ver verso</summary>

**Técnico:** Read replica não substitui Multi-AZ para failover síncrono. A aplicação precisa separar endpoints e aceitar eventual consistency nas leituras.

**Como criança:** Uma cópia recente do livro fica com a turma de relatórios, enquanto o original continua livre para registrar vendas.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

**Prática:** ../labs/README.md — RDS Multi-AZ e read replica

</details>

---

## FC-139 — Read replicas para escalar leituras

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve Read replicas para escalar leituras: “Usar o standby Multi-AZ diretamente para todas as consultas de relatório.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Na implantação Multi-AZ tradicional, o standby não é endpoint de leitura da aplicação.

**Como criança:** Uma cópia recente do livro fica com a turma de relatórios, enquanto o original continua livre para registrar vendas.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

**Prática:** ../labs/README.md — RDS Multi-AZ e read replica

</details>

---

## FC-140 — Read replicas para escalar leituras

> **Domínio:** D3

**Frente:** Ensine — Explique Read replicas para escalar leituras em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Read replicas usam replicação assíncrona para retirar consultas de leitura do primário; a tolerância a defasagem torna a solução adequada.

**Como criança:** Uma cópia recente do livro fica com a turma de relatórios, enquanto o original continua livre para registrar vendas.

**Pegadinha:** Mnemônica: conecte “Read replicas para escalar leituras” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

**Prática:** ../labs/README.md — RDS Multi-AZ e read replica

</details>

---

## FC-141 — Tipos de volume EBS

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito Tipos de volume EBS costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** io2 é SSD de Provisioned IOPS para workloads críticos que precisam de desempenho consistente e alta durabilidade.

**Como criança:** É uma pista expressa com número de faixas reservado, em vez de torcer para a rua comum estar vazia.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. gp3 é excelente padrão custo/desempenho e permite provisionar IOPS/throughput, mas io2 atende os requisitos mais rigorosos. st1/sc1 são HDD para acesso sequencial e não podem ser boot volume.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

**Prática:** ../labs/README.md — EC2, EBS e teste de I/O

</details>

---

## FC-142 — Tipos de volume EBS

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente Tipos de volume EBS?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar EBS io2, dimensionando IOPS e throughput conforme a instância e a carga, e validar limites ponta a ponta.

**Como criança:** É uma pista expressa com número de faixas reservado, em vez de torcer para a rua comum estar vazia.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

**Prática:** ../labs/README.md — EC2, EBS e teste de I/O

</details>

---

## FC-143 — Tipos de volume EBS

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar Tipos de volume EBS?

<details>
<summary>Ver verso</summary>

**Técnico:** gp3 é excelente padrão custo/desempenho e permite provisionar IOPS/throughput, mas io2 atende os requisitos mais rigorosos. st1/sc1 são HDD para acesso sequencial e não podem ser boot volume.

**Como criança:** É uma pista expressa com número de faixas reservado, em vez de torcer para a rua comum estar vazia.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

**Prática:** ../labs/README.md — EC2, EBS e teste de I/O

</details>

---

## FC-144 — Tipos de volume EBS

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve Tipos de volume EBS: “Usar sc1 porque é o volume com menor latência para bancos críticos.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** sc1 é HDD de baixo custo para acesso pouco frequente e não oferece latência SSD.

**Como criança:** É uma pista expressa com número de faixas reservado, em vez de torcer para a rua comum estar vazia.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

**Prática:** ../labs/README.md — EC2, EBS e teste de I/O

</details>

---

## FC-145 — Tipos de volume EBS

> **Domínio:** D3

**Frente:** Ensine — Explique Tipos de volume EBS em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** io2 é SSD de Provisioned IOPS para workloads críticos que precisam de desempenho consistente e alta durabilidade.

**Como criança:** É uma pista expressa com número de faixas reservado, em vez de torcer para a rua comum estar vazia.

**Pegadinha:** Mnemônica: conecte “Tipos de volume EBS” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

**Prática:** ../labs/README.md — EC2, EBS e teste de I/O

</details>

---

## FC-146 — Transferência para Amazon S3

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito Transferência para Amazon S3 costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Multipart divide o objeto, permite upload paralelo e repetição de partes; Transfer Acceleration usa a rede global da AWS a partir da borda.

**Como criança:** Um caminhão enorme vira várias caixas; se uma cai, reenviamos só aquela, e elas entram pela garagem mais próxima.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Transfer Acceleration tem custo adicional e benefício dependente da rota; deve ser testado. Para migração offline massiva, Snowball pode ser mais apropriado.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

**Prática:** ../labs/README.md — S3, multipart e desempenho

</details>

---

## FC-147 — Transferência para Amazon S3

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente Transferência para Amazon S3?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar S3 multipart upload e avaliar S3 Transfer Acceleration para ingressar pela edge location mais próxima.

**Como criança:** Um caminhão enorme vira várias caixas; se uma cai, reenviamos só aquela, e elas entram pela garagem mais próxima.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

**Prática:** ../labs/README.md — S3, multipart e desempenho

</details>

---

## FC-148 — Transferência para Amazon S3

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar Transferência para Amazon S3?

<details>
<summary>Ver verso</summary>

**Técnico:** Transfer Acceleration tem custo adicional e benefício dependente da rota; deve ser testado. Para migração offline massiva, Snowball pode ser mais apropriado.

**Como criança:** Um caminhão enorme vira várias caixas; se uma cai, reenviamos só aquela, e elas entram pela garagem mais próxima.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

**Prática:** ../labs/README.md — S3, multipart e desempenho

</details>

---

## FC-149 — Transferência para Amazon S3

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve Transferência para Amazon S3: “Enviar cada arquivo em uma única requisição e reiniciar tudo em qualquer falha.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Isso perde paralelismo e torna falhas caras em objetos grandes.

**Como criança:** Um caminhão enorme vira várias caixas; se uma cai, reenviamos só aquela, e elas entram pela garagem mais próxima.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

**Prática:** ../labs/README.md — S3, multipart e desempenho

</details>

---

## FC-150 — Transferência para Amazon S3

> **Domínio:** D3

**Frente:** Ensine — Explique Transferência para Amazon S3 em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Multipart divide o objeto, permite upload paralelo e repetição de partes; Transfer Acceleration usa a rede global da AWS a partir da borda.

**Como criança:** Um caminhão enorme vira várias caixas; se uma cai, reenviamos só aquela, e elas entram pela garagem mais próxima.

**Pegadinha:** Mnemônica: conecte “Transferência para Amazon S3” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

**Prática:** ../labs/README.md — S3, multipart e desempenho

</details>

---

## FC-151 — AWS Global Accelerator

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito AWS Global Accelerator costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Global Accelerator fornece IPs anycast estáticos, leva tráfego TCP/UDP pela borda à rede global e muda endpoints conforme saúde e políticas.

**Como criança:** Todos usam o mesmo endereço de portão; por dentro, uma estrada rápida leva cada jogador ao parque saudável mais próximo.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. CloudFront é ideal para HTTP(S) cacheável e também pode acelerar conteúdo dinâmico, mas não fornece a mesma proposta para protocolos TCP/UDP genéricos e IPs anycast de entrada.

**Referência oficial:** [https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

**Prática:** ../labs/README.md — Roteamento global e failover

</details>

---

## FC-152 — AWS Global Accelerator

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente AWS Global Accelerator?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar AWS Global Accelerator com endpoint groups regionais e health checks.

**Como criança:** Todos usam o mesmo endereço de portão; por dentro, uma estrada rápida leva cada jogador ao parque saudável mais próximo.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

**Prática:** ../labs/README.md — Roteamento global e failover

</details>

---

## FC-153 — AWS Global Accelerator

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar AWS Global Accelerator?

<details>
<summary>Ver verso</summary>

**Técnico:** CloudFront é ideal para HTTP(S) cacheável e também pode acelerar conteúdo dinâmico, mas não fornece a mesma proposta para protocolos TCP/UDP genéricos e IPs anycast de entrada.

**Como criança:** Todos usam o mesmo endereço de portão; por dentro, uma estrada rápida leva cada jogador ao parque saudável mais próximo.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

**Prática:** ../labs/README.md — Roteamento global e failover

</details>

---

## FC-154 — AWS Global Accelerator

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve AWS Global Accelerator: “Usar CloudFront para armazenar pacotes UDP de sessão em cache.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** CloudFront não é cache genérico para UDP.

**Como criança:** Todos usam o mesmo endereço de portão; por dentro, uma estrada rápida leva cada jogador ao parque saudável mais próximo.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

**Prática:** ../labs/README.md — Roteamento global e failover

</details>

---

## FC-155 — AWS Global Accelerator

> **Domínio:** D3

**Frente:** Ensine — Explique AWS Global Accelerator em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Global Accelerator fornece IPs anycast estáticos, leva tráfego TCP/UDP pela borda à rede global e muda endpoints conforme saúde e políticas.

**Como criança:** Todos usam o mesmo endereço de portão; por dentro, uma estrada rápida leva cada jogador ao parque saudável mais próximo.

**Pegadinha:** Mnemônica: conecte “AWS Global Accelerator” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

**Prática:** ../labs/README.md — Roteamento global e failover

</details>

---

## FC-156 — FSx for Lustre

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito FSx for Lustre costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** FSx for Lustre é um sistema de arquivos paralelo de alto desempenho integrado ao S3, adequado a HPC, ML e processamento massivo.

**Como criança:** Mil cozinheiros abrem gavetas de uma despensa super-rápida ao mesmo tempo, e os pratos prontos voltam ao armazém.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Scratch oferece custo menor para dados temporários sem replicação durável; Persistent atende workloads mais longos. O S3 continua sendo a fonte/repositório durável quando desenhado assim.

**Referência oficial:** [https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)

**Prática:** ../labs/README.md — Armazenamento de alto desempenho

</details>

---

## FC-157 — FSx for Lustre

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente FSx for Lustre?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar Amazon FSx for Lustre vinculado ao repositório de dados S3 e escolher deployment type/capacidade adequados.

**Como criança:** Mil cozinheiros abrem gavetas de uma despensa super-rápida ao mesmo tempo, e os pratos prontos voltam ao armazém.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)

**Prática:** ../labs/README.md — Armazenamento de alto desempenho

</details>

---

## FC-158 — FSx for Lustre

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar FSx for Lustre?

<details>
<summary>Ver verso</summary>

**Técnico:** Scratch oferece custo menor para dados temporários sem replicação durável; Persistent atende workloads mais longos. O S3 continua sendo a fonte/repositório durável quando desenhado assim.

**Como criança:** Mil cozinheiros abrem gavetas de uma despensa super-rápida ao mesmo tempo, e os pratos prontos voltam ao armazém.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)

**Prática:** ../labs/README.md — Armazenamento de alto desempenho

</details>

---

## FC-159 — FSx for Lustre

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve FSx for Lustre: “Usar um único volume gp2 pequeno compartilhado por todas as instâncias em regiões diferentes.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** EBS é zonal, e esse desenho não fornece sistema de arquivos paralelo ou throughput agregado.

**Como criança:** Mil cozinheiros abrem gavetas de uma despensa super-rápida ao mesmo tempo, e os pratos prontos voltam ao armazém.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)

**Prática:** ../labs/README.md — Armazenamento de alto desempenho

</details>

---

## FC-160 — FSx for Lustre

> **Domínio:** D3

**Frente:** Ensine — Explique FSx for Lustre em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** FSx for Lustre é um sistema de arquivos paralelo de alto desempenho integrado ao S3, adequado a HPC, ML e processamento massivo.

**Como criança:** Mil cozinheiros abrem gavetas de uma despensa super-rápida ao mesmo tempo, e os pratos prontos voltam ao armazém.

**Pegadinha:** Mnemônica: conecte “FSx for Lustre” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)

**Prática:** ../labs/README.md — Armazenamento de alto desempenho

</details>

---

## FC-161 — Amazon Kinesis Data Streams

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito Amazon Kinesis Data Streams costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Kinesis mantém registros ordenados por shard/partition key, permite múltiplos consumidores e replay durante o período de retenção.

**Como criança:** Cada sensor põe bilhetes numa esteira própria; várias equipes podem reler a sequência enquanto ela ainda está guardada.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Uma partition key muito concentrada cria hot shard. SQS é excelente para filas de trabalho, mas normalmente cada mensagem é consumida como tarefa e não oferece o mesmo modelo de stream/replay.

**Referência oficial:** [https://docs.aws.amazon.com/streams/latest/dev/introduction.html](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

**Prática:** ../labs/README.md — Streaming e processamento de eventos

</details>

---

## FC-162 — Amazon Kinesis Data Streams

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente Amazon Kinesis Data Streams?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar Kinesis Data Streams, com device ID como partition key, capacidade dimensionada/on-demand e consumidores apropriados.

**Como criança:** Cada sensor põe bilhetes numa esteira própria; várias equipes podem reler a sequência enquanto ela ainda está guardada.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/streams/latest/dev/introduction.html](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

**Prática:** ../labs/README.md — Streaming e processamento de eventos

</details>

---

## FC-163 — Amazon Kinesis Data Streams

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar Amazon Kinesis Data Streams?

<details>
<summary>Ver verso</summary>

**Técnico:** Uma partition key muito concentrada cria hot shard. SQS é excelente para filas de trabalho, mas normalmente cada mensagem é consumida como tarefa e não oferece o mesmo modelo de stream/replay.

**Como criança:** Cada sensor põe bilhetes numa esteira própria; várias equipes podem reler a sequência enquanto ela ainda está guardada.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/streams/latest/dev/introduction.html](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

**Prática:** ../labs/README.md — Streaming e processamento de eventos

</details>

---

## FC-164 — Amazon Kinesis Data Streams

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve Amazon Kinesis Data Streams: “Usar uma única fila SQS e esperar que todos os consumidores recebam cada evento e possam reler a sequência.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Uma fila distribui trabalho; fan-out e replay ordenado exigiriam outro desenho.

**Como criança:** Cada sensor põe bilhetes numa esteira própria; várias equipes podem reler a sequência enquanto ela ainda está guardada.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/streams/latest/dev/introduction.html](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

**Prática:** ../labs/README.md — Streaming e processamento de eventos

</details>

---

## FC-165 — Amazon Kinesis Data Streams

> **Domínio:** D3

**Frente:** Ensine — Explique Amazon Kinesis Data Streams em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Kinesis mantém registros ordenados por shard/partition key, permite múltiplos consumidores e replay durante o período de retenção.

**Como criança:** Cada sensor põe bilhetes numa esteira própria; várias equipes podem reler a sequência enquanto ela ainda está guardada.

**Pegadinha:** Mnemônica: conecte “Amazon Kinesis Data Streams” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/streams/latest/dev/introduction.html](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

**Prática:** ../labs/README.md — Streaming e processamento de eventos

</details>

---

## FC-166 — Políticas de Auto Scaling

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito Políticas de Auto Scaling costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Target tracking ajusta capacidade para manter a métrica perto do alvo e gerencia os alarmes subjacentes, reduzindo lógica manual.

**Como criança:** O gerente abre caixas até cada caixa ter mais ou menos a fila combinada e fecha os extras quando o movimento cai.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Step scaling é útil quando a resposta precisa variar por faixas; scheduled/predictive scaling ajuda cargas previsíveis. Cooldown e warmup evitam oscilações.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)

**Prática:** ../labs/README.md — ALB, Auto Scaling e health checks

</details>

---

## FC-167 — Políticas de Auto Scaling

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente Políticas de Auto Scaling?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar target tracking no Auto Scaling com ALBRequestCountPerTarget definido para o valor desejado e warmup apropriado.

**Como criança:** O gerente abre caixas até cada caixa ter mais ou menos a fila combinada e fecha os extras quando o movimento cai.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)

**Prática:** ../labs/README.md — ALB, Auto Scaling e health checks

</details>

---

## FC-168 — Políticas de Auto Scaling

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar Políticas de Auto Scaling?

<details>
<summary>Ver verso</summary>

**Técnico:** Step scaling é útil quando a resposta precisa variar por faixas; scheduled/predictive scaling ajuda cargas previsíveis. Cooldown e warmup evitam oscilações.

**Como criança:** O gerente abre caixas até cada caixa ter mais ou menos a fila combinada e fecha os extras quando o movimento cai.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)

**Prática:** ../labs/README.md — ALB, Auto Scaling e health checks

</details>

---

## FC-169 — Políticas de Auto Scaling

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve Políticas de Auto Scaling: “Usar somente scheduled scaling para uma carga totalmente imprevisível.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Agendamento depende de horários conhecidos e não reage bem a rajadas imprevisíveis.

**Como criança:** O gerente abre caixas até cada caixa ter mais ou menos a fila combinada e fecha os extras quando o movimento cai.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)

**Prática:** ../labs/README.md — ALB, Auto Scaling e health checks

</details>

---

## FC-170 — Políticas de Auto Scaling

> **Domínio:** D3

**Frente:** Ensine — Explique Políticas de Auto Scaling em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Target tracking ajusta capacidade para manter a métrica perto do alvo e gerencia os alarmes subjacentes, reduzindo lógica manual.

**Como criança:** O gerente abre caixas até cada caixa ter mais ou menos a fila combinada e fecha os extras quando o movimento cai.

**Pegadinha:** Mnemônica: conecte “Políticas de Auto Scaling” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)

**Prática:** ../labs/README.md — ALB, Auto Scaling e health checks

</details>

---

## FC-171 — Lambda provisioned concurrency

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito Lambda provisioned concurrency costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Provisioned concurrency mantém ambientes inicializados e prontos, reduzindo cold starts para invocações atendidas pela capacidade provisionada.

**Como criança:** Os cozinheiros ficam de avental e panela quente antes do primeiro pedido, em vez de abrir a cozinha do zero.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Provisioned concurrency gera custo enquanto alocada; para cargas tolerantes a cold start, memória maior, código otimizado ou SnapStart em runtimes compatíveis podem ser melhores.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e desempenho

</details>

---

## FC-172 — Lambda provisioned concurrency

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente Lambda provisioned concurrency?

<details>
<summary>Ver verso</summary>

**Técnico:** Configurar provisioned concurrency no alias/versão e, se adequado, escalá-la por agenda ou Application Auto Scaling.

**Como criança:** Os cozinheiros ficam de avental e panela quente antes do primeiro pedido, em vez de abrir a cozinha do zero.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e desempenho

</details>

---

## FC-173 — Lambda provisioned concurrency

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar Lambda provisioned concurrency?

<details>
<summary>Ver verso</summary>

**Técnico:** Provisioned concurrency gera custo enquanto alocada; para cargas tolerantes a cold start, memória maior, código otimizado ou SnapStart em runtimes compatíveis podem ser melhores.

**Como criança:** Os cozinheiros ficam de avental e panela quente antes do primeiro pedido, em vez de abrir a cozinha do zero.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e desempenho

</details>

---

## FC-174 — Lambda provisioned concurrency

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve Lambda provisioned concurrency: “Aumentar o timeout e assumir que isso inicializa a função antes da chamada.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Timeout limita duração após invocação; não pré-inicializa ambientes.

**Como criança:** Os cozinheiros ficam de avental e panela quente antes do primeiro pedido, em vez de abrir a cozinha do zero.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e desempenho

</details>

---

## FC-175 — Lambda provisioned concurrency

> **Domínio:** D3

**Frente:** Ensine — Explique Lambda provisioned concurrency em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Provisioned concurrency mantém ambientes inicializados e prontos, reduzindo cold starts para invocações atendidas pela capacidade provisionada.

**Como criança:** Os cozinheiros ficam de avental e panela quente antes do primeiro pedido, em vez de abrir a cozinha do zero.

**Pegadinha:** Mnemônica: conecte “Lambda provisioned concurrency” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e desempenho

</details>

---

## FC-176 — Athena, partições e formato colunar

> **Domínio:** D3

**Frente:** Decisão — Em qual requisito Athena, partições e formato colunar costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Formatos colunares leem apenas colunas necessárias; partições permitem ignorar diretórios inteiros, reduzindo I/O, latência e custo por dados examinados.

**Como criança:** Em vez de ler todos os cadernos, organizamos gavetas por dia e guardamos cada assunto em colunas fáceis de pegar.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Partições demais e arquivos minúsculos também prejudicam desempenho. Compactação e tamanho de arquivo devem ser equilibrados com paralelismo.

**Referência oficial:** [https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html)

**Prática:** ../labs/README.md — Data lake no S3 e consultas Athena

</details>

---

## FC-177 — Athena, partições e formato colunar

> **Domínio:** D3

**Frente:** Solução — Qual implementação resume corretamente Athena, partições e formato colunar?

<details>
<summary>Ver verso</summary>

**Técnico:** Converter dados para Parquet/ORC comprimido, particionar por campos usados em filtros e garantir partition pruning/projection nas consultas.

**Como criança:** Em vez de ler todos os cadernos, organizamos gavetas por dia e guardamos cada assunto em colunas fáceis de pegar.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html)

**Prática:** ../labs/README.md — Data lake no S3 e consultas Athena

</details>

---

## FC-178 — Athena, partições e formato colunar

> **Domínio:** D3

**Frente:** Trade-off — O que precisa ser lembrado ao usar Athena, partições e formato colunar?

<details>
<summary>Ver verso</summary>

**Técnico:** Partições demais e arquivos minúsculos também prejudicam desempenho. Compactação e tamanho de arquivo devem ser equilibrados com paralelismo.

**Como criança:** Em vez de ler todos os cadernos, organizamos gavetas por dia e guardamos cada assunto em colunas fáceis de pegar.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html)

**Prática:** ../labs/README.md — Data lake no S3 e consultas Athena

</details>

---

## FC-179 — Athena, partições e formato colunar

> **Domínio:** D3

**Frente:** Pegadinha — Por que esta alternativa não resolve Athena, partições e formato colunar: “Renomear JSON para .parquet sem transformar o conteúdo.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** A extensão não muda o formato físico nem habilita leitura colunar.

**Como criança:** Em vez de ler todos os cadernos, organizamos gavetas por dia e guardamos cada assunto em colunas fáceis de pegar.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html)

**Prática:** ../labs/README.md — Data lake no S3 e consultas Athena

</details>

---

## FC-180 — Athena, partições e formato colunar

> **Domínio:** D3

**Frente:** Ensine — Explique Athena, partições e formato colunar em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Formatos colunares leem apenas colunas necessárias; partições permitem ignorar diretórios inteiros, reduzindo I/O, latência e custo por dados examinados.

**Como criança:** Em vez de ler todos os cadernos, organizamos gavetas por dia e guardamos cada assunto em colunas fáceis de pegar.

**Pegadinha:** Mnemônica: conecte “Athena, partições e formato colunar” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html)

**Prática:** ../labs/README.md — Data lake no S3 e consultas Athena

</details>

---

## FC-181 — S3 Lifecycle

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito S3 Lifecycle costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Lifecycle automatiza transições e expiração por idade; a seleção deve considerar duração mínima, custo de recuperação e latência de cada classe.

**Como criança:** Caixas novas ficam na prateleira perto; depois vão ao depósito barato e, no prazo certo, são recicladas.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Glacier Flexible Retrieval/Deep Archive reduzem armazenamento, mas cobram recuperação e não servem a acesso imediato. Transições muito precoces podem gerar cobranças mínimas.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

**Prática:** ../labs/README.md — S3, lifecycle e otimização de custos

</details>

---

## FC-182 — S3 Lifecycle

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente S3 Lifecycle?

<details>
<summary>Ver verso</summary>

**Técnico:** Criar S3 Lifecycle para transicionar objetos às classes adequadas ao padrão de acesso e expirá-los somente após o prazo regulatório.

**Como criança:** Caixas novas ficam na prateleira perto; depois vão ao depósito barato e, no prazo certo, são recicladas.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

**Prática:** ../labs/README.md — S3, lifecycle e otimização de custos

</details>

---

## FC-183 — S3 Lifecycle

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar S3 Lifecycle?

<details>
<summary>Ver verso</summary>

**Técnico:** Glacier Flexible Retrieval/Deep Archive reduzem armazenamento, mas cobram recuperação e não servem a acesso imediato. Transições muito precoces podem gerar cobranças mínimas.

**Como criança:** Caixas novas ficam na prateleira perto; depois vão ao depósito barato e, no prazo certo, são recicladas.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

**Prática:** ../labs/README.md — S3, lifecycle e otimização de custos

</details>

---

## FC-184 — S3 Lifecycle

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve S3 Lifecycle: “Manter tudo em S3 Standard para sempre porque todas as classes têm o mesmo preço.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** As classes têm preços e características diferentes; o padrão conhecido permite economizar.

**Como criança:** Caixas novas ficam na prateleira perto; depois vão ao depósito barato e, no prazo certo, são recicladas.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

**Prática:** ../labs/README.md — S3, lifecycle e otimização de custos

</details>

---

## FC-185 — S3 Lifecycle

> **Domínio:** D4

**Frente:** Ensine — Explique S3 Lifecycle em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Lifecycle automatiza transições e expiração por idade; a seleção deve considerar duração mínima, custo de recuperação e latência de cada classe.

**Como criança:** Caixas novas ficam na prateleira perto; depois vão ao depósito barato e, no prazo certo, são recicladas.

**Pegadinha:** Mnemônica: conecte “S3 Lifecycle” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

**Prática:** ../labs/README.md — S3, lifecycle e otimização de custos

</details>

---

## FC-186 — Savings Plans e Spot

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito Savings Plans e Spot costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Savings Plans descontam uso comprometido de compute; Spot aproveita capacidade excedente com grande desconto para workloads interrompíveis.

**Como criança:** Assinamos um passe barato para a viagem diária e compramos lugares promocionais para passeios que podem esperar.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Não se deve comprometer acima da base bem conhecida. Spot precisa checkpoints, múltiplos tipos/AZs e resposta ao interruption notice.

**Referência oficial:** [https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)

**Prática:** ../labs/README.md — Auto Scaling com On-Demand, Savings Plans e Spot

</details>

---

## FC-187 — Savings Plans e Spot

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente Savings Plans e Spot?

<details>
<summary>Ver verso</summary>

**Técnico:** Cobrir a base previsível com Savings Plans e executar a capacidade batch flexível em Spot, com diversificação e tratamento de interrupções.

**Como criança:** Assinamos um passe barato para a viagem diária e compramos lugares promocionais para passeios que podem esperar.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)

**Prática:** ../labs/README.md — Auto Scaling com On-Demand, Savings Plans e Spot

</details>

---

## FC-188 — Savings Plans e Spot

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar Savings Plans e Spot?

<details>
<summary>Ver verso</summary>

**Técnico:** Não se deve comprometer acima da base bem conhecida. Spot precisa checkpoints, múltiplos tipos/AZs e resposta ao interruption notice.

**Como criança:** Assinamos um passe barato para a viagem diária e compramos lugares promocionais para passeios que podem esperar.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)

**Prática:** ../labs/README.md — Auto Scaling com On-Demand, Savings Plans e Spot

</details>

---

## FC-189 — Savings Plans e Spot

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve Savings Plans e Spot: “Executar toda a base crítica apenas em uma única Spot Instance sem checkpoint.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Interrupções podem remover toda a capacidade crítica.

**Como criança:** Assinamos um passe barato para a viagem diária e compramos lugares promocionais para passeios que podem esperar.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)

**Prática:** ../labs/README.md — Auto Scaling com On-Demand, Savings Plans e Spot

</details>

---

## FC-190 — Savings Plans e Spot

> **Domínio:** D4

**Frente:** Ensine — Explique Savings Plans e Spot em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Savings Plans descontam uso comprometido de compute; Spot aproveita capacidade excedente com grande desconto para workloads interrompíveis.

**Como criança:** Assinamos um passe barato para a viagem diária e compramos lugares promocionais para passeios que podem esperar.

**Pegadinha:** Mnemônica: conecte “Savings Plans e Spot” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)

**Prática:** ../labs/README.md — Auto Scaling com On-Demand, Savings Plans e Spot

</details>

---

## FC-191 — RDS Reserved DB Instances

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito RDS Reserved DB Instances costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Reserved DB Instances oferecem desconto de faturamento para uso RDS previsível; não são uma instância física separada e não alteram a arquitetura.

**Como criança:** A mesma mesa é usada todo dia, então um plano anual sai mais barato que pagar diária.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Reserva reduz compute do RDS, mas armazenamento, I/O, backup e transferência podem continuar cobrados. Rightsizing deve vir antes do compromisso.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)

**Prática:** ../labs/README.md — RDS, capacidade e custo

</details>

---

## FC-192 — RDS Reserved DB Instances

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente RDS Reserved DB Instances?

<details>
<summary>Ver verso</summary>

**Técnico:** Adquirir Reserved DB Instance para a configuração/família elegível após validar utilização, prazo e opção de pagamento.

**Como criança:** A mesma mesa é usada todo dia, então um plano anual sai mais barato que pagar diária.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)

**Prática:** ../labs/README.md — RDS, capacidade e custo

</details>

---

## FC-193 — RDS Reserved DB Instances

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar RDS Reserved DB Instances?

<details>
<summary>Ver verso</summary>

**Técnico:** Reserva reduz compute do RDS, mas armazenamento, I/O, backup e transferência podem continuar cobrados. Rightsizing deve vir antes do compromisso.

**Como criança:** A mesma mesa é usada todo dia, então um plano anual sai mais barato que pagar diária.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)

**Prática:** ../labs/README.md — RDS, capacidade e custo

</details>

---

## FC-194 — RDS Reserved DB Instances

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve RDS Reserved DB Instances: “Comprar Spot Instances para substituir diretamente a instância RDS gerenciada.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** RDS não oferece modelo Spot para a instância de banco gerenciada.

**Como criança:** A mesma mesa é usada todo dia, então um plano anual sai mais barato que pagar diária.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)

**Prática:** ../labs/README.md — RDS, capacidade e custo

</details>

---

## FC-195 — RDS Reserved DB Instances

> **Domínio:** D4

**Frente:** Ensine — Explique RDS Reserved DB Instances em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Reserved DB Instances oferecem desconto de faturamento para uso RDS previsível; não são uma instância física separada e não alteram a arquitetura.

**Como criança:** A mesma mesa é usada todo dia, então um plano anual sai mais barato que pagar diária.

**Pegadinha:** Mnemônica: conecte “RDS Reserved DB Instances” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)

**Prática:** ../labs/README.md — RDS, capacidade e custo

</details>

---

## FC-196 — Custo de NAT e VPC endpoints

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito Custo de NAT e VPC endpoints costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** O endpoint de gateway para S3 evita o processamento pelo NAT e não possui cobrança por hora, reduzindo custo e simplificando o caminho privado.

**Como criança:** Abrimos uma porta direta e gratuita para o depósito, então os caminhões não pagam mais o pedágio da estrada geral.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Interface endpoints para outros serviços cobram por hora e dados, então seu custo deve ser comparado ao NAT e ao volume por AZ; alta disponibilidade do NAT também importa.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

</details>

---

## FC-197 — Custo de NAT e VPC endpoints

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente Custo de NAT e VPC endpoints?

<details>
<summary>Ver verso</summary>

**Técnico:** Criar Gateway VPC Endpoint para S3, atualizar route tables/policies e manter o NAT apenas para destinos que realmente exigem internet.

**Como criança:** Abrimos uma porta direta e gratuita para o depósito, então os caminhões não pagam mais o pedágio da estrada geral.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

</details>

---

## FC-198 — Custo de NAT e VPC endpoints

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar Custo de NAT e VPC endpoints?

<details>
<summary>Ver verso</summary>

**Técnico:** Interface endpoints para outros serviços cobram por hora e dados, então seu custo deve ser comparado ao NAT e ao volume por AZ; alta disponibilidade do NAT também importa.

**Como criança:** Abrimos uma porta direta e gratuita para o depósito, então os caminhões não pagam mais o pedágio da estrada geral.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

</details>

---

## FC-199 — Custo de NAT e VPC endpoints

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve Custo de NAT e VPC endpoints: “Adicionar mais NAT Gateways e continuar roteando S3 por todos eles.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Isso pode melhorar resiliência, mas não remove a cobrança de processamento responsável pelo custo.

**Como criança:** Abrimos uma porta direta e gratuita para o depósito, então os caminhões não pagam mais o pedágio da estrada geral.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

</details>

---

## FC-200 — Custo de NAT e VPC endpoints

> **Domínio:** D4

**Frente:** Ensine — Explique Custo de NAT e VPC endpoints em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** O endpoint de gateway para S3 evita o processamento pelo NAT e não possui cobrança por hora, reduzindo custo e simplificando o caminho privado.

**Como criança:** Abrimos uma porta direta e gratuita para o depósito, então os caminhões não pagam mais o pedágio da estrada geral.

**Pegadinha:** Mnemônica: conecte “Custo de NAT e VPC endpoints” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

**Prática:** ../labs/README.md — VPC multi-AZ, NAT e endpoints

</details>

---

## FC-201 — AWS Compute Optimizer

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito AWS Compute Optimizer costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Compute Optimizer analisa métricas e oferece recomendações de tipo/tamanho e risco; a validação em carga real evita reduzir capacidade cegamente.

**Como criança:** Um treinador observa cada atleta e sugere um tênis do tamanho certo, em vez de comprar o maior para todos.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Cost Explorer Rightsizing também ajuda na visão de custo. Recomendações são insumo, não autorização automática: sazonalidade, licenças e limites de rede precisam ser considerados.

**Referência oficial:** [https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

**Prática:** ../labs/README.md — Observabilidade e rightsizing

</details>

---

## FC-202 — AWS Compute Optimizer

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente AWS Compute Optimizer?

<details>
<summary>Ver verso</summary>

**Técnico:** Ativar AWS Compute Optimizer, garantir métricas suficientes (incluindo memória com agente quando necessário) e testar as recomendações de rightsizing.

**Como criança:** Um treinador observa cada atleta e sugere um tênis do tamanho certo, em vez de comprar o maior para todos.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

**Prática:** ../labs/README.md — Observabilidade e rightsizing

</details>

---

## FC-203 — AWS Compute Optimizer

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar AWS Compute Optimizer?

<details>
<summary>Ver verso</summary>

**Técnico:** Cost Explorer Rightsizing também ajuda na visão de custo. Recomendações são insumo, não autorização automática: sazonalidade, licenças e limites de rede precisam ser considerados.

**Como criança:** Um treinador observa cada atleta e sugere um tênis do tamanho certo, em vez de comprar o maior para todos.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

**Prática:** ../labs/README.md — Observabilidade e rightsizing

</details>

---

## FC-204 — AWS Compute Optimizer

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve AWS Compute Optimizer: “Reduzir todas as instâncias para t3.micro sem medir.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Uma regra única ignora CPU, memória, rede, burst e requisitos diferentes.

**Como criança:** Um treinador observa cada atleta e sugere um tênis do tamanho certo, em vez de comprar o maior para todos.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

**Prática:** ../labs/README.md — Observabilidade e rightsizing

</details>

---

## FC-205 — AWS Compute Optimizer

> **Domínio:** D4

**Frente:** Ensine — Explique AWS Compute Optimizer em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Compute Optimizer analisa métricas e oferece recomendações de tipo/tamanho e risco; a validação em carga real evita reduzir capacidade cegamente.

**Como criança:** Um treinador observa cada atleta e sugere um tênis do tamanho certo, em vez de comprar o maior para todos.

**Pegadinha:** Mnemônica: conecte “AWS Compute Optimizer” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

**Prática:** ../labs/README.md — Observabilidade e rightsizing

</details>

---

## FC-206 — Capacidade do DynamoDB

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito Capacidade do DynamoDB costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** On-demand cobra por requisição e ajusta capacidade automaticamente, sendo adequado a cargas novas, variáveis ou intermitentes sem planejamento de throughput.

**Como criança:** Pagamos cada passeio quando alguém chega, sem manter um ônibus vazio esperando o dia inteiro.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Provisioned pode custar menos em uso estável e previsível, especialmente com auto scaling e reserved capacity elegível. Hot keys continuam sendo problema de modelagem.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e capacidade

</details>

---

## FC-207 — Capacidade do DynamoDB

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente Capacidade do DynamoDB?

<details>
<summary>Ver verso</summary>

**Técnico:** Começar com DynamoDB on-demand e, quando o padrão se tornar previsível e sustentado, comparar com provisioned capacity e auto scaling.

**Como criança:** Pagamos cada passeio quando alguém chega, sem manter um ônibus vazio esperando o dia inteiro.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e capacidade

</details>

---

## FC-208 — Capacidade do DynamoDB

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar Capacidade do DynamoDB?

<details>
<summary>Ver verso</summary>

**Técnico:** Provisioned pode custar menos em uso estável e previsível, especialmente com auto scaling e reserved capacity elegível. Hot keys continuam sendo problema de modelagem.

**Como criança:** Pagamos cada passeio quando alguém chega, sem manter um ônibus vazio esperando o dia inteiro.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e capacidade

</details>

---

## FC-209 — Capacidade do DynamoDB

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve Capacidade do DynamoDB: “Provisionar imediatamente o pico teórico máximo 24x7 sem métricas.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Isso tende a pagar capacidade ociosa durante a maior parte do tempo.

**Como criança:** Pagamos cada passeio quando alguém chega, sem manter um ônibus vazio esperando o dia inteiro.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e capacidade

</details>

---

## FC-210 — Capacidade do DynamoDB

> **Domínio:** D4

**Frente:** Ensine — Explique Capacidade do DynamoDB em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** On-demand cobra por requisição e ajusta capacidade automaticamente, sendo adequado a cargas novas, variáveis ou intermitentes sem planejamento de throughput.

**Como criança:** Pagamos cada passeio quando alguém chega, sem manter um ônibus vazio esperando o dia inteiro.

**Pegadinha:** Mnemônica: conecte “Capacidade do DynamoDB” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)

**Prática:** ../labs/README.md — DynamoDB, DAX e capacidade

</details>

---

## FC-211 — Snapshots EBS com Data Lifecycle Manager

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito Snapshots EBS com Data Lifecycle Manager costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** DLM automatiza ciclo de vida de snapshots EBS e AMIs com seleção por tags, eliminando servidor de agendamento e acúmulo indefinido.

**Como criança:** Um robô fotografa os cadernos todo dia e descarta sozinho as fotos que passaram do prazo.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Snapshots são incrementais no armazenamento, mas cada snapshot aparece como ponto completo de restauração. A política precisa respeitar retenção e testes de restore.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)

**Prática:** ../labs/README.md — EBS, snapshots e recuperação

</details>

---

## FC-212 — Snapshots EBS com Data Lifecycle Manager

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente Snapshots EBS com Data Lifecycle Manager?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar Amazon Data Lifecycle Manager com tags para criar e expirar snapshots segundo a política.

**Como criança:** Um robô fotografa os cadernos todo dia e descarta sozinho as fotos que passaram do prazo.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)

**Prática:** ../labs/README.md — EBS, snapshots e recuperação

</details>

---

## FC-213 — Snapshots EBS com Data Lifecycle Manager

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar Snapshots EBS com Data Lifecycle Manager?

<details>
<summary>Ver verso</summary>

**Técnico:** Snapshots são incrementais no armazenamento, mas cada snapshot aparece como ponto completo de restauração. A política precisa respeitar retenção e testes de restore.

**Como criança:** Um robô fotografa os cadernos todo dia e descarta sozinho as fotos que passaram do prazo.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)

**Prática:** ../labs/README.md — EBS, snapshots e recuperação

</details>

---

## FC-214 — Snapshots EBS com Data Lifecycle Manager

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve Snapshots EBS com Data Lifecycle Manager: “Manter todos os snapshots para sempre porque snapshots incrementais não custam.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Blocos exclusivos ainda ocupam armazenamento e retenção infinita gera custo.

**Como criança:** Um robô fotografa os cadernos todo dia e descarta sozinho as fotos que passaram do prazo.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)

**Prática:** ../labs/README.md — EBS, snapshots e recuperação

</details>

---

## FC-215 — Snapshots EBS com Data Lifecycle Manager

> **Domínio:** D4

**Frente:** Ensine — Explique Snapshots EBS com Data Lifecycle Manager em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** DLM automatiza ciclo de vida de snapshots EBS e AMIs com seleção por tags, eliminando servidor de agendamento e acúmulo indefinido.

**Como criança:** Um robô fotografa os cadernos todo dia e descarta sozinho as fotos que passaram do prazo.

**Pegadinha:** Mnemônica: conecte “Snapshots EBS com Data Lifecycle Manager” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)

**Prática:** ../labs/README.md — EBS, snapshots e recuperação

</details>

---

## FC-216 — AWS Budgets e Cost Explorer

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito AWS Budgets e Cost Explorer costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Budgets compara gasto/uso com limites e envia alertas; Cost Explorer permite explorar a composição e a evolução dos custos.

**Como criança:** O alarme avisa que a mesada vai estourar, e a lupa mostra em quais brinquedos o dinheiro foi gasto.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Cost Anomaly Detection complementa com alertas de padrões incomuns. Tags precisam ser ativadas como cost allocation tags e a organização deve manter governança de marcação.

**Referência oficial:** [https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)

**Prática:** ../labs/README.md — Budgets, tags e análise de custos

</details>

---

## FC-217 — AWS Budgets e Cost Explorer

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente AWS Budgets e Cost Explorer?

<details>
<summary>Ver verso</summary>

**Técnico:** Configurar AWS Budgets com alertas de custo previsto/real e usar Cost Explorer para analisar tendências, filtros, grupos e relatórios.

**Como criança:** O alarme avisa que a mesada vai estourar, e a lupa mostra em quais brinquedos o dinheiro foi gasto.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)

**Prática:** ../labs/README.md — Budgets, tags e análise de custos

</details>

---

## FC-218 — AWS Budgets e Cost Explorer

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar AWS Budgets e Cost Explorer?

<details>
<summary>Ver verso</summary>

**Técnico:** Cost Anomaly Detection complementa com alertas de padrões incomuns. Tags precisam ser ativadas como cost allocation tags e a organização deve manter governança de marcação.

**Como criança:** O alarme avisa que a mesada vai estourar, e a lupa mostra em quais brinquedos o dinheiro foi gasto.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)

**Prática:** ../labs/README.md — Budgets, tags e análise de custos

</details>

---

## FC-219 — AWS Budgets e Cost Explorer

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve AWS Budgets e Cost Explorer: “Usar CloudTrail sozinho para calcular a previsão da fatura.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** CloudTrail registra APIs e não é ferramenta de previsão e análise financeira.

**Como criança:** O alarme avisa que a mesada vai estourar, e a lupa mostra em quais brinquedos o dinheiro foi gasto.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)

**Prática:** ../labs/README.md — Budgets, tags e análise de custos

</details>

---

## FC-220 — AWS Budgets e Cost Explorer

> **Domínio:** D4

**Frente:** Ensine — Explique AWS Budgets e Cost Explorer em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Budgets compara gasto/uso com limites e envia alertas; Cost Explorer permite explorar a composição e a evolução dos custos.

**Como criança:** O alarme avisa que a mesada vai estourar, e a lupa mostra em quais brinquedos o dinheiro foi gasto.

**Pegadinha:** Mnemônica: conecte “AWS Budgets e Cost Explorer” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)

**Prática:** ../labs/README.md — Budgets, tags e análise de custos

</details>

---

## FC-221 — S3 Intelligent-Tiering

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito S3 Intelligent-Tiering costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Intelligent-Tiering monitora acesso e move objetos entre tiers automáticos sem cobrança de recuperação nos tiers de acesso frequente/infrequente, cobrando pequena taxa de monitoramento.

**Como criança:** Um bibliotecário observa quais livros são lidos e muda sozinho os pouco usados para estantes mais baratas.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Objetos menores que 128 KB não são monitorados nem movidos automaticamente e permanecem no tier Frequent Access. Archive Access/Deep Archive Access têm recuperação assíncrona e devem ser habilitados conscientemente.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)

**Prática:** ../labs/README.md — S3, lifecycle e classes de armazenamento

</details>

---

## FC-222 — S3 Intelligent-Tiering

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente S3 Intelligent-Tiering?

<details>
<summary>Ver verso</summary>

**Técnico:** Usar S3 Intelligent-Tiering, habilitando tiers de archive opcionais apenas se a latência de recuperação for aceitável.

**Como criança:** Um bibliotecário observa quais livros são lidos e muda sozinho os pouco usados para estantes mais baratas.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)

**Prática:** ../labs/README.md — S3, lifecycle e classes de armazenamento

</details>

---

## FC-223 — S3 Intelligent-Tiering

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar S3 Intelligent-Tiering?

<details>
<summary>Ver verso</summary>

**Técnico:** Objetos menores que 128 KB não são monitorados nem movidos automaticamente e permanecem no tier Frequent Access. Archive Access/Deep Archive Access têm recuperação assíncrona e devem ser habilitados conscientemente.

**Como criança:** Um bibliotecário observa quais livros são lidos e muda sozinho os pouco usados para estantes mais baratas.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)

**Prática:** ../labs/README.md — S3, lifecycle e classes de armazenamento

</details>

---

## FC-224 — S3 Intelligent-Tiering

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve S3 Intelligent-Tiering: “Colocar tudo diretamente em Glacier Deep Archive e exigir leitura imediata.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Deep Archive não oferece recuperação em milissegundos.

**Como criança:** Um bibliotecário observa quais livros são lidos e muda sozinho os pouco usados para estantes mais baratas.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)

**Prática:** ../labs/README.md — S3, lifecycle e classes de armazenamento

</details>

---

## FC-225 — S3 Intelligent-Tiering

> **Domínio:** D4

**Frente:** Ensine — Explique S3 Intelligent-Tiering em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Intelligent-Tiering monitora acesso e move objetos entre tiers automáticos sem cobrança de recuperação nos tiers de acesso frequente/infrequente, cobrando pequena taxa de monitoramento.

**Como criança:** Um bibliotecário observa quais livros são lidos e muda sozinho os pouco usados para estantes mais baratas.

**Pegadinha:** Mnemônica: conecte “S3 Intelligent-Tiering” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)

**Prática:** ../labs/README.md — S3, lifecycle e classes de armazenamento

</details>

---

## FC-226 — Arquitetura serverless para carga esporádica

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito Arquitetura serverless para carga esporádica costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Serviços serverless escalam sob demanda e cobram por requisição/execução, evitando instâncias ociosas para uma carga esporádica.

**Como criança:** A barraca abre e chama ajudantes só quando chegam clientes, em vez de pagar uma equipe vazia o dia inteiro.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Em carga alta e constante, contêineres/instâncias bem utilizados podem custar menos. Cold starts, limites de execução e dependências precisam ser avaliados.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html](https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e IAM roles

</details>

---

## FC-227 — Arquitetura serverless para carga esporádica

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente Arquitetura serverless para carga esporádica?

<details>
<summary>Ver verso</summary>

**Técnico:** API Gateway com Lambda e um armazenamento serverless apropriado, configurando limites, observabilidade e controle de concorrência.

**Como criança:** A barraca abre e chama ajudantes só quando chegam clientes, em vez de pagar uma equipe vazia o dia inteiro.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html](https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e IAM roles

</details>

---

## FC-228 — Arquitetura serverless para carga esporádica

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar Arquitetura serverless para carga esporádica?

<details>
<summary>Ver verso</summary>

**Técnico:** Em carga alta e constante, contêineres/instâncias bem utilizados podem custar menos. Cold starts, limites de execução e dependências precisam ser avaliados.

**Como criança:** A barraca abre e chama ajudantes só quando chegam clientes, em vez de pagar uma equipe vazia o dia inteiro.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html](https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e IAM roles

</details>

---

## FC-229 — Arquitetura serverless para carga esporádica

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve Arquitetura serverless para carga esporádica: “Manter dez instâncias On-Demand grandes 24x7 para o pico raro.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** A maior parte da capacidade ficaria ociosa e paga.

**Como criança:** A barraca abre e chama ajudantes só quando chegam clientes, em vez de pagar uma equipe vazia o dia inteiro.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html](https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e IAM roles

</details>

---

## FC-230 — Arquitetura serverless para carga esporádica

> **Domínio:** D4

**Frente:** Ensine — Explique Arquitetura serverless para carga esporádica em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Serviços serverless escalam sob demanda e cobram por requisição/execução, evitando instâncias ociosas para uma carga esporádica.

**Como criança:** A barraca abre e chama ajudantes só quando chegam clientes, em vez de pagar uma equipe vazia o dia inteiro.

**Pegadinha:** Mnemônica: conecte “Arquitetura serverless para carga esporádica” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html](https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html)

**Prática:** ../labs/README.md — Lambda, API Gateway e IAM roles

</details>

---

## FC-231 — Consolidated billing e compartilhamento de descontos

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito Consolidated billing e compartilhamento de descontos costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** Organizations consolida cobrança e permite que uso agregado e compartilhamento elegível de descontos melhorem aproveitamento, além de centralizar relatórios.

**Como criança:** A família junta todas as compras numa conta só e aproveita melhor o cartão de desconto do supermercado.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Consolidar não elimina a necessidade de chargeback/showback. Savings Plans/RI sharing pode ser configurado e políticas organizacionais não concedem permissões automaticamente.

**Referência oficial:** [https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)

**Prática:** ../labs/README.md — FinOps multi-conta e alocação de custos

</details>

---

## FC-232 — Consolidated billing e compartilhamento de descontos

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente Consolidated billing e compartilhamento de descontos?

<details>
<summary>Ver verso</summary>

**Técnico:** Gerenciar as contas com AWS Organizations e consolidated billing, estruturando OUs, tags e controles de compartilhamento de descontos.

**Como criança:** A família junta todas as compras numa conta só e aproveita melhor o cartão de desconto do supermercado.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)

**Prática:** ../labs/README.md — FinOps multi-conta e alocação de custos

</details>

---

## FC-233 — Consolidated billing e compartilhamento de descontos

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar Consolidated billing e compartilhamento de descontos?

<details>
<summary>Ver verso</summary>

**Técnico:** Consolidar não elimina a necessidade de chargeback/showback. Savings Plans/RI sharing pode ser configurado e políticas organizacionais não concedem permissões automaticamente.

**Como criança:** A família junta todas as compras numa conta só e aproveita melhor o cartão de desconto do supermercado.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)

**Prática:** ../labs/README.md — FinOps multi-conta e alocação de custos

</details>

---

## FC-234 — Consolidated billing e compartilhamento de descontos

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve Consolidated billing e compartilhamento de descontos: “Compartilhar a senha do usuário raiz entre todas as equipes.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Isso é inseguro e não cria organização ou faturamento consolidado.

**Como criança:** A família junta todas as compras numa conta só e aproveita melhor o cartão de desconto do supermercado.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)

**Prática:** ../labs/README.md — FinOps multi-conta e alocação de custos

</details>

---

## FC-235 — Consolidated billing e compartilhamento de descontos

> **Domínio:** D4

**Frente:** Ensine — Explique Consolidated billing e compartilhamento de descontos em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** Organizations consolida cobrança e permite que uso agregado e compartilhamento elegível de descontos melhorem aproveitamento, além de centralizar relatórios.

**Como criança:** A família junta todas as compras numa conta só e aproveita melhor o cartão de desconto do supermercado.

**Pegadinha:** Mnemônica: conecte “Consolidated billing e compartilhamento de descontos” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)

**Prática:** ../labs/README.md — FinOps multi-conta e alocação de custos

</details>

---

## FC-236 — EFS lifecycle e Infrequent Access

> **Domínio:** D4

**Frente:** Decisão — Em qual requisito EFS lifecycle e Infrequent Access costuma ser a melhor resposta?

<details>
<summary>Ver verso</summary>

**Técnico:** EFS lifecycle move dados frios para classes mais baratas mantendo o mesmo sistema de arquivos e acesso transparente à aplicação.

**Como criança:** Os brinquedos esquecidos vão para uma prateleira barata, mas continuam no catálogo e voltam quando alguém pede.

**Pegadinha:** Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. Classes IA/Archive têm cobrança de acesso e são melhores para arquivos realmente frios. One Zone reduz custo adicional, mas muda a resiliência e não deve ser escolhido sem aceitar risco de AZ.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)

**Prática:** ../labs/README.md — EFS, classes e custo

</details>

---

## FC-237 — EFS lifecycle e Infrequent Access

> **Domínio:** D4

**Frente:** Solução — Qual implementação resume corretamente EFS lifecycle e Infrequent Access?

<details>
<summary>Ver verso</summary>

**Técnico:** Configurar EFS lifecycle management para mover arquivos não acessados a IA/Archive conforme elegibilidade e, se adequado, voltar ao Standard no primeiro acesso.

**Como criança:** Os brinquedos esquecidos vão para uma prateleira barata, mas continuam no catálogo e voltam quando alguém pede.

**Pegadinha:** A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)

**Prática:** ../labs/README.md — EFS, classes e custo

</details>

---

## FC-238 — EFS lifecycle e Infrequent Access

> **Domínio:** D4

**Frente:** Trade-off — O que precisa ser lembrado ao usar EFS lifecycle e Infrequent Access?

<details>
<summary>Ver verso</summary>

**Técnico:** Classes IA/Archive têm cobrança de acesso e são melhores para arquivos realmente frios. One Zone reduz custo adicional, mas muda a resiliência e não deve ser escolhido sem aceitar risco de AZ.

**Como criança:** Os brinquedos esquecidos vão para uma prateleira barata, mas continuam no catálogo e voltam quando alguém pede.

**Pegadinha:** Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)

**Prática:** ../labs/README.md — EFS, classes e custo

</details>

---

## FC-239 — EFS lifecycle e Infrequent Access

> **Domínio:** D4

**Frente:** Pegadinha — Por que esta alternativa não resolve EFS lifecycle e Infrequent Access: “Copiar manualmente arquivos para discos locais e apagar o EFS.” ?

<details>
<summary>Ver verso</summary>

**Técnico:** Isso perde compartilhamento, durabilidade e automação do namespace existente.

**Como criança:** Os brinquedos esquecidos vão para uma prateleira barata, mas continuam no catálogo e voltam quando alguém pede.

**Pegadinha:** Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)

**Prática:** ../labs/README.md — EFS, classes e custo

</details>

---

## FC-240 — EFS lifecycle e Infrequent Access

> **Domínio:** D4

**Frente:** Ensine — Explique EFS lifecycle e Infrequent Access em linguagem simples e depois dê a justificativa técnica.

<details>
<summary>Ver verso</summary>

**Técnico:** EFS lifecycle move dados frios para classes mais baratas mantendo o mesmo sistema de arquivos e acesso transparente à aplicação.

**Como criança:** Os brinquedos esquecidos vão para uma prateleira barata, mas continuam no catálogo e voltam quando alguém pede.

**Pegadinha:** Mnemônica: conecte “EFS lifecycle e Infrequent Access” à imagem da analogia infantil.

**Referência oficial:** [https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)

**Prática:** ../labs/README.md — EFS, classes e custo

</details>

---
