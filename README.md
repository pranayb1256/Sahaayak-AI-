# Sahaayak AI 

### Agentic AI Elder-Care Coordinator for Indian Families

Sahaayak AI is an AI-powered elder-care coordination platform designed for Indian families.

The system helps elderly people manage everyday care activities such as medications, appointments, check-ins, and important events while helping family caregivers stay informed.

The goal is not to replace doctors or caregivers. Sahaayak acts as an intelligent coordination layer between an elderly person and their family.

---

## 🚨 Problem

India's elderly population is growing rapidly, while many families are increasingly distributed across different cities.

A common situation is:

```text
Parent in Pune
      ↓
Child in Mumbai
      ↓
Sibling in Bangalore
      ↓
Care coordination through
WhatsApp + phone calls + memory
```

This creates problems such as:

* Missed medication reminders
* Forgotten appointments
* Poor communication between family members
* Difficulty tracking recurring symptoms or care events
* Lack of a central view of an elderly parent's day-to-day situation

Sahaayak aims to address this using AI-assisted care coordination.

---

## 💡 Solution

Sahaayak provides an AI assistant that can:

* Understand natural language and Hinglish
* Retrieve medication information
* Retrieve upcoming appointments
* Record care events
* Maintain long-term care context
* Perform tool-based actions
* Provide proactive check-ins
* Escalate potentially urgent situations to caregivers
* Provide caregivers with a summarized view of the elder's recent activity

---

# 🧠 Core Idea

A traditional chatbot works like:

```text
User
  ↓
LLM
  ↓
Response
```

Sahaayak is designed as an agentic system:

```text
User
  ↓
Conversation Agent
  ↓
Understand intent
  ↓
Retrieve relevant context
  ↓
Select tool
  ↓
Execute tool
  ↓
Validate result
  ↓
Update memory
  ↓
Respond
```

This allows the AI to interact with real application state instead of simply generating text.

---

# 🏗️ Architecture

```text
                         ┌──────────────────┐
                         │      Elder       │
                         │ Voice / Text     │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Conversation     │
                         │ Agent             │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Care Agent     │
                         └────────┬─────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
        Medication Tool     Appointment Tool     Event Tool
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Database      │
                         │ PostgreSQL       │
                         │ + pgvector       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Safety Layer     │
                         │ + Escalation     │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Family Caregiver │
                         │ Dashboard        │
                         └──────────────────┘
```

---

# ⚙️ Tech Stack

## Backend

* Python
* FastAPI
* SQLModel
* PostgreSQL
* SQLAlchemy

## AI

* OpenAI API
* LangChain
* LangGraph
* RAG
* Tool calling
* Long-term memory

## Frontend

* Next.js
* React
* Tailwind CSS

## Voice

* Speech-to-Text
* Text-to-Speech

## Messaging

* WhatsApp API

## Infrastructure

* Docker
* PostgreSQL
* Redis
* Cloud deployment

---

# ✨ Planned Features

### Elder Assistant

Natural language interaction for elderly users.

Example:

```text
"Meri medicine kab leni hai?"
```

```text
"Kal doctor ka appointment hai kya?"
```

```text
"Mujhe thoda chakkar aa raha hai."
```

The agent interprets the request and interacts with the appropriate tools.

---

### Medication Management

Store:

```text
Medicine
Dosage
Schedule
Notes
```

The system will eventually support proactive reminders and missed-medication detection.

---

### Appointment Management

Track:

```text
Doctor
Specialty
Date
Time
Location
Notes
```

Example:

```text
"Cardiology appointment Friday at 11 AM."
```

---

### Care Event Timeline

Important events are stored as part of the elder's care history.

Example:

```text
09:15 AM
Morning check-in completed

11:30 AM
Mild dizziness reported

06:30 PM
Evening medication confirmed
```

---

### Agentic AI

The agent will be able to decide when to use tools.

Example:

```text
User:
"Papa ka next doctor appointment kab hai?"

Agent:
→ get_upcoming_appointments()

Database:
→ Cardiology
→ 25 September
→ 11:00 AM

Agent:
→ Returns the result to the user
```

---

### Memory + RAG

The system will eventually maintain:

```text
Short-term conversation memory
+
Long-term care events
+
Semantic memory
```

This allows the agent to answer questions using relevant historical context.

---

### Safety Layer

LLM reasoning will not independently control critical safety decisions.

The architecture will use:

```text
LLM
 ↓
Safety validation
 ↓
Deterministic rules
 ↓
Escalation
```

This separation is intentional.

Sahaayak is a care coordination system and does not replace professional medical diagnosis or treatment.

---

# 🇮🇳 Built for India

Sahaayak is designed around Indian family-care workflows.

Potential capabilities include:

* Hindi interaction
* Hinglish interaction
* WhatsApp-first communication
* Family caregiver networks
* Doctor appointment coordination
* Medication reminders
* Local caregiver escalation
* Multi-city family coordination

Example:

```text
"Mummy ki kal doctor ki appointment hai kya?"
```

The system should understand the intent without requiring formal English.

---

# 📂 Project Structure

```text
sahaayak-ai/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── elders.py
│       ├── medications.py
│       ├── appointments.py
│       └── events.py
│
├── tests/
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# 🚀 Local Development

## Requirements

* Python 3.11+
* uv
* Git

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/sahaayak-ai.git
cd sahaayak-ai
```

## Install dependencies

```bash
uv sync
```

## Start the API

```bash
uv run uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 🎯 Project Goal

The goal of Sahaayak is to explore how agentic AI can be used for real-world elder-care coordination.

The project focuses on:

```text
LLMs
+
Agentic workflows
+
Tool calling
+
Memory
+
RAG
+
Voice AI
+
Safety engineering
+
Real-world backend systems
```

This is an educational and prototype project. It is not a medical device and does not provide professional medical diagnosis or treatment.

---

# � Author

## Pranay

Built as a learning project focused on:

* Backend Engineering
* Agentic AI
* Generative AI
* AI Systems
* Healthcare Technology
