---
name: financing-advisor
description: Orientação sobre financiamento imobiliário. Simulação, comparação de bancos, uso de FGTS, Casa Verde Amarela, e análise de capacidade de pagamento. Use quando lead precisa entender opções de financiamento.
allowed-tools: Read, Glob, Grep
skills: real-estate-qualification
---

# Financing Advisor - Orientação de Financiamento Imobiliário

> **Filosofia:** Financiamento não é burocracia, é a ponte entre o sonho e a realidade.
> **Princípio Central:** Cliente bem informado fecha mais rápido e com menos arrependimento.

---

## 🎯 Componentes do Financiamento Imobiliário

```
VALOR DO IMÓVEL
      ↓
┌─────────────────────────────────┐
│ ENTRADA (20-30%)                │
│ ├── Recursos próprios           │
│ ├── FGTS                        │
│ └── Venda de outro imóvel       │
└─────────────────────────────────┘
      +
┌─────────────────────────────────┐
│ FINANCIAMENTO (70-80%)          │
│ ├── Banco (CEF, Itaú, etc)      │
│ ├── Prazo (até 420 meses)       │
│ └── Taxa de juros (8-12% a.a.)  │
└─────────────────────────────────┘
      =
PRESTAÇÃO MENSAL (máx 30% renda)
```

---

## 💰 Regras Fundamentais

### Comprometimento de Renda

| Regra | Descrição |
|-------|-----------|
| **Máximo 30%** | Parcela não pode ultrapassar 30% da renda bruta familiar |
| **Renda comprovada** | CTPS, holerite, IR, extratos (autônomos) |
| **Composição** | Pode somar renda de cônjuge, pais, filhos |

**Exemplo Prático:**
```
Renda familiar: R$ 10.000/mês
Parcela máxima: R$ 3.000/mês
Financiamento possível: ~R$ 350.000 (30 anos, juros ~10%)
+ Entrada: R$ 100.000
= Imóvel até: R$ 450.000
```

### Valor de Entrada

| Sistema | Entrada Mínima | Observação |
|---------|----------------|------------|
| **SFH** | 20% | Sistema Financeiro da Habitação |
| **SFI** | 20-30% | Sistema Financeiro Imobiliário (imóveis >R$1.5M) |
| **Minha Casa Minha Vida** | 0-5% | Depende da faixa de renda |
| **Direto com Construtora** | Varia | Geralmente mais flexível |

---

## 🏦 Comparativo de Bancos

### Principais Instituições (Referência 2025)

| Banco | Taxa (a.a.) | Prazo Máximo | Diferenciais |
|-------|-------------|--------------|--------------|
| **Caixa Econômica** | 8.99% - 9.99% | 420 meses | FGTS, Minha Casa Minha Vida |
| **Banco do Brasil** | 9.49% - 10.49% | 420 meses | Correntistas têm desconto |
| **Itaú** | 9.90% - 10.90% | 360 meses | Processo digital rápido |
| **Bradesco** | 9.90% - 10.90% | 360 meses | Portabilidade fácil |
| **Santander** | 9.99% - 10.99% | 420 meses | Financiamento de terreno |
| **Inter** | 9.90% + IPCA | 360 meses | 100% digital |

> [!WARNING]
> **Taxas são referenciais.** Sempre simular no banco para valor exato.
> Taxa efetiva inclui: juros + seguros (MIP + DFI) + tarifa de administração.

### Quando Escolher Cada Banco

| Perfil | Banco Recomendado | Por quê |
|--------|-------------------|---------|
| **Primeiro imóvel + FGTS** | Caixa | Melhores condições MCMV |
| **Imóvel usado, processo rápido** | Itaú/Bradesco | Digital, menos burocracia |
| **Alta renda, imóvel >R$1.5M** | Bradesco/Santander | Experiência em alto padrão |
| **Autônomo** | Caixa/BB | Mais flexíveis com comprovação |

---

## 🏡 FGTS no Financiamento

### Regras para Uso do FGTS

| Regra | Descrição |
|-------|-----------|
| **Tempo de FGTS** | Mínimo 3 anos de contribuição (soma de contratos) |
| **Primeiro imóvel** | Não pode ter outro imóvel na mesma cidade |
| **Valor do imóvel** | Até R$ 1.500.000 (limite SFH 2025) |
| **Não ter financiamento ativo** | No SFH |
| **Residência própria** | Não pode usar para investimento |

### Formas de Usar o FGTS

```
1. ENTRADA
   └── Abate do valor de entrada
   
2. AMORTIZAÇÃO
   └── Reduz saldo devedor (a cada 2 anos)
   
3. PAGAMENTO DE PARCELAS
   └── Usa FGTS para pagar até 80% da parcela (12 meses)
```

### Simulação com FGTS

```
Cenário:
- Imóvel: R$ 400.000
- FGTS disponível: R$ 50.000
- Entrada adicional: R$ 30.000

Cálculo:
- Entrada total: R$ 80.000 (20%)
- Financiamento: R$ 320.000
- Economia de juros: ~R$ 100.000 ao longo do contrato
```

---

## 🏠 Programas Habitacionais

### Minha Casa Minha Vida (2025)

| Faixa | Renda Familiar | Subsídio | Taxa de Juros |
|-------|----------------|----------|---------------|
| **Faixa 1** | Até R$ 2.640 | Até R$ 55.000 | 4.00% - 4.25% |
| **Faixa 2** | R$ 2.640 - R$ 4.400 | Até R$ 29.000 | 4.75% - 6.00% |
| **Faixa 3** | R$ 4.400 - R$ 8.000 | Sem subsídio | 7.66% - 8.16% |

### Casa Verde Amarela (Transição)

> [!NOTE]
> Programa Casa Verde Amarela foi substituído pelo MCMV em 2023.
> Contratos antigos seguem vigentes.

### SBPE (Poupança)

| Característica | Descrição |
|----------------|-----------|
| **Fonte** | Caderneta de poupança |
| **Limite** | Sem limite de valor do imóvel |
| **Entrada** | Mínimo 20% |
| **Taxas** | Geralmente maiores que SFH |

---

## 📊 Tabelas de Amortização

### SAC (Sistema de Amortização Constante)

```
Características:
✅ Parcelas decrescentes (começa alto, termina baixo)
✅ Amortização fixa todo mês
✅ Juros diminuem conforme saldo reduz
✅ Paga menos juros no total

Ideal para: Quem tem renda folgada agora
```

**Exemplo SAC:**
| Mês | Amortização | Juros | Parcela |
|-----|-------------|-------|---------|
| 1 | R$ 1.000 | R$ 800 | R$ 1.800 |
| 120 | R$ 1.000 | R$ 400 | R$ 1.400 |
| 240 | R$ 1.000 | R$ 100 | R$ 1.100 |

### PRICE (Parcelas Fixas)

```
Características:
✅ Parcelas fixas do início ao fim
⚠️ No início, parcela é quase toda de juros
⚠️ Paga mais juros no total

Ideal para: Quem precisa de previsibilidade
```

**Exemplo PRICE:**
| Mês | Amortização | Juros | Parcela |
|-----|-------------|-------|---------|
| 1 | R$ 300 | R$ 1.200 | R$ 1.500 |
| 120 | R$ 600 | R$ 900 | R$ 1.500 |
| 240 | R$ 1.200 | R$ 300 | R$ 1.500 |

### Comparativo

| Aspecto | SAC | PRICE |
|---------|-----|-------|
| Parcela inicial | Maior | Menor |
| Parcela final | Menor | Igual |
| Total de juros | Menor | Maior |
| Qualificação | Mais difícil | Mais fácil |

---

## 💬 Perguntas para Qualificação Financeira

### Descobrir Capacidade

```
✅ "Você já tem uma ideia de quanto poderia dar de entrada?"

✅ "Qual é a renda mensal da família, aproximadamente? 
    Isso ajuda a simular a parcela máxima."

✅ "Você já consultou seu saldo de FGTS? 
    Pode fazer diferença significativa."

✅ "Tem algum imóvel para vender que entraria como parte do pagamento?"
```

### Descobrir Preferência

```
✅ "Você prefere parcela menor agora que sobe depois, 
    ou parcela fixa por todo o contrato?"

✅ "Tem preferência por algum banco específico? 
    Às vezes a conta corrente dá desconto."

✅ "Você já fez simulação em algum banco?"
```

---

## 🧮 Fórmula Simplificada de Simulação

### Cálculo Rápido (Aproximado)

```
Para SAC, 30 anos, juros ~10% a.a.:

Parcela Inicial ≈ Valor Financiado × 0.0095

Exemplo:
Financiamento: R$ 300.000
Parcela Inicial: R$ 300.000 × 0.0095 = R$ 2.850
```

### Capacidade de Financiamento

```
Parcela Máxima = Renda × 0.30
Financiamento ≈ Parcela Máxima × 105 (para 30 anos)

Exemplo:
Renda: R$ 12.000
Parcela Máxima: R$ 3.600
Financiamento: R$ 3.600 × 105 = R$ 378.000
```

---

## 📋 Documentos Necessários

### Pessoa Física (Comprador)

| Documento | Observação |
|-----------|------------|
| RG e CPF | Cópias legíveis |
| Comprovante de estado civil | Certidão casamento/nascimento |
| Comprovante de renda | Últimos 3 holerites ou IR |
| Comprovante de endereço | Últimos 3 meses |
| Extrato FGTS | Se for usar |
| Declaração IR | Últimos 2 anos |
| Certidões negativas | Protestos, ações |

### Autônomo/MEI

| Documento | Observação |
|-----------|------------|
| Tudo acima | + |
| Extratos bancários | Últimos 6-12 meses |
| Contrato social | Se empresa |
| DECORE | Declaração de rendimentos |
| Declaração de IR PJ | Se aplicável |

---

## ⚠️ Armadilhas a Evitar

### ❌ Erros Comuns

| Erro | Consequência | Evite assim |
|------|--------------|-------------|
| Não considerar custos extras | ITBI, registro, escritura = +5% | Calcule custo total |
| Esquecer condomínio e IPTU | Compromete orçamento | Some à parcela |
| Escolher menor taxa nominal | Taxa efetiva pode ser maior | Compare CET |
| Não simular em 3+ bancos | Perde economia de milhares | Sempre compare |
| Prazo muito longo sem necessidade | Paga muito mais juros | Equilibre parcela × juros |

### ❌ Frases de Alerta

```
⚠️ "A parcela cabe no bolso" → Cabe HOJE, e daqui 5 anos?
⚠️ "É só 10% ao ano" → Ao longo de 30 anos, dobra o valor
⚠️ "Depois eu amortizo" → Muitos não conseguem
⚠️ "Vou usar o FGTS para amortizar" → E se perder o emprego?
```

---

## 📈 Métricas e Indicadores

### Para Orientar o Cliente

| Indicador | Saudável | Atenção | Risco |
|-----------|----------|---------|-------|
| Parcela/Renda | <25% | 25-30% | >30% |
| Entrada própria | >20% | 10-20% | <10% |
| Prazo | <240 meses | 240-360 | >360 |
| Reserva emergência | >6 meses | 3-6 meses | <3 meses |

---

## 🔄 Processo de Aprovação

```
1. PRÉ-ANÁLISE (7 dias)
   └── Envio de documentos básicos
   └── Score de crédito
   
2. ANÁLISE DE CRÉDITO (15 dias)
   └── Avaliação de renda
   └── Consulta a bureaus
   
3. AVALIAÇÃO DO IMÓVEL (15 dias)
   └── Engenheiro do banco visita
   └── Laudo de avaliação
   
4. APROVAÇÃO (5 dias)
   └── Carta de crédito aprovada
   └── Condições finais
   
5. ASSINATURA (15 dias)
   └── Contrato no cartório
   └── Registro da alienação fiduciária
   
6. LIBERAÇÃO (5 dias)
   └── Recursos liberados ao vendedor

TOTAL TÍPICO: 45-60 dias
```

---

> **Lembre-se:** Financiamento é compromisso de décadas. Ajude o cliente a entender todas as variáveis para uma decisão consciente. Melhor adiar a compra do que comprometer o futuro financeiro.
