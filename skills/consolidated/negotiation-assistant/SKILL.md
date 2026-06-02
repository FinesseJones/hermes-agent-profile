---
name: negotiation-assistant
description: Suporte à negociação de propostas imobiliárias. Cobre técnicas de negociação, gestão de objeções, contra-propostas, e estratégias de fechamento. Use quando lead estiver em fase de proposta ou negociação.
allowed-tools: Read, Glob, Grep
skills: real-estate-qualification, property-matching
---

# Negotiation Assistant - Assistente de Negociação Imobiliária

> **Filosofia:** Negociação boa é quando os dois lados sentem que ganharam.
> **Princípio Central:** Nunca vá direto para o preço. Construa valor primeiro.

---

## 🎯 As 4 Fases da Negociação Imobiliária

```
ÂNCORA → EXPLORAÇÃO → CONCESSÃO → FECHAMENTO
   ↓          ↓            ↓           ↓
 Proposta   Objeções    Ajustes    Contrato
 inicial    surgem      mútuos     assinado
```

| Fase | Duração Típica | Objetivo |
|------|----------------|----------|
| **Âncora** | 1 dia | Estabelecer ponto de partida |
| **Exploração** | 2-5 dias | Entender limites reais |
| **Concessão** | 1-3 dias | Ceder estrategicamente |
| **Fechamento** | 1-2 dias | Formalizar acordo |

---

## 💰 Estrutura de Proposta

### Elementos de Uma Proposta

```typescript
interface PropostaImobiliaria {
  // Valor
  valorProposto: number;
  valorPedido: number;
  desconto: number; // percentual
  
  // Pagamento
  sinalValor: number;
  sinalData: Date;
  formaPagamento: 'avista' | 'financiamento' | 'direto' | 'misto';
  prazoFinanciamento?: number; // meses
  bancoFinanciamento?: string;
  
  // Condições
  condicoes: string[]; // "Sujeito a vistoria", "Inclui mobília", etc
  prazoResposta: Date;
  validadeProposta: Date;
  
  // Status
  status: 'enviada' | 'contraproposta' | 'aceita' | 'recusada' | 'expirada';
}
```

### Faixas de Desconto por Contexto

| Contexto | Desconto Esperado | Sinal de Risco |
|----------|-------------------|----------------|
| Lançamento em pré-venda | 0-5% | >5% = problema |
| Imóvel novo (pronta entrega) | 3-8% | >10% = desesperado |
| Imóvel usado (bom estado) | 5-10% | >15% = superavaliado |
| Imóvel usado (precisa reforma) | 10-20% | >25% = negócio ruim |
| Imóvel há muito tempo no mercado | 10-15% | Normal |
| Compra à vista | +3-5% extra | Esperado |

---

## 🗣️ Gestão de Objeções

### As 10 Objeções Mais Comuns

#### 1. "O preço está muito alto"

```
NUNCA: "É o preço de mercado" (defensivo)

MELHOR: "Entendo sua preocupação com o valor. 
        Me ajuda a entender: você está comparando 
        com outros imóveis da região ou tem um 
        orçamento específico em mente?"

DESCOBRIR: É objeção real ou tática de negociação?
```

**Se for real:**
- Mostrar comparativos de mercado
- Destacar diferenciais do imóvel
- Explorar formas de pagamento

**Se for tática:**
- Manter posição com argumentos
- Ceder em condições, não em preço

#### 2. "Preciso pensar"

```
NUNCA: "Ok, pense e me liga" (perde o lead)

MELHOR: "Claro! Para te ajudar a decidir, 
        o que especificamente você precisa analisar?
        É o valor, a localização, ou alguma característica?"

OBJETIVO: Descobrir a objeção real escondida
```

#### 3. "Vou ver outros imóveis"

```
NUNCA: "Tudo bem, boa sorte" (desiste fácil)

MELHOR: "Faz total sentido comparar! 
        Inclusive, o que você está buscando que 
        este imóvel não atendeu completamente?
        Posso te indicar outras opções também."

OBJETIVO: Entender o gap, ajustar match
```

#### 4. "Meu marido/esposa precisa ver"

```
NUNCA: Ignorar ou pressionar a decisão

MELHOR: "Claro! Quando ele(a) poderia vir?
        Posso já deixar agendado."

OBJETIVO: Incluir o decisor, não perder momentum
```

#### 5. "O condomínio está muito caro"

```
ESTRATÉGIA: Contextualize o custo

RESPOSTA: "Entendo. O condomínio é de R$X porque inclui 
          [listar itens: piscina, academia, portaria 24h].
          Se você fosse pagar separado, custaria mais.
          Mas se custo recorrente é prioridade, 
          tenho opções com condomínio mais baixo."
```

#### 6. "Precisa de muita reforma"

```
ESTRATÉGIA: Transformar problema em oportunidade

RESPOSTA: "Por isso o valor está [X% abaixo] da média.
          Na prática, você economiza Y e pode reformar 
          exatamente do seu jeito. Quer que eu estime 
          o custo de reforma?"
```

#### 7. "A localização não é ideal"

```
ESTRATÉGIA: Explorar prioridades

RESPOSTA: "O que seria a localização ideal para você?
          Às vezes o 'perfeito' não existe, mas podemos 
          ver o que pesa mais: preço, tamanho ou local."
```

#### 8. "Estou esperando os preços caírem"

```
ESTRATÉGIA: Dados + escassez

RESPOSTA: "Entendo a preocupação. Nos últimos 12 meses,
          imóveis nessa região [valorizaram X%].
          Além disso, esse tipo de imóvel é raro.
          Mas posso te manter informado sobre o mercado."
```

#### 9. "A entrada é muito alta"

```
ESTRATÉGIA: Explorar alternativas

RESPOSTA: "Qual valor de entrada seria confortável?
          Algumas construtoras parcelam a entrada.
          E se usar FGTS, consegue diminuir."
```

#### 10. "Preciso vender meu imóvel primeiro"

```
ESTRATÉGIA: Oferecer solução

RESPOSTA: "Isso é comum! Posso já avaliar seu imóvel 
          para venda e trabalhar os dois em paralelo.
          Em alguns casos, conseguimos uma ponte."
```

---

## 🔄 Estratégias de Contra-Proposta

### Quando o Vendedor Recusa

```
AVALIAR:
├── Proposta foi muito baixa? (>15% desconto)
│   └── Subir, mas pedir algo em troca
│
├── Vendedor inflexível no preço?
│   └── Negociar condições (prazo, mobília, etc)
│
└── Gap muito grande? (>20% diferença)
    └── Posicionar: "Até X é o máximo possível"
       Se não aceitar, não era para ser
```

### Táticas de Concessão

| Tática | Como Usar |
|--------|-----------|
| **Salame** | Ceder aos poucos, não tudo de uma vez |
| **Troca** | "Aceito X se você incluir Y" |
| **Prazo** | "Pago o valor se der 30 dias a mais" |
| **Pacote**| "No valor X, quero mobília + eletros" |
| **À vista** | "Pago X, mas à vista esta semana" |

### Exemplo de Negociação em Etapas

```
PROPOSTA INICIAL: R$480.000 (pedido R$550.000, -12.7%)

CONTRA 1 (Vendedor): R$530.000
→ Análise: Cedeu R$20k, sinal de flexibilidade

PROPOSTA 2 (Comprador): R$495.000 + entrada em 30 dias
→ Tática: Subiu R$15k, mas pediu prazo

CONTRA 2 (Vendedor): R$515.000, entrada em 15 dias
→ Análise: Cedeu mais R$15k, acelerou prazo

PROPOSTA 3 (Comprador): R$505.000, entrada em 20 dias, inclui ar-condicionado
→ Tática: Ponto médio + item extra

ACEITE: R$508.000, 20 dias, com ar-condicionado
→ Ambos cederem, fechou no meio
```

---

## ✅ Gatilhos de Fechamento

### Sinais de Que Pode Fechar

| Sinal Verbal | Significa |
|--------------|-----------|
| "Se eu fechar hoje..." | Pronto para negociar termos |
| "Quando posso mudar?" | Já se vê morando |
| "Minha esposa adorou" | Decisor aprovou |
| "Pode mandar o contrato?" | Quer formalizar |
| "Qual o próximo passo?" | Precisa de direção |

### Sinais Não-Verbais (Observados pelo Corretor)

| Comportamento | Interpretação |
|---------------|---------------|
| Mediu cômodos | Planejando uso |
| Tirou muitas fotos | Vai mostrar para alguém importante |
| Ficou muito tempo na varanda | Conectou emocionalmente |
| Perguntou sobre vizinhos | Preocupação real = interesse real |
| Voltou uma segunda vez | Muito interessado |

### Técnicas de Fechamento

#### 1. Fechamento Assumido
```
"Perfeito! Vou preparar a proposta para R$X.
 Prefere fazer a entrada via TED ou cheque?"
```

#### 2. Fechamento Alternativo
```
"Ótimo! Podemos assinar segunda ou terça.
 Qual dia funciona melhor para você?"
```

#### 3. Fechamento por Escassez (use com honestidade)
```
"Tenho outro interessado que visita amanhã.
 Se quiser garantir, podemos formalizar hoje."
```

#### 4. Fechamento por Resumo
```
"Então temos: R$500k, entrada de 50k,
 financiamento pelo Itaú, chaves em 60 dias.
 Está tudo certo para você?"
```

---

## ⚠️ Anti-Patterns de Negociação

### ❌ O que NUNCA fazer

| Erro | Por quê | Faça isso |
|------|---------|-----------|
| Falar mal do vendedor | Perde credibilidade | Mantenha neutralidade |
| Revelar urgência do comprador | Enfraquece posição | "Está avaliando opções" |
| Aceitar primeira contraproposta | Deixa dinheiro na mesa | Sempre negocie um pouco |
| Ignorar objeção | Ela volta depois | Resolva na hora |
| Pressionar demais | Perde o lead | Dê espaço, mantenha contato |
| Mentir sobre outros interessados | Antiético + pega fogo | Só use se for verdade |
| Falar preço por mensagem | Perde nuance, negociação fraca | Sempre ao vivo ou call |

### ❌ Frases Proibidas

```
❌ "É pegar ou largar" → Extremamente agressivo
❌ "Meu cliente não aceita nada abaixo de X" → Fecha portas
❌ "Você não vai encontrar nada melhor" → Arrogante
❌ "O vendedor está desesperado" → Desvaloriza, antiético
❌ "Só tem esse valor mesmo" → Sem empatia
```

---

## 📊 Métricas de Negociação

| Métrica | Meta | Descrição |
|---------|------|-----------|
| **Taxa de Proposta → Fechamento** | >30% | Propostas que viram contrato |
| **Desconto Médio Concedido** | 5-10% | Saudável para o mercado |
| **Tempo de Negociação** | 3-7 dias | Muito rápido = dinheiro na mesa |
| **Propostas por Fechamento** | <3 | Quantas tentativas até fechar |
| **Taxa de Abandono** | <20% | Leads que somem na negociação |

---

## 💬 Templates de Mensagens

### Envio de Proposta

```
"Olá, [Nome do Vendedor/Proprietário]!

Seguindo nosso interesse no imóvel [endereço], 
formalizamos a proposta:

💰 Valor: R$ [valor]
📅 Sinal: R$ [valor] até [data]
💳 Forma: [à vista/financiamento]
📋 Condições: [listar]

A proposta é válida até [data].

Aguardamos retorno!
[Assinatura]"
```

### Resposta a Contra-Proposta

```
"Olá!

Recebemos a contraproposta de R$ [valor].

Avaliamos com o comprador e podemos chegar a 
R$ [novo valor], mantendo [condições].

É o máximo que conseguimos. 
O que acha?

[Assinatura]"
```

### Comunicação de Aceite

```
"🎉 Ótimas notícias, [Nome]!

A proposta foi aceita! Fechamos em:

💰 R$ [valor final]
📅 Sinal até [data]
📋 [Resumo das condições]

Próximos passos:
1. Envio de documentação
2. Análise de crédito (se financiado)
3. Assinatura do contrato

Parabéns pelo novo imóvel!"
```

---

## 🔄 Fluxo de Status da Proposta

```
PROPOSTA ENVIADA
      ↓
┌─────────────────────────────────┐
│                                 │
↓                                 ↓
ACEITA                    CONTRAPROPOSTA
  ↓                              ↓
DOCUMENTAÇÃO              ANÁLISE PELO COMPRADOR
  ↓                              ↓
ASSINATURA               ┌───────┴───────┐
  ↓                      ↓               ↓
FECHADO ✅           ACEITA         NOVA PROPOSTA
                        ↓               ↓
                   DOCUMENTAÇÃO    (ciclo repete)
                        ↓
                   FECHADO ✅

                  ou

              RECUSADA → Fim ou novo imóvel
```

---

> **Lembre-se:** A melhor negociação é quando você conhece tão bem as necessidades do cliente que a proposta parece perfeita para ele. Se chegou à negociação com bom match, o fechamento é natural.
