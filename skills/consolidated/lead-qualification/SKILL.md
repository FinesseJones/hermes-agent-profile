---
name: lead-qualification
description: Expert framework for qualifying leads through conversational AI, particularly via WhatsApp. Covers BANT methodology, scoring algorithms, progressive profiling, and CRM integration. Use when building or optimizing lead qualification chatbots, sales automation, or customer qualification systems.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
skills: clean-code, api-patterns, nodejs-best-practices
---

# Lead Qualification - WhatsApp Sales Automation

> **Transform conversations into qualified leads with proven frameworks**

---

## 🏗️ Specialized Domains

> **Building for Real Estate?**
> Use the specialized skill [real-estate-qualification](../real-estate-qualification/SKILL.md) instead! It includes:
> - Property-specific BANT framework
> - Buyer/Renter/Seller persona flows
> - CRM integration for real estate

---

## 🎯 The Lead Qualification Funnel

```
CONVERSATION START
       ↓
┌──────────────────┐
│  1. ENGAGE       │  Get them talking
│  (First 30s)     │  ✅ Friendly greeting
└────────┬─────────┘  ✅ Quick value prop
         ↓
┌──────────────────┐
│  2. DISCOVER     │  Learn their needs
│  (2-3 minutes)   │  ✅ Ask smart questions
└────────┬─────────┘  ✅ Active listening
         ↓
┌──────────────────┐
│  3. QUALIFY      │  BANT framework
│  (3-5 minutes)   │  ✅ Budget
└────────┬─────────┘  ✅ Authority
         ↓             ✅ Need
┌──────────────────┐  ✅ Timing
│  4. SCORE        │  Calculate lead score
│  (Real-time)     │  ✅ 0-100 points
└────────┬─────────┘  ✅ Hot/Warm/Cold
         ↓
┌──────────────────┐
│  5. ROUTE        │  Smart handoff
│  (Instant)       │  ✅ Hot → Sales team
└────────┬─────────┘  ✅ Warm → Nurture
         ↓             ✅ Cold → Drip campaign
   QUALIFIED LEAD
```

---

## 🔥 BANT Framework (Your Foundation)

### B - Budget

**Goal**: Understand their financial capacity

**Questions** (Natural, not interrogative):
```
❌ Bad: "What's your budget?"
✅ Good: "Just to make sure I recommend the right plan - are you looking at 
         solutions around $500/month, $1000/month, or more?"

❌ Bad: "How much can you spend?"
✅ Good: "Most of our clients invest between $X and $Y per month. 
         Does that range work for your team?"
```

**Extraction Patterns**:
```typescript
function extractBudget(conversation: string): Budget {
  // Direct mentions
  if (/\$\d+|\d+\s*dollars|\d+\s*reais/i.test(conversation)) {
    const amount = extractNumber(conversation);
    return classifyBudget(amount);
  }
  
  // Indirect signals
  if (/cheap|affordable|low cost|tight budget/i.test(conversation)) {
    return 'low';
  }
  
  if (/premium|enterprise|best|unlimited/i.test(conversation)) {
    return 'high';
  }
  
  // Company size proxy
  if (/startup|small business|10 people/i.test(conversation)) {
    return 'low-medium';
  }
  
  if (/enterprise|500\+ employees|corporation/i.test(conversation)) {
    return 'high';
  }
  
  return 'unknown';
}
```

---

### A - Authority

**Goal**: Identify decision-making power

**Questions**:
```
✅ "Are you the one who'll be making the final decision on this, 
    or will you be involving others?"

✅ "Who else on your team would need to approve this?"

✅ "Walk me through your typical decision process for new tools"
```

**Classification**:
```typescript
enum Authority {
  DECISION_MAKER = 'decision_maker',     // Can say yes alone (25 pts)
  INFLUENCER = 'influencer',             // Strong voice (15 pts)
  CHAMPION = 'champion',                 // Will advocate (10 pts)
  END_USER = 'end_user',                 // Just using it (5 pts)
  RESEARCHER = 'researcher',             // Just looking (0 pts)
}

function detectAuthority(conversation: string): Authority {
  // Strong signals
  if (/I'm the (CEO|founder|owner|head of)/i.test(conversation)) {
    return Authority.DECISION_MAKER;
  }
  
  if (/I decide|my decision|I approve|I sign off/i.test(conversation)) {
    return Authority.DECISION_MAKER;
  }
  
  // Moderate signals
  if (/I'll recommend|I'll propose|I'm evaluating for/i.test(conversation)) {
    return Authority.INFLUENCER;
  }
  
  // Weak signals
  if (/just looking|researching|comparing options/i.test(conversation)) {
    return Authority.RESEARCHER;
  }
  
  return Authority.END_USER;
}
```

---

### N - Need

**Goal**: Understand urgency and pain level

**Questions**:
```
✅ "What's prompting you to look for a solution right now?"

✅ "What happens if you don't solve this soon?"

✅ "On a scale of 1-10, how urgent is this for you?"
```

**Classification**:
```typescript
enum NeedLevel {
  CRITICAL = 'critical',      // Hair on fire (25 pts)
  HIGH = 'high',              // Urgent (20 pts)
  MODERATE = 'moderate',      // Exploring (10 pts)
  LOW = 'low',                // Nice to have (5 pts)
  UNKNOWN = 'unknown',        // Not discussed (0 pts)
}

function detectNeedLevel(conversation: string): NeedLevel {
  // Critical urgency signals
  const criticalPatterns = [
    /urgently need|ASAP|emergency|losing (money|customers)/i,
    /current solution (broke|failing|down)/i,
    /can't continue without|must have by/i
  ];
  
  if (criticalPatterns.some(p => p.test(conversation))) {
    return NeedLevel.CRITICAL;
  }
  
  // High urgency
  const highPatterns = [
    /need (soon|quickly|this (month|quarter))/i,
    /growing (fast|rapidly)|scaling/i,
    /competitors are|falling behind/i
  ];
  
  if (highPatterns.some(p => p.test(conversation))) {
    return NeedLevel.HIGH;
  }
  
  // Exploring
  if (/just looking|researching|comparing/i.test(conversation)) {
    return NeedLevel.MODERATE;
  }
  
  return NeedLevel.UNKNOWN;
}
```

---

### T - Timing

**Goal**: When will they buy?

**Questions**:
```
✅ "When are you looking to get started?"

✅ "What's your ideal timeline for this?"

✅ "Any specific deadline you're working toward?"
```

**Classification**:
```typescript
enum Timing {
  IMMEDIATE = 'immediate',           // This week (20 pts)
  THIS_MONTH = 'this_month',         // Within 30 days (15 pts)
  THIS_QUARTER = 'this_quarter',     // 1-3 months (10 pts)
  LONG_TERM = 'long_term',           // 3+ months (5 pts)
  UNKNOWN = 'unknown',               // Not discussed (0 pts)
}

function detectTiming(conversation: string): Timing {
  if (/today|tomorrow|this week|right now|immediately/i.test(conversation)) {
    return Timing.IMMEDIATE;
  }
  
  if (/this month|next (week|month)|within 30 days/i.test(conversation)) {
    return Timing.THIS_MONTH;
  }
  
  if (/next quarter|Q[1-4]|in \d-3 months/i.test(conversation)) {
    return Timing.THIS_QUARTER;
  }
  
  if (/next year|long term|future|someday/i.test(conversation)) {
    return Timing.LONG_TERM;
  }
  
  return Timing.UNKNOWN;
}
```

---

## 🎯 Lead Scoring Algorithm

### Complete Scoring System

```typescript
interface LeadScore {
  total: number;              // 0-100
  category: 'hot' | 'warm' | 'cold';
  breakdown: {
    budget: number;           // 0-30
    authority: number;        // 0-25
    need: number;             // 0-25
    timing: number;           // 0-20
  };
  confidence: number;         // 0-100 (how certain we are)
  readyForSales: boolean;
}

function calculateLeadScore(
  budget: Budget,
  authority: Authority,
  need: NeedLevel,
  timing: Timing
): LeadScore {
  let budgetScore = 0;
  let authorityScore = 0;
  let needScore = 0;
  let timingScore = 0;
  let confidence = 0;
  
  // Budget scoring (30 points max)
  switch (budget) {
    case 'high':
      budgetScore = 30;
      confidence += 25;
      break;
    case 'medium':
      budgetScore = 20;
      confidence += 25;
      break;
    case 'low':
      budgetScore = 10;
      confidence += 25;
      break;
    case 'unknown':
      budgetScore = 5;  // Give some benefit of doubt
      break;
  }
  
  // Authority scoring (25 points max)
  switch (authority) {
    case Authority.DECISION_MAKER:
      authorityScore = 25;
      confidence += 25;
      break;
    case Authority.INFLUENCER:
      authorityScore = 15;
      confidence += 20;
      break;
    case Authority.CHAMPION:
      authorityScore = 10;
      confidence += 15;
      break;
    case Authority.END_USER:
      authorityScore = 5;
      confidence += 10;
      break;
  }
  
  // Need scoring (25 points max)
  switch (need) {
    case NeedLevel.CRITICAL:
      needScore = 25;
      confidence += 25;
      break;
    case NeedLevel.HIGH:
      needScore = 20;
      confidence += 20;
      break;
    case NeedLevel.MODERATE:
      needScore = 10;
      confidence += 15;
      break;
    case NeedLevel.LOW:
      needScore = 5;
      confidence += 10;
      break;
  }
  
  // Timing scoring (20 points max)
  switch (timing) {
    case Timing.IMMEDIATE:
      timingScore = 20;
      confidence += 25;
      break;
    case Timing.THIS_MONTH:
      timingScore = 15;
      confidence += 20;
      break;
    case Timing.THIS_QUARTER:
      timingScore = 10;
      confidence += 15;
      break;
    case Timing.LONG_TERM:
      timingScore = 5;
      confidence += 10;
      break;
  }
  
  const total = budgetScore + authorityScore + needScore + timingScore;
  
  // Categorize
  let category: 'hot' | 'warm' | 'cold';
  if (total >= 70) category = 'hot';
  else if (total >= 40) category = 'warm';
  else category = 'cold';
  
  // Ready for sales if:
  // - Score >= 70 OR
  // - Score >= 50 AND need is critical
  const readyForSales = total >= 70 || (total >= 50 && need === NeedLevel.CRITICAL);
  
  return {
    total,
    category,
    breakdown: {
      budget: budgetScore,
      authority: authorityScore,
      need: needScore,
      timing: timingScore,
    },
    confidence: Math.min(confidence, 100),
    readyForSales,
  };
}
```

---

## 💬 Conversation Patterns for Qualification

### Pattern 1: Natural BANT Extraction

```typescript
// Example conversation flow
const qualificationFlow = {
  stage1_engage: {
    bot: "Hey! 👋 I'm here to help. What brings you to us today?",
    extract: ['initial_need', 'pain_point']
  },
  
  stage2_understand_need: {
    bot: "Got it! [Reflect their need]. How long has this been a challenge?",
    extract: ['need_level', 'timing_hints']
  },
  
  stage3_explore_impact: {
    bot: "I hear you. What happens if you don't solve this soon?",
    extract: ['need_urgency', 'budget_hints']
  },
  
  stage4_team_context: {
    bot: "Makes sense. Are you evaluating this for yourself or your team?",
    extract: ['company_size', 'authority']
  },
  
  stage5_decision_process: {
    bot: "Cool! Walk me through how you typically decide on new tools?",
    extract: ['authority_level', 'timing']
  },
  
  stage6_budget_range: {
    bot: "Just to make sure I point you to the right solution - most of our clients invest $X-$Y/month. Does that range work?",
    extract: ['budget']
  },
  
  stage7_timeline: {
    bot: "Perfect! When are you looking to get started?",
    extract: ['timing']
  }
};
```

### Pattern 2: Progressive Profiling

Don't ask everything at once. Build profile gradually:

```typescript
interface UserProfile {
  // Session 1
  name?: string;
  initialNeed?: string;
  
  // Session 2
  company?: string;
  role?: string;
  
  // Session 3
  teamSize?: number;
  budget?: Budget;
  
  // Session 4
  authority?: Authority;
  timing?: Timing;
  
  // Calculated
  lastActivity: Date;
  totalSessions: number;
  leadScore: LeadScore;
}

// Only ask what you don't know
function getNextQuestion(profile: UserProfile): string {
  if (!profile.name) {
    return "By the way, what should I call you?";
  }
  
  if (!profile.company) {
    return `Nice to meet you, ${profile.name}! What company are you with?`;
  }
  
  if (!profile.teamSize) {
    return "How big is your team?";
  }
  
  if (!profile.budget) {
    return "Just to recommend the right plan - what's your budget range?";
  }
  
  // All info collected!
  return null;
}
```

---

## 🔄 Smart Routing Logic

### Routing Rules

```typescript
async function routeLead(lead: LeadScore, profile: UserProfile) {
  // HOT LEADS (70-100) → Immediate sales handoff
  if (lead.category === 'hot') {
    await notifySalesTeam({
      urgency: 'high',
      lead: profile,
      score: lead.total,
      message: `🔥 HOT LEAD: ${profile.name} from ${profile.company} - Score: ${lead.total}`
    });
    
    // Also send to CRM
    await syncToCRM(profile, {
      status: 'hot_lead',
      assignTo: await getAvailableSalesRep(),
      priority: 'high'
    });
    
    // Tell user
    return {
      message: `Great! ${profile.name}, I'm connecting you with Sarah from our sales team. 
                She'll reach out within 15 minutes to help you get started! 📞`,
      action: 'handoff_to_sales'
    };
  }
  
  // WARM LEADS (40-69) → Nurture sequence
  if (lead.category === 'warm') {
    await addToNurtureSequence(profile, {
      sequence: 'warm_lead_nurture',
      startDelay: '1 hour',
      emails: ['value_prop', 'case_study', 'demo_offer']
    });
    
    return {
      message: `Thanks ${profile.name}! I've sent you some info about how we've helped companies like ${profile.company}. 
                Want to schedule a quick 15-min demo?`,
      action: 'offer_demo'
    };
  }
  
  // COLD LEADS (<40) → Long-term nurture
  if (lead.category === 'cold') {
    await addToDripCampaign(profile, {
      campaign: 'cold_lead_education',
      frequency: 'weekly',
      duration: '3 months'
    });
    
    return {
      message: `Thanks for chatting, ${profile.name}! I've added you to our newsletter. 
                When you're ready to explore further, just ping me! 👍`,
      action: 'add_to_newsletter'
    };
  }
}
```

---

## 📊 Performance Metrics

### Key Metrics to Track

```typescript
interface QualificationMetrics {
  // Funnel
  conversationsStarted: number;
  conversationsCompleted: number;
  leadsQualified: number;
  
  // Quality
  hotLeads: number;
  warmLeads: number;
  coldLeads: number;
  averageScore: number;
  
  // Efficiency
  averageQualificationTime: number;  // minutes
  questionsToQualify: number;
  
  // Conversion
  leadToSQLRate: number;  // Sales Qualified Lead
  SQLToCustomerRate: number;
  
  // Revenue
  pipelineValue: number;
  averageDealSize: number;
}

// Dashboard
async function generateQualificationDashboard(): Promise<Dashboard> {
  const metrics = await getMetrics();
  
  return {
    summary: {
      totalLeads: metrics.leadsQualified,
      hotLeadRate: (metrics.hotLeads / metrics.leadsQualified) * 100,
      avgScore: metrics.averageScore,
      pipelineValue: metrics.pipelineValue,
    },
    
    funnel: {
      started: metrics.conversationsStarted,
      completed: metrics.conversationsCompleted,
      qualified: metrics.leadsQualified,
      sql: metrics.leadsQualified * metrics.leadToSQLRate,
      customers: metrics.leadsQualified * metrics.leadToSQLRate * metrics.SQLToCustomerRate,
    },
    
    quality: {
      hot: metrics.hotLeads,
      warm: metrics.warmLeads,
      cold: metrics.coldLeads,
      distribution: calculateDistribution(metrics),
    },
    
    efficiency: {
      avgTime: metrics.averageQualificationTime,
      avgQuestions: metrics.questionsToQualify,
      completionRate: (metrics.conversationsCompleted / metrics.conversationsStarted) * 100,
    }
  };
}
```

---

## 🎯 50% Improvement Checklist

To achieve 50% improvement in lead qualification:

### Phase 1: Foundation (Week 1)
- [ ] Implement BANT framework
- [ ] Add lead scoring algorithm
- [ ] Track all 4 BANT criteria
- [ ] Set up basic routing (hot/warm/cold)

**Expected Impact**: +20%

### Phase 2: Intelligence (Week 2)
- [ ] Add NLP for better extraction
- [ ] Implement progressive profiling
- [ ] Add context memory
- [ ] Smart question sequencing

**Expected Impact**: +15%

### Phase 3: Optimization (Week 3)
- [ ] A/B test conversation flows
- [ ] Optimize qualification time
- [ ] Improve intent accuracy
- [ ] Add sentiment analysis

**Expected Impact**: +10%

### Phase 4: Integration (Week 4)
- [ ] Real-time CRM sync
- [ ] Sales team notifications
- [ ] Automated follow-ups
- [ ] Analytics dashboard

**Expected Impact**: +5%

**Total**: +50% improvement

---

## 💡 Pro Tips

### 1. Don't Qualify Too Early
❌ Asking BANT questions in first message  
✅ Build rapport first (3-5 messages), THEN qualify

### 2. Make It Conversational
❌ "What is your budget?"  
✅ "Most teams invest around $X-$Y. Does that work for you?"

### 3. Use Social Proof
```
"Companies like [similar company] typically start with our Pro plan 
for teams your size. Sound about right?"
```

### 4. Extract Implicitly
Don't always ask directly. Extract from context:
- "We're a startup" → Budget = low-medium
- "I'm the CEO" → Authority = decision_maker
- "Current tool is broken" → Need = critical

### 5. Know When to Hand Off
If score > 70 OR user requests human → Hand off immediately

---

## 🔧 Implementation Example

See `examples/lead-qualification-bot.ts` for complete working example.

---

> **Remember**: Lead qualification is a balance between gathering information and building rapport. Too pushy = drop-off. Too passive = unqualified leads. Find the sweet spot.
