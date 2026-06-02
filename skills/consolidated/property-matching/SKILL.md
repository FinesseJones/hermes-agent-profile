---
name: property-matching
description: Algoritmo de match entre perfil do cliente e portfólio de imóveis. Decision trees para priorização, scoring de compatibilidade, e estratégias de apresentação. Use quando precisar recomendar imóveis para leads qualificados.
allowed-tools: Read, Glob, Grep
skills: real-estate-qualification, brainstorming
---

# Property Matching - Match Inteligente Cliente × Imóvel

> **Filosofia:** O melhor imóvel não é o mais caro, é o que resolve o problema do cliente.
> **Princípio Central:** Match perfeito = necessidades atendidas + orçamento respeitado + emoção ativada.

---

## 🎯 O Triângulo do Match Perfeito

```
           NECESSIDADE
              /\
             /  \
            /    \
           /  ✓✓  \
          /________\
    ORÇAMENTO ←→ EMOÇÃO
```

| Pilar | O que avalia | Peso |
|-------|-------------|------|
| **Necessidade** | Atende requisitos funcionais (quartos, região, etc) | 40% |
| **Orçamento** | Compatível com capacidade financeira | 35% |
| **Emoção** | Conecta com estilo de vida e aspirações | 25% |

---

## 📊 Sistema de Scoring de Compatibilidade

### Critérios de Match

```typescript
interface PropertyMatchScore {
  imovelId: string;
  leadId: string;
  
  scores: {
    // Necessidades Funcionais (40 pontos)
    localizacao: number;      // 0-15 (região, proximidades)
    tamanho: number;          // 0-10 (quartos, área)
    caracteristicas: number;  // 0-10 (vaga, varanda, etc)
    tipoImovel: number;       // 0-5 (casa vs apto)
    
    // Financeiro (35 pontos)
    valorCompativel: number;  // 0-20 (dentro do orçamento)
    formaPagamento: number;   // 0-10 (aceita financiamento, etc)
    custoTotal: number;       // 0-5 (condomínio, IPTU)
    
    // Emocional (25 pontos)
    estiloVida: number;       // 0-10 (família, solteiro, etc)
    aspiracional: number;     // 0-10 (status, sonho)
    primeiraImpressao: number;// 0-5 (fotos, apresentação)
  };
  
  totalScore: number;         // 0-100
  ranking: number;            // Posição na lista
  destaques: string[];        // Por que combina
  ressalvas: string[];        // Pontos de atenção
}
```

### Matriz de Scoring por Critério

#### Localização (0-15 pontos)

| Condição | Pontos |
|----------|--------|
| Região exata solicitada | 15 |
| Região adjacente/similar | 10 |
| Mesma zona da cidade | 5 |
| Fora da zona, mas acessível | 2 |
| Incompatível | 0 |

**Fatores Adicionais:**
- Próximo ao trabalho declarado: +3
- Próximo a escola (se tem filhos): +3
- Próximo a metrô/transporte: +2
- Área verde/parque próximo: +1

#### Tamanho (0-10 pontos)

| Condição | Pontos |
|----------|--------|
| Quartos = solicitado | 10 |
| Quartos = solicitado + 1 | 8 |
| Quartos = solicitado - 1 | 4 |
| Muito maior ou menor | 0 |

#### Valor (0-20 pontos)

| Condição | Pontos |
|----------|--------|
| Dentro da faixa declarada | 20 |
| Até 10% acima | 15 |
| 10-20% acima | 8 |
| Abaixo do orçamento (economia) | 18 |
| Mais de 20% acima | 0 |

---

## 🔀 Decision Trees para Match

### Árvore 1: Tipo de Imóvel

```
É primeiro imóvel?
├── SIM → Prefira apartamentos em condomínio com estrutura
│         (mais segurança, menos manutenção para inexperientes)
│
└── NÃO → Tem filhos pequenos?
          ├── SIM → Priorize térreo, playground, áreas verdes
          │
          └── NÃO → Tem pets grandes?
                    ├── SIM → Casa > Apartamento
                    │         Ou apto com área externa
                    │
                    └── NÃO → Match padrão por preferência
```

### Árvore 2: Prioridade de Região

```
Qual o gatilho de mudança?
├── TRABALHO → Priorizar proximidade do emprego
│              Aceitar 30+ min se metrô direto
│
├── FAMÍLIA (casamento/filhos) → Priorizar segurança e escolas
│                                 Aceitar região mais afastada
│
├── INSATISFAÇÃO ATUAL → Entender O QUE incomoda
│                         Match = oposto do problema
│
└── INVESTIMENTO → ROI > Localização pessoal
                   Priorizar valorização e liquidez
```

### Árvore 3: Faixa de Preço

```
Orçamento declarado é realista para a região?
├── SIM → Match direto
│
└── NÃO → É muito baixo?
          ├── SIM → Sugerir regiões alternativas
          │         OU imóveis menores na região desejada
          │         OU imóveis usados vs lançamento
          │
          └── Orçamento acima do necessário?
              └── SIM → Upsell gentil
                        "Com esse orçamento, você consegue..."
```

---

## 📋 Matriz de Compatibilidade por Perfil

### Jovem Solteiro (22-32)

| Prioridade | Característica | Peso |
|------------|----------------|------|
| 1 | Localização central/vida noturna | Alto |
| 2 | Transporte público | Alto |
| 3 | Studio ou 1 quarto | Médio |
| 4 | Academia no prédio | Baixo |
| 5 | Tamanho do apartamento | Baixo |

**Match ideal:** Studio ou 1Q em bairro jovem, próximo ao metrô

### Casal Sem Filhos (25-40)

| Prioridade | Característica | Peso |
|------------|----------------|------|
| 1 | 2 quartos (um vira escritório) | Alto |
| 2 | Segurança do bairro | Alto |
| 3 | Espaço para home office | Médio |
| 4 | Varanda/área gourmet | Médio |
| 5 | Proximidade de restaurantes | Baixo |

**Match ideal:** 2Q com varanda em bairro seguro, potencial para família

### Família com Crianças

| Prioridade | Característica | Peso |
|------------|----------------|------|
| 1 | 3+ quartos | Crítico |
| 2 | Proximidade de escola | Alto |
| 3 | Área de lazer/playground | Alto |
| 4 | Segurança (condomínio fechado) | Alto |
| 5 | Espaço para brincar | Médio |
| 6 | 2+ vagas de garagem | Médio |

**Match ideal:** 3Q+ em condomínio com lazer, próximo a escolas

### Investidor

| Prioridade | Característica | Peso |
|------------|----------------|------|
| 1 | Potencial de valorização | Crítico |
| 2 | Liquidez (fácil revenda/locação) | Alto |
| 3 | Custo x Retorno (yield) | Alto |
| 4 | Baixa manutenção | Médio |
| 5 | Localização estratégica | Médio |

**Match ideal:** Imóvel com demanda comprovada, bom yield, região em crescimento

### Aposentado/Downsizing

| Prioridade | Característica | Peso |
|------------|----------------|------|
| 1 | Acessibilidade (elevador, térreo) | Alto |
| 2 | Segurança e portaria 24h | Alto |
| 3 | Proximidade de serviços de saúde | Alto |
| 4 | Baixo custo de manutenção | Médio |
| 5 | Área menor, mais prática | Médio |

**Match ideal:** 2Q em prédio com elevador, bairro com infraestrutura

---

## 🎯 Estratégia de Apresentação

### Regra dos 3

> **Nunca apresente mais de 3 opções iniciais.** Mais opções = mais confusão = menos decisão.

```
OPÇÃO 1: O Racional
├── Atende todos os requisitos
├── Dentro do orçamento
└── "A escolha segura"

OPÇÃO 2: O Aspiracional  
├── Um pouco acima do orçamento
├── Tem algo especial (vista, acabamento)
└── "E se você pudesse..."

OPÇÃO 3: O Curinga
├── Fora do padrão declarado
├── Mas pode surpreender
└── "Clientes como você geralmente..."
```

### Ordem de Apresentação

| Estratégia | Quando Usar |
|------------|-------------|
| **Melhor primeiro** | Lead quente, decisor rápido |
| **Crescendo** | Lead analítico, gosta de comparar |
| **Âncora alta** | Quando quer valorizar opção do meio |
| **Único foco** | Lead já demonstrou interesse específico |

---

## 🧠 Sinais de Match Emocional

### Durante a Conversa

| Sinal | Interpretação | Ação |
|-------|---------------|------|
| "Sempre sonhei com..." | Aspiração forte | Buscar imóvel que ative esse sonho |
| "Igual ao da minha avó" | Nostalgia, conforto | Valorizar elementos tradicionais |
| "Meus filhos precisam..." | Foco na família | Priorizar infraestrutura para crianças |
| "Para receber amigos" | Vida social ativa | Valorizar área gourmet, espaço |
| "Preciso de silêncio" | Perfil introspectivo | Andar alto, pouco movimento |

### Durante a Visita (se corretor reportar)

| Comportamento | Significado |
|---------------|-------------|
| Fotografou muito | Interesse alto, vai mostrar para alguém |
| Ficou mais que 20 min | Está se imaginando morando |
| Perguntou sobre vizinhos | Preocupação genuína com comunidade |
| Abriu todos os armários | Prático, está avaliando de verdade |
| Voltou à sala várias vezes | Conectou emocionalmente |

---

## ⚠️ Anti-Patterns de Match

### ❌ O que NÃO fazer

| Erro | Por que é ruim | Faça isso |
|------|----------------|-----------|
| Mostrar 10+ imóveis | Paralisia de escolha | Máximo 3 iniciais |
| Ignorar orçamento | Perde credibilidade | Sempre respeite +/- 10% |
| Só imóveis novos | Pode perder oportunidades | Inclua usados se fizer sentido |
| Match só por região | Superficial demais | Considere todos os critérios |
| Forçar imóvel encalhado | Perde o lead | Transparência sempre |
| Ignorar pets | Fator decisivo para muitos | Pergunte ativamente |

---

## 📊 Métricas de Qualidade do Match

| Métrica | Meta | Descrição |
|---------|------|-----------|
| **Hit Rate 1º Imóvel** | >25% | Fechou no primeiro apresentado |
| **Taxa de Visita** | >60% | Leads que visitaram ao menos 1 sugestão |
| **Precisão do Match** | >80% | "Gostei" vs "Não era isso" |
| **Tempo até Match** | <3 sugestões | Encontrou ideal em até 3 tentativas |
| **NPS do Match** | >70 | Satisfação com recomendações |

---

## 🔄 Loop de Feedback

### Após Cada Visita/Rejeição

```
1. COLETAR: "O que você achou?"
2. CATEGORIZAR:
   - Gostou, mas não fechou → Por quê?
   - Não gostou → O que faltou?
3. AJUSTAR: Refinar critérios de match
4. REPETIR: Nova sugestão calibrada
```

### Perguntas de Refinamento

```
✅ "O tamanho foi o esperado ou você prefere algo maior/menor?"

✅ "A localização te atendeu ou precisa ser mais central/tranquila?"

✅ "Faltou alguma característica que você considera essencial?"

✅ "O valor estava dentro do esperado? Podemos ajustar a faixa?"
```

---

## 💡 Dicas de Ouro

1. **Primeiro match ≠ melhor match.** Use o primeiro para calibrar.

2. **Leia nas entrelinhas.** "Interessante" geralmente significa "não gostei".

3. **Imóvel perfeito não existe.** Ajude a priorizar o que importa.

4. **Match emocional fecha negócio.** Funcional só abre portas.

5. **Feedback negativo é ouro.** Use para refinar o algoritmo.

---

> **Lembre-se:** O match perfeito acontece quando o cliente se VISUALIZA morando ali. Seu trabalho é criar essa conexão entre pessoa e lugar.
