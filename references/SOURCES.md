# Fontes, blueprint e simulados — AWS Certified Solutions Architect – Associate (SAA-C03)

> Pesquisa verificada em **14 de julho de 2026**. Preços, promoções, contagens de avaliações e catálogos podem mudar. Para fatos técnicos, a fonte de verdade deste projeto é sempre a documentação oficial da AWS.

## Política de fontes do projeto

Use esta ordem de precedência:

1. **Guia oficial do exame e lista oficial de serviços em escopo.**
2. **Documentação, FAQs, whitepapers e Well-Architected da AWS.**
3. **Questões oficiais de amostra e AWS Skill Builder.**
4. **Simulados originais de terceiros**, somente para treino de interpretação, ritmo e identificação de lacunas.
5. **Nunca usar dumps** como fonte de conteúdo, resposta ou inspiração para questões.

Quando uma explicação de terceiro divergir da documentação atual, prevalece a fonte oficial mais recente. Toda questão criada neste repositório deve ser original e deve citar ao menos uma referência oficial da AWS em sua explicação.

## Blueprint oficial atual

Fontes canônicas:

- [Guia oficial SAA-C03 em HTML](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) — versão viva e mais fácil de consultar.
- [Guia oficial SAA-C03 em PDF](https://d1.awsstatic.com/training-and-certification/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate_Exam-Guide.pdf) — snapshot oficial para arquivamento.
- [Página oficial da certificação](https://aws.amazon.com/certification/certified-solutions-architect-associate/) — duração, formato, preço, idiomas e preparação.
- [Serviços AWS atualmente em escopo](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html) — lista não exaustiva e sujeita a mudança.
- [Tecnologias e conceitos em escopo](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-technologies-concepts.html).
- [Serviços fora do escopo](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-out-of-scope-services.html).

### Domínios e pesos

| Domínio oficial | Peso do conteúdo pontuado | Tarefas oficiais |
|---|---:|---|
| **1. Design Secure Architectures** | **30%** | 1.1 Projetar acesso seguro aos recursos AWS; 1.2 projetar workloads e aplicações seguras; 1.3 determinar controles apropriados de segurança de dados. |
| **2. Design Resilient Architectures** | **26%** | 2.1 Projetar arquiteturas escaláveis e fracamente acopladas; 2.2 projetar arquiteturas altamente disponíveis e/ou tolerantes a falhas. |
| **3. Design High-Performing Architectures** | **24%** | 3.1 armazenamento; 3.2 computação elástica; 3.3 bancos de dados; 3.4 redes; 3.5 ingestão e transformação de dados de alto desempenho. |
| **4. Design Cost-Optimized Architectures** | **20%** | 4.1 armazenamento; 4.2 computação; 4.3 bancos de dados; 4.4 redes com otimização de custos. |

Links diretos para os detalhes de cada domínio: [Domínio 1](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain1.html), [Domínio 2](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain2.html), [Domínio 3](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html) e [Domínio 4](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain4.html).

### Formato do exame

| Item | Informação oficial |
|---|---|
| Duração | 130 minutos |
| Questões | 65 no total: 50 pontuadas e 15 não pontuadas, sem identificação entre elas |
| Tipos | Múltipla escolha (1 correta + 3 distratores) e múltiplas respostas (2 ou mais corretas em 5 ou mais opções) |
| Pontuação | Escala de 100 a 1.000; aprovação a partir de 720 |
| Penalidade por chute | Não há; resposta em branco conta como incorreta |
| Preço oficial observado | US$ 150, antes de impostos/conversão cambial |
| Experiência recomendada | Pelo menos 1 ano de experiência prática projetando soluções com serviços AWS |
| Idioma relevante | Português (Brasil) está entre os idiomas oferecidos |

## Os dois PDFs fornecidos

### 1. AWS Sample Questions — fonte oficial e recomendada

- Link direto: [AWS Certified Solutions Architect – Associate (SAA-C03) Sample Questions](https://d1.awsstatic.com/training-and-certification/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate_Sample-Questions.pdf).
- Proveniência: `d1.awsstatic.com`, publicado pela AWS.
- Conteúdo constatado: 10 questões de amostra SAA-C03, seguidas de respostas e justificativas.
- Uso recomendado: entender extensão, estilo de cenário, distratores e nível de trade-off. É um conjunto de amostra, não um simulado estatisticamente representativo.
- Regra deste projeto: referenciar o PDF e seus padrões, sem republicar integralmente as perguntas protegidas.

### 2. PDF rotulado “Exam Dump” no GitHub — não recomendado

- Link fornecido: [AWS Certified Solutions Architect Associate SAA-C03.pdf no GitHub](https://github.com/Iamrushabhshahh/AWS-Certified-Solutions-Architect-Associate-SAA-C03-Exam-Dump-With-Solution/blob/main/AWS%20Certified%20Solutions%20Architect%20Associate%20SAA-C03.pdf).
- Proveniência: repositório público de terceiro; **não é uma publicação da AWS**. A página o rotula como “Exam Dump” e não apresenta comprovação de autoria/licença ou método editorial.
- Decisão: o arquivo fica registrado apenas porque foi fornecido pelo usuário. **Não foi usado para extrair, validar, adaptar ou gerar perguntas.**

O [AWS Certification Program Agreement](https://aws.amazon.com/certification/certification-agreement/) classifica materiais de avaliação como confidenciais e proíbe possuir, acessar ou usar materiais não autorizados e divulgar conteúdo de exame. A própria AWS chama conteúdo real divulgado indevidamente de *brain dump* e alerta para riscos à integridade da certificação em [Protecting AWS Certification value through security measures](https://aws.amazon.com/blogs/training-and-certification/protecting-aws-certification-value-through-security-measures/). Violações podem levar a cancelamento de resultado, restrições ou exclusão do programa.

**Conclusão:** um dump não é fonte oficial, pode conter respostas erradas ou desatualizadas e pode violar as políticas da AWS. Use apenas questões oficiais ou simulados que afirmem produzir itens originais alinhados ao blueprint. Este repositório não copia questões protegidas.

## Simulados confiáveis — comparação de 7 opções

Critério de avaliação:

- **A:** escopo SAA-C03 atual demonstrável, bom volume, modos realistas e feedback detalhado/referenciado.
- **B:** opção útil e legítima, mas a página pública não demonstra algum item importante (atualização, volume ou profundidade do feedback), ou o simulado é apenas parte de uma assinatura ampla.
- **Oficial:** melhor calibração de estilo, mas não necessariamente o maior banco de questões.

Os preços abaixo foram observados em páginas públicas em 14/07/2026, em USD, antes de impostos. Confirme o checkout no Brasil; promoções e localização podem alterar o valor.

| Provedor e link direto | Evidências públicas | Feedback e atualização | Preço constatável | Avaliação e melhor uso |
|---|---|---|---|---|
| **AWS Skill Builder — Oficial**: [plano SAA](https://skillbuilder.aws/exam-prep/solutions-architect-associate), [assinaturas](https://skillbuilder.aws/subscriptions) e [FAQ de treinamento](https://aws.amazon.com/training/faqs/) | Conjunto oficial gratuito com 20 questões; pretest e Official Practice Exam têm o mesmo comprimento do exame real e geram relatório. | Desenvolvido pela AWS, com feedback sobre alternativas e recursos recomendados. É a melhor referência de estilo e rigor oficiais. | Conjunto de 20 questões: gratuito. Simulado completo: assinatura Individual, **US$29/mês** ou **US$449/ano**. | **Oficial — obrigatório como benchmark final.** Faça perto da prova, quando ainda houver tempo para corrigir lacunas. Limitação: menor volume que bancos de terceiros. |
| **Tutorials Dojo / Jon Bonso**: [SAA-C03 Practice Exams](https://portal.tutorialsdojo.com/product/aws-certified-solutions-architect-associate-practice-exams/) | 401 questões; modos timed, review, section-based, topic-based e randomized; flashcards; acesso por 1 ano. | Explicações completas, referências e cheat sheets declaradas; produto identificado como SAA-C03 2026. | Lista observada **US$14,99**; promoção temporária observada **US$11,99**. | **A — melhor custo-benefício para banco dedicado.** Bom para ciclos “simulado → análise de erros → revisão por tópico”. As respostas técnicas devem ser conferidas na documentação oficial quando houver ambiguidade. |
| **Stéphane Maarek + Abhishek Singh / Udemy**: [Practice Exams SAA-C03](https://www.udemy.com/course/practice-exams-aws-certified-solutions-architect-associate/) | 390 questões em conjuntos de 65; 4,5/5 e mais de 21 mil avaliações observadas. | Explicações detalhadas, suporte do instrutor e itens declarados como escritos do zero; atualização exibida **04/2026**. | A Udemy não expôs um preço público estável: varia por país, conta e promoção. | **A− — grande volume e boa segunda perspectiva.** Útil depois de uma primeira base teórica. Não trate nota de 90% anunciada pelo curso como garantia de aprovação. |
| **Digital Cloud Training / Neal Davis**: [trilha SAA-C03](https://digitalcloud.training/aws-certified-solutions-architect-associate/), [practice exams](https://digitalcloud.training/practice-exams/) e [preços](https://digitalcloud.training/plans-pricing/) | Banco com mais de 500 questões únicas; simulador final com 65 questões; exam mode, training mode e knowledge reviews; amostra gratuita de 20 questões. | Página declara alinhamento ao blueprint SAA-C03 e atualizações regulares; respostas com explicações e links de referência. | **US$24,99/mês** ou **US$149/ano** para a biblioteca. | **A− — melhor para quem quer curso + simulados.** Forte em revisão por área e explicação visual. Custa mais que um banco avulso se a meta for somente praticar questões. |
| **MeasureUp**: [Practice Test SAA-C03](https://www.measureup.com/saa-c03-aws-certified-solutions-architect-associate-practice-test.html) | 215 questões; modos Practice e Certification; personalização por domínio/tempo; tradução automática para português disponível. | Explica opções corretas e incorretas com referências online. A página exibe data de lançamento **12/2022**, sem uma data recente de revisão visível. | Preço regular **US$99**; promoção observada “a partir de **US$69,30**”. | **B+ — simulador sólido, porém caro e com risco de frescor.** Antes de comprar, confirme com o fornecedor a data da última revisão SAA-C03. A versão inglesa é a fonte autoral; traduções podem perder nuance. |
| **ExamPro / Andrew Brown**: [SAA-C03](https://www.exampro.co/saa-c03) | 3 simulados, 539 flashcards, 51,5 h de vídeo, 1 ano de acesso e um simulado gratuito para teste. | Página atual está rotulada SAA-C03, mas não publica contagem de questões nem profundidade das justificativas por alternativa. | Promoção observada **US$29**; lista **US$60**. Assinatura geral a partir de cerca de US$39/mês. | **B — bom pacote de estudo, não a primeira escolha como banco isolado.** Faça o exame gratuito e avalie a qualidade do feedback antes da compra. |
| **Pluralsight Cloud+ / A Cloud Guru**: [trilha SAA-C03](https://www.pluralsight.com/paths/aws-certified-solutions-architect-associate-saa-c03) e [preços individuais](https://www.pluralsight.com/individuals/pricing) | Trilha pública com 12 cursos, 6 labs, cerca de 97 horas e practice exam; novos labs publicados em 2026 e cursos modernizados em 2024–2025. | A página promete atualização contínua e feedback durante a experiência, mas não divulga o número de perguntas nem a cobertura das justificativas do simulado. | Cloud+ exibido por **US$29/mês** ou **US$299/ano**; teste gratuito de 10 dias disponível e com renovação automática se não for cancelado. | **B+ para trilha completa; B para simulado isolado.** Vale se também forem usados cursos, labs e sandbox. É excessivo se a necessidade for apenas um banco de questões. |

### Combinação recomendada

- **Orçamento mínimo:** PDF oficial de 10 questões + conjunto oficial gratuito de 20 + amostras gratuitas do Tutorials Dojo, Digital Cloud Training e ExamPro.
- **Melhor custo-benefício:** Tutorials Dojo como banco principal + um mês de AWS Skill Builder no final para o Official Practice Exam.
- **Preparação completa:** Digital Cloud Training **ou** Pluralsight para conteúdo/labs, Tutorials Dojo para volume e AWS Skill Builder para calibração final.
- **Perspectiva adicional:** Maarek/Udemy como segundo banco, sem repetir questões memorizadas.

Não é necessário comprar todos. Duas fontes com análise rigorosa de erros valem mais que centenas de questões respondidas sem revisão.

## Whitepapers, documentação e FAQs oficiais por domínio

Legenda de prioridade:

- **P0:** leitura-base antes dos simulados.
- **P1:** leitura orientada pelos erros dos simulados.
- **P2:** consulta pontual para comparar serviços e limites.

### Base comum aos quatro domínios

- **P0 — [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html):** princípios, trade-offs e processo de revisão arquitetural.
- **P0 — [Serviços SAA-C03 em escopo](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html):** conferir antes de cada ciclo de atualização do material.
- **P1 — [AWS Architecture Center](https://aws.amazon.com/architecture/):** arquiteturas de referência e padrões oficiais.
- **P2 — [AWS Product and Technical FAQs](https://aws.amazon.com/faqs/):** índice central das FAQs oficiais.

### Domínio 1 — Design Secure Architectures (30%)

Leitura principal:

- **P0 — [Security Pillar — Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html):** priorizar identidade, permissões, detecção, proteção de infraestrutura, proteção de dados e resposta a incidentes.
- **P0 — [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/):** distinguir segurança “da” nuvem e “na” nuvem.
- **P1 — [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html):** contas múltiplas, Organizations, guardrails, logging e serviços de segurança. A edição consultada é de dezembro de 2025.
- **P1 — [AWS Best Practices for DDoS Resiliency](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency.html):** CloudFront, Route 53, Global Accelerator, Shield, WAF, ELB e Auto Scaling em defesa em camadas.

FAQs para revisar após erros:

- [IAM](https://aws.amazon.com/iam/faqs/) — roles, credenciais temporárias, políticas, explicit deny, RBAC/ABAC, SCPs e Access Analyzer.
- [AWS Organizations](https://aws.amazon.com/organizations/faqs/) — contas, OUs, SCPs e billing consolidado.
- [AWS KMS](https://aws.amazon.com/kms/faqs/) — envelope encryption, tipos de chave, key policies, rotação e integrações.
- [Amazon VPC](https://aws.amazon.com/vpc/faqs/) — security groups, NACLs, endpoints, NAT, VPN e conectividade privada.
- [AWS WAF](https://aws.amazon.com/waf/faqs/) e [AWS Shield](https://aws.amazon.com/shield/faqs/) — camada 7 versus DDoS de rede/transporte.
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/faqs/) — armazenamento e rotação de segredos.
- [Amazon S3](https://aws.amazon.com/s3/faqs/) — policies, Block Public Access, criptografia, versionamento, Object Lock e replicação.

### Domínio 2 — Design Resilient Architectures (26%)

Leitura principal:

- **P0 — [Reliability Pillar — Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html):** fundações, arquitetura resiliente, gerenciamento de mudanças e recuperação comprovada.
- **P0 — [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/introduction.html):** RTO, RPO, alta disponibilidade versus DR e testes.
- **P1 — [DR options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html):** backup/restore, pilot light, warm standby e multi-site active/active.

FAQs para revisar após erros:

- [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/faqs/) — ALB, NLB, GWLB, health checks e cross-zone.
- [EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/faqs/) — target tracking, step/scheduled scaling, warmup e lifecycle.
- [Route 53](https://aws.amazon.com/route53/faqs/) — routing policies, health checks, failover e DNS.
- [Amazon SQS](https://aws.amazon.com/sqs/faqs/) — desacoplamento, Standard/FIFO, visibility timeout, DLQ e long polling.
- [Amazon RDS](https://aws.amazon.com/rds/faqs/) e [Aurora](https://aws.amazon.com/rds/aurora/faqs/) — Multi-AZ, réplicas de leitura, failover e endpoints.
- [AWS Backup](https://aws.amazon.com/backup/faqs/) — políticas, vaults, cópia cross-account/cross-Region e restore.
- [AWS Lambda](https://aws.amazon.com/lambda/faqs/) — concorrência, retries, DLQ/destinations e integração orientada a eventos.

### Domínio 3 — Design High-Performing Architectures (24%)

Leitura principal:

- **P0 — [Performance Efficiency Pillar — Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html):** seleção, compute, dados, rede, métricas e melhoria contínua.
- **P1 — [AWS service decision guides](https://aws.amazon.com/getting-started/decision-guides/):** comparações oficiais de serviços conforme padrão de acesso e requisitos.

FAQs de armazenamento e computação:

- [Amazon S3](https://aws.amazon.com/s3/faqs/) — classes, consistência, multipart upload, Transfer Acceleration e performance.
- [Amazon EBS](https://aws.amazon.com/ebs/faqs/) — tipos de volume, IOPS, throughput, snapshots e Multi-Attach.
- [Amazon EFS](https://aws.amazon.com/efs/faq/) — modos de performance/throughput, mount targets e classes.
- [Amazon EC2](https://aws.amazon.com/ec2/faqs/) — famílias, rede, storage e opções de capacidade.
- [AWS Lambda](https://aws.amazon.com/lambda/faqs/) — memória/CPU, concorrência, cold starts e limites.

FAQs de banco, rede e ingestão:

- [Amazon RDS](https://aws.amazon.com/rds/faqs/), [Aurora](https://aws.amazon.com/rds/aurora/faqs/), [DynamoDB](https://aws.amazon.com/dynamodb/faqs/) e [ElastiCache](https://aws.amazon.com/elasticache/faqs/) — escolher pelo padrão de acesso, consistência, escala, cache e réplicas.
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/faqs/) e [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/faqs/) — CDN/cache HTTP versus aceleração de rede com IPs anycast.
- [AWS Direct Connect](https://aws.amazon.com/directconnect/faqs/) e [Amazon VPC](https://aws.amazon.com/vpc/faqs/) — conectividade híbrida, throughput e topologia.
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/faqs/) — streaming, shards/on-demand, retenção e consumidores.
- [AWS DataSync](https://aws.amazon.com/datasync/faqs/) e [AWS Storage Gateway](https://aws.amazon.com/storagegateway/faqs/) — transferência online versus acesso híbrido persistente.
- [AWS Glue](https://aws.amazon.com/glue/faqs/) — catálogo, ETL e transformação de dados.

### Domínio 4 — Design Cost-Optimized Architectures (20%)

Leitura principal:

- **P0 — [Cost Optimization Pillar — Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html):** Cloud Financial Management, consciência de gastos, recursos econômicos, oferta/demanda e otimização contínua.
- **P1 — [Cost Optimization: Laying the Foundation (PDF)](https://docs.aws.amazon.com/pdfs/whitepapers/latest/cost-optimization-laying-the-foundation/cost-optimization-laying-the-foundation.pdf):** governança, visibilidade, accountability e controles.
- **P0 — [AWS Pricing Calculator](https://calculator.aws/):** comparar arquiteturas com região, volume, requests e data transfer explícitos.

FAQs e páginas de preço:

- [AWS Cost Explorer FAQ](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/faqs/) e [AWS Budgets FAQ](https://aws.amazon.com/aws-cost-management/aws-budgets/faqs/) — análise, forecast, alertas e ações.
- [Savings Plans FAQ](https://aws.amazon.com/savingsplans/faqs/) — compromisso versus flexibilidade; não confundir desconto com reserva de capacidade.
- [EC2 Spot](https://aws.amazon.com/ec2/spot/) e [como Spot funciona](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-spot-instances-work.html) — workloads tolerantes a interrupção, diversificação e aviso de interrupção.
- Páginas de preço de [EC2](https://aws.amazon.com/ec2/pricing/), [S3](https://aws.amazon.com/s3/pricing/), [RDS](https://aws.amazon.com/rds/pricing/), [DynamoDB](https://aws.amazon.com/dynamodb/pricing/), [VPC/NAT/endpoints](https://aws.amazon.com/vpc/pricing/) e [CloudFront](https://aws.amazon.com/cloudfront/pricing/).

Ao comparar custos, sempre verificar: horas/segundos de compute, armazenamento provisionado e consumido, IOPS/throughput, requests, recuperação de arquivo, duração mínima, NAT por hora e por GB, tráfego entre AZs/Regions e saída para a internet.

## Processo de manutenção das fontes

1. Revalidar o [guia oficial](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) e a [lista em escopo](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html) no início de cada mês e sete dias antes da prova.
2. Registrar a data da última verificação em todo quiz/simulado interno.
3. Corrigir ou retirar questões quando um serviço mudar de nome, comportamento, limite ou modelo de preço.
4. Usar preços somente como exemplos datados; labs devem orientar o uso da Pricing Calculator e incluir cleanup.
5. Não importar questões de PDFs, cursos, fóruns ou bancos pagos. Criar cenários originais a partir dos objetivos oficiais e da documentação AWS.
