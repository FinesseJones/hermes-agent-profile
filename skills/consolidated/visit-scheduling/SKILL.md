---
name: visit-scheduling
description: Princípios e estratégias para agendamento inteligente de visitas a imóveis. Cobre disponibilidade, priorização, confirmação, e otimização de rotas. Use quando precisar agendar visitas entre leads e corretores.
allowed-tools: Read, Glob, Grep
skills: real-estate-qualification, property-matching
---

# Visit Scheduling - Agendamento Inteligente de Visitas

> **Filosofia:** Uma visita bem agendada já é meio caminho para o fechamento.
> **Princípio Central:** Respeite o tempo do cliente E do corretor. Visita cancelada = oportunidade perdida.

---

## 🎯 O Triângulo do Agendamento Perfeito

```
          CLIENTE
            /\
           /  \
          / ✓✓ \
         /______\
   CORRETOR ←→ IMÓVEL
```

| Pilar | O que considerar |
|-------|------------------|
| **Cliente** | Disponibilidade, localização, quem vai junto |
| **Corretor** | Agenda, especialidade, proximidade |
| **Imóvel** | Ocupado? Chave com quem? Melhor horário? |

---

## 📅 Slots Ideais para Visitas

### Por Tipo de Lead

| Perfil | Melhor Dia | Melhor Horário | Por quê |
|--------|------------|----------------|---------|
| **Casal trabalhador** | Sábado | 10h-12h / 14h-16h | Único dia livre |
| **Aposentado** | Terça-Quinta | 10h-12h | Evita correria do fim de semana |
| **Investidor** | Qualquer dia útil | 14h-17h | Flexibilidade, foco |
| **Família com filhos** | Sábado | 10h-12h | Antes do almoço das crianças |
| **Solteiro jovem** | Sábado | 14h-18h | Dorme até tarde |

### Horários a EVITAR

| Horário | Por quê |
|---------|---------|
| Segunda-feira manhã | Reuniões de trabalho |
| Sexta-feira tarde | Cabeça no fim de semana |
| Domingo | Dia de família (baixa conversão) |
| Horário de almoço | Pressa, não decide |
| Após 18h (escuro) | Não vê o imóvel direito |

---

## 🔀 Decision Tree: Priorização de Visitas

### Quem atender primeiro?

```
Lead qualificado como QUENTE?
├── SIM → Agendar em até 24h
│         Prioridade máxima
│
└── NÃO → Lead é MORNO?
          ├── SIM → Agendar em até 72h
          │         Encaixar na agenda
          │
          └── NÃO → Lead FRIO
                    Nutrir antes de agendar visita
                    (não desperdiçar corretor)
```

### Qual corretor designar?

```
Valor do imóvel > R$1M?
├── SIM → Corretor sênior
│         Experiência em alto padrão
│
└── NÃO → Primeiro imóvel do lead?
          ├── SIM → Corretor didático
          │         Paciência para explicar
          │
          └── NÃO → Investidor?
                    ├── SIM → Corretor analítico
                    │         Fala de números
                    │
                    └── NÃO → Corretor por região
                              Conhece o bairro
```

---

## 💬 Fluxo de Agendamento Conversacional

### Fase 1: Proposta de Visita

```
Bot: "Ótimo, [Nome]! Encontrei [X] imóveis que combinam com você.
      Quer agendar uma visita para conhecer pessoalmente?
      
      📅 Posso verificar a disponibilidade para esta semana ou 
         você prefere a próxima?"
```

### Fase 2: Coleta de Disponibilidade

```
Bot: "Perfeito! Para agendar, me conta:
      
      🗓 Qual dia funciona melhor?
      ⏰ Manhã, tarde ou início da noite?
      👥 Vai sozinho(a) ou alguém vem junto?"
```

### Fase 3: Confirmação de Dados

```
[Se não tem telefone ainda]
Bot: "Para confirmar a visita e te enviar a localização,
      qual o melhor WhatsApp para contato?"

[Se não tem email]
Bot: "Posso te enviar os detalhes do imóvel por email também.
      Qual seu email?"
```

### Fase 4: Proposta de Horário Específico

```
Bot: "Encontrei disponibilidade para:
      
      📅 Sábado, 15/02 às 10:30
      📍 Rua das Flores, 123 - Jardins
      👤 Com o corretor Carlos
      
      Confirma esse horário? (Sim/Não/Outro)"
```

### Fase 5: Confirmação Final

```
Bot: "✅ Visita agendada!
      
      📅 Sábado, 15/02/2025 às 10:30
      📍 Rua das Flores, 123, Apto 71 - Jardins
      👤 Corretor: Carlos Silva (11) 99999-9999
      
      Vou te enviar um lembrete 24h antes e 2h antes.
      Qualquer dúvida, é só me chamar! 🏠"
```

---

## 📱 Sequência de Confirmação

### Timeline de Lembretes

```
AGENDAMENTO
    ↓
D-1 (24h antes)
    → "Olá [Nome]! Lembrando da visita amanhã às [hora] em [endereço]"
    → "Confirma presença? (Sim/Reagendar)"
    ↓
D-0 (2h antes)
    → "Sua visita é em 2 horas! 🏠
        📍 [endereço] 
        👤 [corretor] já está te esperando"
    ↓
D+0 (pós-visita, 2h depois)
    → "E aí, [Nome]! O que achou do imóvel?
        Podemos agendar outra visita ou bater um papo sobre propostas?"
```

### Mensagem de Lembrete D-1

```
"Olá, [Nome]! 👋

Passando para confirmar sua visita amanhã:

📅 [Data] às [Hora]
📍 [Endereço completo]
🏠 [Descrição breve do imóvel]
👤 [Nome do corretor]

Confirma presença?
✅ Sim, estarei lá
🔄 Preciso reagendar
❌ Cancelar

Qualquer dúvida, estou por aqui!"
```

---

## 🗺️ Otimização de Rotas

### Quando o Lead Quer Ver Múltiplos Imóveis

**Princípios:**
1. **Máximo 3 visitas por período** (manhã OU tarde)
2. **Intervalo de 40-60 min** entre visitas
3. **Roteiro geográfico** (evitar ziguezague)
4. **Melhor imóvel por último** (efeito recência)

**Exemplo de Roteiro:**

```
MANHÃ DE SÁBADO - 3 VISITAS

09:30 - Imóvel 1 (Bairro A) - "Aquecimento"
        Bom imóvel, estabelece expectativa
        ↓ 15 min de deslocamento
        
10:30 - Imóvel 2 (Bairro B) - "Comparação"
        Diferente do primeiro, amplia visão
        ↓ 20 min de deslocamento
        
11:30 - Imóvel 3 (Bairro C) - "Favorito"
        Melhor match, fecha com chave de ouro
        
12:30 - Encerramento
        "E aí, qual mais gostou?"
```

---

## ⚠️ Gestão de Cancelamentos e No-Shows

### Prevenção de No-Show

| Estratégia | Implementação |
|------------|---------------|
| **Confirmação D-1** | Obrigatória, esperar resposta |
| **Lembrete D-0** | 2h antes, com mapa |
| **Skin in the game** | "O corretor reservou a tarde para você" |
| **Alternativa imediata** | "Se não puder, posso reagendar para..." |

### Quando Lead Cancela

```
Bot: "Entendi, [Nome]. Sem problemas! 
      
      Posso já reagendar para outro dia?
      
      📅 [Próxima sugestão disponível]
      
      Ou prefere que eu entre em contato na próxima semana?"
```

### Quando Lead Dá No-Show

```
[Esperar 15 min após horário]

Bot: "Oi, [Nome]! Tudo bem?
      O corretor Carlos está te esperando no endereço.
      Você está a caminho?"

[Se não responder em 30 min]

Bot: "Vimos que não foi possível comparecer hoje.
      Sem problemas! Quer remarcar para outro dia?
      
      [Opções de reagendamento]"
```

---

## 🏠 Considerações por Tipo de Imóvel

### Imóvel Ocupado (Morador Atual)

| Cuidado | Ação |
|---------|------|
| Horário restrito | Agendar com antecedência maior |
| Menos flexibilidade | Confirmar com morador antes |
| Imóvel "vivido" | Preparar lead para imperfeições |
| Constrangimento | Visita mais rápida, objetiva |

### Imóvel Vazio

| Vantagem | Como aproveitar |
|----------|-----------------|
| Flexibilidade total | Oferecer múltiplos horários |
| Cliente à vontade | Permitir visita mais longa |
| Foco no espaço | Levar planta, fita métrica |

### Lançamento na Planta

| Diferença | Abordagem |
|-----------|-----------|
| Não há imóvel físico | Agendar visita ao decorado |
| Stand de vendas | Horário comercial do stand |
| Plantão de vendas | Fim de semana mais movimento |

---

## 📊 Métricas de Agendamento

| Métrica | Meta | Fórmula |
|---------|------|---------|
| **Taxa de Confirmação** | >80% | Confirmados / Agendados |
| **Taxa de Comparecimento** | >85% | Compareceram / Confirmados |
| **No-Show Rate** | <10% | Não compareceram / Agendados |
| **Reagendamento Rate** | <20% | Reagendados / Agendados |
| **Time to Schedule** | <2h | Tempo entre qualificação e agendamento |

---

## ❌ Anti-Patterns de Agendamento

| Erro | Por que é ruim | Faça isso |
|------|----------------|-----------|
| Agendar sem confirmar lead | Alta taxa de no-show | Confirme antes de reservar corretor |
| Muitas visitas no mesmo dia | Cansa o cliente, confunde | Máximo 3 por período |
| Não perguntar quem vem junto | Decidor ausente | Sempre pergunte |
| Horário vago "período da tarde" | Desencontros | Horário específico sempre |
| Não enviar lembretes | Esquecimento | D-1 e D-0 obrigatórios |
| Forçar horário do corretor | Cliente desiste | Adapte-se ao cliente |

---

## 💡 Scripts de Reagendamento

### Quando Corretor Não Pode

```
"Oi, [Nome]! Infelizmente o corretor Carlos teve um imprevisto
e não poderá atender no horário combinado. Peço desculpas!

Posso te oferecer:
📅 Mesmo dia, às [novo horário] com o corretor [outro]
📅 [Próximo dia], mesmo horário com Carlos

Qual prefere?"
```

### Quando Lead Pede para Remarcar

```
"Sem problemas! Vamos encontrar um novo horário.

[Próximas 3 opções disponíveis]

Qual funciona melhor para você?"
```

---

## 🔄 Integração com Calendário

### Campos Essenciais do Evento

```typescript
interface VisitaAgendada {
  // Identificação
  id: string;
  leadId: string;
  imovelId: string;
  corretorId: string;
  
  // Agendamento
  dataHora: Date;
  duracao: number; // minutos
  
  // Local
  endereco: string;
  complemento?: string;
  instrucoes?: string; // "Interfone 71, falar com portaria"
  
  // Participantes
  acompanhantes: number;
  quemVem: string; // "Casal", "Sozinho", "Com filhos"
  
  // Status
  status: 'agendada' | 'confirmada' | 'realizada' | 'cancelada' | 'no_show';
  
  // Lembretes
  lembreteD1Enviado: boolean;
  lembreteD0Enviado: boolean;
  
  // Feedback
  feedback?: string;
  interesseContinua?: boolean;
}
```

---

> **Lembre-se:** A visita é o momento da verdade. Todo o trabalho de qualificação e match leva a esse encontro. Não desperdice com agendamento ruim.
