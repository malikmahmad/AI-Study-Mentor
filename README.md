# 🧠 AI Study Mentor — Multi-Agent Learning System

> **Microsoft Agents League Hackathon 2026 | Reasoning Agents Track**  
> Built with Microsoft Foundry · Foundry IQ · Work IQ · Fabric IQ

---

## 📌 Problem Statement

Organizations invest heavily in employee certification programmes, yet most fail due to three core gaps:

- **No personalized guidance** — one-size-fits-all study plans ignore individual capacity and workload
- **No adaptive feedback loops** — learners don't know *why* they're failing, only *that* they are
- **No manager visibility** — teams operate blind, with no signal on who is at risk until it's too late

**AI Study Mentor** solves this with a multi-agent AI system that reasons, adapts, and acts — not just responds.

---

## 🤖 System Architecture

```
User Goal Input
      │
      ▼
┌─────────────────────────────────────────────────────────┐
│              ORCHESTRATOR (Reasoning Coordinator)        │
│         Routes agents · Manages reasoning loop          │
└────┬──────────┬──────────┬──────────┬───────────────────┘
     │          │          │          │
     ▼          ▼          ▼          ▼
┌─────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐
│Learning │ │  Study   │ │Engagement│ │   Assessment     │
│  Path   │ │ Planner  │ │  Agent   │ │     Agent        │
│ Curator │ │  Agent   │ │          │ │                  │
└────┬────┘ └────┬─────┘ └────┬─────┘ └────────┬─────────┘
     │           │             │                │
     └───────────┴─────────────┴────────────────┘
                                │
                    ┌───────────▼──────────┐
                    │  REASONING LOOP      │
                    │  (if score < thresh) │
                    │  → optimize plan     │
                    │  → re-evaluate       │
                    └───────────┬──────────┘
                                │
                    ┌───────────▼──────────┐
                    │  Manager Insights    │
                    │     Agent           │
                    └──────────────────────┘
```

---

## 🧩 Agent Responsibilities

| Agent | Role | IQ Layer |
|-------|------|----------|
| 📚 **Learning Path Curator** | Maps certification goals to skill gaps, retrieves grounded learning resources | Foundry IQ |
| 🗓 **Study Planner Agent** | Builds adaptive, capacity-aware study schedules | Foundry IQ + Fabric IQ |
| ⏰ **Engagement Agent** | Sends context-sensitive reminders based on calendar and work patterns | Work IQ |
| 🧠 **Assessment Agent** | Evaluates readiness, performs skill gap analysis, reasons over performance data | Foundry IQ + Fabric IQ |
| 📊 **Manager Insights Agent** | Surfaces team-level risk, progress trends, and capacity correlations | Fabric IQ + Work IQ |
| 🔄 **Orchestrator** | Coordinates agent flow, triggers reasoning loop when threshold not met | Core |

---

## 💡 Microsoft IQ Integration

### Foundry IQ
Retrieves grounded learning materials, cited certification resources, and generates assessment questions from an indexed knowledge base. Used by the Learning Path Curator and Assessment Agent to ensure answers are sourced — not hallucinated.

### Work IQ
Reads organizational work context signals — meeting load, focus-time windows, collaboration patterns. Used by the Engagement Agent to schedule learning blocks that don't conflict with peak work periods.

### Fabric IQ
Builds a semantic ontology connecting **Employee → Role → Skills → Certification → Readiness Score**. Used by the Assessment Agent and Insights Agent to reason over structured relationships, detect skill gaps, and identify workforce risk patterns.

---

## 🔄 Reasoning Loop

When assessment score falls below the pass threshold, the system does not simply report failure. It **reasons**:

```
Assessment Agent → detects gap
        ↓
Orchestrator → root cause analysis
        ↓
Study Planner → optimized re-learning path
        ↓
Engagement Agent → re-scheduled reminders
        ↓
Assessment Agent → re-evaluation cycle
```

This iterative loop mirrors real enterprise AI behavior — acting until the goal is achieved, not stopping at first failure.

---

## 🏗️ Project Structure

```
AI-Study-Mentor/
│
├── agents/
│   ├── planner_agent.py        # Learning path + study schedule generation
│   ├── assessment_agent.py     # Performance evaluation + skill gap analysis
│   ├── engagement_agent.py     # Work IQ-aware reminders and scheduling
│   └── insights_agent.py       # Team-level analytics and risk detection
│
├── core/
│   └── orchestrator.py         # Reasoning loop + agent coordination
│
├── data/
│   └── synthetic_data.json     # Synthetic learner + work signal + cert data
│
├── main.py                     # System entry point + agent orchestration
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Git
- (Optional) Azure subscription for Foundry integration

### Installation

```bash
# Clone the repository
git clone https://github.com/malikmahmad/AI-Study-Mentor.git
cd AI-Study-Mentor

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

---

## 📊 Sample System Output

```
============================================================
  AI STUDY MENTOR – Multi-Agent Learning System
============================================================
  Microsoft Foundry | Reasoning Agents Track

  [Foundry IQ]  Connecting to knowledge base...
  [Work IQ]     Analyzing meeting load, focus time, and activity patterns...
  [Fabric IQ]   Mapping: Employee → Role → Skills → Certification → Readiness

  ✓ All Microsoft IQ layers initialized successfully.

  AGENT 3 – Assessment Agent  [Foundry IQ + Fabric IQ]
  ──────────────────────────────────────────────────
  Current Score : 67%    Pass Threshold: 70%    Gap: 3%
  Status        : ⚠  CLOSE – Minor gap detected
  Reasoning     : Learner is near-ready with small knowledge gaps.
  Recommendation: 2-day focused review on weak areas.

  REASONING LOOP TRIGGERED → Returning to Study Planner.
  Root Cause    : Minor knowledge gaps in specific topics.
  Strategy      : 2-day targeted revision + 1 mock test.
  Additional Hours: +4 hrs recommended
============================================================
```

---

## 🧪 Reasoning Patterns Applied

| Pattern | Where Used |
|---------|-----------|
| **Planner–Executor** | Orchestrator routes tasks to specialized agents |
| **Critic / Verifier** | Assessment Agent validates readiness before proceeding |
| **Self-reflection & Iteration** | Reasoning loop triggers re-optimization when below threshold |
| **Role-based Specialisation** | Each agent has one clear responsibility, no overlap |

---

## 🔐 Security & Data Policy

> ⚠️ **All data in this project is 100% synthetic.**  
> No real customer data, real employee records, or PII of any kind is used.  
> Synthetic identifiers (L-1001, EMP-001) are used throughout.  
> This project complies fully with Microsoft's hackathon data guidelines.

**Security practices followed:**
- `.env` files excluded via `.gitignore`
- No credentials, API keys, or connection strings committed
- No confidential or proprietary information included

---

## 🏆 Evaluation Alignment

| Criterion | How This Project Addresses It |
|-----------|-------------------------------|
| **Accuracy & Relevance (25%)** | Directly implements the enterprise learning scenario from the challenge brief |
| **Reasoning & Multi-step Thinking (25%)** | 5-agent orchestration + iterative reasoning loop |
| **Creativity & Originality (15%)** | Adaptive scoring, root cause analysis, Work IQ-aware scheduling |
| **User Experience & Presentation (15%)** | Clean structured output, clear agent flow, demoable from CLI |
| **Reliability & Safety (20%)** | Synthetic data only, no secrets committed, safe guardrails |

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Architecture:** Multi-Agent Reasoning System
- **AI Platform:** Microsoft Azure AI Foundry (conceptual integration)
- **IQ Layers:** Foundry IQ · Work IQ · Fabric IQ
- **Dev Tools:** GitHub Copilot (AI-assisted development)
- **Data:** Synthetic JSON datasets (no PII)

---

## 👤 Author

**Malik Muhammad Ahmad**  
Full-Stack Developer & AI Engineer · Pakistan  
GitHub: [@malikmahmad](https://github.com/malikmahmad)  

*Submitted for Microsoft Agents League Hackathon 2026 — Reasoning Agents Track*
