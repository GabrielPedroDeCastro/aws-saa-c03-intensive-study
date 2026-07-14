# Dia 1 completo - intensivo

**Resultado do dia:** ambiente seguro, baseline mensurável, arquitetura VPC multi-AZ compreendida e validada, 10 questões corrigidas e plano dos dez pontos fracos. Duração sugerida: **10 horas líquidas + pausas**.

## Agenda

| Horário sugerido | Bloco | Entregável |
|---|---|---|
| 08:00-08:50 | Setup de conta, perfil, região e orçamento | `aws sts get-caller-identity` correto |
| 09:00-10:20 | Diagnóstico de 40 questões, sem consulta | arquivo de respostas |
| 10:30-11:20 | Correção e relatório por domínio | baseline + top 10 inicial |
| 11:30-12:20 | VPC: resumo técnico + desenho de memória | diagrama com 2 AZs |
| 12:20-13:30 | Almoço e tela desligada | pausa real |
| 13:30-16:30 | Lab 01 por CloudFormation **ou** Terraform | outputs e checkpoints 1-5 |
| 16:30-17:00 | Cleanup e confirmação de custo | nenhum recurso órfão |
| 17:10-18:00 | Repetição do fluxo com `plan`/validação do outro IaC, sem segundo deploy | diferenças registradas |
| 18:10-18:40 | Quiz Dia 1, 10 questões (15-20 min + revisão) | feedback de cada alternativa |
| 18:40-19:20 | Flashcards + diário de erros | 20 cards revisados |
| 19:20-19:40 | Plano do Dia 2 | três prioridades claras |

## VPC em duas camadas

### Explicação técnica

Uma VPC é um domínio de roteamento regional. O CIDR define o espaço de endereços; cada subnet pertence a uma única Availability Zone. Uma subnet é considerada pública quando sua route table envia `0.0.0.0/0` a um Internet Gateway. Separadamente, uma instância precisa de IPv4 público/Elastic IP para comunicar-se por IPv4 através desse IGW. A subnet privada do lab envia saída por um **public NAT Gateway zonal** situado em subnet pública; o NAT não aceita conexão iniciada da internet.

Route tables escolhem o próximo salto. Security Groups são stateful e protegem ENIs; NACLs são stateless, ordenadas e protegem a borda da subnet. DNS e DHCP options resolvem nomes, mas não criam conectividade. Para S3 e DynamoDB, um gateway endpoint pode evitar NAT; interface endpoints criam ENIs privadas para muitos outros serviços.

No modo zonal ensinado pelo lab, alta disponibilidade exige um NAT Gateway por AZ e a route table privada apontando ao NAT local. O **Regional NAT Gateway**, lançado depois do desenho clássico do exame, usa um único ID, expande automaticamente para as AZs com workloads e não precisa residir em subnet pública. O lab mantém o modo zonal para tornar rotas, dependência entre AZs e custo visíveis; compare ambos antes de um projeto real.

### Como criança

A VPC é uma cidade cercada. Subnets públicas são bairros com avenida até o portão; bairros privados só saem por um motorista NAT, que leva o pedido e traz a resposta, mas não deixa desconhecidos começarem uma visita. A tabela de rotas é o GPS, o Security Group é o porteiro que lembra quem entrou e a NACL é a cancela que checa ida e volta.

## O que saber antes do lab

- CIDRs não podem se sobrepor quando redes precisam conversar.
- Internet Gateway é altamente disponível, mas a rota e o IP público ainda são necessários.
- **Public NAT Gateway zonal** deve ficar em subnet pública com Elastic IP; o private NAT zonal não usa EIP e não fornece internet.
- **Regional NAT Gateway** não precisa de subnet pública e fornece expansão/afinidade zonal automática com um único ID; não oferece private NAT e tem disponibilidade regional própria.
- `0.0.0.0/0 -> igw` na subnet privada não torna uma instância sem IP público acessível, mas também não entrega a saída esperada via NAT.
- No modo zonal, uma route table privada por AZ permite NAT local e reduz dependência/custo cross-AZ; no modo regional, a mesma rota pode usar o único ID regional.
- SG permite apenas `allow`; NACL permite `allow/deny` e exige portas efêmeras.

## Executar

1. Abra [Lab 01 - VPC multi-AZ](../labs/01-vpc-multi-az-nat/README.md).
2. Escolha **um** motor de IaC e mantenha a região definida no lab.
3. Salve os outputs esperados, valide rotas/subnets/NAT e execute os testes do roteiro.
4. Faça cleanup antes de tentar o segundo motor. No Dia 1 basta validar (`terraform validate/plan` ou `aws cloudformation validate-template`) o segundo, sem implantá-lo.

## Quiz e diagnóstico

- [Diagnóstico de 40 questões](../simulados/diagnostico-40.md)
- [Quiz Dia 1 - 10 questões](../quizzes/dia-01-10.md)

Execução interativa:

```powershell
python tools/quiz_runner.py simulados/diagnostico-40.json
python tools/quiz_runner.py quizzes/dia-01-10.json
```

## Check-out obrigatório

- [ ] Sei explicar por que o **public NAT zonal do lab** fica na subnet pública e como o Regional NAT Gateway difere.
- [ ] Sei diferenciar rota, SG e NACL.
- [ ] Consigo desenhar duas AZs sem olhar o lab.
- [ ] Todos os checkpoints passaram.
- [ ] Cleanup confirmado no console e pela CLI.
- [ ] Corrigi as 10 questões explicando os quatro distratores.
- [ ] Meu relatório contém acertos, erros, tempo médio e top 10 fracos.
