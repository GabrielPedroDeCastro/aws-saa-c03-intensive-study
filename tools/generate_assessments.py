#!/usr/bin/env python3
"""Gera, de forma deterministica, todo o conteudo avaliativo autoral do projeto.

Saidas canonicas:
* 40 mini-quizzes (10 por dominio, 5 questoes cada) em JSON e Markdown;
* banco agregado de 200 questoes;
* diagnostico de 40 questoes;
* 3 simulados de 65 questoes;
* 240 flashcards em JSON e Markdown.

O catalogo abaixo foi escrito especificamente para este projeto. Ele nao usa nem
reproduz dumps de prova. A geracao apenas combina contextos autorais, alterna a
ordem das opcoes e materializa formatos de consumo diferentes.
"""

from __future__ import annotations

import json
import shutil
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUIZZES = ROOT / "quizzes"
SIMULADOS = ROOT / "simulados"
FLASHCARDS = ROOT / "flashcards"

DOMAINS = {
    "D1": {
        "nome": "Domínio 1 — Projetar arquiteturas seguras",
        "peso_oficial_percentual": 30,
        "slug": "dominio-1-seguranca",
    },
    "D2": {
        "nome": "Domínio 2 — Projetar arquiteturas resilientes",
        "peso_oficial_percentual": 26,
        "slug": "dominio-2-resiliencia",
    },
    "D3": {
        "nome": "Domínio 3 — Projetar arquiteturas de alto desempenho",
        "peso_oficial_percentual": 24,
        "slug": "dominio-3-desempenho",
    },
    "D4": {
        "nome": "Domínio 4 — Projetar arquiteturas otimizadas em custos",
        "peso_oficial_percentual": 20,
        "slug": "dominio-4-custos",
    },
}

LETTERS = "ABCD"
DIFFICULTIES = ["média", "fácil", "média", "difícil", "fácil", "média", "média", "difícil", "fácil", "média"]
TIME_BY_DIFFICULTY = {"fácil": 90, "média": 110, "difícil": 130}
POINTS_BY_DIFFICULTY = {"fácil": 1, "média": 2, "difícil": 3}

ORGS = [
    "a fintech Aurora", "a rede hospitalar Horizonte", "a varejista Nuvem Sul",
    "a edtech Farol", "a fabricante Serra Azul", "o marketplace Beija-Flor",
    "a seguradora Atlântico", "a empresa de logística Rota Certa", "a startup Ipê Digital",
    "a cooperativa Campo Vivo", "a plataforma de mídia Onda", "o banco digital Pioneiro",
    "a agência pública Portal Aberto", "a empresa de jogos Capivara", "a rede de hotéis Brisa",
    "a companhia aérea Ventos", "a healthtech Pulso", "a universidade Saber",
    "a empresa de energia Raio", "a plataforma de ingressos Palco", "a indústria Cedro",
    "a empresa de geoprocessamento Mapa Vivo", "a foodtech Panela", "a proptech Janela",
]

CONTEXTS = [
    "está migrando uma carga crítica para a AWS",
    "precisa corrigir uma descoberta da revisão Well-Architected",
    "vai lançar o serviço em três países",
    "opera com uma equipe pequena e quer reduzir tarefas manuais",
    "recebe picos imprevisíveis sem poder degradar o SLA",
    "precisa atender a uma auditoria sem redesenhar toda a aplicação",
    "quer substituir um componente autogerenciado por um serviço gerenciado",
    "está preparando a arquitetura para a próxima campanha anual",
    "deve manter a solução simples para a equipe de plantão",
    "está separando produção e desenvolvimento em contas distintas",
    "precisa tomar uma decisão com base em desempenho, segurança e custo total",
    "está eliminando um ponto único de falha identificado em teste",
]

SCALES = [
    "O tráfego normal é estável, mas cresce oito vezes em campanhas.",
    "A carga atende milhares de requisições por segundo em horários de pico.",
    "Os dados incluem informações reguladas e devem permanecer auditáveis.",
    "A aplicação é global e a latência percebida pelo usuário é uma métrica de negócio.",
    "O orçamento é limitado e a operação manual deve ser mínima.",
    "Uma interrupção de poucos minutos gera impacto financeiro mensurável.",
    "A equipe precisa provar a decisão com um teste pequeno e reversível.",
    "A solução atual funciona, mas não atende ao novo requisito não funcional.",
]


def case(topic, stem, correct, why, child, ref, lab, tradeoff, wrong):
    """Atalho para declarar um cenario curado e suas tres distracoes."""
    assert len(wrong) == 3
    return {
        "topic": topic,
        "stem": stem,
        "options": [(correct, why), *wrong],
        "why": why,
        "child": child,
        "ref": ref,
        "lab": lab,
        "tradeoff": tradeoff,
    }


CATALOG = {
"D1": [
case(
    "Acesso entre contas com IAM Roles",
    "Uma aplicação na conta de produção precisa ler objetos de um bucket pertencente à conta de dados, sem armazenar chaves de acesso. O acesso deve ser temporário, auditável e seguir privilégio mínimo. Qual solução atende melhor?",
    "Criar uma IAM Role na conta de dados, confiar na role da aplicação e usar AWS STS AssumeRole com política limitada ao bucket.",
    "AssumeRole entrega credenciais temporárias e separa a política de confiança da política de permissões, permitindo acesso entre contas sem segredo de longa duração.",
    "É como dar um crachá de visitante que abre só uma sala e expira no fim da visita.",
    "https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html",
    "../labs/README.md — Lambda/API Gateway com IAM e acesso entre contas",
    "Uma bucket policy também participa do controle de acesso, mas a role com STS é a opção central quando a aplicação precisa de uma identidade temporária na outra conta.",
    [
        ("Criar um usuário IAM na conta de dados e copiar access key e secret key para a instância.", "Chaves de longa duração aumentam o risco de vazamento e exigem rotação; não são necessárias para workloads na AWS."),
        ("Tornar o bucket público e restringir o endereço IP na aplicação.", "Exposição pública viola o requisito e endereço IP não substitui autenticação e autorização."),
        ("Compartilhar a senha do usuário raiz da conta de dados pelo Secrets Manager.", "Credenciais do usuário raiz não devem ser usadas por aplicações, mesmo quando armazenadas em um cofre."),
    ],
),
case(
    "S3 privado atrás do CloudFront",
    "Um site estático precisa ser distribuído globalmente. Os objetos do S3 não podem ser acessados diretamente pela internet, e a equipe quer aplicar regras contra requisições maliciosas na borda. O que deve ser configurado?",
    "CloudFront com Origin Access Control para o bucket privado, bucket policy restrita à distribuição e AWS WAF associado ao CloudFront.",
    "O OAC permite que somente a distribuição autorizada leia o bucket, enquanto o WAF inspeciona requisições HTTP(S) antes de elas alcançarem a origem.",
    "O depósito fica trancado; um entregador com crachá busca os pacotes, e um porteiro barra visitantes perigosos.",
    "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html",
    "../labs/README.md — S3, CloudFront e WAF",
    "Shield Standard já protege contra ataques DDoS comuns, mas WAF é o controle apropriado para padrões de camada 7 e o OAC evita bypass da distribuição.",
    [
        ("Habilitar website hosting público no S3 e filtrar acessos apenas com security groups.", "Buckets S3 não usam security groups, e o endpoint de website exigiria exposição pública da origem."),
        ("Colocar o bucket em uma subnet privada e anexar uma network ACL.", "S3 é um serviço regional, não um recurso implantado dentro de subnets do cliente."),
        ("Usar somente uma URL pré-assinada permanente para cada objeto.", "URLs pré-assinadas expiram e não substituem uma arquitetura de distribuição, cache e proteção de borda."),
    ],
),
case(
    "Criptografia com AWS KMS",
    "Um banco RDS deve ser criptografado em repouso com uma chave controlada pela empresa. A segurança exige separação de funções, auditoria de uso da chave e rotação anual automática. Qual desenho é apropriado?",
    "Criar uma chave simétrica gerenciada pelo cliente no AWS KMS, limitar key policy/grants, habilitar rotação e selecioná-la ao criar o RDS.",
    "Uma chave KMS gerenciada pelo cliente oferece controle de política, trilha de auditoria no CloudTrail e rotação automática compatível com a criptografia do RDS.",
    "É um cofre cuja chave mestra tem lista de convidados, diário de uso e troca automática de segredo.",
    "https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html",
    "../labs/README.md — KMS e criptografia em repouso",
    "A chave gerenciada pela AWS reduz administração, porém não dá o mesmo nível de controle de política exigido; a escolha da chave ocorre na criação ou restauração criptografada.",
    [
        ("Usar uma chave gerenciada pela AWS e editar diretamente sua key policy para impor a separação de funções.", "Key policies de chaves gerenciadas pela AWS não são editáveis pelo cliente como as de uma chave gerenciada pelo cliente."),
        ("Guardar uma senha AES em user data e criptografar manualmente cada página do banco.", "User data não é cofre de segredos e criptografia manual acrescenta risco e operação desnecessários."),
        ("Habilitar apenas TLS no endpoint do RDS.", "TLS protege dados em trânsito; não satisfaz o requisito de criptografia em repouso."),
    ],
),
case(
    "Rotação de credenciais com Secrets Manager",
    "Uma aplicação usa credenciais de um banco RDS. A senha precisa rotacionar automaticamente a cada 30 dias sem ser gravada no código ou na imagem do contêiner. Qual é a solução com menor esforço operacional?",
    "Armazenar a credencial no AWS Secrets Manager, configurar rotação com Lambda e conceder à task role permissão de leitura do segredo.",
    "Secrets Manager armazena, versiona e integra a rotação de segredos; a role do workload elimina credenciais AWS embutidas no contêiner.",
    "A senha mora num cofrinho que troca a combinação sozinho e só mostra a nova combinação ao robô autorizado.",
    "https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html",
    "../labs/README.md — Lambda/API Gateway com IAM roles",
    "Parameter Store SecureString pode guardar valores sensíveis com KMS, mas a rotação gerenciada de credenciais de banco é a vantagem decisiva do Secrets Manager neste cenário.",
    [
        ("Salvar a senha em uma variável de ambiente no Dockerfile e recriar a imagem mensalmente.", "A imagem pode vazar a senha e a rotação permanece manual e acoplada ao deploy."),
        ("Guardar a senha em uma tag do recurso RDS protegida por IAM.", "Tags não são um mecanismo de armazenamento seguro de segredos."),
        ("Criar access keys para o usuário raiz e usá-las como senha do banco.", "Credenciais AWS não substituem credenciais do banco e o usuário raiz não deve ser usado por workloads."),
    ],
),
case(
    "VPC Gateway Endpoint para S3",
    "Instâncias EC2 em subnets privadas enviam grandes volumes ao S3. O tráfego não pode atravessar a internet e a solução deve evitar cobrança por hora de um componente de rede. Qual opção usar?",
    "Criar um Gateway VPC Endpoint para S3, associá-lo às route tables privadas e restringir acesso com endpoint/bucket policies.",
    "Gateway endpoints para S3 adicionam rotas privadas ao serviço, não exigem NAT e não têm a cobrança por hora típica de interface endpoints.",
    "É uma estrada particular e gratuita do escritório até o armazém, sem sair para a avenida pública.",
    "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html",
    "../labs/README.md — VPC multi-AZ, NAT e endpoints",
    "Um NAT Gateway também permite chegar ao endpoint público do S3, mas adiciona custo por hora e por dados e não atende tão diretamente à exigência de caminho privado.",
    [
        ("Enviar o tráfego por um NAT Gateway em cada AZ.", "O NAT adiciona custo e o caminho usa o endpoint público; é desnecessário quando há gateway endpoint para S3."),
        ("Criar um Interface Endpoint para qualquer serviço e esperar que ele seja sempre gratuito.", "Interface endpoints têm cobrança por hora e processamento de dados; a afirmação de gratuidade é incorreta."),
        ("Atribuir IPv4 público às instâncias e permitir saída 0.0.0.0/0.", "Isso expõe as instâncias a uma rota de internet e viola o requisito de tráfego privado."),
    ],
),
case(
    "SCP em AWS Organizations",
    "A organização quer impedir que qualquer conta membro desative o CloudTrail ou crie recursos fora de regiões aprovadas, inclusive quando um administrador local concede Allow. Qual controle deve formar o guardrail?",
    "Aplicar Service Control Policies nas OUs, com exceções cuidadosamente definidas para serviços e funções indispensáveis.",
    "SCPs definem o teto de permissões de contas membros; um Allow local não consegue ultrapassar um Deny explícito aplicável da organização.",
    "É o muro do condomínio: cada morador escolhe as regras da casa, mas ninguém pode atravessar o muro externo.",
    "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html",
    "../labs/README.md — IAM, KMS e guardrails",
    "SCP não concede permissões e não substitui policies de identidade ou recurso; ele limita o conjunto máximo que esses mecanismos podem conceder.",
    [
        ("Adicionar uma IAM policy Allow a todos os administradores das contas.", "Um Allow amplia permissões locais e não cria o guardrail organizacional solicitado."),
        ("Usar somente security groups para bloquear chamadas de API fora da região.", "Security groups filtram tráfego de recursos e não governam permissões de APIs ou regiões."),
        ("Criar uma tag chamada RegiãoPermitida e confiar que os serviços a aplicarão sozinhos.", "Tags só têm efeito de autorização quando policies explicitamente as avaliam."),
    ],
),
case(
    "Trilha de auditoria organizacional",
    "Auditores exigem registro centralizado e resistente a adulteração das chamadas de API de todas as contas atuais e futuras. Também é preciso alertar quando alguém tentar apagar uma trilha. Qual arquitetura é adequada?",
    "Criar uma organization trail no CloudTrail para bucket central dedicado, habilitar validação de integridade, restringir o bucket e monitorar eventos com EventBridge/CloudWatch.",
    "Uma organization trail cobre contas da organização de forma central; políticas do bucket e validação de logs protegem a evidência, e eventos permitem alertas rápidos.",
    "Todas as salas escrevem no mesmo diário lacrado; se alguém tentar arrancar uma página, um alarme toca.",
    "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html",
    "../labs/README.md — Observabilidade, CloudTrail e alertas",
    "CloudTrail Lake pode ajudar em consultas e retenção, mas não elimina a necessidade de definir proteção, governança e alertas coerentes para os registros.",
    [
        ("Confiar apenas no Event history de 90 dias de cada conta.", "O histórico é limitado, regionalmente consultado e não fornece sozinho retenção central protegida."),
        ("Usar VPC Flow Logs como substituto para chamadas de API.", "Flow Logs registram metadados de fluxos de rede, não ações de controle executadas via APIs."),
        ("Habilitar logs de acesso do ALB para registrar alterações no IAM.", "Logs do ALB mostram requisições ao balanceador, não alterações administrativas em serviços AWS."),
    ],
),
case(
    "Security groups e network ACLs",
    "Servidores web em subnets públicas aceitam HTTPS do mundo e acessam servidores de aplicação em subnets privadas. A equipe quer controles stateful por recurso e uma camada stateless de bloqueio explícito por CIDR na subnet. Qual combinação usar?",
    "Security groups para permitir apenas os fluxos necessários entre tiers e network ACLs para regras stateless de allow/deny no limite das subnets.",
    "Security groups são stateful e associados a interfaces; NACLs são stateless, ordenadas e associadas a subnets, podendo negar CIDRs explicitamente.",
    "O crachá lembra quem entrou e deixa a resposta voltar; a cancela da rua verifica ida e volta e pode barrar uma placa.",
    "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html",
    "../labs/README.md — VPC multi-AZ com SG e NACL",
    "Na maioria dos desenhos, security groups fazem o controle principal. NACLs são defesa adicional e exigem atenção às portas efêmeras nos dois sentidos.",
    [
        ("Usar apenas uma NACL, pois ela mantém estado das conexões automaticamente.", "NACLs são stateless e exigem regras correspondentes de entrada e saída."),
        ("Usar security group para negar explicitamente um CIDR malicioso.", "Security groups têm regras de allow, não regras de deny explícito."),
        ("Associar uma NACL diretamente a cada instância EC2.", "NACLs são associadas a subnets; security groups são associados às interfaces de rede."),
    ],
),
case(
    "Autenticação de clientes com Amazon Cognito",
    "Um aplicativo móvel voltado a milhões de consumidores precisa cadastro, login, recuperação de senha, MFA opcional e tokens para chamar uma API. A equipe não quer manter um diretório próprio. Qual serviço é indicado?",
    "Usar um Amazon Cognito User Pool como diretório e emissor de tokens, integrando-o ao API Gateway; usar Identity Pool apenas se forem necessárias credenciais AWS temporárias.",
    "User Pools fornecem autenticação de usuários e tokens OIDC/OAuth; a API valida esses tokens sem a equipe operar o armazenamento de senhas.",
    "É uma portaria pronta que cadastra visitantes e entrega pulseiras válidas para entrar na festa.",
    "https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html",
    "../labs/README.md — API Gateway, Lambda e autenticação",
    "IAM Identity Center atende principalmente força de trabalho; Cognito é adequado a identidades de clientes. Identity Pools cumprem outro papel: trocar identidades por credenciais AWS temporárias.",
    [
        ("Criar um usuário IAM para cada consumidor do aplicativo.", "IAM users não são um diretório de clientes em escala e gerariam riscos e operação excessivos."),
        ("Salvar senhas em uma tabela DynamoDB sem hash e validar na Lambda.", "Armazenamento de senhas em texto é inseguro e recria capacidades já gerenciadas pelo Cognito."),
        ("Usar somente uma API key do API Gateway compartilhada por todos.", "API keys ajudam em medição e planos de uso; não autenticam individualmente usuários finais."),
    ],
),
case(
    "Proteção de camada 7 com AWS WAF",
    "Uma API pública atrás de um ALB sofre credential stuffing e rajadas de um pequeno conjunto de endereços IP. É necessário bloquear padrões HTTP e limitar requisições por origem sem alterar a aplicação. O que fazer?",
    "Associar um Web ACL do AWS WAF ao ALB, usando managed rules e uma rate-based rule ajustada ao tráfego legítimo.",
    "WAF inspeciona atributos HTTP(S) e regras baseadas em taxa agregam requisições por chave, bloqueando ou desafiando origens abusivas na camada 7.",
    "O porteiro reconhece truques nas cartas e manda quem bate vezes demais esperar do lado de fora.",
    "https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html",
    "../labs/README.md — S3/CloudFront/WAF e proteção web",
    "Shield Standard está incluído e lida com ataques DDoS comuns de rede e transporte; Shield Advanced acrescenta resposta e proteção de custo, mas não substitui regras HTTP do WAF.",
    [
        ("Editar a NACL para bloquear palavras presentes no corpo HTTP.", "NACLs operam em rede e não inspecionam conteúdo HTTP."),
        ("Usar apenas AWS Shield Standard para identificar senhas reutilizadas.", "Shield não implementa lógica de credential stuffing baseada em campos e padrões HTTP."),
        ("Aumentar o número de instâncias do Auto Scaling sem filtrar as requisições.", "Escalar pode absorver carga, mas não bloqueia abuso e ainda amplia custo."),
    ],
),
case(
    "S3 Block Public Access e políticas",
    "Uma empresa armazena relatórios confidenciais em centenas de buckets. Ela precisa impedir exposição pública acidental em toda a organização e permitir acesso apenas por um VPC endpoint específico. Qual desenho é mais seguro?",
    "Ativar S3 Block Public Access no nível da organização/contas e aplicar bucket policies com condição aws:SourceVpce e negação fora do endpoint autorizado.",
    "Block Public Access neutraliza políticas e ACLs públicas; uma bucket policy com condição e Deny explícito restringe o caminho de acesso ao endpoint aprovado.",
    "Primeiro fechamos todas as janelas do prédio; depois damos uma chave que só funciona na passagem secreta certa.",
    "https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html",
    "../labs/README.md — S3 privado e endpoints VPC",
    "Ao usar condições de endpoint, é preciso preservar acessos administrativos e de serviços necessários para não bloquear operações legítimas de forma acidental.",
    [
        ("Usar ACL public-read e esconder os nomes dos objetos.", "Obscuridade de nomes não é controle de acesso, e a ACL tornaria dados públicos."),
        ("Associar um security group diretamente ao bucket.", "Buckets S3 não aceitam security groups."),
        ("Criptografar os objetos, mas deixar leitura pública para qualquer principal.", "Criptografia em repouso não corrige uma autorização pública; serviços autorizados ainda descriptografariam dados."),
    ],
),
case(
    "Permissions boundaries e delegação",
    "Uma plataforma permite que times de produto criem suas próprias roles, mas segurança precisa garantir que nenhuma role criada ultrapasse um conjunto máximo de ações. Os times ainda devem escolher permissões dentro desse limite. Qual recurso usar?",
    "Exigir uma permissions boundary nas roles criadas e controlar iam:PermissionsBoundary nas políticas do time.",
    "A permissions boundary define o máximo que uma policy de identidade pode conceder, permitindo delegação sem entregar privilégios ilimitados.",
    "A criança escolhe onde brincar no quintal, mas a cerca define até onde ela pode ir.",
    "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html",
    "../labs/README.md — IAM least privilege e roles",
    "Boundary não concede acesso por si só e precisa ser avaliada junto de policies de identidade, recurso, SCPs e negações explícitas.",
    [
        ("Anexar AdministratorAccess e pedir que cada time não use ações perigosas.", "Confiança processual não impõe um limite técnico e AdministratorAccess viola privilégio mínimo."),
        ("Usar uma NACL para limitar quais APIs IAM podem ser chamadas.", "NACLs filtram pacotes e não avaliam ações IAM."),
        ("Criar somente tags sem nenhuma condição de IAM associada.", "Tags isoladas são metadados; o controle exige policies que as avaliem."),
    ],
),
],
"D2": [
case(
    "RDS Multi-AZ",
    "Um banco transacional RDS precisa recuperar automaticamente de falha de instância ou de AZ, preservando o mesmo endpoint. A carga de leitura não é o problema principal. Qual configuração atende ao requisito?",
    "Habilitar uma implantação RDS Multi-AZ com standby síncrono e failover gerenciado.",
    "RDS Multi-AZ replica de forma síncrona para outra AZ e executa failover do endpoint, sendo uma solução de alta disponibilidade e não de escalabilidade de leitura.",
    "Há uma loja gêmea pronta em outro bairro; se a primeira fecha, a placa aponta sozinha para a segunda.",
    "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html",
    "../labs/README.md — RDS Multi-AZ e read replica",
    "Read replicas são assíncronas e adequadas para escalar leituras; podem ser promovidas, mas isso não equivale ao failover automático de Multi-AZ.",
    [
        ("Criar uma read replica na mesma AZ e usá-la como standby síncrono automático.", "Read replicas usam replicação assíncrona e não fornecem o mesmo mecanismo de failover Multi-AZ."),
        ("Fazer snapshot manual uma vez por semana.", "Snapshots ajudam em restauração, mas não fornecem failover rápido nem RPO próximo de zero."),
        ("Aumentar a classe da instância sem criar réplica.", "Uma instância maior continua sendo um ponto único de falha."),
    ],
),
case(
    "ALB e Auto Scaling multi-AZ",
    "Uma aplicação HTTP stateless precisa continuar disponível quando uma instância ou uma AZ falhar e deve ajustar capacidade conforme o volume de requisições. Qual arquitetura escolher?",
    "ALB em pelo menos duas AZs, Auto Scaling group distribuído nessas AZs e target tracking baseado em uma métrica apropriada.",
    "O ALB encaminha apenas para targets saudáveis e o Auto Scaling substitui capacidade e distribui instâncias entre AZs, eliminando pontos únicos no tier web.",
    "Vários caixas trabalham em lojas de bairros diferentes; um organizador manda clientes só aos caixas abertos e chama reforço quando a fila cresce.",
    "https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html",
    "../labs/README.md — ALB, Auto Scaling e health checks",
    "Sessões devem ficar fora das instâncias ou usar um armazenamento compartilhado; sticky sessions podem ajudar temporariamente, mas reduzem flexibilidade e não substituem estado externo.",
    [
        ("Executar uma única instância grande e reiniciá-la com um cron job.", "Ainda há ponto único de falha e recuperação dependente de automação frágil."),
        ("Colocar duas instâncias na mesma AZ sem health check.", "Uma falha da AZ afeta ambas, e sem health check o tráfego pode chegar a targets defeituosos."),
        ("Usar somente DNS round-robin com endereços fixos e sem Auto Scaling.", "DNS não substitui health checks do balanceador nem reposição e ajuste automático de capacidade."),
    ],
),
case(
    "Route 53 failover",
    "Uma aplicação possui um endpoint primário em uma região e um site de recuperação em outra. O DNS deve enviar tráfego ao secundário apenas quando o primário não estiver saudável. Qual política usar?",
    "Criar registros Route 53 com failover routing, marcar primário/secundário e associar health check ao endpoint primário.",
    "A política de failover usa a saúde do recurso para responder com o secundário quando o primário falha, implementando active-passive no DNS.",
    "O mapa aponta para a loja principal; se a luz dela apaga, passa a apontar para a loja reserva.",
    "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html",
    "../labs/README.md — Failover multi-região e Route 53",
    "TTL influencia quanto tempo resolvers mantêm respostas antigas; failover DNS não encerra conexões já abertas e deve ser combinado com um plano de dados consistente.",
    [
        ("Usar simple routing com dois endereços e nenhum health check.", "Simple routing não fornece o comportamento primário/secundário orientado por saúde."),
        ("Usar geolocation apenas, pois localização detecta falha automaticamente.", "Geolocation roteia pela origem do usuário; não é, por si só, política de recuperação por saúde."),
        ("Aumentar o TTL para 24 horas para acelerar a mudança.", "TTL alto faz caches manterem a resposta anterior por mais tempo, retardando a convergência."),
    ],
),
case(
    "Desacoplamento com SQS e DLQ",
    "Pedidos chegam em rajadas e o processador pode ficar temporariamente indisponível. Nenhum pedido pode ser perdido, falhas repetidas devem ser isoladas e o produtor não deve esperar o processamento. Qual desenho usar?",
    "Enviar pedidos para uma fila SQS, processar com consumidores idempotentes, configurar visibility timeout e redrive para uma DLQ.",
    "SQS armazena mensagens de forma durável e desacopla ritmos; visibility timeout evita processamento concorrente imediato e a DLQ isola mensagens após tentativas definidas.",
    "Os pedidos entram numa caixa de correio; o cozinheiro pega um, e pedidos problemáticos vão para uma bandeja de investigação.",
    "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html",
    "../labs/README.md — Lambda, filas e tratamento de falhas",
    "Standard queues entregam ao menos uma vez e podem duplicar; idempotência é essencial. FIFO deve ser usada apenas quando ordenação estrita/deduplicação justificarem suas restrições.",
    [
        ("Fazer o produtor chamar o processador de forma síncrona com retries infinitos.", "Isso acopla os componentes, prende recursos e pode criar tempestades de retries."),
        ("Publicar somente em uma SNS topic sem qualquer assinatura durável.", "SNS sozinho não mantém backlog para um consumidor indisponível; uma assinatura SQS adicionaria durabilidade."),
        ("Gravar pedidos em instance store de uma única EC2.", "Instance store é efêmero e a instância continua sendo ponto único de falha."),
    ],
),
case(
    "Fan-out com SNS e SQS",
    "Cada evento de pedido deve ser processado independentemente por faturamento, estoque e analytics. Se um consumidor parar, os outros devem continuar e o backlog daquele consumidor deve ser preservado. Qual arquitetura é apropriada?",
    "Publicar em uma SNS topic e criar uma fila SQS separada para cada consumidor, com subscriptions e DLQs próprias.",
    "SNS replica cada mensagem para as filas assinantes; cada SQS mantém seu próprio backlog, ritmo e política de falhas, isolando consumidores.",
    "Um locutor anuncia a notícia para três caixas de correio; cada equipe abre a sua quando puder.",
    "https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html",
    "../labs/README.md — Eventos, SNS, SQS e Lambda",
    "Uma única fila com três consumidores distribuiria mensagens entre eles, em vez de entregar uma cópia a cada função de negócio.",
    [
        ("Usar uma única fila SQS e fazer os três serviços competirem pela mesma mensagem.", "Consumidores concorrentes em uma fila recebem mensagens diferentes; não há fan-out por consumidor."),
        ("Chamar os três serviços sequencialmente dentro do produtor.", "A falha ou lentidão de um serviço afeta todos e acopla o produtor aos consumidores."),
        ("Guardar eventos em logs locais da instância produtora.", "Logs locais não são um canal durável e consumível de integração."),
    ],
),
case(
    "Estratégias de disaster recovery",
    "Um sistema regional exige RTO de 15 minutos e RPO de poucos minutos. A empresa aceita manter capacidade reduzida ativa na região de recuperação, mas não quer pagar por uma cópia em escala total. Qual estratégia se encaixa melhor?",
    "Warm standby: manter uma versão funcional em escala reduzida na região secundária, replicar dados e escalar durante o failover.",
    "Warm standby já executa todos os componentes essenciais, reduzindo o RTO em comparação a pilot light sem manter capacidade integral como active-active.",
    "Há uma lojinha reserva já aberta com poucos caixas; numa emergência, ela chama reforços rapidamente.",
    "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html",
    "../labs/README.md — Cenário de recuperação multi-região",
    "Pilot light custa menos, mas precisa iniciar/implantar parte relevante da aplicação; multi-site active-active oferece RTO menor com maior custo e complexidade.",
    [
        ("Backup and restore com backups semanais offline.", "Em geral não atende RPO de minutos nem RTO de 15 minutos."),
        ("Pilot light contendo somente dados, sem automação para subir a aplicação.", "A ausência de componentes e automação torna o RTO incerto e provavelmente maior."),
        ("Multi-site active-active em escala total obrigatoriamente.", "Atenderia ou superaria o RTO, mas viola a intenção de evitar custo de capacidade integral quando warm standby basta."),
    ],
),
case(
    "Replicação S3 entre regiões",
    "Objetos de um bucket precisam ser copiados automaticamente para outra região para recuperação. A empresa também quer preservar versões e impedir que uma exclusão acidental destrua imediatamente a cópia histórica. O que configurar?",
    "Habilitar versionamento nos buckets, configurar S3 Cross-Region Replication e definir cuidadosamente replicação de delete markers e retenção/Object Lock quando exigido.",
    "CRR requer versionamento e replica novos objetos conforme as regras. A política de delete markers e mecanismos de retenção determinam o comportamento diante de exclusões.",
    "Cada desenho ganha uma cópia em outra cidade e versões antigas ficam num fichário que uma borracha comum não apaga.",
    "https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
    "../labs/README.md — S3 versionado e recuperação",
    "Replicação não é retroativa por padrão e não substitui toda estratégia de backup; S3 Batch Replication pode tratar objetos existentes.",
    [
        ("Usar lifecycle expiration no bucket de origem como mecanismo de cópia.", "Lifecycle gerencia transição/expiração e não replica objetos para outra região."),
        ("Montar o bucket como EBS e fazer snapshot da instância.", "S3 não é montado como volume EBS, e snapshot de EC2 não protege objetos do bucket."),
        ("Desativar versionamento para reduzir o número de cópias.", "CRR exige versionamento e desativá-lo prejudica recuperação de alterações/exclusões."),
    ],
),
case(
    "Amazon EFS Regional",
    "Um conjunto de instâncias Linux em várias AZs precisa compartilhar arquivos POSIX. Os dados devem permanecer acessíveis quando uma instância ou uma AZ falhar, sem gerenciar servidores de arquivos. Qual armazenamento usar?",
    "Amazon EFS Regional montado pelos clientes nas diferentes AZs, com mount targets e security groups adequados.",
    "EFS Regional fornece sistema de arquivos gerenciado, elástico e multi-AZ, adequado ao compartilhamento simultâneo entre instâncias Linux.",
    "É uma estante compartilhada com portas em vários bairros; se uma porta fecha, as outras ainda chegam aos livros.",
    "https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html",
    "../labs/README.md — Armazenamento compartilhado multi-AZ",
    "EFS One Zone pode custar menos, mas não atende ao requisito de tolerância à perda de uma AZ. EBS é zonal e normalmente anexado a uma instância.",
    [
        ("Usar um único volume EBS em uma AZ e anexá-lo simultaneamente a qualquer número de instâncias Linux.", "EBS é zonal e Multi-Attach possui tipos e cenários restritos; não vira um sistema de arquivos regional gerenciado."),
        ("Usar instance store e copiar arquivos manualmente à noite.", "Instance store é efêmero e a cópia manual não dá consistência nem alta disponibilidade."),
        ("Hospedar um servidor NFS único em EC2 sem standby.", "O servidor seria ponto único de falha e exigiria administração."),
    ],
),
case(
    "Aurora Global Database",
    "Uma aplicação de leitura global baseada em Aurora precisa latência local em regiões secundárias e recuperação regional com replicação rápida. Escritas permanecem centralizadas durante operação normal. Qual recurso escolher?",
    "Usar Aurora Global Database com cluster primário gravável e clusters secundários de leitura nas regiões necessárias.",
    "Aurora Global Database usa replicação dedicada entre regiões, oferece leituras locais e permite promover uma região secundária em um evento de recuperação.",
    "O livro mestre é escrito numa cidade, enquanto cópias quase instantâneas chegam às bibliotecas do mundo.",
    "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html",
    "../labs/README.md — RDS/Aurora, réplicas e failover",
    "A promoção e o roteamento da aplicação ainda precisam ser planejados. Multi-AZ protege dentro de uma região e não fornece, sozinho, leituras globais.",
    [
        ("Usar apenas Multi-AZ no cluster primário e esperar endpoints de leitura em outras regiões.", "Multi-AZ oferece resiliência regional, não clusters de leitura entre regiões."),
        ("Exportar snapshots manualmente uma vez por mês.", "Snapshots mensais não oferecem replicação contínua nem RPO/RTO compatíveis."),
        ("Colocar o endpoint regional atrás de CloudFront para armazenar respostas SQL em cache.", "CloudFront não se conecta diretamente a um protocolo de banco e não cria réplicas do Aurora."),
    ],
),
case(
    "DynamoDB Global Tables",
    "Usuários em duas regiões precisam ler e gravar em uma tabela DynamoDB com baixa latência local. A aplicação aceita consistência eventual entre regiões e deve continuar gravando se uma região falhar. Qual solução usar?",
    "Criar uma DynamoDB global table no modo de consistência eventual multi-região (MREC) e tornar a aplicação tolerante à resolução last-writer-wins.",
    "Global Tables em MREC fornecem replicação multi-active gerenciada, permitindo leitura e gravação locais nas regiões participantes.",
    "São dois cadernos mágicos: dá para escrever em qualquer cidade e as novidades aparecem no outro.",
    "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html",
    "../labs/README.md — DynamoDB, DAX e desenho de chaves",
    "No modo MREC, conflitos concorrentes usam last-writer-wins e a aplicação deve entender essa semântica. O modo MRSC oferece consistência forte multi-região com outra semântica, topologia e disponibilidade regional; a escolha depende do requisito de consistência.",
    [
        ("Criar uma tabela comum em uma única região e usar Multi-AZ manualmente.", "DynamoDB já é multi-AZ na região, mas isso não fornece gravações locais em duas regiões."),
        ("Adicionar DAX em duas regiões sem replicar a tabela.", "DAX é cache regional e não torna a tabela multi-region ou multi-active."),
        ("Fazer backup diário e restaurar em cada falha regional.", "Backup/restauração não atende baixa latência local nem continuidade de gravações com RTO curto."),
    ],
),
case(
    "Falhas assíncronas do Lambda",
    "Uma função Lambda é invocada de modo assíncrono por eventos. Após as tentativas automáticas, eventos malsucedidos devem ser preservados para investigação e reprocessamento, sem bloquear eventos saudáveis. O que configurar?",
    "Configurar uma on-failure destination para SQS/SNS/EventBridge ou uma DLQ compatível, além de alarmes e processamento idempotente.",
    "Invocações assíncronas possuem fila e retries gerenciados; destinations entregam contexto do resultado após as tentativas, permitindo análise e reprocessamento desacoplado.",
    "Cartinhas que o robô não consegue ler vão para uma caixa vermelha, sem parar a leitura das demais.",
    "https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html",
    "../labs/README.md — Lambda, API Gateway e tratamento de erros",
    "DLQ e destination têm formatos e capacidades diferentes; a equipe deve escolher um, observar idade máxima do evento e evitar loops de reprocessamento.",
    [
        ("Definir timeout infinito para garantir que toda execução termine.", "Lambda tem limite de timeout e aumentar duração não resolve eventos permanentemente inválidos."),
        ("Desativar logs para impedir que falhas afetem o serviço.", "Logs não causam a falha e removê-los prejudica diagnóstico e observabilidade."),
        ("Reenviar o mesmo evento recursivamente dentro da função sem limite.", "Isso pode criar loop, duplicidade e custo sem isolar o evento defeituoso."),
    ],
),
case(
    "Políticas centralizadas com AWS Backup",
    "Dezenas de contas precisam de backups consistentes de EBS, RDS e EFS, cópias entre regiões e proteção contra exclusão pela conta de origem. Segurança quer governança central. Qual abordagem usar?",
    "Usar AWS Backup com backup policies da organização, cofre central/cross-account, cópia cross-region e Vault Lock quando a imutabilidade for requerida.",
    "AWS Backup centraliza planos, seleção, retenção e cópias entre serviços e contas; Vault Lock ajuda a impor retenção WORM contra alterações indevidas.",
    "Um bibliotecário central faz cópias de todos os livros, guarda outra caixa em outra cidade e lacra as caixas pelo prazo certo.",
    "https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html",
    "../labs/README.md — Backup, restore e testes de recuperação",
    "Backup só é confiável quando restaurações são testadas e métricas de RPO/RTO são verificadas; replicação e alta disponibilidade não substituem backups protegidos.",
    [
        ("Pedir que cada desenvolvedor crie snapshots manuais quando lembrar.", "O processo não é consistente, auditável nem centralmente imposto."),
        ("Usar apenas RDS Multi-AZ como backup histórico.", "Multi-AZ é alta disponibilidade e replica também erros lógicos; não é retenção histórica independente."),
        ("Copiar arquivos para o disco local de uma instância na mesma conta.", "A cópia permanece vulnerável a falhas e exclusões na mesma fronteira administrativa."),
    ],
),
],
"D3": [
case(
    "Cache global com CloudFront",
    "Um portal entrega imagens e arquivos estáticos do S3 a usuários globais. A origem recebe leituras repetidas e usuários distantes observam alta latência. Qual mudança melhora desempenho com menor operação?",
    "Distribuir o conteúdo com CloudFront, definir cache policies/TTLs adequados, compressão e OAC para a origem S3 privada.",
    "CloudFront guarda objetos em edge locations próximas aos usuários, reduzindo latência e carga na origem; políticas de cache controlam a chave e a validade.",
    "Em vez de buscar cada brinquedo na fábrica distante, pequenas lojas perto das crianças guardam os mais pedidos.",
    "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html",
    "../labs/README.md — S3, CloudFront e WAF",
    "TTL longo aumenta hit ratio, mas atrasa atualizações; versionar nomes de objetos é geralmente mais previsível que invalidar grandes volumes.",
    [
        ("Aumentar o tamanho do bucket S3.", "S3 não precisa de provisionamento de capacidade do bucket e isso não aproxima conteúdo do usuário."),
        ("Copiar manualmente todos os objetos para volumes EBS em cada região.", "Isso cria operação, inconsistência e não fornece uma rede de borda global."),
        ("Usar Route 53 weighted routing para armazenar objetos em cache.", "Route 53 responde DNS; ele não armazena nem entrega o conteúdo."),
    ],
),
case(
    "ElastiCache for Redis",
    "Uma API lê repetidamente os mesmos registros de sessão e catálogo em um banco relacional. O banco está no limite de CPU, e dados em cache podem expirar em minutos. Qual solução reduz a latência?",
    "Adicionar ElastiCache for Redis e aplicar cache-aside com TTL, tratamento de cache miss e invalidação coerente.",
    "Redis oferece acesso em memória de baixa latência e remove leituras repetitivas do banco; cache-aside mantém o banco como fonte de verdade.",
    "As respostas mais usadas ficam em post-its na mesa, em vez de procurar o livro inteiro a cada pergunta.",
    "https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html",
    "../labs/README.md — Cache, banco e observabilidade",
    "Cache introduz risco de dados obsoletos e stampede. TTL, jitter, réplicas e comportamento quando o cache falha devem ser desenhados.",
    [
        ("Criar uma read replica e gravar sessões diretamente nela.", "Read replicas relacionais normalmente são somente leitura e não são ideais como armazenamento de sessão volátil."),
        ("Aumentar indefinidamente o TTL de DNS do banco.", "Cache DNS não armazena resultados de consulta nem reduz CPU de execução SQL."),
        ("Mover registros de sessão para S3 Glacier Deep Archive.", "A classe tem recuperação lenta e não serve a acesso interativo de baixa latência."),
    ],
),
case(
    "Chave de partição do DynamoDB",
    "Uma tabela DynamoDB recebe gravações intensas. A chave de partição atual usa apenas o código de um país, e um país concentra 80% do tráfego, causando throttling. Qual redesign é mais apropriado?",
    "Escolher uma chave de alta cardinalidade que distribua acessos, usando write sharding quando necessário, e manter padrões de consulta com índices adequados.",
    "DynamoDB distribui itens pela chave de partição; poucas chaves populares concentram capacidade. Alta cardinalidade e sharding espalham as requisições.",
    "Se todos entrarem pela mesma porta, forma fila; várias portas bem escolhidas distribuem a turma.",
    "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html",
    "../labs/README.md — DynamoDB, DAX e modelagem de chaves",
    "On-demand ajusta capacidade, mas não elimina todos os efeitos de uma hot partition. O modelo deve começar pelos padrões de acesso, não por normalização relacional.",
    [
        ("Manter o país como única chave e aumentar o tamanho de uma instância DynamoDB.", "DynamoDB é serverless e não expõe tamanho de instância; a chave quente continua problemática."),
        ("Criar uma chave constante para garantir ordem global.", "Uma única chave concentra toda a carga em uma partição lógica."),
        ("Adicionar apenas mais atributos sem alterar chaves ou índices.", "Atributos extras não mudam a distribuição das requisições."),
    ],
),
case(
    "Read replicas para escalar leituras",
    "Um banco RDS atende relatórios pesados que disputam CPU e I/O com transações. Os relatórios toleram alguns segundos de defasagem e a alta disponibilidade já está coberta. O que fazer?",
    "Criar read replicas e direcionar consultas de relatório aos endpoints de leitura, monitorando replication lag.",
    "Read replicas usam replicação assíncrona para retirar consultas de leitura do primário; a tolerância a defasagem torna a solução adequada.",
    "Uma cópia recente do livro fica com a turma de relatórios, enquanto o original continua livre para registrar vendas.",
    "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html",
    "../labs/README.md — RDS Multi-AZ e read replica",
    "Read replica não substitui Multi-AZ para failover síncrono. A aplicação precisa separar endpoints e aceitar eventual consistency nas leituras.",
    [
        ("Usar o standby Multi-AZ diretamente para todas as consultas de relatório.", "Na implantação Multi-AZ tradicional, o standby não é endpoint de leitura da aplicação."),
        ("Fazer snapshots a cada minuto e consultar os snapshots.", "Snapshots não são uma interface de consulta e restaurações frequentes não servem a relatórios online."),
        ("Aumentar o TTL do Route 53 do endpoint do banco.", "TTL DNS não reduz a carga de consultas no primário."),
    ],
),
case(
    "Tipos de volume EBS",
    "Um banco autogerenciado em EC2 exige latência de I/O consistente e dezenas de milhares de IOPS sustentadas. A performance deve ser previsível, mesmo que custe mais que uso geral. Qual volume escolher?",
    "Usar EBS io2, dimensionando IOPS e throughput conforme a instância e a carga, e validar limites ponta a ponta.",
    "io2 é SSD de Provisioned IOPS para workloads críticos que precisam de desempenho consistente e alta durabilidade.",
    "É uma pista expressa com número de faixas reservado, em vez de torcer para a rua comum estar vazia.",
    "https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html",
    "../labs/README.md — EC2, EBS e teste de I/O",
    "gp3 é excelente padrão custo/desempenho e permite provisionar IOPS/throughput, mas io2 atende os requisitos mais rigorosos. st1/sc1 são HDD para acesso sequencial e não podem ser boot volume.",
    [
        ("Usar sc1 porque é o volume com menor latência para bancos críticos.", "sc1 é HDD de baixo custo para acesso pouco frequente e não oferece latência SSD."),
        ("Usar st1 para milhões de pequenos I/Os aleatórios.", "st1 é otimizado a throughput sequencial, não IOPS aleatórios de banco."),
        ("Usar instance store sem replicação porque todo dado EBS é efêmero.", "EBS é persistente; instance store é que é efêmero e exigiria proteção adicional."),
    ],
),
case(
    "Transferência para Amazon S3",
    "Filiais globais enviam arquivos de 200 GB ao S3 por links de longa distância. A equipe quer paralelizar uploads, retomar partes com falha e melhorar o caminho pela rede AWS. Qual combinação usar?",
    "Usar S3 multipart upload e avaliar S3 Transfer Acceleration para ingressar pela edge location mais próxima.",
    "Multipart divide o objeto, permite upload paralelo e repetição de partes; Transfer Acceleration usa a rede global da AWS a partir da borda.",
    "Um caminhão enorme vira várias caixas; se uma cai, reenviamos só aquela, e elas entram pela garagem mais próxima.",
    "https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html",
    "../labs/README.md — S3, multipart e desempenho",
    "Transfer Acceleration tem custo adicional e benefício dependente da rota; deve ser testado. Para migração offline massiva, Snowball pode ser mais apropriado.",
    [
        ("Enviar cada arquivo em uma única requisição e reiniciar tudo em qualquer falha.", "Isso perde paralelismo e torna falhas caras em objetos grandes."),
        ("Usar S3 Glacier restore antes de cada upload.", "Restore recupera objetos arquivados e não acelera novos uploads."),
        ("Colocar um NAT Gateway na filial sem conexão com a AWS.", "NAT Gateway é implantado em VPC e não melhora sozinho a rota WAN da filial."),
    ],
),
case(
    "AWS Global Accelerator",
    "Um aplicativo de jogos usa TCP/UDP, possui endpoints em duas regiões e precisa de IPs anycast estáticos, failover rápido e tráfego pela rede global da AWS. O conteúdo não é cacheável. Qual serviço usar?",
    "Usar AWS Global Accelerator com endpoint groups regionais e health checks.",
    "Global Accelerator fornece IPs anycast estáticos, leva tráfego TCP/UDP pela borda à rede global e muda endpoints conforme saúde e políticas.",
    "Todos usam o mesmo endereço de portão; por dentro, uma estrada rápida leva cada jogador ao parque saudável mais próximo.",
    "https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
    "../labs/README.md — Roteamento global e failover",
    "CloudFront é ideal para HTTP(S) cacheável e também pode acelerar conteúdo dinâmico, mas não fornece a mesma proposta para protocolos TCP/UDP genéricos e IPs anycast de entrada.",
    [
        ("Usar CloudFront para armazenar pacotes UDP de sessão em cache.", "CloudFront não é cache genérico para UDP."),
        ("Usar apenas um registro DNS com TTL de 24 horas.", "DNS não fornece IPs anycast estáticos nem failover tão rápido, e TTL alto retarda mudança."),
        ("Criar Elastic IPs regionais e anunciar manualmente BGP pela internet.", "Elastic IP é regional e clientes não anunciam esse prefixo globalmente dessa forma."),
    ],
),
case(
    "FSx for Lustre",
    "Um workload HPC em milhares de vCPUs processa um dataset grande do S3 e precisa de sistema de arquivos paralelo com throughput muito alto. Ao final, os resultados devem voltar ao S3. Qual serviço usar?",
    "Usar Amazon FSx for Lustre vinculado ao repositório de dados S3 e escolher deployment type/capacidade adequados.",
    "FSx for Lustre é um sistema de arquivos paralelo de alto desempenho integrado ao S3, adequado a HPC, ML e processamento massivo.",
    "Mil cozinheiros abrem gavetas de uma despensa super-rápida ao mesmo tempo, e os pratos prontos voltam ao armazém.",
    "https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html",
    "../labs/README.md — Armazenamento de alto desempenho",
    "Scratch oferece custo menor para dados temporários sem replicação durável; Persistent atende workloads mais longos. O S3 continua sendo a fonte/repositório durável quando desenhado assim.",
    [
        ("Usar um único volume gp2 pequeno compartilhado por todas as instâncias em regiões diferentes.", "EBS é zonal, e esse desenho não fornece sistema de arquivos paralelo ou throughput agregado."),
        ("Usar S3 Glacier Deep Archive como sistema de arquivos POSIX interativo.", "Deep Archive exige restauração e não expõe semântica POSIX de baixa latência."),
        ("Executar um servidor SMB t3.micro como ponto central.", "O servidor seria gargalo e ponto único, além de protocolo inadequado ao padrão HPC descrito."),
    ],
),
case(
    "Amazon Kinesis Data Streams",
    "Sensores enviam eventos continuamente e vários consumidores precisam processar o mesmo stream com baixa latência, preservando ordem por dispositivo e possibilidade de replay dentro da retenção. Qual serviço escolher?",
    "Usar Kinesis Data Streams, com device ID como partition key, capacidade dimensionada/on-demand e consumidores apropriados.",
    "Kinesis mantém registros ordenados por shard/partition key, permite múltiplos consumidores e replay durante o período de retenção.",
    "Cada sensor põe bilhetes numa esteira própria; várias equipes podem reler a sequência enquanto ela ainda está guardada.",
    "https://docs.aws.amazon.com/streams/latest/dev/introduction.html",
    "../labs/README.md — Streaming e processamento de eventos",
    "Uma partition key muito concentrada cria hot shard. SQS é excelente para filas de trabalho, mas normalmente cada mensagem é consumida como tarefa e não oferece o mesmo modelo de stream/replay.",
    [
        ("Usar uma única fila SQS e esperar que todos os consumidores recebam cada evento e possam reler a sequência.", "Uma fila distribui trabalho; fan-out e replay ordenado exigiriam outro desenho."),
        ("Gravar eventos em arquivos locais e copiá-los semanalmente.", "Isso não atende baixa latência, durabilidade gerenciada ou múltiplos consumidores."),
        ("Usar SNS sem assinantes duráveis nem retenção.", "SNS faz push, mas sozinho não fornece retenção e replay do stream."),
    ],
),
case(
    "Políticas de Auto Scaling",
    "Uma API em EC2 apresenta carga proporcional a requisições por target. A equipe quer manter cerca de 1.000 requisições por target, adicionando e removendo capacidade automaticamente. Qual política é mais simples?",
    "Usar target tracking no Auto Scaling com ALBRequestCountPerTarget definido para o valor desejado e warmup apropriado.",
    "Target tracking ajusta capacidade para manter a métrica perto do alvo e gerencia os alarmes subjacentes, reduzindo lógica manual.",
    "O gerente abre caixas até cada caixa ter mais ou menos a fila combinada e fecha os extras quando o movimento cai.",
    "https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html",
    "../labs/README.md — ALB, Auto Scaling e health checks",
    "Step scaling é útil quando a resposta precisa variar por faixas; scheduled/predictive scaling ajuda cargas previsíveis. Cooldown e warmup evitam oscilações.",
    [
        ("Usar somente scheduled scaling para uma carga totalmente imprevisível.", "Agendamento depende de horários conhecidos e não reage bem a rajadas imprevisíveis."),
        ("Criar uma instância por usuário autenticado.", "A relação não é operacionalmente adequada e ignora utilização agregada e limites."),
        ("Desabilitar health checks para evitar substituições durante picos.", "Isso mantém instâncias defeituosas e prejudica disponibilidade e desempenho."),
    ],
),
case(
    "Lambda provisioned concurrency",
    "Uma função Lambda síncrona atende uma API sensível à latência. Após períodos ociosos, cold starts ultrapassam o SLA; o volume do horário comercial é previsível. Qual recurso reduz essa variação?",
    "Configurar provisioned concurrency no alias/versão e, se adequado, escalá-la por agenda ou Application Auto Scaling.",
    "Provisioned concurrency mantém ambientes inicializados e prontos, reduzindo cold starts para invocações atendidas pela capacidade provisionada.",
    "Os cozinheiros ficam de avental e panela quente antes do primeiro pedido, em vez de abrir a cozinha do zero.",
    "https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html",
    "../labs/README.md — Lambda, API Gateway e desempenho",
    "Provisioned concurrency gera custo enquanto alocada; para cargas tolerantes a cold start, memória maior, código otimizado ou SnapStart em runtimes compatíveis podem ser melhores.",
    [
        ("Aumentar o timeout e assumir que isso inicializa a função antes da chamada.", "Timeout limita duração após invocação; não pré-inicializa ambientes."),
        ("Usar reserved concurrency como sinônimo de ambientes sempre aquecidos.", "Reserved concurrency protege/limita capacidade, mas não inicializa ambientes como provisioned concurrency."),
        ("Colocar respostas da função em um volume instance store.", "Lambda não fornece instance store persistente dessa forma e isso não elimina inicialização."),
    ],
),
case(
    "Athena, partições e formato colunar",
    "Consultas Athena leem logs no S3 particionados apenas em arquivos JSON grandes e escaneiam terabytes para filtrar um único dia e região. Como reduzir tempo e bytes processados?",
    "Converter dados para Parquet/ORC comprimido, particionar por campos usados em filtros e garantir partition pruning/projection nas consultas.",
    "Formatos colunares leem apenas colunas necessárias; partições permitem ignorar diretórios inteiros, reduzindo I/O, latência e custo por dados examinados.",
    "Em vez de ler todos os cadernos, organizamos gavetas por dia e guardamos cada assunto em colunas fáceis de pegar.",
    "https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html",
    "../labs/README.md — Data lake no S3 e consultas Athena",
    "Partições demais e arquivos minúsculos também prejudicam desempenho. Compactação e tamanho de arquivo devem ser equilibrados com paralelismo.",
    [
        ("Renomear JSON para .parquet sem transformar o conteúdo.", "A extensão não muda o formato físico nem habilita leitura colunar."),
        ("Usar SELECT * em todas as consultas para aumentar o cache.", "Ler todas as colunas aumenta dados examinados e normalmente piora custo e latência."),
        ("Mover logs para S3 Glacier Deep Archive e consultá-los diretamente a cada minuto.", "Objetos arquivados exigem restauração e não são adequados a consultas interativas contínuas."),
    ],
),
],
"D4": [
case(
    "S3 Lifecycle",
    "Logs são acessados diariamente por 30 dias, raramente até o primeiro ano e precisam ser retidos por sete anos. A equipe quer reduzir custo automaticamente sem scripts. Qual abordagem usar?",
    "Criar S3 Lifecycle para transicionar objetos às classes adequadas ao padrão de acesso e expirá-los somente após o prazo regulatório.",
    "Lifecycle automatiza transições e expiração por idade; a seleção deve considerar duração mínima, custo de recuperação e latência de cada classe.",
    "Caixas novas ficam na prateleira perto; depois vão ao depósito barato e, no prazo certo, são recicladas.",
    "https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
    "../labs/README.md — S3, lifecycle e otimização de custos",
    "Glacier Flexible Retrieval/Deep Archive reduzem armazenamento, mas cobram recuperação e não servem a acesso imediato. Transições muito precoces podem gerar cobranças mínimas.",
    [
        ("Manter tudo em S3 Standard para sempre porque todas as classes têm o mesmo preço.", "As classes têm preços e características diferentes; o padrão conhecido permite economizar."),
        ("Excluir os logs aos 30 dias apesar da retenção de sete anos.", "Isso viola o requisito regulatório."),
        ("Copiar os objetos diariamente para mais buckets Standard na mesma região.", "Cópias adicionais aumentam armazenamento sem implementar uma política de arquivamento econômica."),
    ],
),
case(
    "Savings Plans e Spot",
    "Uma plataforma tem uma base de compute estável 24x7 e jobs batch tolerantes a interrupção durante a madrugada. Qual combinação tende a otimizar custo sem comprometer a base?",
    "Cobrir a base previsível com Savings Plans e executar a capacidade batch flexível em Spot, com diversificação e tratamento de interrupções.",
    "Savings Plans descontam uso comprometido de compute; Spot aproveita capacidade excedente com grande desconto para workloads interrompíveis.",
    "Assinamos um passe barato para a viagem diária e compramos lugares promocionais para passeios que podem esperar.",
    "https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html",
    "../labs/README.md — Auto Scaling com On-Demand, Savings Plans e Spot",
    "Não se deve comprometer acima da base bem conhecida. Spot precisa checkpoints, múltiplos tipos/AZs e resposta ao interruption notice.",
    [
        ("Executar toda a base crítica apenas em uma única Spot Instance sem checkpoint.", "Interrupções podem remover toda a capacidade crítica."),
        ("Comprar compromisso para o pico máximo anual que dura uma hora.", "Compromisso ocioso destrói a economia; ele deve mirar uso consistente."),
        ("Usar Dedicated Hosts obrigatoriamente para qualquer job batch.", "Dedicated Hosts costumam ter custo maior e só se justificam por licença/compliance específicos."),
    ],
),
case(
    "RDS Reserved DB Instances",
    "Um banco RDS de produção possui classe e região estáveis, funciona continuamente e deve permanecer assim por pelo menos um ano. A empresa quer desconto sem redesenhar a aplicação. O que avaliar?",
    "Adquirir Reserved DB Instance para a configuração/família elegível após validar utilização, prazo e opção de pagamento.",
    "Reserved DB Instances oferecem desconto de faturamento para uso RDS previsível; não são uma instância física separada e não alteram a arquitetura.",
    "A mesma mesa é usada todo dia, então um plano anual sai mais barato que pagar diária.",
    "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html",
    "../labs/README.md — RDS, capacidade e custo",
    "Reserva reduz compute do RDS, mas armazenamento, I/O, backup e transferência podem continuar cobrados. Rightsizing deve vir antes do compromisso.",
    [
        ("Comprar Spot Instances para substituir diretamente a instância RDS gerenciada.", "RDS não oferece modelo Spot para a instância de banco gerenciada."),
        ("Criar uma read replica sem carga apenas para obter desconto.", "A réplica acrescenta custo; não cria desconto de compromisso."),
        ("Trocar para Multi-AZ exclusivamente para reduzir a fatura pela metade.", "Multi-AZ adiciona capacidade para alta disponibilidade e normalmente aumenta custo."),
    ],
),
case(
    "Custo de NAT e VPC endpoints",
    "Instâncias privadas baixam terabytes mensalmente do S3 através de NAT Gateways. A fatura mostra alto processamento de dados no NAT. Como reduzir o custo mantendo caminho privado?",
    "Criar Gateway VPC Endpoint para S3, atualizar route tables/policies e manter o NAT apenas para destinos que realmente exigem internet.",
    "O endpoint de gateway para S3 evita o processamento pelo NAT e não possui cobrança por hora, reduzindo custo e simplificando o caminho privado.",
    "Abrimos uma porta direta e gratuita para o depósito, então os caminhões não pagam mais o pedágio da estrada geral.",
    "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html",
    "../labs/README.md — VPC multi-AZ, NAT e endpoints",
    "Interface endpoints para outros serviços cobram por hora e dados, então seu custo deve ser comparado ao NAT e ao volume por AZ; alta disponibilidade do NAT também importa.",
    [
        ("Adicionar mais NAT Gateways e continuar roteando S3 por todos eles.", "Isso pode melhorar resiliência, mas não remove a cobrança de processamento responsável pelo custo."),
        ("Dar IP público às instâncias e remover todos os controles de saída.", "Isso altera a postura de segurança e não mantém o caminho privado."),
        ("Mover objetos para EBS em uma única instância para evitar S3.", "EBS não substitui armazenamento de objetos escalável e cria capacidade, disponibilidade e operação adicionais."),
    ],
),
case(
    "AWS Compute Optimizer",
    "Centenas de instâncias EC2 têm baixa utilização, mas a equipe não sabe quais podem ser reduzidas sem risco de memória ou performance. Ela quer recomendações baseadas em métricas antes de mudar tamanhos. Qual serviço usar?",
    "Ativar AWS Compute Optimizer, garantir métricas suficientes (incluindo memória com agente quando necessário) e testar as recomendações de rightsizing.",
    "Compute Optimizer analisa métricas e oferece recomendações de tipo/tamanho e risco; a validação em carga real evita reduzir capacidade cegamente.",
    "Um treinador observa cada atleta e sugere um tênis do tamanho certo, em vez de comprar o maior para todos.",
    "https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html",
    "../labs/README.md — Observabilidade e rightsizing",
    "Cost Explorer Rightsizing também ajuda na visão de custo. Recomendações são insumo, não autorização automática: sazonalidade, licenças e limites de rede precisam ser considerados.",
    [
        ("Reduzir todas as instâncias para t3.micro sem medir.", "Uma regra única ignora CPU, memória, rede, burst e requisitos diferentes."),
        ("Comprar Reserved Instances para todos os tamanhos atuais antes do rightsizing.", "Isso pode comprometer gasto em capacidade superdimensionada."),
        ("Usar AWS Budgets como ferramenta de benchmark de CPU e memória.", "Budgets alerta sobre custo/uso, mas não faz análise técnica de dimensionamento."),
    ],
),
case(
    "Capacidade do DynamoDB",
    "Uma tabela nova tem tráfego imprevisível e pode ficar horas ociosa antes de picos abruptos. A equipe não conhece a capacidade necessária e quer evitar administração inicial. Qual modo escolher?",
    "Começar com DynamoDB on-demand e, quando o padrão se tornar previsível e sustentado, comparar com provisioned capacity e auto scaling.",
    "On-demand cobra por requisição e ajusta capacidade automaticamente, sendo adequado a cargas novas, variáveis ou intermitentes sem planejamento de throughput.",
    "Pagamos cada passeio quando alguém chega, sem manter um ônibus vazio esperando o dia inteiro.",
    "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html",
    "../labs/README.md — DynamoDB, DAX e capacidade",
    "Provisioned pode custar menos em uso estável e previsível, especialmente com auto scaling e reserved capacity elegível. Hot keys continuam sendo problema de modelagem.",
    [
        ("Provisionar imediatamente o pico teórico máximo 24x7 sem métricas.", "Isso tende a pagar capacidade ociosa durante a maior parte do tempo."),
        ("Escolher uma chave constante porque on-demand elimina hot partitions.", "Modo de capacidade não corrige uma chave de partição mal distribuída."),
        ("Executar DynamoDB em uma EC2 Spot para pagar menos.", "DynamoDB é serviço gerenciado e não é implantado pelo cliente em EC2."),
    ],
),
case(
    "Snapshots EBS com Data Lifecycle Manager",
    "Volumes EBS precisam de snapshots diários, retenção por 35 dias e exclusão automática dos antigos. O processo atual usa scripts em uma instância que frequentemente falha. Qual opção reduz operação e custo?",
    "Usar Amazon Data Lifecycle Manager com tags para criar e expirar snapshots segundo a política.",
    "DLM automatiza ciclo de vida de snapshots EBS e AMIs com seleção por tags, eliminando servidor de agendamento e acúmulo indefinido.",
    "Um robô fotografa os cadernos todo dia e descarta sozinho as fotos que passaram do prazo.",
    "https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html",
    "../labs/README.md — EBS, snapshots e recuperação",
    "Snapshots são incrementais no armazenamento, mas cada snapshot aparece como ponto completo de restauração. A política precisa respeitar retenção e testes de restore.",
    [
        ("Manter todos os snapshots para sempre porque snapshots incrementais não custam.", "Blocos exclusivos ainda ocupam armazenamento e retenção infinita gera custo."),
        ("Usar instance store como destino durável dos backups.", "Instance store é efêmero e não é serviço de backup."),
        ("Criar uma instância maior apenas para executar o cron de snapshots.", "Isso aumenta custo e mantém uma automação desnecessariamente autogerenciada."),
    ],
),
case(
    "AWS Budgets e Cost Explorer",
    "FinOps precisa alertar quando a previsão mensal ultrapassar o orçamento e depois investigar quais serviços e tags explicam a variação. Qual combinação usar?",
    "Configurar AWS Budgets com alertas de custo previsto/real e usar Cost Explorer para analisar tendências, filtros, grupos e relatórios.",
    "Budgets compara gasto/uso com limites e envia alertas; Cost Explorer permite explorar a composição e a evolução dos custos.",
    "O alarme avisa que a mesada vai estourar, e a lupa mostra em quais brinquedos o dinheiro foi gasto.",
    "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html",
    "../labs/README.md — Budgets, tags e análise de custos",
    "Cost Anomaly Detection complementa com alertas de padrões incomuns. Tags precisam ser ativadas como cost allocation tags e a organização deve manter governança de marcação.",
    [
        ("Usar CloudTrail sozinho para calcular a previsão da fatura.", "CloudTrail registra APIs e não é ferramenta de previsão e análise financeira."),
        ("Usar security groups para impedir qualquer recurso de gerar custo.", "Security groups controlam rede e não funcionam como orçamento ou governança financeira."),
        ("Esperar a fatura fechar e analisar apenas uma vez por ano.", "Isso elimina alerta precoce e capacidade de correção durante o período."),
    ],
),
case(
    "S3 Intelligent-Tiering",
    "Milhões de objetos têm padrões de acesso desconhecidos e mudam ao longo do tempo. A aplicação exige acesso em milissegundos aos objetos ativos, e a equipe não quer criar regras por prefixo. Qual classe considerar?",
    "Usar S3 Intelligent-Tiering, habilitando tiers de archive opcionais apenas se a latência de recuperação for aceitável.",
    "Intelligent-Tiering monitora acesso e move objetos entre tiers automáticos sem cobrança de recuperação nos tiers de acesso frequente/infrequente, cobrando pequena taxa de monitoramento.",
    "Um bibliotecário observa quais livros são lidos e muda sozinho os pouco usados para estantes mais baratas.",
    "https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html",
    "../labs/README.md — S3, lifecycle e classes de armazenamento",
    "Objetos menores que 128 KB não são monitorados nem movidos automaticamente e permanecem no tier Frequent Access. Archive Access/Deep Archive Access têm recuperação assíncrona e devem ser habilitados conscientemente.",
    [
        ("Colocar tudo diretamente em Glacier Deep Archive e exigir leitura imediata.", "Deep Archive não oferece recuperação em milissegundos."),
        ("Duplicar cada objeto em todas as classes de armazenamento.", "Isso multiplica custo e não automatiza seleção do tier apropriado."),
        ("Usar EBS io2 para armazenar todos os objetos desconhecidos.", "EBS provisionado seria mais caro e não oferece a semântica/escala de armazenamento de objetos."),
    ],
),
case(
    "Arquitetura serverless para carga esporádica",
    "Uma API recebe poucas chamadas na maior parte do dia e picos curtos imprevisíveis. Não mantém conexões longas nem estado local. A equipe quer pagar principalmente por uso e não administrar servidores. Qual arquitetura é adequada?",
    "API Gateway com Lambda e um armazenamento serverless apropriado, configurando limites, observabilidade e controle de concorrência.",
    "Serviços serverless escalam sob demanda e cobram por requisição/execução, evitando instâncias ociosas para uma carga esporádica.",
    "A barraca abre e chama ajudantes só quando chegam clientes, em vez de pagar uma equipe vazia o dia inteiro.",
    "https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html",
    "../labs/README.md — Lambda, API Gateway e IAM roles",
    "Em carga alta e constante, contêineres/instâncias bem utilizados podem custar menos. Cold starts, limites de execução e dependências precisam ser avaliados.",
    [
        ("Manter dez instâncias On-Demand grandes 24x7 para o pico raro.", "A maior parte da capacidade ficaria ociosa e paga."),
        ("Usar Dedicated Hosts para cada requisição.", "Hosts dedicados são inadequados à granularidade e aumentariam drasticamente o custo."),
        ("Executar a API em um NAT Gateway.", "NAT Gateway é serviço de tradução de endereços, não runtime de aplicação."),
    ],
),
case(
    "Consolidated billing e compartilhamento de descontos",
    "Uma empresa possui muitas contas AWS e quer uma fatura consolidada, visão central de custos e melhor aproveitamento agregado de descontos elegíveis. Qual recurso usar?",
    "Gerenciar as contas com AWS Organizations e consolidated billing, estruturando OUs, tags e controles de compartilhamento de descontos.",
    "Organizations consolida cobrança e permite que uso agregado e compartilhamento elegível de descontos melhorem aproveitamento, além de centralizar relatórios.",
    "A família junta todas as compras numa conta só e aproveita melhor o cartão de desconto do supermercado.",
    "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html",
    "../labs/README.md — FinOps multi-conta e alocação de custos",
    "Consolidar não elimina a necessidade de chargeback/showback. Savings Plans/RI sharing pode ser configurado e políticas organizacionais não concedem permissões automaticamente.",
    [
        ("Compartilhar a senha do usuário raiz entre todas as equipes.", "Isso é inseguro e não cria organização ou faturamento consolidado."),
        ("Criar VPC peering entre contas para combinar as faturas.", "Peering conecta redes e não consolida cobrança."),
        ("Duplicar os mesmos compromissos em cada conta sem analisar uso agregado.", "Isso pode gerar excesso de compromisso e perde o benefício da visão consolidada."),
    ],
),
case(
    "EFS lifecycle e Infrequent Access",
    "Um sistema EFS Regional contém muitos arquivos antigos raramente lidos, mas eles ainda precisam aparecer no mesmo namespace POSIX. Como reduzir o custo sem migração manual?",
    "Configurar EFS lifecycle management para mover arquivos não acessados a IA/Archive conforme elegibilidade e, se adequado, voltar ao Standard no primeiro acesso.",
    "EFS lifecycle move dados frios para classes mais baratas mantendo o mesmo sistema de arquivos e acesso transparente à aplicação.",
    "Os brinquedos esquecidos vão para uma prateleira barata, mas continuam no catálogo e voltam quando alguém pede.",
    "https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html",
    "../labs/README.md — EFS, classes e custo",
    "Classes IA/Archive têm cobrança de acesso e são melhores para arquivos realmente frios. One Zone reduz custo adicional, mas muda a resiliência e não deve ser escolhido sem aceitar risco de AZ.",
    [
        ("Copiar manualmente arquivos para discos locais e apagar o EFS.", "Isso perde compartilhamento, durabilidade e automação do namespace existente."),
        ("Aumentar o throughput provisionado para reduzir armazenamento.", "Throughput e classe de armazenamento são dimensões diferentes; aumentar throughput pode elevar custo."),
        ("Criar um EFS novo para cada arquivo frio.", "Isso aumenta complexidade e não usa o lifecycle transparente disponível."),
    ],
),
],
}


# Pacote especial do Dia 1: fundamentos de VPC e networking. Mantido separado
# do banco por domínio para que os cronogramas tenham 10 IDs próprios e para
# evitar que uma regeneração transforme o pacote em simples cópia de um quiz.
DAY1_CATALOG = [
case(
    "Subnets públicas e Internet Gateway",
    "Uma instância web precisa receber conexões HTTPS diretamente da internet. A subnet já possui uma rota 0.0.0.0/0 para um Internet Gateway, mas a instância tem somente endereço IPv4 privado. O que falta para o caminho IPv4 funcionar, além das regras de segurança?",
    "Associar um endereço IPv4 público ou Elastic IP à interface da instância e manter a rota para o Internet Gateway.",
    "Para comunicação IPv4 direta pela internet, a subnet precisa de rota ao IGW e a interface precisa de endereço público mapeado; o IGW realiza a tradução entre o endereço público e o privado.",
    "A rua já chega ao portão, mas a casa ainda precisa de um número público para o entregador encontrá-la.",
    "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html",
    "../labs/README.md — VPC multi-AZ com subnets públicas e privadas",
    "Para a maioria dos servidores de aplicação, um ALB público e targets privados é mais seguro do que IPs públicos em cada instância.",
    [
        ("Criar apenas uma rota para um NAT Gateway na subnet pública.", "NAT Gateway fornece saída iniciada por recursos privados e não aceita conexões de entrada não solicitadas para a instância."),
        ("Associar um Gateway Endpoint do S3 à route table.", "O endpoint cria caminho privado para S3, não conectividade geral de entrada pela internet."),
        ("Habilitar VPC peering com a própria VPC.", "Uma VPC não faz peering consigo mesma, e peering não fornece acesso à internet."),
    ],
),
case(
    "NAT Gateway resiliente por AZ",
    "Instâncias em subnets privadas de duas AZs precisam baixar atualizações da internet. A empresa manterá NAT Gateways no modo zonal nesta janela e exige controles/rotas independentes por AZ. A solução deve sobreviver à falha de uma AZ e evitar tráfego cross-AZ. Qual desenho usar?",
    "Implantar um NAT Gateway zonal em subnet pública de cada AZ e rotear cada subnet privada para o NAT da mesma AZ.",
    "Um NAT Gateway zonal é resiliente dentro da AZ em que foi criado; um por AZ remove a dependência da outra AZ e evita cobrança/latência de tráfego cross-AZ.",
    "Cada bairro tem sua própria saída para a rodovia; se uma ponte fecha, o outro bairro ainda consegue sair.",
    "https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html",
    "../labs/README.md — VPC multi-AZ com NAT Gateway",
    "Um único NAT zonal custa menos, mas vira dependência de uma AZ e pode gerar tráfego entre zonas; endpoints VPC devem retirar do NAT o tráfego de serviços compatíveis. Regional NAT Gateway é uma alternativa atual para alta disponibilidade automática quando seus requisitos e modo são compatíveis.",
    [
        ("Usar um único NAT Gateway na primeira AZ para todas as subnets e chamá-lo de multi-AZ.", "O serviço é resiliente na AZ, mas a arquitetura passa a depender daquela AZ e cruza zonas."),
        ("Colocar o NAT Gateway em uma subnet privada sem rota ao Internet Gateway.", "Um NAT público precisa estar em subnet pública e alcançar o IGW para fornecer saída à internet."),
        ("Dar IP público a todas as instâncias privadas e remover seus security groups.", "Isso muda a postura de segurança e remove controles essenciais."),
    ],
),
case(
    "Planejamento de CIDR",
    "Três VPCs serão conectadas no futuro e também terão ligação com a rede on-premises 10.0.0.0/8. A equipe ainda pode escolher os CIDRs. Qual decisão reduz conflitos de roteamento e retrabalho?",
    "Reservar blocos RFC 1918 não sobrepostos para cada VPC e para on-premises, deixando espaço para crescimento antes de criar as redes.",
    "Conectividade roteada como peering, Transit Gateway e VPN depende de prefixos não sobrepostos; planejar IPAM e crescimento evita NAT complexo ou renumeração.",
    "Antes de desenhar ruas novas, damos números diferentes a cada bairro para o mapa não confundir dois lugares.",
    "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html",
    "../labs/README.md — VPC multi-AZ e plano de endereçamento",
    "AWS VPC IPAM ajuda a governar alocações em escala. Um CIDR maior oferece crescimento, mas também deve respeitar limites, segurança e disponibilidade de endereços.",
    [
        ("Usar 10.0.0.0/16 em todas as VPCs porque endereços privados podem sempre se sobrepor.", "Sobreposição impede roteamento direto inequívoco entre as redes."),
        ("Usar endereços públicos aleatórios sem possuí-los para evitar RFC 1918.", "Isso pode conflitar com destinos reais e não é prática de endereçamento válida."),
        ("Escolher /28 para toda VPC porque subnets podem conter qualquer quantidade de recursos.", "Um /28 tem poucos endereços e a AWS reserva cinco por subnet; dificilmente acomoda crescimento."),
    ],
),
case(
    "VPC Peering não transitivo",
    "A VPC A tem peering com B e B tem peering com C. Não existe peering direto entre A e C. Uma instância em A precisa falar com C usando o caminho por B. O que é verdadeiro?",
    "VPC peering não é transitivo; criar peering A–C e rotas/regras correspondentes ou adotar Transit Gateway para conectividade centralizada.",
    "Uma conexão de peering só roteia entre as duas VPCs participantes e não permite usar uma VPC como roteador transitivo.",
    "Ter uma ponte A–B e outra B–C não dá ao carro permissão automática para atravessar B; falta uma ligação válida A–C.",
    "https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html",
    "../labs/README.md — VPC peering e Transit Gateway",
    "Peering direto é simples para poucas VPCs; à medida que a malha cresce, Transit Gateway reduz a quantidade de conexões e tabelas distribuídas.",
    [
        ("Adicionar apenas uma rota A→C apontando para o peering A–B; B encaminhará automaticamente.", "O peering não oferece roteamento de borda a borda ou trânsito via uma terceira VPC."),
        ("Ativar DNS hostnames em B para transformar o peering em transitivo.", "DNS altera resolução, não a propriedade de roteamento transitivo."),
        ("Associar um Internet Gateway a B e usar endereços privados de C pela internet.", "IGW não roteia endereços privados entre VPCs nem corrige a não transitividade."),
    ],
),
case(
    "AWS Transit Gateway",
    "Quarenta VPCs e duas redes on-premises precisam de conectividade hub-and-spoke, segmentação entre produção e desenvolvimento e administração central de rotas. Qual serviço simplifica o desenho?",
    "Usar AWS Transit Gateway com attachments e route tables separadas para controlar quais segmentos se comunicam.",
    "Transit Gateway funciona como hub de roteamento regional para VPCs e conexões híbridas; múltiplas route tables permitem segmentação sem uma malha de peerings.",
    "Em vez de construir uma ponte entre cada par de cidades, todas chegam a uma rodoviária central com plataformas separadas.",
    "https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html",
    "../labs/README.md — Transit Gateway e VPC peering",
    "TGW cobra por attachment e dados processados; para duas VPCs simples, peering pode ser mais barato. TGW é regional, embora possa haver peering entre TGWs.",
    [
        ("Criar uma full mesh de peerings e esperar propagação transitiva entre todas as VPCs.", "Peerings não são transitivos e a malha cresce quadraticamente."),
        ("Usar CloudFront como roteador de pacotes privados entre VPCs.", "CloudFront é CDN HTTP(S), não um roteador de rede privada."),
        ("Associar todas as VPCs ao mesmo Internet Gateway.", "Um IGW pertence a uma VPC e não fornece hub privado multi-VPC."),
    ],
),
case(
    "Interface VPC Endpoints e Private DNS",
    "Instâncias privadas precisam chamar a API regional do Secrets Manager sem NAT ou internet. A aplicação usa o hostname público padrão do serviço e não deve ser alterada. O que configurar?",
    "Criar um Interface VPC Endpoint do Secrets Manager, habilitar Private DNS e permitir HTTPS no security group do endpoint a partir dos clientes.",
    "PrivateLink cria ENIs privadas nas subnets; Private DNS faz o hostname regional padrão resolver para esses endereços dentro da VPC.",
    "O nome da loja continua igual, mas o mapa interno passa a apontar para uma porta particular dentro do prédio.",
    "https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html",
    "../labs/README.md — VPC endpoints de gateway e interface",
    "Interface endpoints cobram por hora e dados e precisam de SG/DNS corretos. S3 e DynamoDB também oferecem gateway endpoints com outro modelo de custo.",
    [
        ("Criar um Gateway Endpoint genérico para qualquer API AWS.", "Gateway endpoints existem somente para serviços compatíveis como S3 e DynamoDB, não para Secrets Manager."),
        ("Habilitar apenas VPC Flow Logs e remover o NAT.", "Flow Logs observam tráfego, mas não criam caminho de rede."),
        ("Adicionar uma rota ao Internet Gateway e manter as instâncias sem endereço público nem NAT.", "Instâncias apenas com IPv4 privado não obtêm saída IPv4 pela internet dessa forma."),
    ],
),
case(
    "Referência de security group entre camadas",
    "Um ALB público encaminha tráfego a instâncias privadas cujo endereço muda com Auto Scaling. Somente requisições vindas do ALB devem alcançar a porta 8080 dos targets. Qual regra é mais robusta?",
    "No security group dos targets, permitir TCP 8080 tendo como origem o security group do ALB.",
    "Referenciar o SG do ALB autoriza interfaces que pertencem àquele grupo e acompanha endereços dinâmicos, evitando manter listas de IPs.",
    "A porta deixa entrar quem usa o crachá do balanceador, mesmo quando o número do carro muda.",
    "https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html",
    "../labs/README.md — ALB, Auto Scaling e health checks",
    "A referência não encaminha tráfego e não copia regras do SG de origem; é necessário configurar saída do ALB e entrada dos targets de forma coerente.",
    [
        ("Permitir 0.0.0.0/0 na porta 8080 porque as instâncias estão em subnet privada.", "Isso amplia desnecessariamente a origem e pode se tornar explorável por caminhos privados ou futuros."),
        ("Fixar os IPs atuais do ALB em uma NACL.", "IPs do ALB podem mudar e NACLs não aceitam referência a security group."),
        ("Permitir a porta 8080 apenas a partir do Internet Gateway.", "IGW não é uma origem válida de SG e os targets recebem tráfego das interfaces do ALB."),
    ],
),
case(
    "NACLs e portas efêmeras",
    "Após endurecer a NACL de uma subnet privada, instâncias conseguem iniciar conexões HTTPS, mas as respostas são descartadas. Security groups estão corretos. Qual característica deve ser verificada?",
    "Como NACLs são stateless, permitir também o tráfego de retorno nas portas efêmeras apropriadas e nos dois sentidos exigidos pelas regras ordenadas.",
    "A NACL avalia entrada e saída separadamente e não lembra conexões; uma sessão iniciada na porta 443 retorna a uma porta efêmera do cliente.",
    "A cancela confere a ida e a volta como viagens diferentes; liberar só a saída não abre a volta.",
    "https://docs.aws.amazon.com/vpc/latest/userguide/custom-network-acl.html",
    "../labs/README.md — VPC multi-AZ com SG e NACL",
    "Security groups são stateful e normalmente são o controle primário. Faixas efêmeras variam por cliente/sistema e regras estreitas demais causam falhas intermitentes.",
    [
        ("Remover a rota local da VPC para forçar o retorno pelo IGW.", "A rota local é necessária à comunicação interna e não corrige o caráter stateless."),
        ("Adicionar uma regra de deny com número menor que o allow e esperar que o allow vença.", "NACLs usam a primeira regra correspondente; o deny de número menor vencerá."),
        ("Trocar o security group por um que negue explicitamente portas efêmeras.", "SGs não possuem regras de deny e bloquear o retorno pioraria o problema."),
    ],
),
case(
    "ALB versus NLB",
    "Dois microserviços HTTP precisam compartilhar um endpoint e receber roteamento por host e caminho, como api.exemplo.com/pedidos e /catalogo. Qual balanceador atende diretamente?",
    "Usar Application Load Balancer com listeners HTTPS e regras de host/path para target groups separados.",
    "ALB opera na camada 7 e inspeciona host, caminho, headers e outros atributos HTTP para escolher o target group.",
    "O recepcionista lê o nome e o assunto da carta antes de mandá-la ao balcão correto.",
    "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html",
    "../labs/README.md — ALB, Auto Scaling e health checks",
    "NLB é apropriado para TCP/UDP/TLS, IPs estáticos, alta taxa e preservação de IP; ele não oferece a mesma riqueza de regras HTTP por caminho.",
    [
        ("Usar Network Load Balancer e criar regras nativas de caminho /pedidos e /catalogo.", "NLB trabalha em camada 4 e não roteia por caminho HTTP."),
        ("Usar um NAT Gateway como balanceador reverso HTTP.", "NAT fornece tradução para saída/entrada mapeada e não executa balanceamento de aplicação."),
        ("Usar Route 53 para inspecionar a URL completa após /.", "DNS resolve nomes e não recebe o caminho HTTP da requisição."),
    ],
),
case(
    "Route 53 Resolver híbrido",
    "Servidores on-premises precisam resolver nomes privados de uma VPC, e workloads na VPC precisam resolver o domínio corporativo interno. Já existe Direct Connect. Qual desenho DNS usar?",
    "Criar Route 53 Resolver inbound endpoint para consultas on-premises, outbound endpoint com rules para o domínio corporativo e encaminhar DNS pelos links híbridos.",
    "Inbound endpoints recebem consultas destinadas à resolução na VPC; outbound endpoints e forwarding rules enviam domínios selecionados aos resolvers on-premises.",
    "Dois intérpretes ficam em cada direção da ponte: um entende nomes da nuvem e outro leva nomes da empresa para casa.",
    "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html",
    "../labs/README.md — DNS híbrido, VPN e Direct Connect",
    "Direct Connect fornece transporte, não encaminhamento DNS automático. Regras podem ser compartilhadas via RAM e os endpoints devem usar múltiplas AZs para disponibilidade.",
    [
        ("Confiar que Direct Connect publica automaticamente todas as private hosted zones no DNS on-premises.", "A conexão de rede não cria a integração de resolução; endpoints e regras ainda são necessários."),
        ("Usar um Internet Gateway para enviar consultas do domínio interno à internet pública.", "Isso pode vazar nomes e não alcança necessariamente o resolver corporativo privado."),
        ("Criar apenas registros públicos para todos os hosts internos.", "Isso expõe metadados e não resolve o requisito de namespace privado bidirecional."),
    ],
),
]


class QuestionFactory:
    def __init__(self):
        self.global_serial = 0
        self.domain_serial = defaultdict(int)
        self.seen_prompts = set()

    def build(self, domain_code, question_id, local_index, answer_shift=0, item_override=None):
        self.global_serial += 1
        dserial = self.domain_serial[domain_code]
        self.domain_serial[domain_code] += 1
        item = item_override or CATALOG[domain_code][dserial % len(CATALOG[domain_code])]

        difficulty = DIFFICULTIES[(local_index + answer_shift) % len(DIFFICULTIES)]
        org = ORGS[(self.global_serial * 5 + dserial) % len(ORGS)]
        context = CONTEXTS[(self.global_serial * 7 + local_index) % len(CONTEXTS)]
        scale = SCALES[(self.global_serial * 3 + dserial) % len(SCALES)]
        qualifier = {
            "fácil": "Escolha a alternativa que atende diretamente ao requisito.",
            "média": "Considere o principal trade-off operacional e escolha a melhor solução.",
            "difícil": "Priorize simultaneamente o requisito explícito, o menor acoplamento operacional e o comportamento em falhas.",
        }[difficulty]
        prompt = f"{org.capitalize()} {context}. {scale} {item['stem']} {qualifier}"
        if prompt in self.seen_prompts:
            # Raro encontro de ciclos dos seletores de contexto. Acrescenta um
            # identificador narrativo sem mudar o requisito nem dar pista.
            prompt += f" Para rastreabilidade, o comitê registrou este caso como {question_id}."
        self.seen_prompts.add(prompt)

        desired = (local_index + answer_shift) % 4
        correct = item["options"][0]
        distractors = item["options"][1:]
        rotate = (self.global_serial + dserial) % 3
        distractors = distractors[rotate:] + distractors[:rotate]
        ordered = [None, None, None, None]
        ordered[desired] = correct
        free = [i for i in range(4) if i != desired]
        for pos, option in zip(free, distractors):
            ordered[pos] = option

        alternatives = {LETTERS[i]: ordered[i][0] for i in range(4)}
        explanations = {}
        for i, (_, rationale) in enumerate(ordered):
            label = LETTERS[i]
            explanations[label] = ("Correta — " if i == desired else "Incorreta — ") + rationale

        correct_letter = LETTERS[desired]
        technical = (
            f"{item['why']}\n\n"
            f"Trade-off: {item['tradeoff']} A decisão deve ser confirmada com métricas, limites de serviço e um teste de falha controlado."
        )
        return {
            "id": question_id,
            "tipo": "múltipla escolha — uma resposta",
            "dominio": DOMAINS[domain_code]["nome"],
            "codigo_dominio": domain_code,
            "topico": item["topic"],
            "dificuldade": difficulty,
            "tempo_sugerido_segundos": TIME_BY_DIFFICULTY[difficulty],
            "pontos": POINTS_BY_DIFFICULTY[difficulty],
            "enunciado": prompt,
            "alternativas": alternatives,
            "resposta_correta": correct_letter,
            "explicacao_tecnica": technical,
            "explicacao_crianca": item["child"],
            "feedback_acerto": (
                f"Acertou: {item['why']} Quando outra opção poderia valer: {item['tradeoff']} "
                f"Mnemônica: associe “{item['topic']}” ao requisito decisivo destacado no cenário."
            ),
            "feedback_erro": (
                f"A resposta correta é {correct_letter}. O erro típico aqui é escolher um serviço relacionado sem verificar o requisito decisivo. "
                f"Compare estado, escopo, consistência, recuperação e custo operacional. Revise todas as justificativas A–D e execute o exercício indicado."
            ),
            "explicacao_alternativas": explanations,
            "referencia_oficial": item["ref"],
            "referencia_lab": item["lab"],
            "exercicio_recomendado": (
                f"No {item['lab'].replace('../labs/README.md — ', 'lab ')}, monte uma prova de conceito de {item['topic']}; "
                "registre a métrica principal, provoque uma falha ou mudança de carga e explique por que uma alternativa incorreta não atende."
            ),
            "origem": "Cenário autoral criado para este projeto; não derivado de dumps de certificação.",
        }


def answer_distribution(questions):
    return dict(sorted(Counter(q["resposta_correta"] for q in questions).items()))


def difficulty_distribution(questions):
    return dict(sorted(Counter(q["dificuldade"] for q in questions).items()))


def domain_distribution(questions):
    return dict(sorted(Counter(q["codigo_dominio"] for q in questions).items()))


def assessment_payload(identifier, title, kind, questions, duration_minutes):
    return {
        "id": identifier,
        "titulo": title,
        "tipo": kind,
        "versao_exame": "AWS Certified Solutions Architect – Associate (SAA-C03)",
        "autoria": "Conteúdo original deste projeto; não reproduz questões reais nem dumps.",
        "instrucoes": [
            "Marque uma única alternativa (A, B, C ou D) por questão.",
            "Faça a primeira tentativa sem consultar o gabarito.",
            "Depois, leia a explicação de todas as alternativas e execute o exercício recomendado nos erros.",
        ],
        "quantidade_questoes": len(questions),
        "tempo_total_sugerido_minutos": duration_minutes,
        "pontos_totais": sum(q["pontos"] for q in questions),
        "distribuicao_dominios": domain_distribution(questions),
        "distribuicao_dificuldade": difficulty_distribution(questions),
        "distribuicao_gabarito": answer_distribution(questions),
        "questoes": questions,
    }


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def markdown_assessment(payload):
    lines = [
        f"# {payload['titulo']}", "",
        f"- **Tipo:** {payload['tipo']}",
        f"- **Questões:** {payload['quantidade_questoes']}",
        f"- **Tempo sugerido:** {payload['tempo_total_sugerido_minutos']} minutos",
        f"- **Autoria:** {payload['autoria']}", "",
        "## Instruções", "",
    ]
    lines += [f"- {x}" for x in payload["instrucoes"]]
    lines += ["", "---", ""]
    for number, q in enumerate(payload["questoes"], 1):
        lines += [
            f"## {number}. {q['topico']}", "",
            f"> **ID:** `{q['id']}` · **Domínio:** {q['codigo_dominio']} · **Dificuldade:** {q['dificuldade']} · "
            f"**Tempo:** {q['tempo_sugerido_segundos']} s · **Pontos:** {q['pontos']}", "",
            q["enunciado"], "",
        ]
        for letter in LETTERS:
            lines += [f"- **{letter})** {q['alternativas'][letter]}"]
        lines += [
            "", "<details>", "<summary>Gabarito e feedback detalhado</summary>", "",
            f"**Resposta correta:** {q['resposta_correta']}", "",
            "**Explicação técnica**", "", q["explicacao_tecnica"], "",
            f"**Como se fosse para uma criança:** {q['explicacao_crianca']}", "",
            f"**Se acertou:** {q['feedback_acerto']}", "",
            f"**Se errou:** {q['feedback_erro']}", "",
            "**Por que cada alternativa está certa ou errada**", "",
        ]
        for letter in LETTERS:
            lines += [f"- **{letter}:** {q['explicacao_alternativas'][letter]}"]
        lines += [
            "", f"**Referência oficial:** [{q['referencia_oficial']}]({q['referencia_oficial']})", "",
            f"**Referência prática:** {q['referencia_lab']}", "",
            f"**Exercício recomendado:** {q['exercicio_recomendado']}", "",
            "</details>", "", "---", "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def write_assessment(base_path, payload):
    write_json(base_path.with_suffix(".json"), payload)
    base_path.with_suffix(".md").write_text(markdown_assessment(payload), encoding="utf-8")


def weighted_order(counts):
    remaining = dict(counts)
    order = []
    while sum(remaining.values()):
        for code in DOMAINS:
            if remaining.get(code, 0) > 0:
                order.append(code)
                remaining[code] -= 1
    return order


def generate_quizzes(factory):
    all_questions = []
    index_rows = []
    for dpos, (code, meta) in enumerate(DOMAINS.items()):
        domain_dir = QUIZZES / meta["slug"]
        domain_dir.mkdir(parents=True, exist_ok=True)
        for quiz_no in range(1, 11):
            questions = []
            for qno in range(1, 6):
                local = qno - 1
                qid = f"QUIZ-{code}-{quiz_no:02d}-Q{qno:02d}"
                questions.append(factory.build(code, qid, local, answer_shift=(quiz_no + dpos) % 4))
            payload = assessment_payload(
                f"QUIZ-{code}-{quiz_no:02d}",
                f"Mini-quiz {quiz_no:02d} — {meta['nome']}",
                "mini-quiz por domínio",
                questions,
                10,
            )
            base = domain_dir / f"quiz-{quiz_no:02d}"
            write_assessment(base, payload)
            all_questions.extend(questions)
            index_rows.append((code, quiz_no, base.relative_to(QUIZZES).as_posix(), answer_distribution(questions)))

    bank = assessment_payload(
        "BANCO-QUIZZES-200",
        "Banco agregado — 200 questões dos mini-quizzes",
        "banco de questões (os mesmos IDs dos 40 mini-quizzes)",
        all_questions,
        400,
    )
    write_assessment(QUIZZES / "banco-200", bank)
    readme = [
        "# Mini-quizzes SAA-C03", "",
        "Este diretório contém **40 mini-quizzes autorais**, dez por domínio, com cinco questões cada: **200 questões únicas**. "
        "Cada quiz existe em JSON e Markdown; `banco-200.*` apenas agrega os mesmos IDs para busca/correção e não é conteúdo duplicado conceitualmente.", "",
        "| Domínio | Quiz | JSON | Markdown | Distribuição A–D |", "|---|---:|---|---|---|",
    ]
    for code, quiz_no, rel, distribution in index_rows:
        readme.append(
            f"| {code} | {quiz_no:02d} | [{rel}.json]({rel}.json) | [{rel}.md]({rel}.md) | "
            f"{', '.join(f'{k}:{v}' for k, v in distribution.items())} |"
        )
    readme += [
        "", "## Cobertura", "",
        "- D1: 50 questões — arquiteturas seguras.",
        "- D2: 50 questões — arquiteturas resilientes.",
        "- D3: 50 questões — arquiteturas de alto desempenho.",
        "- D4: 50 questões — arquiteturas otimizadas em custos.",
        "- Todos os cenários são originais e exigem decisão entre serviços, comportamento em falha, desempenho, segurança ou custo.",
    ]
    (QUIZZES / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    return all_questions


def generate_day1(factory):
    questions = []
    for i, item in enumerate(DAY1_CATALOG):
        questions.append(
            factory.build("D1", f"DIA01-Q{i+1:03d}", i, answer_shift=2, item_override=item)
        )
    payload = assessment_payload(
        "DIA-01-NETWORKING-10",
        "Dia 1 — Fundamentos de VPC e networking (10 questões)",
        "quiz de integração do cronograma — IDs próprios, fora do banco de 200",
        questions,
        20,
    )
    write_assessment(QUIZZES / "dia-01-10", payload)
    with (QUIZZES / "README.md").open("a", encoding="utf-8") as stream:
        stream.write(
            "\n## Pacote de integração do Dia 1\n\n"
            "- [`dia-01-10.json`](dia-01-10.json) / [`dia-01-10.md`](dia-01-10.md): "
            "10 questões adicionais com IDs `DIA01-Q001`–`DIA01-Q010`, dedicadas a VPC e networking. "
            "Elas não são contadas nas 200 questões dos 40 mini-quizzes.\n"
        )
    return questions


def generate_simulados(factory):
    produced = []
    diag_counts = {"D1": 12, "D2": 10, "D3": 10, "D4": 8}
    diag_questions = []
    for i, code in enumerate(weighted_order(diag_counts)):
        diag_questions.append(factory.build(code, f"DIAG-Q{i+1:03d}", i, answer_shift=0))
    diagnostic = assessment_payload(
        "DIAGNOSTICO-40", "Simulado diagnóstico — 40 questões", "diagnóstico inicial", diag_questions, 75
    )
    write_assessment(SIMULADOS / "diagnostico-40", diagnostic)
    produced.append(diagnostic)

    exam_counts = {"D1": 20, "D2": 17, "D3": 15, "D4": 13}
    for sim_no in range(1, 4):
        questions = []
        order = weighted_order(exam_counts)
        # desloca a ordem dos domínios sem alterar o peso e evita três provas com sequência idêntica
        offset = sim_no * 7
        order = order[offset:] + order[:offset]
        for i, code in enumerate(order):
            questions.append(factory.build(code, f"SIM{sim_no:02d}-Q{i+1:03d}", i, answer_shift=sim_no))
        payload = assessment_payload(
            f"SIMULADO-{sim_no:02d}-65",
            f"Simulado completo {sim_no:02d} — 65 questões",
            "simulado completo no estilo SAA-C03",
            questions,
            130,
        )
        write_assessment(SIMULADOS / f"simulado-{sim_no:02d}-65", payload)
        produced.append(payload)

    readme = [
        "# Simulados SAA-C03", "",
        "Questões autorais, sem reprodução de dumps. O diagnóstico segue a proporção 12/10/10/8; cada simulado completo usa 20/17/15/13, aproximação inteira dos pesos oficiais 30%/26%/24%/20%.", "",
        "| Arquivo | Questões | Tempo | D1/D2/D3/D4 | Gabarito A/B/C/D |", "|---|---:|---:|---|---|",
    ]
    for p in produced:
        name = "diagnostico-40" if p["id"] == "DIAGNOSTICO-40" else p["id"].lower()
        dd = p["distribuicao_dominios"]
        ad = p["distribuicao_gabarito"]
        readme.append(
            f"| [{name}.json]({name}.json) / [{name}.md]({name}.md) | {p['quantidade_questoes']} | "
            f"{p['tempo_total_sugerido_minutos']} min | {dd.get('D1',0)}/{dd.get('D2',0)}/{dd.get('D3',0)}/{dd.get('D4',0)} | "
            f"{ad.get('A',0)}/{ad.get('B',0)}/{ad.get('C',0)}/{ad.get('D',0)} |"
        )
    readme += [
        "", "## Uso recomendado", "",
        "1. Faça o diagnóstico no Dia 1 e registre domínio, tempo e tema de cada erro.",
        "2. Faça os simulados completos sem consulta, em uma sessão de 130 minutos.",
        "3. Para cada erro, leia A–D, realize o exercício recomendado e refaça a questão após 48 horas.",
        "4. Não memorize letras: a ordem das alternativas foi deliberadamente balanceada.",
        "5. `python tools/quiz_runner.py simulados/diagnostico-40.json` adia o feedback automaticamente em avaliações com mais de 10 questões, preservando o baseline. Use `--immediate-feedback` somente em revisão deliberada.",
    ]
    (SIMULADOS / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    return produced


def generate_flashcards():
    cards = []
    card_no = 0
    for code, cases in CATALOG.items():
        for item in cases:
            correct_text, _ = item["options"][0]
            first_wrong, first_wrong_reason = item["options"][1]
            variants = [
                (
                    f"Decisão — Em qual requisito {item['topic']} costuma ser a melhor resposta?",
                    item["why"],
                    item["child"],
                    f"Não escolha pelo nome do serviço; identifique o requisito que elimina as alternativas. {item['tradeoff']}",
                ),
                (
                    f"Solução — Qual implementação resume corretamente {item['topic']}?",
                    correct_text,
                    item["child"],
                    f"A implementação só está completa quando políticas, métricas e comportamento em falha também são verificados.",
                ),
                (
                    f"Trade-off — O que precisa ser lembrado ao usar {item['topic']}?",
                    item["tradeoff"],
                    item["child"],
                    "Uma resposta absoluta como 'sempre mais barato' ou 'sempre mais disponível' geralmente ignora o contexto.",
                ),
                (
                    f"Pegadinha — Por que esta alternativa não resolve {item['topic']}: “{first_wrong}” ?",
                    first_wrong_reason,
                    item["child"],
                    "Serviços vizinhos podem resolver parte do cenário, mas falham no requisito decisivo.",
                ),
                (
                    f"Ensine — Explique {item['topic']} em linguagem simples e depois dê a justificativa técnica.",
                    item["why"],
                    item["child"],
                    f"Mnemônica: conecte “{item['topic']}” à imagem da analogia infantil.",
                ),
            ]
            for front, technical, child, trap in variants:
                card_no += 1
                cards.append({
                    "id": f"FC-{card_no:03d}",
                    "dominio": DOMAINS[code]["nome"],
                    "codigo_dominio": code,
                    "topico": item["topic"],
                    "frente": front,
                    "verso_tecnico": technical,
                    "verso_crianca": child,
                    "pegadinha_de_prova": trap,
                    "referencia_oficial": item["ref"],
                    "referencia_lab": item["lab"],
                    "tags": [code, item["topic"], "SAA-C03"],
                })

    payload = {
        "titulo": "Flashcards SAA-C03",
        "quantidade": len(cards),
        "metodo_sugerido": "Repetição espaçada: errou = rever amanhã; hesitou = 3 dias; acertou com segurança = 7–14 dias.",
        "distribuicao_dominios": dict(sorted(Counter(c["codigo_dominio"] for c in cards).items())),
        "cards": cards,
    }
    write_json(FLASHCARDS / "flashcards.json", payload)

    md = [
        "# 240 flashcards SAA-C03", "",
        "> Use repetição espaçada. Diga a resposta em voz alta antes de abrir o verso e sempre conecte a decisão a um requisito do cenário.", "",
        f"**Distribuição:** {payload['distribuicao_dominios']}", "", "---", "",
    ]
    for card in cards:
        md += [
            f"## {card['id']} — {card['topico']}", "",
            f"> **Domínio:** {card['codigo_dominio']}", "",
            f"**Frente:** {card['frente']}", "",
            "<details>", "<summary>Ver verso</summary>", "",
            f"**Técnico:** {card['verso_tecnico']}", "",
            f"**Como criança:** {card['verso_crianca']}", "",
            f"**Pegadinha:** {card['pegadinha_de_prova']}", "",
            f"**Referência oficial:** [{card['referencia_oficial']}]({card['referencia_oficial']})", "",
            f"**Prática:** {card['referencia_lab']}", "", "</details>", "", "---", "",
        ]
    (FLASHCARDS / "flashcards.md").write_text("\n".join(md).rstrip() + "\n", encoding="utf-8")
    return cards


def validate_question(q):
    required = {
        "id", "dominio", "dificuldade", "tempo_sugerido_segundos", "pontos", "enunciado",
        "alternativas", "resposta_correta", "explicacao_tecnica", "explicacao_crianca",
        "feedback_acerto", "feedback_erro", "explicacao_alternativas", "referencia_oficial",
        "referencia_lab", "exercicio_recomendado",
    }
    missing = sorted(required - set(q))
    assert not missing, f"{q.get('id')}: campos ausentes {missing}"
    assert list(q["alternativas"].keys()) == list(LETTERS), q["id"]
    assert list(q["explicacao_alternativas"].keys()) == list(LETTERS), q["id"]
    assert q["resposta_correta"] in LETTERS, q["id"]
    assert q["alternativas"][q["resposta_correta"]], q["id"]
    assert q["dificuldade"] in {"fácil", "média", "difícil"}, q["id"]
    assert q["tempo_sugerido_segundos"] > 0 and q["pontos"] > 0, q["id"]


def clean_generated():
    for base in (QUIZZES, SIMULADOS, FLASHCARDS):
        base.mkdir(parents=True, exist_ok=True)
    # Limpa somente saídas conhecidas deste gerador; preserva arquivos alheios.
    for child in QUIZZES.glob("dominio-*"):
        if child.is_dir():
            shutil.rmtree(child)
    for pattern in ("banco-200.json", "banco-200.md", "README.md", "manifesto-avaliacoes.json"):
        path = QUIZZES / pattern
        if path.exists():
            path.unlink()
    for pattern in ("diagnostico-40.*", "simulado-??-65.*", "README.md"):
        for path in SIMULADOS.glob(pattern):
            if path.is_file():
                path.unlink()
    for pattern in ("flashcards.json", "flashcards.md"):
        path = FLASHCARDS / pattern
        if path.exists():
            path.unlink()


def main():
    clean_generated()
    factory = QuestionFactory()
    quiz_questions = generate_quizzes(factory)
    day1_questions = generate_day1(factory)
    simulated = generate_simulados(factory)
    cards = generate_flashcards()

    canonical_questions = quiz_questions + day1_questions + [q for p in simulated for q in p["questoes"]]
    for q in canonical_questions:
        validate_question(q)
    ids = [q["id"] for q in canonical_questions]
    assert len(ids) == len(set(ids)) == 445
    assert len(quiz_questions) == 200
    assert len(day1_questions) == 10
    assert len(simulated[0]["questoes"]) == 40
    assert all(len(p["questoes"]) == 65 for p in simulated[1:])
    assert len(cards) >= 200

    manifesto = {
        "gerador": "tools/generate_assessments.py",
        "conteudo_autoral": True,
        "mini_quizzes": 40,
        "questoes_mini_quizzes_unicas": len(quiz_questions),
        "questoes_dia_01_networking": len(day1_questions),
        "diagnostico_questoes": len(simulated[0]["questoes"]),
        "simulados_completos": 3,
        "questoes_por_simulado": [len(p["questoes"]) for p in simulated[1:]],
        "questoes_canonicas_totais_incluindo_dia_01": len(canonical_questions),
        "flashcards": len(cards),
        "gabarito_total": answer_distribution(canonical_questions),
        "dificuldade_total": difficulty_distribution(canonical_questions),
        "dominios_total": domain_distribution(canonical_questions),
        "validacoes": [
            "JSON serializado em UTF-8 e relido pelo parser",
            "IDs canônicos únicos",
            "quatro alternativas A-D",
            "resposta correta pertencente a A-D",
            "explicação individual de A-D",
            "todos os campos pedagógicos obrigatórios presentes",
        ],
    }
    write_json(QUIZZES / "manifesto-avaliacoes.json", manifesto)

    # Round-trip de todos os JSON materializados.
    for path in [*QUIZZES.rglob("*.json"), *SIMULADOS.rglob("*.json"), *FLASHCARDS.rglob("*.json")]:
        json.loads(path.read_text(encoding="utf-8"))
    print(json.dumps(manifesto, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
