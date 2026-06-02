---
name: real-estate-qualification
description: Framework BANT adaptado para qualificação de leads imobiliários. Cobre perfil do comprador/locatário, capacidade financeira, urgência de mudança, autoridade de decisão e timeline. Use para chatbots imobiliários, atendimento de corretores, e sistemas de CRM.
allowed-tools: Read, Glob, Grep
skills: lead-qualification, brainstorming
---

# Real Estate Lead Qualification

> **Filosofia:** Qualificar não é interrogar. É entender sonhos, necessidades e capacidades através de conversa natural.
> **Princípio Central:** No mercado imobiliário, a jornada é longa (até 18 meses). Qualificação é progressiva, não instantânea.

---

## 🎯 Selective Reading Rule

| Arquivo | Status | Quando Ler |
|---------|--------|------------|
| `buyer-qualification.md` | 🔴 **REQUIRED** | Qualificando comprador |
| `renter-qualification.md` | 🔴 **REQUIRED** | Qualificando locatário |
| `seller-qualification.md` | ⚪ Opcional | Captando imóvel para venda |
| `investor-qualification.md` | ⚪ Opcional | Lead investidor |
| `financing-patterns.md` | ⚪ Opcional | Questões de financiamento |

---

## 🏠 Framework BANT Imobiliário

O BANT tradicional adaptado para o contexto de compra/locação de imóveis:

### B - Budget (Orçamento/Capacidade Financeira)

**Diferença do BANT tradicional:** No imobiliário, orçamento envolve:
- Valor de entrada/sinal
- Capacidade de financiamento (comprometimento de renda)
- FGTS disponível
- Imóvel para vender/trocar
- Garantias para locação

**Perguntas Naturais (NÃO interrogativas):**

```
❌ Ruim: "Qual seu orçamento?"
✅ Bom: "Você já tem uma ideia de valor que está buscando? 
        A maioria dos imóveis nessa região fica entre R$X e R$Y."

❌ Ruim: "Vai financiar?"
✅ Bom: "Muitos clientes optam por financiar parte do valor. 
        Você já conversou com algum banco ou prefere à vista?"

❌ Ruim: "Tem entrada?"
✅ Bom: "Para dar uma ideia mais precisa das opções, 
        você teria disponível algum valor para entrada?"
```

**Sinais Implícitos de Budget:**

| Sinal na Conversa | Interpretação | Score |
|-------------------|---------------|-------|
| "Apartamento de 3 quartos em Leblon" | Budget alto (>2M) | +30 |
| "Preciso usar meu FGTS" | Budget limitado, provável primeira compra | +15 |
| "Vou vender meu apartamento atual" | Tem capital, upgrade | +25 |
| "Aluguel até R$2.000" | Budget definido, realista | +20 |
| "O mais barato possível" | Budget restrito | +10 |
| "Não me preocupo com valor" | Budget alto, decisor | +30 |

### A - Authority (Autoridade de Decisão)

**Particularidade Imobiliária:** Decisão geralmente é familiar/compartilhada.

**Padrões de Autoridade:**

| Perfil | Descrição | Abordagem |
|--------|-----------|-----------|
| **Decisor Solo** | Solteiro, investidor, divorciado | Foco direto, agilidade |
| **Casal** | Decisão conjunta | Incluir ambos nas visitas |
| **Família** | Pais + filhos opinando | Entender quem pesa mais |
| **Procurador** | Comprando para terceiro | Identificar decisor real |
| **Pesquisador** | "Só olhando para minha mãe" | Qualificar o decisor, não ele |

**Perguntas de Detecção:**

```
✅ "Você está buscando para você mesmo ou está ajudando alguém?"

✅ "Quem mais vai participar da decisão? Assim posso agendar 
    as visitas em horários que funcionem para todos."

✅ "Além de você, tem mais alguém que precisa aprovar antes de fechar?"
```

### N - Need (Necessidade/Urgência)

**Gatilhos de Mudança Imobiliária:**

| Gatilho | Urgência | Perfil Típico |
|---------|----------|---------------|
| Casamento | Alta (3-6 meses) | Primeiro imóvel |
| Nascimento de filho | Alta (imediata a 6 meses) | Upgrade de espaço |
| Divórcio | Muito Alta | Precisa resolver rápido |
| Mudança de emprego | Alta | Relocation |
| Aposentadoria | Média | Downsizing ou mudança de cidade |
| Investimento | Baixa-Média | Sem urgência, busca oportunidade |
| Fim de contrato de aluguel | Alta | Data definida |
| Insatisfação atual | Média | Pode esperar pelo certo |

**Perguntas de Detecção:**

```
✅ "O que está motivando essa busca agora? 
    Mudança de trabalho, família crescendo...?"

✅ "Você tem alguma data específica em mente para a mudança?"

✅ "Qual o principal problema do lugar onde você mora hoje?"
```

**Escala de Urgência:**

```typescript
enum UrgenciaImobiliaria {
  CRITICA = 'critica',        // Precisa em 30 dias (divórcio, despejo)
  ALTA = 'alta',              // 1-3 meses (casamento, nascimento)
  MEDIA = 'media',            // 3-6 meses (planejando mudança)
  BAIXA = 'baixa',            // 6-12 meses (pesquisando mercado)
  INVESTIDOR = 'investidor',  // Sem prazo, busca oportunidade
}
```

### T - Timing (Timeline)

**Fases da Jornada Imobiliária:**

```
DESCOBERTA (1-3 meses)
    ↓ Pesquisando mercado, definindo região
CONSIDERAÇÃO (2-4 meses)
    ↓ Visitando imóveis, comparando
DECISÃO (1-2 meses)
    ↓ Negociação, documentação
FECHAMENTO (1-3 meses)
    ↓ Financiamento, cartório, mudança
```

**Perguntas de Timeline:**

```
✅ "Você já visitou outros imóveis ou está começando a pesquisa agora?"

✅ "Se encontrar o imóvel ideal amanhã, você estaria pronto para 
    avançar com proposta?"

✅ "Tem algum prazo específico? Fim de contrato, data de casamento...?"
```

---

## 📊 Sistema de Scoring Imobiliário

### Pontuação por Critério

```typescript
interface LeadScoreImobiliario {
  total: number;              // 0-100
  categoria: 'quente' | 'morno' | 'frio' | 'nurture';
  breakdown: {
    budget: number;           // 0-30 (capacidade financeira)
    authority: number;        // 0-20 (poder de decisão)
    need: number;             // 0-25 (urgência real)
    timing: number;           // 0-15 (prontidão para agir)
    engagement: number;       // 0-10 (nível de interação)
  };
  proximaAcao: string;
  prioridade: 'P1' | 'P2' | 'P3' | 'P4';
}
```

### Matriz de Scoring

| Critério | Baixo (5-10) | Médio (15-20) | Alto (25-30) |
|----------|--------------|---------------|--------------|
| **Budget** | Indefinido, fora da realidade | Compatível com mercado | Comprovado, pré-aprovado |
| **Authority** | Pesquisando para terceiro | Decisão compartilhada | Decisor único |
| **Need** | "Só olhando" | Insatisfação moderada | Gatilho de vida (casamento, filho) |
| **Timing** | Sem prazo | 6+ meses | Menos de 3 meses |
| **Engagement** | Responde pouco | Faz perguntas | Solicita visitas |

### Classificação Final

| Score | Categoria | Ação | SLA de Resposta |
|-------|-----------|------|-----------------|
| 80-100 | 🔥 **Quente** | Corretor sênior, visita imediata | < 15 minutos |
| 60-79 | 🟠 **Morno** | Corretor padrão, agendar visita | < 2 horas |
| 40-59 | 🟡 **Frio** | Nutrir com conteúdo, requalificar | < 24 horas |
| 0-39 | ⚪ **Nurture** | Drip campaign, longo prazo | Automático |

---

## 💬 Fluxo de Qualificação Conversacional

### Fase 1: Engajamento (Primeiros 30 segundos)

```
Bot: "Olá! 👋 Sou o assistente da [Imobiliária]. 
      Vi que você se interessou por imóveis em [região/tipo]. 
      Posso te ajudar a encontrar o lugar ideal?"

→ Extrair: canal_origem, interesse_inicial
```

### Fase 2: Descoberta de Necessidade (2-3 minutos)

```
Bot: "Para te indicar as melhores opções, me conta: 
      você está buscando para comprar ou alugar?"

[Se comprar]
Bot: "Ótimo! É seu primeiro imóvel ou você já é proprietário?"

[Se alugar]
Bot: "Entendi! Você mora sozinho ou com mais alguém?"

→ Extrair: tipo_transacao, perfil_familiar, experiencia_anterior
```

### Fase 3: Definição do Imóvel (2-3 minutos)

```
Bot: "E sobre o imóvel em si, você tem preferência por:
      🏢 Apartamento
      🏠 Casa
      🏪 Comercial
      🤷 Ainda estou decidindo"

Bot: "Quantos quartos você precisa no mínimo?"

Bot: "Tem alguma região específica que você prefere? 
      Ou posso sugerir com base no seu perfil?"

→ Extrair: tipo_imovel, quartos_min, regioes_interesse
```

### Fase 4: Qualificação Financeira (sutil)

```
Bot: "Para te mostrar opções realistas, você tem uma faixa de 
      valor em mente? Por exemplo:
      
      💰 Até R$300 mil
      💰 R$300 a R$500 mil
      💰 R$500 mil a R$800 mil
      💰 Acima de R$800 mil"

[Se compra]
Bot: "Você pretende financiar ou seria à vista?"

→ Extrair: faixa_valor, forma_pagamento, tem_entrada
```

### Fase 5: Timeline e Próximos Passos

```
Bot: "Quando você imagina fazer essa mudança?
      
      📅 O mais rápido possível
      📅 Nos próximos 3 meses
      📅 Nos próximos 6 meses
      📅 Ainda estou só pesquisando"

Bot: "Perfeito, [Nome]! Com base no que você me contou, 
      temos [X] opções que podem te interessar.
      
      Quer que eu te envie algumas sugestões agora ou 
      prefere agendar uma conversa com um de nossos especialistas?"

→ Extrair: urgencia, preferencia_contato
```

---

## 🚨 Anti-Patterns (O que NÃO Fazer)

### ❌ Erros Comuns na Qualificação Imobiliária

| Anti-Pattern | Por que é ruim | Faça isso |
|--------------|----------------|-----------|
| Perguntar orçamento logo no início | Invasivo, assusta o lead | Construa rapport antes |
| Assumir que quem pergunta é o decisor | Perda de tempo com não-decisores | Confirme autoridade cedo |
| Ignorar sinais de urgência | Perde oportunidades quentes | Detecte gatilhos de vida |
| Tratar investidor como comprador final | Abordagem errada | Foque em ROI, não em "lar" |
| Forçar visita sem qualificar | Desperdiça tempo do corretor | Qualifique antes de agendar |
| Não perguntar sobre imóvel atual | Perde contexto valioso | Entenda de onde vem |

### ❌ Frases a Evitar

```
❌ "Qual seu orçamento máximo?" → Muito direto
❌ "Você tem dinheiro para entrada?" → Constrangedor
❌ "Quando quer fechar?" → Pressão desnecessária
❌ "Posso te ligar agora?" → Invasivo sem permissão
❌ "Esse é o melhor preço" → Antes de negociar
```

---

## 📋 Checklist de Qualificação Completa

### Informações Mínimas para Lead Qualificado

- [ ] **Nome completo** do lead
- [ ] **Telefone** com WhatsApp
- [ ] **Tipo de transação** (compra/aluguel)
- [ ] **Tipo de imóvel** preferido
- [ ] **Região(ões)** de interesse
- [ ] **Número de quartos** mínimo
- [ ] **Faixa de valor** aproximada
- [ ] **Timeline** de mudança
- [ ] **Quem decide** (sozinho/casal/família)
- [ ] **Motivo da busca** (gatilho)

### Informações Bônus (Aumentam Score)

- [ ] Tem imóvel para vender?
- [ ] Já fez simulação de financiamento?
- [ ] Visitou outros imóveis?
- [ ] Trabalha em qual região?
- [ ] Tem filhos? Quantos? Idades?
- [ ] Tem pets?
- [ ] Precisa de vaga de garagem?

---

## 🔄 Integração com CRM

### Campos Obrigatórios para Sync

```typescript
interface LeadImobiliarioCRM {
  // Identificação
  id: string;
  nome: string;
  telefone: string;
  email?: string;
  
  // Qualificação
  tipoTransacao: 'compra' | 'aluguel' | 'ambos';
  tipoImovel: 'apartamento' | 'casa' | 'comercial' | 'terreno';
  quartos: number;
  regioes: string[];
  
  // Financeiro
  faixaValorMin: number;
  faixaValorMax: number;
  formaPagamento: 'avista' | 'financiamento' | 'fgts' | 'misto';
  temEntrada: boolean;
  valorEntrada?: number;
  
  // Timeline
  urgencia: 'imediata' | 'curto' | 'medio' | 'longo';
  dataLimite?: Date;
  motivoMudanca: string;
  
  // Scoring
  leadScore: number;
  categoria: 'quente' | 'morno' | 'frio' | 'nurture';
  
  // Atribuição
  corretor?: string;
  origem: string;
  dataContato: Date;
}
```

---

## 📈 Métricas de Sucesso

### KPIs de Qualificação

| Métrica | Meta | Fórmula |
|---------|------|---------|
| **Taxa de Qualificação** | >60% | Leads qualificados / Total leads |
| **Precisão do Score** | >80% | Leads quentes que visitam / Total quentes |
| **Tempo de Qualificação** | <5 min | Média de duração da conversa |
| **Taxa de Agendamento** | >40% | Visitas agendadas / Leads qualificados |
| **Conversão Quente** | >15% | Fechamentos / Leads quentes |

---

## 🎯 Personas Específicas

Para qualificação detalhada por persona, consulte:

- [buyer-qualification.md](buyer-qualification.md) - Comprador de imóvel
- [renter-qualification.md](renter-qualification.md) - Locatário
- [seller-qualification.md](seller-qualification.md) - Proprietário vendedor
- [investor-qualification.md](investor-qualification.md) - Investidor imobiliário

---

> **Lembre-se:** A compra de um imóvel é uma das maiores decisões financeiras da vida. Qualifique com empatia, não com pressa. O lead que hoje está "só pesquisando" pode fechar em 6 meses se bem nutrido.
