# Guia por domínios - AWS Certified Solutions Architect - Associate (SAA-C03)

Verificado em **2026-07-14**. As faixas são didáticas e relativas. O total depende de região, duração, tráfego e quantidade. Confirme no AWS Pricing Calculator antes do deploy.

## Mapa do exame

| Domínio | Peso | Meta de estudo |
|---|---:|---|
| [D1 - Projetar arquiteturas seguras](#d1) | 30% | Controlar identidade, rede, dados e detecção aplicando privilégio mínimo e defesa em profundidade. |
| [D2 - Projetar arquiteturas resilientes](#d2) | 26% | Tolerar falhas, recuperar dados e escalar componentes desacoplados sem criar pontos únicos de falha. |
| [D3 - Projetar arquiteturas de alto desempenho](#d3) | 24% | Selecionar compute, armazenamento, banco, rede e ingestão compatíveis com o padrão real de acesso. |
| [D4 - Projetar arquiteturas otimizadas para custos](#d4) | 20% | Atender requisitos pelo menor custo total, eliminando desperdício sem sacrificar segurança ou resiliência necessárias. |

> Regra de prova: sublinhe requisito, restrição e palavra de decisão (mais resiliente, menor custo, menor esforço operacional ou maior desempenho). Elimine respostas tecnicamente possíveis que não otimizam o requisito pedido.

<a id="d1"></a>
## D1 - Projetar arquiteturas seguras (30%)

Controlar identidade, rede, dados e detecção aplicando privilégio mínimo e defesa em profundidade.

### IAM, federação e múltiplas contas

**Técnico.** IAM policies avaliam identidade, recurso, condições e negações explícitas. Roles entregam credenciais temporárias via STS; IAM Identity Center centraliza acesso humano; Organizations, OUs e SCPs criam limites de permissão entre contas.

**Como criança.** É um parque com pulseiras: cada pessoa ganha só as chaves dos brinquedos permitidos, e a regra do parque pode proibir uma porta mesmo que alguém tenha uma chave.

**Quando usar.** Acesso humano federado, workloads sem chaves longas, delegação cross-account e governança multi-account.

**Limitações.** SCP não concede permissão; define o teto. Resource policy, permissions boundary e session policy podem reduzir o acesso efetivo. Root user não é governado como um usuário IAM comum.

**Custo estimado.** IAM, STS e Organizations não têm tarifa direta; serviços auxiliares e logs podem cobrar.

**Melhores práticas.** MFA, roles temporárias, menor privilégio, contas separadas, Access Analyzer e bloqueio do root.

**Pegadinhas de prova.** Confundir autenticação com autorização; achar que SCP concede acesso; guardar access key em EC2 em vez de usar instance profile.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) · [AWS 2](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

### Segmentação de rede, SG, NACL e endpoints

**Técnico.** Security Groups são stateful e associados a ENIs; NACLs são stateless e atuam na borda da subnet com allow e deny ordenados. Public NAT Gateway zonal fica em subnet pública; Regional NAT Gateway usa um ID e expande entre AZs sem subnet pública. Gateway endpoints atendem S3/DynamoDB; interface endpoints usam PrivateLink e ENIs privadas.

**Como criança.** O segurança da casa lembra quem entrou; a cancela da rua checa cada ida e volta. Um túnel privado leva ao serviço sem passar pela avenida pública.

**Quando usar.** Isolar camadas, limitar portas, manter tráfego para serviços AWS privado e reduzir exposição/NAT.

**Limitações.** SG não oferece deny explícito. NACL exige portas efêmeras de retorno. Regional NAT não oferece private NAT e pode não estar disponível em todas as partições/regiões. Interface endpoints têm custo por hora e dados e são regionais.

**Custo estimado.** SG/NACL sem tarifa direta; gateway endpoint sem tarifa; interface endpoint é custo médio por AZ/hora e GB.

**Melhores práticas.** Referenciar SGs entre camadas, negar public IP por padrão, escolher conscientemente NAT zonal ou regional, usar endpoints privados e VPC Flow Logs para diagnóstico.

**Pegadinhas de prova.** Colocar public NAT zonal em subnet privada; achar que todo NAT atual exige subnet pública; bloquear resposta na NACL; achar que endpoint policy substitui IAM/resource policy.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) · [AWS 2](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) · [AWS 3](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html)

### Proteção de borda: CloudFront, WAF, Shield e Route 53

**Técnico.** CloudFront distribui e filtra conteúdo na borda; AWS WAF aplica regras L7; Shield Standard oferece mitigação DDoS básica automática; Route 53 entrega DNS e políticas de roteamento com health checks.

**Como criança.** São postos de entrega perto das crianças, com um porteiro que barra pedidos maldosos e um escudo contra multidões de robôs.

**Quando usar.** Aplicações globais, sites estáticos, APIs públicas, baixa latência e proteção HTTP/S.

**Limitações.** WAF não substitui autenticação nem corrige vulnerabilidade. CloudFront exige estratégia de cache/invalidação. Health check DNS não move estado de banco.

**Custo estimado.** CloudFront por dados/requests; WAF por Web ACL, regras e requests; Shield Standard incluído, Shield Advanced é alto custo fixo.

**Melhores práticas.** OAC para S3, TLS, managed rule groups, rate limit, logs amostrados e origin restrito ao CloudFront.

**Pegadinhas de prova.** Usar website endpoint S3 com OAC; confundir Global Accelerator L4 com CloudFront L7/cache; supor que WAF atua em NLB comum.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) · [AWS 2](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)

### Criptografia, KMS, ACM e segredos

**Técnico.** KMS gerencia chaves e envelope encryption; key policy é o controle primário. ACM provisiona certificados integrados e também certificados públicos exportáveis quando essa opção é habilitada na solicitação. Secrets Manager armazena e rotaciona segredos; Parameter Store atende configuração e segredos simples.

**Como criança.** O dado entra numa caixa com cadeado; o cofre guarda a chave-mestra e só empresta uma chavinha temporária a quem tem autorização.

**Quando usar.** Dados em repouso, TLS, controle/auditoria de chaves e credenciais rotacionáveis.

**Limitações.** KMS tem quotas e cobra chamadas; chaves são regionais, salvo multi-Region keys. Certificado público ACM só é exportável se solicitado com export habilitado; certificados emitidos antes do recurso ou sem essa opção permanecem não exportáveis.

**Custo estimado.** AWS owned keys geralmente sem mensalidade; customer managed keys e chamadas KMS cobram; Secrets Manager cobra por segredo e API; certificado público ACM exportável tem cobrança adicional conforme a página vigente.

**Melhores práticas.** Separar admins de usuários da chave, rotação, grants com cuidado, preferir integração ACM não exportável quando possível, proteger private keys exportadas, TLS obrigatório e nenhum segredo no código.

**Pegadinhas de prova.** Confundir alias com chave; esquecer key policy; afirmar que nenhum certificado público ACM pode ser exportado; escolher SSE-S3 quando a exigência pede controle/auditoria de CMK.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) · [AWS 2](https://docs.aws.amazon.com/acm/latest/userguide/acm-exportable-certificates.html) · [AWS 3](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

### Auditoria e detecção: CloudTrail, Config, GuardDuty e Macie

**Técnico.** CloudTrail registra chamadas de API; Config avalia configuração e histórico; GuardDuty detecta ameaças a partir de sinais; Security Hub agrega achados; Macie descobre dados sensíveis em S3; CloudWatch monitora métricas/logs/alarmes.

**Como criança.** Uma câmera grava quem mexeu, um fiscal compara a sala com as regras, e um detetive procura comportamentos estranhos.

**Quando usar.** Auditoria, conformidade, investigação, detecção de ameaça e resposta automatizada.

**Limitações.** Cada serviço observa um tipo de sinal; nenhum bloqueia tudo sozinho. Data events do CloudTrail e análise de dados podem elevar custo.

**Custo estimado.** Trilha de management events tem camada inicial; cópias, data events, Config items, GuardDuty e Macie cobram por uso.

**Melhores práticas.** Trilha organizacional multi-Region, logs imutáveis, alarmes críticos, agregador Config e resposta via EventBridge.

**Pegadinhas de prova.** Usar CloudWatch como trilha de auditoria completa; esperar prevenção do GuardDuty; ativar data events indiscriminadamente.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) · [AWS 2](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

<a id="d2"></a>
## D2 - Projetar arquiteturas resilientes (26%)

Tolerar falhas, recuperar dados e escalar componentes desacoplados sem criar pontos únicos de falha.

### Multi-AZ com ELB e Auto Scaling

**Técnico.** ALB distribui HTTP/S por targets saudáveis; Auto Scaling mantém capacidade e substitui instâncias. Subnets em duas ou mais AZs removem o servidor único como ponto de falha.

**Como criança.** Se uma lanchonete fecha, o atendente manda as crianças para outra e chama novos cozinheiros quando a fila cresce.

**Quando usar.** Web/API stateless, demanda variável e requisito de alta disponibilidade regional.

**Limitações.** Sessão local quebra elasticidade; health check mal ajustado causa substituição em loop; Multi-AZ não é multi-Region.

**Custo estimado.** ALB por hora/LCU e EC2 por capacidade; custo médio e elástico. Duas AZs podem gerar transferência entre AZs.

**Melhores práticas.** Imagens imutáveis, session store externo, target tracking, grace period e teste de falha de uma AZ.

**Pegadinhas de prova.** Confundir scale out com scale up; escolher NLB quando precisa roteamento por path; habilitar ASG em uma única AZ.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) · [AWS 2](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html)

### Desacoplamento com SQS, SNS e EventBridge

**Técnico.** SQS cria buffer e pull; SNS faz fanout push; EventBridge roteia eventos por regras e schema. DLQ isola falhas e idempotência torna reprocessamento seguro.

**Como criança.** Em vez de gritar pedido na cozinha, coloque bilhetes numa caixa; vários mensageiros podem copiar ou encaminhar cada bilhete.

**Quando usar.** Picos, processamento assíncrono, fanout, integração entre domínios e redução de dependência temporal.

**Limitações.** Standard entrega ao menos uma vez e pode duplicar; FIFO tem restrições/throughput próprios; visibilidade não é tempo de retenção.

**Custo estimado.** Baixo e por request/volume; payload grande deve ir para S3 com referência na mensagem.

**Melhores práticas.** Idempotência, DLQ/redrive, long polling, visibility timeout maior que processamento e métricas de idade.

**Pegadinhas de prova.** Esperar exactly-once de SQS Standard; usar SNS sem persistência quando consumidor pode ficar fora; apagar antes de concluir.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) · [AWS 2](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)

### Resiliência de dados: RDS, Aurora e DynamoDB

**Técnico.** RDS Multi-AZ fornece failover síncrono; read replicas escalam leitura de forma assíncrona. Aurora usa storage distribuído e endpoints. DynamoDB replica entre AZs por padrão e Global Tables atendem multi-Region ativo-ativo.

**Como criança.** Uma cópia pronta assume quando o caderno principal rasga; outras cópias servem só para muita gente ler ao mesmo tempo.

**Quando usar.** Bancos gerenciados com RTO/RPO, leitura escalável e continuidade regional.

**Limitações.** Standby Multi-AZ comum não atende leitura. Replica pode atrasar. Failover exige reconexão e testes no cliente.

**Custo estimado.** Multi-AZ e replicas elevam compute/storage; DynamoDB on-demand cobra por request e provisioned por capacidade.

**Melhores práticas.** Backups/PITR, endpoints em vez de IP, retry com backoff, proxy quando conexões são voláteis e teste de restore.

**Pegadinhas de prova.** Escolher read replica para HA síncrona; ler do standby; confundir backup com replica e durabilidade com disponibilidade.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) · [AWS 2](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)

### Backup e recuperação de desastre

**Técnico.** RPO mede perda de dados aceitável; RTO mede tempo de restauração. Estratégias evoluem de backup/restore para pilot light, warm standby e active-active, com custo e velocidade crescentes.

**Como criança.** É decidir quantas páginas podemos perder e quanto tempo a loja pode ficar fechada; uma loja reserva pronta custa mais, mas abre rápido.

**Quando usar.** Requisitos de continuidade, corrupção, exclusão acidental e falha regional.

**Limitações.** Snapshot sem restore testado não prova recuperação. Replicação também replica erros. DNS tem TTL e clientes podem cachear.

**Custo estimado.** Backup/restore é menor custo; active-active é maior. Storage, transferência e ambiente ocioso compõem a conta.

**Melhores práticas.** AWS Backup policies, cofres cross-account/Region, runbooks, restore drills e RPO/RTO mensuráveis.

**Pegadinhas de prova.** Escolher active-active sem requisito; afirmar RPO zero com replicação assíncrona; ignorar dependências e secrets no DR.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html) · [AWS 2](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)

### Conectividade híbrida e entre VPCs

**Técnico.** Peering conecta duas VPCs sem trânsito. Transit Gateway cria hub transitivo. Site-to-Site VPN usa internet criptografada; Direct Connect oferece circuito dedicado e pode combinar VPN para criptografia.

**Como criança.** Peering é uma ponte entre duas ilhas; o Transit Gateway é uma rodoviária central; VPN é um túnel secreto pela estrada pública.

**Quando usar.** Muitas VPCs, redes on-premises, segmentação por rotas e conectividade previsível.

**Limitações.** CIDRs sobrepostos impedem rotas simples; peering não é transitivo; DX não é criptografado por padrão e leva tempo para provisionar.

**Custo estimado.** Peering cobra transferência; TGW cobra attachment e dados; VPN por conexão/hora; DX tem porta e trânsito do provedor.

**Melhores práticas.** CIDR planejado, tabelas TGW segmentadas, VPN redundante, BGP e observabilidade de rotas.

**Pegadinhas de prova.** Tentar trânsito A-B-C via peering; escolher DX para implantação imediata; esquecer rotas nos dois lados.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) · [AWS 2](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)

<a id="d3"></a>
## D3 - Projetar arquiteturas de alto desempenho (24%)

Selecionar compute, armazenamento, banco, rede e ingestão compatíveis com o padrão real de acesso.

### Escolha de compute: EC2, Lambda, ECS/EKS e Fargate

**Técnico.** EC2 oferece controle de host; Lambda executa eventos sem servidor; ECS/EKS orquestram contêineres; Fargate remove gestão de instâncias. A escolha depende de duração, estado, portabilidade e controle.

**Como criança.** Você pode ter sua própria cozinha, alugar uma cozinha só por pedido ou usar caixas de almoço organizadas por um gerente.

**Quando usar.** EC2 para controle/legado, Lambda para eventos curtos, contêineres para portabilidade e serviços long-running.

**Limitações.** Lambda tem limite de duração, pacote e concorrência; Fargate tem combinações de CPU/memória; EKS adiciona complexidade operacional.

**Custo estimado.** EC2 por capacidade; Lambda por request/duração; Fargate por vCPU/memória. O mais barato depende de utilização.

**Melhores práticas.** Stateless, métricas de saturação, right-sizing, concurrency control, imagens pequenas e scaling por demanda.

**Pegadinhas de prova.** Escolher Lambda para job além do limite; assumir serverless sempre mais barato; usar target tracking com métrica que cai quando carga sobe.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) · [AWS 2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

### Escolha de armazenamento: S3, EBS, EFS e FSx

**Técnico.** S3 é object storage; EBS é bloco para uma AZ; EFS é NFS regional elástico; FSx oferece sistemas especializados como Windows, Lustre, NetApp e OpenZFS.

**Como criança.** S3 é um depósito de caixas, EBS é o disco preso a um computador e EFS é um armário compartilhado por várias salas.

**Quando usar.** Objetos/data lake, disco de SO/database, arquivos Linux compartilhados ou protocolo/workload especializado.

**Limitações.** S3 não é filesystem POSIX comum; EBS não atravessa AZ; EFS tem latência de rede; tipo e throughput precisam casar com workload.

**Custo estimado.** S3 é baixo por GB com requests; EBS provisiona GB/IOPS; EFS/FSx normalmente custam mais por GB e oferecem tiers.

**Melhores práticas.** Lifecycle, versioning, encryption, performance mode correto, snapshots e medir IOPS/throughput.

**Pegadinhas de prova.** Usar instance store para durabilidade; anexar EBS comum em outra AZ; escolher EFS para arquivo Windows SMB.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) · [AWS 2](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

### Performance de bancos e cache

**Técnico.** RDS/Aurora atendem relações/transações; DynamoDB atende chave-valor em escala; ElastiCache reduz leituras e sessões; DAX acelera DynamoDB com cache compatível; OpenSearch atende busca e analytics.

**Como criança.** O banco é a biblioteca; o cache deixa os livros mais pedidos na mesa, mas ainda precisamos saber qual exemplar é o verdadeiro.

**Quando usar.** Escolher pelo modelo de acesso, consistência, latência, escala e necessidade de joins ou busca textual.

**Limitações.** Cache traz invalidação; DynamoDB exige partition key bem distribuída; replicas têm lag; DAX não acelera writes nem consultas fora do padrão.

**Custo estimado.** Compute/IO/storage para relacional; capacidade/request para DynamoDB; nós por hora para caches.

**Melhores práticas.** Definir access patterns antes do schema, índices seletivos, connection pooling, TTL e evitar hot partitions.

**Pegadinhas de prova.** Adicionar DAX a write-heavy; usar read replica para consistência forte; achar que Multi-AZ melhora leitura.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html) · [AWS 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html)

### Rede global e entrega de conteúdo

**Técnico.** CloudFront usa cache L7; Global Accelerator fornece IPs anycast e backbone para TCP/UDP; Route 53 escolhe endpoints via políticas DNS; VPC endpoints encurtam caminhos privados a serviços.

**Como criança.** Um depósito próximo entrega cópias; uma via expressa global leva o carro ao melhor portão; placas DNS dizem para qual cidade ir.

**Quando usar.** Latência global, failover, aceleração de conteúdo dinâmico/estático e IPs globais estáveis.

**Limitações.** DNS depende de TTL; CloudFront só usa HTTP/S; Global Accelerator não armazena cache.

**Custo estimado.** CloudFront/GA por dados e recursos; Route 53 por zona/query/health check; transferência entre AZ/Region pode cobrar.

**Melhores práticas.** Cache key mínima, compressão, TLS, origin shield quando útil, health checks e testes por geografia.

**Pegadinhas de prova.** Escolher GA quando precisa cache; usar geolocation quando requisito é menor latência; confundir failover DNS com failover instantâneo.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) · [AWS 2](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)

### Ingestão e processamento: Kinesis, SQS, MSK e Glue

**Técnico.** Kinesis Data Streams atende streaming por shards e ordering por partition key; Amazon Data Firehose (antigo Kinesis Data Firehose) entrega lotes gerenciados; MSK executa Kafka; Glue cataloga e processa ETL; SQS desacopla tarefas.

**Como criança.** Pode ser uma esteira contínua, uma caixa de tarefas ou um caminhão que junta pacotes antes de levar ao depósito.

**Quando usar.** Telemetria em tempo real, eventos ordenados, ecossistema Kafka, ETL/data lake e filas de trabalho.

**Limitações.** Ordering é por shard/partition, não global automático; consumidores e retenção têm limites; MSK exige mais operação.

**Custo estimado.** Serverless/managed por volume, duração ou capacidade; MSK provisionado tem custo contínuo.

**Melhores práticas.** Partition key uniforme, backpressure, checkpoint, schema, DLQ e observabilidade do atraso do consumidor.

**Pegadinhas de prova.** Usar SQS para múltiplos consumidores receberem a mesma cópia sem SNS; confundir Amazon Data Firehose com stream de baixa latência bidirecional.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) · [AWS 2](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

<a id="d4"></a>
## D4 - Projetar arquiteturas otimizadas para custos (20%)

Atender requisitos pelo menor custo total, eliminando desperdício sem sacrificar segurança ou resiliência necessárias.

### Custo de compute e modelos de compra

**Técnico.** On-Demand é flexível; Savings Plans e Reserved Instances trocam compromisso por desconto; Spot usa capacidade interrompível; Auto Scaling e right-sizing ajustam quantidade; Graviton pode melhorar preço/desempenho.

**Como criança.** Pague uma corrida avulsa, compre um passe mensal ou aceite sair do brinquedo quando o parque precisar do assento em troca de desconto.

**Quando usar.** Base estável para compromissos, jobs tolerantes a interrupção para Spot e picos imprevisíveis para On-Demand.

**Limitações.** Compromisso pode virar desperdício; Spot pode interromper; licença/arquitetura pode impedir Graviton.

**Custo estimado.** Varia de alto/flexível a baixo/comprometido; meça utilização antes de comprar compromisso.

**Melhores práticas.** Compute Optimizer, cobertura gradual, mix ASG, checkpoint em Spot e desligamento agendado de ambientes não produtivos.

**Pegadinhas de prova.** Comprar RI para carga ainda desconhecida; usar Spot em banco único; confundir Standard RI com flexibilidade de Savings Plans.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) · [AWS 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

### Classes S3, lifecycle, EBS e snapshots

**Técnico.** S3 Standard, Intelligent-Tiering e classes IA/Archive equilibram acesso, duração mínima e recuperação. Lifecycle move/expira objetos. EBS cobra capacidade provisionada e snapshots incrementais.

**Como criança.** Brinquedos diários ficam na prateleira; os de férias vão ao armário; os raros vão ao depósito barato, mas demoram para voltar.

**Quando usar.** Dados com frequência previsível ou desconhecida, retenção regulatória, backup e volumes subutilizados.

**Limitações.** IA/Archive têm duração mínima, tamanho mínimo ou taxa de recuperação; apagar cedo pode cobrar; snapshot não reduz volume atual.

**Custo estimado.** Hot tier custa mais por GB e menos para acessar; archive faz o inverso. Intelligent-Tiering cobra monitoramento por objeto elegível.

**Melhores práticas.** Analytics/inventory, lifecycle testado, abort multipart uploads, gp3 em vez de gp2 quando adequado e excluir snapshots órfãos.

**Pegadinhas de prova.** Glacier para leitura imediata frequente; Intelligent-Tiering para objetos minúsculos de vida curta; esquecer taxa de retrieval.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) · [AWS 2](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

### Custo de bancos de dados

**Técnico.** Right-sizing, instâncias reservadas, Aurora Serverless v2, DynamoDB on-demand/provisioned+auto scaling e a classe DynamoDB Standard-IA para tabelas pouco acessadas ajustam custo ao padrão de carga; políticas de backup e retenção são tratadas separadamente.

**Como criança.** Não alugue um salão gigante para duas pessoas; use uma sala que cresce quando os convidados chegam.

**Quando usar.** Cargas variáveis, ambientes sazonais, base previsível e bancos superdimensionados.

**Limitações.** Serverless não zera necessariamente; mínimo de capacidade existe. Reserva reduz flexibilidade. I/O e storage podem dominar compute.

**Custo estimado.** Medir CPU, memória, conexões, IOPS e requests; não otimizar apenas o tamanho da instância.

**Melhores práticas.** Performance Insights, auto scaling, pausa/desligamento quando suportado, retenção de backup consciente e proxy apenas se necessário.

**Pegadinhas de prova.** Read replica para economizar; provisioned DynamoDB sem auto scaling para tráfego imprevisível; ignorar custo de I/O Aurora.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) · [AWS 2](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-cost-optimization.html)

### Transferência, NAT Gateway e topologia de rede

**Técnico.** Transferência cross-AZ/Region, processamento por NAT/TGW e egress à internet acumulam custo. Public NAT zonal compartilhado pode criar tráfego cross-AZ; Regional NAT mantém afinidade zonal automaticamente. Gateway endpoints evitam NAT para S3/DynamoDB; CloudFront pode reduzir egress do origin.

**Como criança.** Cada pedágio parece pequeno, mas passar por três pontes para entregar a caixa ao vizinho deixa a viagem cara.

**Quando usar.** Arquiteturas com alto volume, muitos serviços privados, tráfego entre AZs ou distribuição global.

**Limitações.** Centralizar um NAT zonal/TGW pode economizar recursos e aumentar processamento/cross-AZ; Regional NAT simplifica HA, mas continua cobrando processamento e não substitui private NAT. Endpoint por AZ também tem custo. Otimize após medir.

**Custo estimado.** NAT/TGW/interface endpoint têm hora e/ou GB; gateway endpoint não tem tarifa; egress e cross-AZ variam por serviço/região.

**Melhores práticas.** Cost and Usage Report, flow logs, endpoints corretos, manter tráfego local à AZ quando seguro e cache na borda.

**Pegadinhas de prova.** NAT zonal único cross-AZ como 'mais barato' sem contar dados e resiliência; ignorar Regional NAT como alternativa atual; interface endpoint para S3 quando gateway atende; ignorar retorno assimétrico.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html) · [AWS 2](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) · [AWS 3](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer)

### Governança financeira e Well-Architected

**Técnico.** Tags/cost allocation, Cost Explorer, Budgets, Cost Anomaly Detection, CUR e Cost Optimization Hub tornam gasto atribuível. O pilar Cost Optimization trata prática de gestão, demanda, oferta e evolução.

**Como criança.** Coloque etiquetas em cada brinquedo, defina um cofrinho e peça um alarme quando alguém gastar rápido demais.

**Quando usar.** Showback/chargeback, alertas, detecção de anomalia, priorização de savings e revisão contínua.

**Limitações.** Budget alerta, mas não bloqueia por padrão. Tags precisam ser ativadas e não retroagem totalmente. Recomendações exigem contexto de negócio.

**Custo estimado.** Ferramentas básicas têm recursos gratuitos; CUR gera storage/query e ações automatizadas podem afetar disponibilidade.

**Melhores práticas.** Owner/cost-center obrigatórios, orçamento por conta, revisão semanal, KPIs unitários e Well-Architected Review trimestral.

**Pegadinhas de prova.** Tratar Budget como limite rígido; desligar recurso crítico só por baixa CPU; otimizar custo antes de requisitos de segurança/RTO.

**Documentação oficial.** [AWS 1](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html) · [AWS 2](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)

## Como transformar leitura em decisão

1. Explique o tópico sem siglas usando a analogia.
2. Desenhe a menor arquitetura que atende o requisito.
3. Nomeie uma limitação, uma cobrança e uma falha possível.
4. Resolva cinco questões e registre por que descartou cada distrator.
5. Execute o lab relacionado e comprove os checkpoints antes do cleanup.

Volte ao [README](README.md), escolha um [cronograma](schedules/README.md) ou abra a [landing page HTML](docs/index.html).
