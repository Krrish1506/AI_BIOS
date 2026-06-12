# AI_BIOS_MASTER.md
# AI Business Intelligence Operating System
## Complete Engineering & Implementation Master Document

> **Version:** 1.0.0  
> **Status:** Production-Ready Blueprint  
> **Document Classification:** Engineering Master Specification  
> **Intended Audience:** AI Coding Agents (Cursor, Claude Code, OpenHands, Roo Code, Continue.dev, Cline) and Engineering Teams  
> **Last Updated:** 2026-06-04  
> **Total Phases:** 5  
> **Estimated Team Size:** 20 Engineers

---

> ⚠️ **AGENT INSTRUCTION:** This document is the SINGLE SOURCE OF TRUTH. Do not deviate from the architecture, folder structure, naming conventions, or technology choices defined here. Implement phase by phase. Do not skip phases. Do not mix concerns across phases. Reference the checklist in Section 28 after completing each phase.

---

## Table of Contents

1. [Executive Overview](#1-executive-overview)
2. [Product Requirements Document](#2-product-requirements-document)
3. [System Architecture](#3-system-architecture)
4. [Technology Decisions](#4-technology-decisions)
5. [Enterprise Folder Structure](#5-enterprise-folder-structure)
6. [Database Architecture](#6-database-architecture)
7. [API Architecture](#7-api-architecture)
8. [Authentication & Authorization](#8-authentication--authorization)
9. [Multi-Agent Architecture](#9-multi-agent-architecture)
10. [LangGraph Workflow](#10-langgraph-workflow)
11. [Data Analysis Engine](#11-data-analysis-engine)
12. [Visualization Engine](#12-visualization-engine)
13. [Forecasting Engine](#13-forecasting-engine)
14. [Reporting Engine](#14-reporting-engine)
15. [Chat With Data](#15-chat-with-data)
16. [File Management System](#16-file-management-system)
17. [SQL Integration](#17-sql-integration)
18. [Power BI Integration](#18-power-bi-integration)
19. [Computer Operator Agent](#19-computer-operator-agent)
20. [Security Architecture](#20-security-architecture)
21. [Performance Architecture](#21-performance-architecture)
22. [Monitoring & Observability](#22-monitoring--observability)
23. [Testing Strategy](#23-testing-strategy)
24. [CI/CD Pipeline](#24-cicd-pipeline)
25. [Deployment Architecture](#25-deployment-architecture)
26. [Phase-by-Phase Roadmap](#26-phase-by-phase-roadmap)
27. [Cursor Development Rules](#27-cursor-development-rules)
28. [Final Completion Checklist](#28-final-completion-checklist)

---

# 1. Executive Overview

## 1.1 Product Vision

AI-BIOS (AI Business Intelligence Operating System) is a production-grade, SaaS-ready platform that democratizes enterprise-level business intelligence by combining the capabilities of a full BI team into a single intelligent operating system. The platform replaces the need for:

- A dedicated Data Analyst who manually cleans and explores data
- A BI Analyst who builds dashboards in Power BI or Tableau
- A Data Scientist who builds forecasting models
- A Business Consultant who interprets findings and recommends actions
- A Report Writer who produces executive summaries and slide decks
- A SQL Analyst who writes complex queries across databases
- A Forecasting Expert who selects and tunes predictive models
- A Dashboard Developer who builds interactive visual interfaces

AI-BIOS provides all of these roles in one conversational, AI-first platform — available to any business user with no technical background required.

## 1.2 Business Goals

| Goal | Description | Success Metric |
|------|-------------|----------------|
| Reduce BI time-to-insight | From weeks to minutes | < 5 minutes for full EDA on a dataset |
| Democratize data analysis | Enable non-technical users | 80% of users require no SQL knowledge |
| SaaS monetization | Subscription tiers | MRR growth 20% MoM post-launch |
| Enterprise readiness | Security, RBAC, audit logs | SOC2-compatible audit trail |
| Agent-first architecture | Autonomous multi-agent workflows | 90% of tasks completed without human intervention |

## 1.3 Problems Solved

### Problem 1: Fragmented BI Tooling
Businesses use 4–8 separate tools (Excel, Power BI, Tableau, Python, SQL clients, Google Sheets) that don't communicate, creating data silos and workflow fragmentation. AI-BIOS consolidates all BI workflows into one platform.

### Problem 2: High Technical Barrier
Most BI platforms (dbt, Metabase, Superset) require SQL knowledge, Python skills, or complex configuration. AI-BIOS lowers the barrier to zero — users can simply upload a CSV and say "What are the key insights from this data?"

### Problem 3: Slow Report Generation
Enterprise reports typically take 2–4 weeks to produce. AI-BIOS generates executive-quality PDF and PPTX reports in under 3 minutes.

### Problem 4: No Forecasting for SMBs
Predictive analytics are out of reach for most SMBs due to cost and complexity. AI-BIOS provides Prophet, XGBoost, and regression-based forecasting behind a natural language interface.

### Problem 5: Disconnected Chat and Data
Existing chatbots have no awareness of uploaded datasets. AI-BIOS provides a RAG-powered chatbot that reasons directly against the user's data with full context memory.

## 1.4 Competitive Advantages

| Feature | AI-BIOS | Tableau | Power BI | ThoughtSpot | Metabase |
|---------|---------|---------|----------|-------------|----------|
| Natural language query | ✅ Full | ⚠️ Limited | ⚠️ Limited | ✅ Yes | ❌ No |
| Multi-agent automation | ✅ Full | ❌ No | ❌ No | ❌ No | ❌ No |
| File upload (CSV/XLSX) | ✅ Yes | ✅ Yes | ✅ Yes | ⚠️ Limited | ✅ Yes |
| Automated EDA | ✅ Full | ❌ No | ❌ No | ❌ No | ❌ No |
| Forecasting built-in | ✅ Full | ⚠️ Limited | ⚠️ Limited | ❌ No | ❌ No |
| PDF/PPTX report gen | ✅ Automated | ⚠️ Manual | ⚠️ Manual | ❌ No | ❌ No |
| Computer Operator Agent | ✅ Unique | ❌ No | ❌ No | ❌ No | ❌ No |
| Open source core | ✅ Yes | ❌ No | ❌ No | ❌ No | ✅ Yes |
| Free-tier deployment | ✅ Yes | ❌ No | ❌ No | ❌ No | ✅ Yes |

## 1.5 Market Positioning

AI-BIOS is positioned as **"The AI BI Team for Everyone"** — sitting at the intersection of enterprise BI (Tableau/Power BI) and AI assistant platforms (ChatGPT/Claude). It targets:

- **Primary:** SMBs (10–500 employees) lacking dedicated BI teams
- **Secondary:** Enterprise teams wanting to automate repetitive BI workflows
- **Tertiary:** Solo analysts and freelancers who need fast, polished deliverables

**Pricing Model (SaaS):**
| Tier | Price | Features |
|------|-------|---------|
| Free | $0/mo | 3 datasets, 5 analyses/mo, 100MB storage |
| Analyst | $29/mo | 20 datasets, unlimited analyses, 5GB storage |
| Team | $99/mo | Unlimited datasets, all agents, 50GB, RBAC |
| Enterprise | Custom | White-label, SSO, audit logs, SLA |

---

# 2. Product Requirements Document

## 2.1 User Personas

### Persona 1: Sarah — Operations Manager
- **Age:** 38 | **Company:** 80-person logistics firm
- **Technical Level:** Low (Excel user)
- **Pain Points:** Spends 6 hours/week manually creating reports in Excel. No visibility into trends until it's too late.
- **Goals:** Understand weekly operations KPIs without writing a single formula. Get automated alerts when metrics drop.
- **AI-BIOS Usage:** Uploads weekly ops CSV → gets instant dashboard + executive summary → shares PDF with leadership.

### Persona 2: Dev — Startup Founder
- **Age:** 29 | **Company:** 12-person SaaS startup
- **Technical Level:** Medium (knows SQL basics)
- **Pain Points:** Can't afford a BI analyst. Data lives in PostgreSQL but can't easily visualize it.
- **Goals:** Connect prod DB → explore cohort retention → forecast churn.
- **AI-BIOS Usage:** Connects PostgreSQL → asks natural language questions → forecasts next 90-day churn → exports PPTX for investor deck.

### Persona 3: Priya — Senior Data Analyst
- **Age:** 34 | **Company:** 500-person retail chain
- **Technical Level:** High (Python, SQL, Power BI)
- **Pain Points:** Spends 70% of time on repetitive EDA and report writing.
- **Goals:** Automate the boring parts of analysis. Focus on strategic insight.
- **AI-BIOS Usage:** Uploads sales data → lets agents run full EDA → reviews and edits insights → publishes to Power BI → shares automated PDF report.

### Persona 4: Marcus — IT Admin
- **Age:** 45 | **Company:** 200-person manufacturing firm
- **Technical Level:** Very High (infra, security)
- **Pain Points:** Need to control who sees what data. Audit trail for compliance.
- **Goals:** Configure RBAC. Manage user access. Review audit logs.
- **AI-BIOS Usage:** Manages users/roles → reviews agent action logs → configures Computer Operator Agent permissions.

## 2.2 User Stories

### Epic 1: Data Ingestion
| ID | Story | Priority |
|----|-------|---------|
| US-001 | As a user, I want to upload a CSV file so that I can analyze my data immediately | P0 |
| US-002 | As a user, I want to upload an Excel file with multiple sheets so that I can select which sheet to analyze | P0 |
| US-003 | As a user, I want to connect a PostgreSQL database so that I can run analysis on live production data | P0 |
| US-004 | As a user, I want to connect MySQL and SQLite databases | P1 |
| US-005 | As a user, I want to see a data preview after upload to verify correct parsing | P0 |
| US-006 | As a user, I want to see detected column types, null counts, and row counts automatically | P0 |

### Epic 2: Automated Analysis
| ID | Story | Priority |
|----|-------|---------|
| US-007 | As a user, I want the system to run automated EDA on my dataset and show me a profiling report | P0 |
| US-008 | As a user, I want to see detected anomalies highlighted in my data | P1 |
| US-009 | As a user, I want correlation heatmaps generated automatically | P1 |
| US-010 | As a user, I want missing value analysis with suggested imputation strategies | P1 |
| US-011 | As a user, I want segmentation analysis to group my customers automatically | P2 |
| US-012 | As a user, I want RFM analysis for e-commerce datasets | P2 |

### Epic 3: Visualization & Dashboards
| ID | Story | Priority |
|----|-------|---------|
| US-013 | As a user, I want AI-generated charts relevant to my data | P0 |
| US-014 | As a user, I want an interactive dashboard auto-built from my dataset | P0 |
| US-015 | As a user, I want to export charts as PNG/SVG | P1 |
| US-016 | As a user, I want to drill down on dashboard charts | P2 |
| US-017 | As a user, I want to customize chart colors and labels | P2 |

### Epic 4: Forecasting
| ID | Story | Priority |
|----|-------|---------|
| US-018 | As a user, I want to select a numeric column and get a 30/60/90-day forecast | P1 |
| US-019 | As a user, I want forecast confidence intervals displayed on charts | P1 |
| US-020 | As a user, I want to see which forecasting model was selected and why | P2 |
| US-021 | As a user, I want to download forecast results as CSV | P2 |

### Epic 5: Reports
| ID | Story | Priority |
|----|-------|---------|
| US-022 | As a user, I want to generate a professional PDF report from my analysis | P0 |
| US-023 | As a user, I want to generate a PowerPoint presentation from my analysis | P1 |
| US-024 | As a user, I want an executive summary auto-generated in plain English | P0 |
| US-025 | As a user, I want to regenerate sections of a report with updated data | P2 |

### Epic 6: Chat With Data
| ID | Story | Priority |
|----|-------|---------|
| US-026 | As a user, I want to ask natural language questions about my dataset | P0 |
| US-027 | As a user, I want follow-up questions to maintain context from previous answers | P1 |
| US-028 | As a user, I want the chat to cite which rows/columns informed each answer | P2 |
| US-029 | As a user, I want to ask the chat to generate a chart from my question | P2 |

### Epic 7: Administration
| ID | Story | Priority |
|----|-------|---------|
| US-030 | As an admin, I want to create and manage user accounts with roles | P0 |
| US-031 | As an admin, I want to view a full audit log of all agent actions | P1 |
| US-032 | As an admin, I want to approve or deny Computer Operator Agent actions | P0 |
| US-033 | As an admin, I want to set data retention policies per project | P2 |

## 2.3 User Journeys

### Journey 1: First-Time Upload & Analysis
```
Landing → Register → Onboarding → New Project → Upload CSV 
→ Data Preview → Auto-EDA Runs → Dashboard Generated 
→ View Insights → Download Report → Share Link
```

### Journey 2: Database Connection & Chat
```
Login → Projects → Connect DB → Enter Credentials → Test Connection 
→ Select Tables → Schema Preview → Open Chat 
→ Ask Question → AI Answers with Chart → Follow-up Q → Export Conversation
```

### Journey 3: Forecast & PPTX Export
```
Login → Open Dataset → Analysis Tab → Forecasting 
→ Select Column → Configure Horizon → Run Forecast 
→ View Chart with Confidence Intervals → Generate PPTX 
→ Download Presentation
```

## 2.4 Functional Requirements

| ID | Requirement | Category |
|----|------------|---------|
| FR-001 | System shall accept CSV files up to 500MB | Ingestion |
| FR-002 | System shall accept XLSX files with up to 20 sheets | Ingestion |
| FR-003 | System shall connect to PostgreSQL, MySQL, SQLite | DB Connectors |
| FR-004 | System shall auto-detect column types (numeric, categorical, date, text, boolean) | Profiling |
| FR-005 | System shall run automated EDA including: distribution, nulls, outliers, correlations | EDA |
| FR-006 | System shall generate at least 8 chart types per dataset (bar, line, scatter, heatmap, histogram, box, pie, area) | Visualization |
| FR-007 | System shall support Prophet, XGBoost, and linear regression for forecasting | Forecasting |
| FR-008 | System shall generate PDF reports using ReportLab | Reporting |
| FR-009 | System shall generate PPTX presentations using python-pptx | Reporting |
| FR-010 | System shall support natural language chat against uploaded datasets via RAG | Chat |
| FR-011 | System shall maintain chat context across a session (minimum 20 turns) | Chat |
| FR-012 | System shall support JWT authentication with refresh tokens | Auth |
| FR-013 | System shall enforce RBAC with Admin, Analyst, Viewer roles | Auth |
| FR-014 | System shall log all agent actions to the audit log | Audit |
| FR-015 | Computer Operator Agent actions shall require explicit user approval | COA |
| FR-016 | System shall support project-based dataset organization | Projects |
| FR-017 | System shall process large files asynchronously via Celery | Performance |
| FR-018 | System shall store vector embeddings of dataset content in ChromaDB | RAG |

## 2.5 Non-Functional Requirements

| Category | Requirement | Target |
|---------|------------|-------|
| Performance | API response time (p95) | < 500ms for non-AI endpoints |
| Performance | AI analysis job completion | < 3 min for 10MB CSV |
| Scalability | Concurrent users | 500 concurrent (Phase 4) |
| Availability | Uptime SLA | 99.5% (Phase 3+) |
| Security | Data at rest | AES-256 encrypted |
| Security | Data in transit | TLS 1.3 |
| Security | OWASP Top 10 | Fully mitigated |
| Usability | Time to first insight (TTFI) | < 5 minutes from upload |
| Compliance | Audit log retention | 90 days minimum |
| Storage | Max file size per upload | 500MB |
| Accessibility | WCAG | 2.1 AA |

## 2.6 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Time to First Insight | < 5 min | Analytics event tracking |
| EDA Completion Rate | > 95% | Task success rate in Celery |
| Report Generation Success | > 98% | API success response rate |
| Chat Answer Relevance | > 4.0/5.0 | User thumbs up/down |
| Agent Retry Rate | < 10% | Agent log analysis |
| User Retention (30-day) | > 60% | Cohort analysis |
| NPS | > 50 | Quarterly survey |

---

# 3. System Architecture

## 3.1 High-Level Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        WEB[Next.js 15 Web App]
        MOBILE[Mobile Browser]
    end

    subgraph "CDN & Edge"
        VERCEL[Vercel Edge Network]
    end

    subgraph "API Gateway"
        NGINX[NGINX Reverse Proxy]
        RATE[Rate Limiter]
        AUTH_MW[Auth Middleware]
    end

    subgraph "Application Layer"
        FASTAPI[FastAPI Application]
        CELERY[Celery Workers]
        BEAT[Celery Beat Scheduler]
    end

    subgraph "AI Layer"
        LANGGRAPH[LangGraph Orchestrator]
        GEMINI_PRO[Gemini 2.5 Pro]
        GEMINI_FLASH[Gemini 2.5 Flash]
        
        subgraph "Agents"
            A1[Data Cleaning Agent]
            A2[EDA Agent]
            A3[Viz Agent]
            A4[Forecast Agent]
            A5[Insight Agent]
            A6[Report Agent]
            A7[Consultant Agent]
            A8[SQL Agent]
            A9[Dataset Agent]
            A10[Chat Agent]
            A11[Computer Operator Agent]
        end
    end

    subgraph "Data Layer"
        POSTGRES[(Neon PostgreSQL)]
        CHROMA[(ChromaDB)]
        REDIS[(Redis Cache)]
        S3[File Storage / S3-Compatible]
    end

    WEB --> VERCEL
    MOBILE --> VERCEL
    VERCEL --> NGINX
    NGINX --> RATE
    RATE --> AUTH_MW
    AUTH_MW --> FASTAPI
    FASTAPI --> CELERY
    FASTAPI --> LANGGRAPH
    LANGGRAPH --> GEMINI_PRO
    LANGGRAPH --> GEMINI_FLASH
    LANGGRAPH --> A1
    LANGGRAPH --> A2
    LANGGRAPH --> A3
    LANGGRAPH --> A4
    LANGGRAPH --> A5
    LANGGRAPH --> A6
    LANGGRAPH --> A7
    LANGGRAPH --> A8
    LANGGRAPH --> A9
    LANGGRAPH --> A10
    LANGGRAPH --> A11
    FASTAPI --> POSTGRES
    FASTAPI --> CHROMA
    FASTAPI --> REDIS
    FASTAPI --> S3
    CELERY --> POSTGRES
    CELERY --> S3
```

## 3.2 Service Architecture

```mermaid
graph LR
    subgraph "Frontend Services"
        NEXT[Next.js App<br/>Port 3000]
    end

    subgraph "Backend Services"
        API[FastAPI<br/>Port 8000]
        WORKER[Celery Worker<br/>Processes: 4]
        BEAT[Celery Beat<br/>Scheduler]
    end

    subgraph "Message Broker"
        REDIS_MQ[Redis<br/>Port 6379<br/>Message Queue + Cache]
    end

    subgraph "Databases"
        PG[Neon PostgreSQL<br/>Port 5432]
        CHROMA_DB[ChromaDB<br/>Port 8001]
    end

    subgraph "File Storage"
        FILES[Local / S3<br/>uploads/]
    end

    NEXT -->|REST/WebSocket| API
    API -->|Enqueue Tasks| REDIS_MQ
    WORKER -->|Consume Tasks| REDIS_MQ
    API --> PG
    WORKER --> PG
    API --> CHROMA_DB
    WORKER --> CHROMA_DB
    WORKER --> FILES
    API --> FILES
    BEAT --> REDIS_MQ
```

## 3.3 Component Architecture

```mermaid
graph TB
    subgraph "Frontend Components"
        LAYOUT[Root Layout]
        LAYOUT --> DASH[Dashboard Page]
        LAYOUT --> UPLOAD[Upload Page]
        LAYOUT --> CHAT_UI[Chat Page]
        LAYOUT --> SETTINGS[Settings Page]
        LAYOUT --> ADMIN_UI[Admin Page]
        
        DASH --> KPICARD[KPI Cards]
        DASH --> CHARTGRID[Chart Grid]
        DASH --> INSIGHTPANEL[Insight Panel]
        
        CHAT_UI --> CHATWINDOW[Chat Window]
        CHAT_UI --> CONTEXTPANEL[Context Panel]
        CHAT_UI --> SOURCECITATION[Source Citations]
    end

    subgraph "Backend Components"
        ROUTER[FastAPI Router]
        ROUTER --> AUTH_R[Auth Router]
        ROUTER --> DATASET_R[Dataset Router]
        ROUTER --> ANALYSIS_R[Analysis Router]
        ROUTER --> CHAT_R[Chat Router]
        ROUTER --> REPORT_R[Report Router]
        ROUTER --> ADMIN_R[Admin Router]
        
        SERVICES[Service Layer]
        SERVICES --> AUTH_SVC[AuthService]
        SERVICES --> DS_SVC[DatasetService]
        SERVICES --> ANALYSIS_SVC[AnalysisService]
        SERVICES --> CHAT_SVC[ChatService]
        SERVICES --> REPORT_SVC[ReportService]
        SERVICES --> AGENT_SVC[AgentService]
    end
```

## 3.4 Data Architecture

```mermaid
graph TB
    subgraph "Ingestion"
        RAW_FILE[Raw File Upload]
        DB_CONN[DB Connection]
    end

    subgraph "Processing Pipeline"
        VALIDATOR[File Validator]
        PARSER[Data Parser<br/>pandas]
        PROFILER[Data Profiler]
        CLEANER[Data Cleaner]
        EMBEDDER[Text Embedder<br/>Gemini Embeddings]
    end

    subgraph "Storage"
        OBJECT[Object Storage<br/>Raw Files]
        RELATIONAL[PostgreSQL<br/>Metadata + Results]
        VECTOR[ChromaDB<br/>Embeddings]
        CACHE[Redis<br/>Analysis Cache]
    end

    RAW_FILE --> VALIDATOR
    DB_CONN --> PARSER
    VALIDATOR --> PARSER
    PARSER --> PROFILER
    PROFILER --> CLEANER
    CLEANER --> EMBEDDER
    PARSER --> OBJECT
    PROFILER --> RELATIONAL
    CLEANER --> RELATIONAL
    EMBEDDER --> VECTOR
    RELATIONAL --> CACHE
```

## 3.5 Event Architecture

```mermaid
sequenceDiagram
    participant U as User
    participant API as FastAPI
    participant Q as Redis Queue
    participant W as Celery Worker
    participant LG as LangGraph
    participant AI as Gemini
    participant DB as PostgreSQL
    participant WS as WebSocket

    U->>API: POST /api/v1/analyses/run
    API->>DB: Create analysis record (status=pending)
    API->>Q: Enqueue analysis task
    API-->>U: 202 Accepted + task_id
    
    W->>Q: Dequeue task
    W->>DB: Update status=running
    W->>WS: Emit progress event
    W->>LG: Initialize workflow
    LG->>AI: Call Gemini Flash (fast tasks)
    AI-->>LG: Response
    LG->>AI: Call Gemini Pro (deep analysis)
    AI-->>LG: Response
    LG-->>W: Workflow complete
    W->>DB: Save results
    W->>DB: Update status=completed
    W->>WS: Emit completion event
    WS-->>U: Real-time update
```

---

# 4. Technology Decisions

## 4.1 Technology Selection Matrix

| Component | Selected | Alternatives Considered | Decision Rationale |
|-----------|---------|------------------------|-------------------|
| Frontend Framework | Next.js 15 | React SPA, Remix, SvelteKit | App Router, SSR/SSG flexibility, Vercel native, TypeScript-first |
| UI Components | ShadCN UI | MUI, Ant Design, Chakra | Headless + Tailwind composability, no vendor lock-in, fully accessible |
| CSS | TailwindCSS | CSS Modules, Styled Components | Utility-first, no runtime overhead, DX speed |
| Animation | Framer Motion | GSAP, CSS Animations | Declarative, React-native, production-grade |
| Charts | Recharts | Chart.js, Victory, Nivo | React-native, composable, SSR-compatible |
| Backend | FastAPI | Django, Flask, Node.js/Express | Async-native, Pydantic validation, OpenAPI auto-docs, Python ecosystem |
| Primary AI | Gemini 2.5 Pro | GPT-4o, Claude 3.5 | Large context window (1M tokens), multimodal, cost-effective, Google ecosystem |
| Fast AI | Gemini 2.5 Flash | GPT-4o-mini | Ultra-low latency, ideal for streaming responses |
| Agent Framework | LangGraph | AutoGen, CrewAI, plain chains | Stateful graph-based orchestration, explicit state control, cycle support |
| Primary DB | PostgreSQL (Neon) | MySQL, CockroachDB | ACID, JSONB support, free-tier Neon, vector extensions, industry standard |
| Vector DB | ChromaDB | Pinecone, Weaviate, pgvector | Open source, Python-native, zero-cost, easy embedding management |
| Task Queue | Celery | RQ, Dramatiq, APScheduler | Battle-tested, Redis broker support, periodic tasks, monitoring tools |
| Message Broker | Redis | RabbitMQ, SQS | Multi-purpose (cache + queue), low latency, free self-hosting |
| Containerization | Docker | Podman | Industry standard, Railway/Vercel compatible |
| Frontend Deploy | Vercel | Netlify, Cloudflare Pages | Next.js native, edge functions, free tier |
| Backend Deploy | Railway | Render, Fly.io, Heroku | Docker support, Redis/PostgreSQL, low cost, simple env management |

## 4.2 AI Model Usage Strategy

| Task Type | Model | Reasoning |
|-----------|-------|-----------|
| Deep EDA analysis | Gemini 2.5 Pro | Complex reasoning on large datasets |
| Chart title/label generation | Gemini 2.5 Flash | Low-latency, simple task |
| Executive summary writing | Gemini 2.5 Pro | Quality output required |
| Chat Q&A (simple) | Gemini 2.5 Flash | Streaming, fast user experience |
| Chat Q&A (complex reasoning) | Gemini 2.5 Pro | Multi-step reasoning over data |
| SQL generation | Gemini 2.5 Pro | High accuracy needed, security-critical |
| Report writing | Gemini 2.5 Pro | Quality, long-form output |
| Forecast explanation | Gemini 2.5 Flash | Fast, routine explanation |
| Anomaly detection summary | Gemini 2.5 Flash | Fast, factual output |
| Computer Operator planning | Gemini 2.5 Pro | Complex multi-step action planning |

---

# 5. Enterprise Folder Structure

## 5.1 Root Layout

```
ai-bios/
├── frontend/                    # Next.js 15 application
├── backend/                     # FastAPI application
├── docker/                      # Docker configuration files
├── docs/                        # Documentation
├── scripts/                     # Dev and ops scripts
├── .github/                     # GitHub Actions CI/CD
├── docker-compose.yml           # Local development stack
├── docker-compose.prod.yml      # Production stack
├── .env.example                 # Environment variable template
├── Makefile                     # Common commands
└── AI_BIOS_MASTER.md            # This document (SSOT)
```

## 5.2 Frontend Structure

```
frontend/
├── app/                              # Next.js App Router
│   ├── (auth)/                       # Auth route group
│   │   ├── login/
│   │   │   └── page.tsx
│   │   ├── register/
│   │   │   └── page.tsx
│   │   └── layout.tsx
│   ├── (dashboard)/                  # Protected dashboard route group
│   │   ├── layout.tsx                # Dashboard shell layout
│   │   ├── page.tsx                  # Home / overview
│   │   ├── projects/
│   │   │   ├── page.tsx              # Projects list
│   │   │   └── [id]/
│   │   │       ├── page.tsx          # Project overview
│   │   │       ├── datasets/
│   │   │       │   ├── page.tsx
│   │   │       │   └── [datasetId]/
│   │   │       │       └── page.tsx
│   │   │       ├── analysis/
│   │   │       │   └── page.tsx
│   │   │       ├── dashboard/
│   │   │       │   └── page.tsx
│   │   │       ├── forecasting/
│   │   │       │   └── page.tsx
│   │   │       ├── reports/
│   │   │       │   └── page.tsx
│   │   │       └── chat/
│   │   │           └── page.tsx
│   │   ├── admin/
│   │   │   ├── page.tsx
│   │   │   ├── users/
│   │   │   │   └── page.tsx
│   │   │   ├── audit-logs/
│   │   │   │   └── page.tsx
│   │   │   └── coa-approvals/
│   │   │       └── page.tsx
│   │   └── settings/
│   │       └── page.tsx
│   ├── api/                          # Next.js API Routes (proxy layer)
│   │   └── [...path]/
│   │       └── route.ts
│   ├── globals.css
│   ├── layout.tsx                    # Root layout
│   └── not-found.tsx
│
├── components/                       # Reusable components
│   ├── ui/                           # ShadCN UI base components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   ├── input.tsx
│   │   ├── table.tsx
│   │   ├── toast.tsx
│   │   └── ... (all shadcn components)
│   ├── layout/                       # Layout components
│   │   ├── Sidebar.tsx
│   │   ├── TopBar.tsx
│   │   ├── BreadcrumbNav.tsx
│   │   └── PageHeader.tsx
│   ├── data/                         # Data display components
│   │   ├── DataTable.tsx
│   │   ├── DataPreview.tsx
│   │   ├── ColumnProfileCard.tsx
│   │   └── SchemaViewer.tsx
│   ├── charts/                       # Chart components
│   │   ├── BarChartCard.tsx
│   │   ├── LineChartCard.tsx
│   │   ├── ScatterChartCard.tsx
│   │   ├── HeatmapCard.tsx
│   │   ├── HistogramCard.tsx
│   │   ├── BoxPlotCard.tsx
│   │   ├── PieChartCard.tsx
│   │   ├── AreaChartCard.tsx
│   │   ├── ForecastChart.tsx
│   │   └── ChartFactory.tsx
│   ├── dashboard/                    # Dashboard components
│   │   ├── KPICard.tsx
│   │   ├── DashboardGrid.tsx
│   │   ├── InsightPanel.tsx
│   │   └── AnomalyBadge.tsx
│   ├── upload/                       # File upload components
│   │   ├── FileDropzone.tsx
│   │   ├── UploadProgress.tsx
│   │   └── DBConnectForm.tsx
│   ├── chat/                         # Chat components
│   │   ├── ChatWindow.tsx
│   │   ├── ChatMessage.tsx
│   │   ├── ChatInput.tsx
│   │   ├── SourceCitation.tsx
│   │   └── ContextPanel.tsx
│   ├── reports/                      # Report components
│   │   ├── ReportPreview.tsx
│   │   ├── ReportBuilder.tsx
│   │   └── ExportButtons.tsx
│   ├── agents/                       # Agent UI components
│   │   ├── AgentStatusPanel.tsx
│   │   ├── AgentLogViewer.tsx
│   │   └── AgentProgress.tsx
│   ├── coa/                          # Computer Operator Agent UI
│   │   ├── ApprovalDialog.tsx
│   │   ├── ActionCard.tsx
│   │   ├── ApprovalHistory.tsx
│   │   └── PermissionBadge.tsx
│   └── shared/                       # Truly shared atoms
│       ├── LoadingSpinner.tsx
│       ├── ErrorBoundary.tsx
│       ├── EmptyState.tsx
│       └── StatusBadge.tsx
│
├── hooks/                            # Custom React hooks
│   ├── useAuth.ts
│   ├── useDataset.ts
│   ├── useAnalysis.ts
│   ├── useChat.ts
│   ├── useWebSocket.ts
│   ├── useFileUpload.ts
│   └── useApproval.ts
│
├── lib/                              # Client-side utilities
│   ├── api-client.ts                 # Axios instance with interceptors
│   ├── auth.ts                       # Auth helpers
│   ├── formatters.ts                 # Data formatters
│   ├── validators.ts                 # Client-side validators
│   └── constants.ts                  # App constants
│
├── stores/                           # State management (Zustand)
│   ├── auth-store.ts
│   ├── project-store.ts
│   ├── dataset-store.ts
│   ├── analysis-store.ts
│   ├── chat-store.ts
│   └── approval-store.ts
│
├── types/                            # TypeScript type definitions
│   ├── api.types.ts
│   ├── auth.types.ts
│   ├── dataset.types.ts
│   ├── analysis.types.ts
│   ├── chart.types.ts
│   ├── chat.types.ts
│   ├── report.types.ts
│   └── coa.types.ts
│
├── public/                           # Static assets
│   ├── icons/
│   ├── images/
│   └── fonts/
│
├── styles/                           # Global styles
│   └── globals.css
│
├── tests/                            # Frontend tests
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── next.config.ts
├── tailwind.config.ts
├── tsconfig.json
├── components.json                   # ShadCN config
└── package.json
```

## 5.3 Backend Structure

```
backend/
├── app/
│   ├── main.py                       # FastAPI app entry point
│   ├── config.py                     # Settings via pydantic-settings
│   ├── dependencies.py               # FastAPI dependency injection
│   │
│   ├── api/                          # API layer
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── router.py             # Main v1 router
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   ├── projects.py
│   │   │   ├── datasets.py
│   │   │   ├── analyses.py
│   │   │   ├── forecasts.py
│   │   │   ├── reports.py
│   │   │   ├── chat.py
│   │   │   ├── dashboards.py
│   │   │   ├── admin.py
│   │   │   └── coa.py
│   │   └── websocket/
│   │       ├── __init__.py
│   │       ├── manager.py
│   │       └── handlers.py
│   │
│   ├── models/                       # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── dataset.py
│   │   ├── analysis.py
│   │   ├── forecast.py
│   │   ├── report.py
│   │   ├── chat_session.py
│   │   ├── chat_message.py
│   │   ├── agent_log.py
│   │   ├── coa_action.py
│   │   ├── audit_log.py
│   │   └── notification.py
│   │
│   ├── schemas/                      # Pydantic schemas (request/response)
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── dataset.py
│   │   ├── analysis.py
│   │   ├── forecast.py
│   │   ├── report.py
│   │   ├── chat.py
│   │   ├── dashboard.py
│   │   └── coa.py
│   │
│   ├── services/                     # Business logic layer
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── project_service.py
│   │   ├── dataset_service.py
│   │   ├── analysis_service.py
│   │   ├── forecast_service.py
│   │   ├── report_service.py
│   │   ├── chat_service.py
│   │   ├── embedding_service.py
│   │   └── file_service.py
│   │
│   ├── agents/                       # AI Agents
│   │   ├── __init__.py
│   │   ├── base_agent.py
│   │   ├── data_cleaning_agent.py
│   │   ├── eda_agent.py
│   │   ├── visualization_agent.py
│   │   ├── forecasting_agent.py
│   │   ├── insight_agent.py
│   │   ├── report_agent.py
│   │   ├── consultant_agent.py
│   │   ├── sql_agent.py
│   │   ├── dataset_agent.py
│   │   ├── chat_agent.py
│   │   └── computer_operator_agent.py
│   │
│   ├── workflows/                    # LangGraph workflows
│   │   ├── __init__.py
│   │   ├── analysis_workflow.py
│   │   ├── report_workflow.py
│   │   ├── chat_workflow.py
│   │   ├── forecast_workflow.py
│   │   └── coa_workflow.py
│   │
│   ├── tools/                        # LangGraph tools
│   │   ├── __init__.py
│   │   ├── data_tools.py
│   │   ├── viz_tools.py
│   │   ├── sql_tools.py
│   │   ├── file_tools.py
│   │   └── system_tools.py
│   │
│   ├── analysis/                     # Data analysis engines
│   │   ├── __init__.py
│   │   ├── profiler.py
│   │   ├── cleaner.py
│   │   ├── eda_engine.py
│   │   ├── anomaly_detector.py
│   │   ├── correlation_engine.py
│   │   ├── segmentation_engine.py
│   │   ├── rfm_engine.py
│   │   └── cohort_engine.py
│   │
│   ├── forecasting/                  # Forecasting engines
│   │   ├── __init__.py
│   │   ├── prophet_engine.py
│   │   ├── xgboost_engine.py
│   │   ├── regression_engine.py
│   │   └── model_selector.py
│   │
│   ├── reporting/                    # Report generation
│   │   ├── __init__.py
│   │   ├── pdf_generator.py
│   │   ├── pptx_generator.py
│   │   └── summary_writer.py
│   │
│   ├── db/                           # Database layer
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── session.py
│   │   ├── migrations/               # Alembic migrations
│   │   └── repositories/             # Repository pattern
│   │       ├── user_repo.py
│   │       ├── project_repo.py
│   │       ├── dataset_repo.py
│   │       └── analysis_repo.py
│   │
│   ├── cache/                        # Redis caching
│   │   ├── __init__.py
│   │   ├── client.py
│   │   └── decorators.py
│   │
│   ├── tasks/                        # Celery tasks
│   │   ├── __init__.py
│   │   ├── celery_app.py
│   │   ├── analysis_tasks.py
│   │   ├── report_tasks.py
│   │   ├── forecast_tasks.py
│   │   └── embedding_tasks.py
│   │
│   ├── middleware/                   # FastAPI middleware
│   │   ├── __init__.py
│   │   ├── auth_middleware.py
│   │   ├── logging_middleware.py
│   │   ├── rate_limit_middleware.py
│   │   └── error_middleware.py
│   │
│   ├── security/                     # Security utilities
│   │   ├── __init__.py
│   │   ├── jwt_handler.py
│   │   ├── password_handler.py
│   │   ├── rbac.py
│   │   └── audit.py
│   │
│   └── utils/                        # Utility functions
│       ├── __init__.py
│       ├── file_utils.py
│       ├── data_utils.py
│       └── response_utils.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── agents/
│   └── conftest.py
│
├── alembic.ini
├── alembic/
│   ├── env.py
│   └── versions/
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── Dockerfile
```

---

# 6. Database Architecture

## 6.1 Entity Relationship Diagram

```mermaid
erDiagram
    USERS {
        uuid id PK
        string email UK
        string hashed_password
        string full_name
        string role
        boolean is_active
        boolean is_verified
        timestamp created_at
        timestamp updated_at
        timestamp last_login
        jsonb preferences
        string subscription_tier
    }

    PROJECTS {
        uuid id PK
        uuid owner_id FK
        string name
        string description
        string status
        jsonb settings
        timestamp created_at
        timestamp updated_at
    }

    PROJECT_MEMBERS {
        uuid id PK
        uuid project_id FK
        uuid user_id FK
        string role
        timestamp joined_at
    }

    DATASETS {
        uuid id PK
        uuid project_id FK
        uuid uploaded_by FK
        string name
        string source_type
        string file_path
        string file_name
        bigint file_size
        string mime_type
        integer row_count
        integer column_count
        jsonb schema_info
        jsonb profile_summary
        string status
        timestamp created_at
        timestamp updated_at
    }

    DB_CONNECTIONS {
        uuid id PK
        uuid project_id FK
        string name
        string db_type
        string host
        integer port
        string database_name
        string username
        string encrypted_password
        boolean is_active
        timestamp last_tested
        timestamp created_at
    }

    ANALYSES {
        uuid id PK
        uuid dataset_id FK
        uuid project_id FK
        uuid requested_by FK
        string analysis_type
        string status
        jsonb config
        jsonb result
        integer progress_pct
        string error_message
        float duration_seconds
        timestamp started_at
        timestamp completed_at
        timestamp created_at
    }

    VISUALIZATIONS {
        uuid id PK
        uuid analysis_id FK
        uuid dataset_id FK
        string chart_type
        string title
        jsonb chart_config
        jsonb data_spec
        string image_path
        timestamp created_at
    }

    DASHBOARDS {
        uuid id PK
        uuid project_id FK
        uuid created_by FK
        string name
        jsonb layout
        jsonb widgets
        boolean is_public
        string share_token
        timestamp created_at
        timestamp updated_at
    }

    FORECASTS {
        uuid id PK
        uuid dataset_id FK
        uuid project_id FK
        uuid requested_by FK
        string target_column
        string model_used
        integer horizon_days
        jsonb model_params
        jsonb forecast_result
        jsonb evaluation_metrics
        string status
        timestamp created_at
        timestamp completed_at
    }

    REPORTS {
        uuid id PK
        uuid project_id FK
        uuid analysis_id FK
        uuid created_by FK
        string title
        string report_type
        text executive_summary
        jsonb sections
        string pdf_path
        string pptx_path
        string status
        timestamp created_at
        timestamp updated_at
    }

    CHAT_SESSIONS {
        uuid id PK
        uuid project_id FK
        uuid dataset_id FK
        uuid user_id FK
        string title
        integer message_count
        jsonb context_summary
        timestamp created_at
        timestamp updated_at
    }

    CHAT_MESSAGES {
        uuid id PK
        uuid session_id FK
        string role
        text content
        jsonb sources
        jsonb chart_data
        integer tokens_used
        float latency_ms
        integer thumbs_rating
        timestamp created_at
    }

    AGENT_LOGS {
        uuid id PK
        uuid analysis_id FK
        string agent_name
        string action
        jsonb input_data
        jsonb output_data
        string status
        string error_message
        integer retry_count
        float duration_ms
        timestamp created_at
    }

    COA_ACTIONS {
        uuid id PK
        uuid requested_by FK
        string agent_name
        string action_type
        string target_application
        string reason
        string expected_outcome
        jsonb action_params
        string approval_status
        string approval_scope
        uuid approved_by FK
        timestamp approved_at
        timestamp executed_at
        boolean was_rolled_back
        timestamp created_at
    }

    AUDIT_LOGS {
        uuid id PK
        uuid user_id FK
        string action
        string resource_type
        uuid resource_id
        string ip_address
        string user_agent
        jsonb metadata
        string severity
        timestamp created_at
    }

    NOTIFICATIONS {
        uuid id PK
        uuid user_id FK
        string type
        string title
        text body
        boolean is_read
        jsonb metadata
        timestamp created_at
        timestamp read_at
    }

    PERMISSIONS {
        uuid id PK
        uuid user_id FK
        uuid project_id FK
        string resource_type
        string resource_id
        string action
        boolean is_granted
        timestamp created_at
    }

    USERS ||--o{ PROJECTS : "owns"
    USERS ||--o{ PROJECT_MEMBERS : "joins"
    PROJECTS ||--o{ PROJECT_MEMBERS : "has"
    PROJECTS ||--o{ DATASETS : "contains"
    PROJECTS ||--o{ DB_CONNECTIONS : "connects"
    PROJECTS ||--o{ ANALYSES : "has"
    PROJECTS ||--o{ DASHBOARDS : "has"
    PROJECTS ||--o{ FORECASTS : "has"
    PROJECTS ||--o{ REPORTS : "has"
    PROJECTS ||--o{ CHAT_SESSIONS : "has"
    DATASETS ||--o{ ANALYSES : "analyzed_by"
    DATASETS ||--o{ VISUALIZATIONS : "visualized_by"
    DATASETS ||--o{ FORECASTS : "forecasted_by"
    DATASETS ||--o{ CHAT_SESSIONS : "chatted_with"
    ANALYSES ||--o{ VISUALIZATIONS : "produces"
    ANALYSES ||--o{ AGENT_LOGS : "logged_by"
    ANALYSES ||--o{ REPORTS : "reported_in"
    CHAT_SESSIONS ||--o{ CHAT_MESSAGES : "has"
    USERS ||--o{ COA_ACTIONS : "requests"
    USERS ||--o{ AUDIT_LOGS : "generates"
    USERS ||--o{ NOTIFICATIONS : "receives"
    USERS ||--o{ PERMISSIONS : "holds"
```

## 6.2 Indexing Strategy

| Table | Index | Type | Purpose |
|-------|-------|------|---------|
| users | email | UNIQUE B-TREE | Login lookup |
| users | created_at | B-TREE | Admin user listing |
| projects | owner_id | B-TREE | User projects list |
| datasets | project_id, status | COMPOSITE | Active dataset fetch |
| datasets | created_at | B-TREE DESC | Recent datasets |
| analyses | dataset_id, status | COMPOSITE | Dataset analysis history |
| analyses | project_id, created_at | COMPOSITE | Project timeline |
| chat_messages | session_id, created_at | COMPOSITE | Conversation scroll |
| agent_logs | analysis_id | B-TREE | Analysis debug |
| agent_logs | created_at | B-TREE DESC | Recent activity |
| audit_logs | user_id, created_at | COMPOSITE | User audit trail |
| audit_logs | resource_type, resource_id | COMPOSITE | Resource history |
| coa_actions | requested_by, approval_status | COMPOSITE | Pending approvals |
| notifications | user_id, is_read | COMPOSITE | Unread count |

## 6.3 Scaling Considerations

- **Read Replicas:** All SELECT-heavy operations (dashboards, reports, chat) routed to read replicas in production
- **Connection Pooling:** PgBouncer in transaction mode, pool size 20 per service
- **Partitioning:** `audit_logs` and `agent_logs` partitioned by month using `created_at`
- **Archival:** Records older than 90 days moved to cold storage table; original tables retain 90-day window
- **JSONB Indexing:** GIN indexes on `schema_info`, `result`, `chart_config` columns used in queries

---

# 7. API Architecture

## 7.1 Versioning Strategy

All APIs are versioned under `/api/v1/`. When breaking changes are required, a new `/api/v2/` prefix is introduced and v1 is deprecated with a 6-month sunset period. Version header `X-API-Version` is supported as alternative versioning.

## 7.2 Authentication Endpoints

| Method | Path | Description | Auth Required |
|--------|------|-------------|--------------|
| POST | `/api/v1/auth/register` | Register new user | No |
| POST | `/api/v1/auth/login` | Login, get JWT pair | No |
| POST | `/api/v1/auth/refresh` | Refresh access token | Refresh Token |
| POST | `/api/v1/auth/logout` | Invalidate tokens | Yes |
| POST | `/api/v1/auth/forgot-password` | Initiate password reset | No |
| POST | `/api/v1/auth/reset-password` | Complete password reset | Reset Token |
| GET | `/api/v1/auth/me` | Get current user | Yes |

### Register Request Schema
```
POST /api/v1/auth/register
{
  "email": string (required, valid email, max 255),
  "password": string (required, min 8, max 128, complexity rules),
  "full_name": string (required, min 2, max 100)
}
```

### Register Response Schema
```
201 Created
{
  "id": uuid,
  "email": string,
  "full_name": string,
  "role": "analyst",
  "subscription_tier": "free",
  "created_at": ISO8601
}
```

### Login Response Schema
```
200 OK
{
  "access_token": string (JWT, 15min expiry),
  "refresh_token": string (JWT, 7day expiry),
  "token_type": "bearer",
  "user": {
    "id": uuid,
    "email": string,
    "full_name": string,
    "role": string,
    "subscription_tier": string
  }
}
```

## 7.3 Dataset Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/projects/{id}/datasets` | List datasets in project |
| POST | `/api/v1/projects/{id}/datasets/upload` | Upload CSV/XLSX file |
| POST | `/api/v1/projects/{id}/datasets/connect-db` | Connect database |
| GET | `/api/v1/datasets/{id}` | Get dataset details |
| GET | `/api/v1/datasets/{id}/preview` | Get first 100 rows |
| GET | `/api/v1/datasets/{id}/profile` | Get data profile |
| DELETE | `/api/v1/datasets/{id}` | Delete dataset |
| PATCH | `/api/v1/datasets/{id}` | Update dataset metadata |

### Upload File Request
```
POST /api/v1/projects/{id}/datasets/upload
Content-Type: multipart/form-data
{
  file: binary (CSV or XLSX, max 500MB),
  name: string (optional, defaults to filename),
  description: string (optional)
}
```

### Dataset Profile Response Schema
```
200 OK
{
  "dataset_id": uuid,
  "row_count": integer,
  "column_count": integer,
  "file_size_bytes": integer,
  "columns": [
    {
      "name": string,
      "detected_type": "numeric|categorical|date|text|boolean",
      "null_count": integer,
      "null_pct": float,
      "unique_count": integer,
      "sample_values": array,
      "statistics": {
        "mean": float,      // numeric only
        "std": float,
        "min": float,
        "max": float,
        "p25": float,
        "p50": float,
        "p75": float,
        "top_values": [{value, count}]  // categorical
      }
    }
  ],
  "quality_score": float (0-100),
  "warnings": [string]
}
```

## 7.4 Analysis Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v1/analyses/run` | Trigger analysis workflow |
| GET | `/api/v1/analyses/{id}` | Get analysis details + results |
| GET | `/api/v1/analyses/{id}/status` | Poll analysis status |
| GET | `/api/v1/datasets/{id}/analyses` | List analyses for dataset |
| DELETE | `/api/v1/analyses/{id}` | Delete analysis |

### Run Analysis Request
```
POST /api/v1/analyses/run
{
  "dataset_id": uuid (required),
  "analysis_types": array of enum [
    "eda", "cleaning", "correlations", "anomalies",
    "segmentation", "rfm", "cohort", "retention", "churn",
    "market_basket"
  ],
  "config": {
    "eda": { "depth": "standard|deep" },
    "cleaning": { "strategy": "auto|conservative|aggressive" },
    "segmentation": { "n_clusters": integer (2-10) },
    "rfm": { "date_column": string, "value_column": string, "id_column": string }
  }
}
```

### Analysis Status Response
```
200 OK
{
  "analysis_id": uuid,
  "status": "pending|running|completed|failed",
  "progress_pct": integer (0-100),
  "current_agent": string,
  "started_at": ISO8601,
  "estimated_completion": ISO8601,
  "error": string|null
}
```

## 7.5 Forecast Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v1/forecasts/run` | Start a forecast job |
| GET | `/api/v1/forecasts/{id}` | Get forecast results |
| GET | `/api/v1/datasets/{id}/forecasts` | List dataset forecasts |

### Run Forecast Request
```
POST /api/v1/forecasts/run
{
  "dataset_id": uuid,
  "target_column": string,
  "date_column": string,
  "horizon_days": integer (7|14|30|60|90|180|365),
  "model_preference": "auto|prophet|xgboost|linear" (default: auto),
  "frequency": "D|W|M" (default: auto-detected),
  "include_components": boolean (default: true)
}
```

## 7.6 Chat Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v1/chat/sessions` | Create new chat session |
| GET | `/api/v1/chat/sessions/{id}` | Get session + messages |
| POST | `/api/v1/chat/sessions/{id}/messages` | Send a message |
| GET | `/api/v1/chat/sessions` | List user's chat sessions |
| DELETE | `/api/v1/chat/sessions/{id}` | Delete session |
| PATCH | `/api/v1/chat/messages/{id}/rate` | Rate a message (thumbs) |

### Send Message Request
```
POST /api/v1/chat/sessions/{id}/messages
{
  "content": string (required, min 1, max 4000),
  "include_chart": boolean (default: false)
}
```

### Message Response Schema
```
200 OK (streaming or complete)
{
  "message_id": uuid,
  "role": "assistant",
  "content": string,
  "sources": [
    {
      "type": "row|column|aggregate",
      "reference": string,
      "confidence": float
    }
  ],
  "chart_data": ChartConfig|null,
  "tokens_used": integer,
  "latency_ms": float
}
```

## 7.7 Computer Operator Agent Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/coa/actions/pending` | List pending approvals |
| POST | `/api/v1/coa/actions/{id}/approve` | Approve an action |
| POST | `/api/v1/coa/actions/{id}/deny` | Deny an action |
| GET | `/api/v1/coa/actions/history` | Approval history |
| POST | `/api/v1/coa/actions/{id}/rollback` | Rollback executed action |

## 7.8 Error Handling Standard

All errors follow RFC 7807 Problem Details format:
```json
{
  "type": "https://aibios.app/errors/validation-error",
  "title": "Validation Error",
  "status": 422,
  "detail": "The request body contains invalid fields.",
  "instance": "/api/v1/analyses/run",
  "errors": [
    {
      "field": "dataset_id",
      "message": "Dataset not found or not accessible",
      "code": "DATASET_NOT_FOUND"
    }
  ]
}
```

### Error Code Reference

| HTTP Status | Code | Meaning |
|------------|------|---------|
| 400 | BAD_REQUEST | Malformed request |
| 401 | UNAUTHORIZED | Missing or invalid token |
| 403 | FORBIDDEN | Insufficient permissions |
| 404 | NOT_FOUND | Resource does not exist |
| 409 | CONFLICT | Duplicate resource |
| 413 | FILE_TOO_LARGE | Upload exceeds limit |
| 422 | VALIDATION_ERROR | Pydantic validation failed |
| 429 | RATE_LIMITED | Too many requests |
| 500 | INTERNAL_ERROR | Unexpected server error |
| 503 | SERVICE_UNAVAILABLE | AI service down |

---

# 8. Authentication & Authorization

## 8.1 JWT Architecture

```mermaid
sequenceDiagram
    participant C as Client
    participant API as FastAPI
    participant DB as PostgreSQL
    participant CACHE as Redis

    C->>API: POST /auth/login (email, password)
    API->>DB: Verify credentials
    DB-->>API: User record
    API->>API: Generate access_token (15min)
    API->>API: Generate refresh_token (7 days)
    API->>CACHE: Store refresh_token hash (with user_id, TTL 7d)
    API-->>C: {access_token, refresh_token}

    C->>API: GET /api/v1/datasets (Bearer: access_token)
    API->>API: Verify JWT signature
    API->>API: Check expiry
    API->>API: Extract user_id, role from claims
    API-->>C: Protected response

    C->>API: POST /auth/refresh (refresh_token)
    API->>CACHE: Validate refresh_token hash
    API->>API: Issue new access_token
    API-->>C: {access_token}

    C->>API: POST /auth/logout (refresh_token)
    API->>CACHE: Delete refresh_token from allowlist
    API-->>C: 200 OK
```

### JWT Claims Structure
```json
{
  "sub": "user-uuid",
  "email": "user@example.com",
  "role": "analyst",
  "tier": "team",
  "iat": 1717000000,
  "exp": 1717000900,
  "jti": "unique-token-id"
}
```

## 8.2 RBAC Design

### Role Definitions

| Role | Description | Scope |
|------|-------------|-------|
| `super_admin` | Full system access, user management, all projects | System-wide |
| `admin` | Organization-level admin, user management, audit logs | Organization |
| `analyst` | Create/run analyses, manage own datasets, generate reports | Project |
| `viewer` | Read-only access to shared dashboards and reports | Project |

### Permissions Matrix

| Permission | super_admin | admin | analyst | viewer |
|-----------|:-----------:|:-----:|:-------:|:------:|
| Create user | ✅ | ✅ | ❌ | ❌ |
| Delete user | ✅ | ✅ | ❌ | ❌ |
| View audit logs | ✅ | ✅ | ❌ | ❌ |
| Create project | ✅ | ✅ | ✅ | ❌ |
| Delete project | ✅ | ✅ | Owner only | ❌ |
| Upload dataset | ✅ | ✅ | ✅ | ❌ |
| Delete dataset | ✅ | ✅ | Owner only | ❌ |
| Run analysis | ✅ | ✅ | ✅ | ❌ |
| View analysis | ✅ | ✅ | ✅ | ✅ (shared) |
| Generate report | ✅ | ✅ | ✅ | ❌ |
| View report | ✅ | ✅ | ✅ | ✅ (shared) |
| Chat with data | ✅ | ✅ | ✅ | ❌ |
| Connect database | ✅ | ✅ | ✅ | ❌ |
| Approve COA | ✅ | ✅ | ❌ | ❌ |
| Manage COA permissions | ✅ | ✅ | ❌ | ❌ |
| Configure Power BI | ✅ | ✅ | ✅ | ❌ |
| Manage members | ✅ | ✅ | Owner only | ❌ |

## 8.3 Row-Level Security (RLS)

Users can only access resources belonging to projects they are members of. Enforced via:

1. **FastAPI Dependency:** `get_current_user_project_access(project_id)` verifies membership
2. **Repository Layer:** All queries filter by `project_id IN (user's projects)`
3. **PostgreSQL RLS:** Optional second layer using `SET LOCAL app.current_user_id`

## 8.4 Rate Limiting

| Endpoint Group | Limit | Window |
|---------------|-------|--------|
| Auth endpoints | 10 requests | per minute per IP |
| File upload | 5 uploads | per minute per user |
| Analysis trigger | 10 runs | per hour per user |
| Chat messages | 60 messages | per minute per user |
| Report generation | 5 reports | per hour per user |
| General API | 200 requests | per minute per user |

---

# 9. Multi-Agent Architecture

## 9.1 Agent Base Class Specification

All agents inherit from `BaseAgent` and implement the following interface:

```
BaseAgent:
  - name: str
  - description: str
  - model: "gemini-2.5-pro" | "gemini-2.5-flash"
  - tools: List[Tool]
  - max_retries: int (default: 3)
  - retry_delay: float (seconds, default: 2.0)
  - timeout: float (seconds)

  Methods:
  - run(state: AgentState) -> AgentState
  - handle_error(error: Exception, state: AgentState) -> AgentState
  - log_action(action, input, output, status)
```

## 9.2 Agent Specifications

### Agent 1: Data Cleaning Agent

| Attribute | Value |
|-----------|-------|
| Name | `data_cleaning_agent` |
| Model | Gemini 2.5 Flash |
| Timeout | 120 seconds |
| Max Retries | 3 |

**Responsibilities:**
- Detect and handle missing values (impute, drop, flag)
- Detect and handle duplicate rows
- Fix data type mismatches (string "2024-01-01" → datetime)
- Standardize string casing and whitespace
- Handle outlier detection and flagging
- Generate a cleaning report summarizing all transformations

**Inputs:**
- `dataset_id`: UUID
- `dataframe`: pandas DataFrame (from S3)
- `cleaning_config`: `{ strategy: "auto|conservative|aggressive", drop_threshold: 0.5 }`

**Outputs:**
- `cleaned_dataframe`: pandas DataFrame
- `cleaning_report`: JSON with transformation log
- `quality_delta`: before/after quality score comparison
- `rows_affected`: count of rows modified/dropped

**Tools Available:**
- `pandas_imputer` — Handles mean/median/mode/forward-fill imputation
- `duplicate_remover` — Removes exact and fuzzy duplicates
- `type_coercer` — Coerces string dates, string numerics
- `outlier_flagging_tool` — IQR-based outlier detection

**Failure Handling:**
- If cleaning fails on a column, that column is flagged as `skipped` and the agent continues
- If >50% of rows would be dropped, agent enters `conservative` mode and prompts user
- Retries on pandas MemoryError with chunked processing

**Memory Usage:** Stateless per invocation. Cleaning config passed via state.

---

### Agent 2: EDA Agent

| Attribute | Value |
|-----------|-------|
| Name | `eda_agent` |
| Model | Gemini 2.5 Pro |
| Timeout | 180 seconds |
| Max Retries | 3 |

**Responsibilities:**
- Run full statistical analysis per column (distributions, skewness, kurtosis)
- Generate correlation matrix with Pearson, Spearman
- Identify highly correlated feature pairs
- Detect multicollinearity
- Identify constant or near-constant columns
- Produce AI-generated narrative explaining key statistical findings
- Recommend follow-up analyses (e.g., "This data is suitable for time-series forecasting")

**Inputs:**
- `cleaned_dataframe`: pandas DataFrame
- `schema_info`: column types and metadata
- `analysis_depth`: `"standard" | "deep"`

**Outputs:**
- `eda_report`: structured JSON with per-column and cross-column stats
- `correlation_matrix`: nested JSON
- `ai_narrative`: markdown text (Gemini-generated)
- `recommended_next_steps`: list of suggested analyses
- `chart_specs`: list of chart configurations for Visualization Agent

**Tools Available:**
- `scipy_stats_tool` — Distribution fitting and statistical tests
- `correlation_tool` — Pearson and Spearman correlation
- `pandas_profiler` — Extended profiling via ydata-profiling
- `gemini_narrator` — Converts stats JSON to narrative text

**Failure Handling:**
- If a column causes a numerical error (e.g., infinite values), skip and log warning
- If Gemini narration fails, output raw stats without narrative (graceful degradation)

---

### Agent 3: Visualization Agent

| Attribute | Value |
|-----------|-------|
| Name | `visualization_agent` |
| Model | Gemini 2.5 Flash |
| Timeout | 90 seconds |
| Max Retries | 2 |

**Responsibilities:**
- Receive chart specs from EDA Agent and generate chart configurations
- Select appropriate chart types based on data characteristics
- Generate chart titles, axis labels, and insight captions
- Create Recharts-compatible JSON configs
- Optionally render to PNG for PDF reports

**Chart Type Selection Rules:**
| Data Pattern | Chart Type |
|-------------|------------|
| Numeric distribution | Histogram + Box Plot |
| Categorical vs Numeric | Bar Chart |
| Time series | Line / Area Chart |
| Two numerics | Scatter Plot |
| Correlation matrix | Heatmap |
| Part-of-whole | Pie / Donut |
| Numeric grouped by category | Grouped Bar |
| Trends over time | Multi-line Chart |

**Inputs:**
- `chart_specs`: list from EDA Agent
- `cleaned_dataframe`: sampled DataFrame (max 5000 rows for viz)
- `project_theme`: color palette config

**Outputs:**
- `chart_configs`: list of Recharts JSON configs
- `chart_images`: list of PNG file paths (for PDF embedding)
- `chart_captions`: AI-generated insight per chart

---

### Agent 4: Forecasting Agent

| Attribute | Value |
|-----------|-------|
| Name | `forecasting_agent` |
| Model | Gemini 2.5 Pro |
| Timeout | 300 seconds |
| Max Retries | 2 |

**Responsibilities:**
- Detect time-series characteristics (stationarity, seasonality, trend)
- Select best forecasting model (Prophet, XGBoost, regression)
- Train selected model on historical data
- Generate forecast for requested horizon
- Calculate confidence intervals
- Evaluate model performance (MAPE, RMSE, MAE)
- Generate plain-English forecast explanation

**Model Selection Logic:**
```
IF data has seasonality AND >2 years of daily data → Prophet
ELSE IF multiple features exist for boosting → XGBoost
ELSE IF linear trend is dominant → Linear Regression
DEFAULT → Prophet
```

**Inputs:**
- `dataset_id`
- `target_column`: column to forecast
- `date_column`: timestamp column
- `horizon_days`: integer
- `model_preference`: override

**Outputs:**
- `forecast_df`: DataFrame with date, yhat, yhat_lower, yhat_upper
- `model_used`: string
- `evaluation_metrics`: { MAPE, RMSE, MAE, R2 }
- `forecast_chart_config`: Recharts config
- `narrative`: plain-English explanation

---

### Agent 5: Insight Agent

| Attribute | Value |
|-----------|-------|
| Name | `insight_agent` |
| Model | Gemini 2.5 Pro |
| Timeout | 120 seconds |
| Max Retries | 3 |

**Responsibilities:**
- Synthesize findings from EDA, cleaning, visualization, and forecasting agents
- Generate 5–10 prioritized business insights
- Classify insights by type: opportunity, risk, anomaly, trend
- Assign confidence scores to each insight
- Generate actionable recommendations per insight

**Inputs:**
- `eda_report`
- `cleaning_report`
- `chart_configs`
- `forecast_result` (optional)
- `dataset_context`: domain/industry hint from user

**Outputs:**
- `insights`: list of structured insight objects
  ```json
  {
    "id": "string",
    "title": "string",
    "description": "string",
    "type": "opportunity|risk|anomaly|trend",
    "confidence": float (0-1),
    "supporting_data": {...},
    "recommended_action": "string",
    "priority": "high|medium|low"
  }
  ```

---

### Agent 6: Report Agent

| Attribute | Value |
|-----------|-------|
| Name | `report_agent` |
| Model | Gemini 2.5 Pro |
| Timeout | 240 seconds |
| Max Retries | 2 |

**Responsibilities:**
- Compile all analysis results into a structured report
- Write executive summary (300–500 words)
- Write detailed findings sections
- Generate PDF via ReportLab
- Generate PPTX via python-pptx
- Embed charts from Visualization Agent

**Report Structure:**
1. Cover Page (title, date, dataset name, prepared by)
2. Executive Summary
3. Dataset Overview (profile stats, quality score)
4. Key Findings (top insights)
5. Detailed Analysis (EDA results, charts)
6. Forecasting Results (if applicable)
7. Anomaly Report (if applicable)
8. Recommendations
9. Appendix (raw statistics tables)

---

### Agent 7: Executive Consultant Agent

| Attribute | Value |
|-----------|-------|
| Name | `consultant_agent` |
| Model | Gemini 2.5 Pro |
| Timeout | 90 seconds |
| Max Retries | 3 |

**Responsibilities:**
- Act as a senior business consultant interpreting the data
- Provide strategic recommendations beyond statistical findings
- Frame insights in business value terms (revenue impact, cost savings, risk)
- Simulate "what-if" scenarios based on user questions
- Provide competitive context when industry is known

**Inputs:** Insight Agent output + user's business context
**Outputs:** Strategic memo (markdown), business impact estimates, prioritized action plan

---

### Agent 8: SQL Agent

| Attribute | Value |
|-----------|-------|
| Name | `sql_agent` |
| Model | Gemini 2.5 Pro |
| Timeout | 60 seconds |
| Max Retries | 3 |

**Responsibilities:**
- Convert natural language questions to SQL queries
- Validate generated SQL for safety (no DROP, DELETE, UPDATE without explicit flag)
- Execute queries against connected databases
- Return results as DataFrames
- Explain the query in plain English

**Security Rules (NON-NEGOTIABLE):**
- NEVER execute DELETE, DROP, TRUNCATE, ALTER, UPDATE, INSERT
- All queries wrapped in read-only transaction
- Query length limited to 5000 characters
- Timeout per query: 30 seconds
- Schema information only passed to model — never raw credentials

**Inputs:** natural language query + database schema (table names, columns, types)
**Outputs:** SQL string, DataFrame result, plain-English explanation, row count

---

### Agent 9: Dataset Agent

| Attribute | Value |
|-----------|-------|
| Name | `dataset_agent` |
| Model | Gemini 2.5 Flash |
| Timeout | 60 seconds |
| Max Retries | 2 |

**Responsibilities:**
- Handle dataset metadata management
- Suggest dataset joins when multiple datasets exist
- Detect compatible columns across datasets for merging
- Provide dataset recommendations ("this dataset lacks a date column for forecasting")

---

### Agent 10: Chat Agent

| Attribute | Value |
|-----------|-------|
| Name | `chat_agent` |
| Model | Gemini 2.5 Flash (simple), Gemini 2.5 Pro (complex) |
| Timeout | 30 seconds |
| Max Retries | 2 |

**Responsibilities:**
- Answer natural language questions about the active dataset
- Retrieve relevant data chunks from ChromaDB using RAG
- Maintain conversation context across session
- Decide when to delegate to SQL Agent (structured queries)
- Decide when to invoke Visualization Agent (chart requests)
- Cite source rows/columns in responses

**Context Memory Strategy:**
- Last 20 messages kept in LangGraph state
- Beyond 20: summarized into `context_summary` via Gemini Flash
- Summary + last 5 messages used for context in long sessions

---

### Agent 11: Computer Operator Agent (COA)

See dedicated Section 19 for full COA specification.

---

# 10. LangGraph Workflow

## 10.1 Analysis Workflow Graph

```mermaid
graph TD
    START([Start]) --> VALIDATE[Validate Dataset]
    VALIDATE -->|Valid| CLEAN[Data Cleaning Agent]
    VALIDATE -->|Invalid| ERROR[Error Handler]
    
    CLEAN --> CLEAN_OK{Clean Success?}
    CLEAN_OK -->|Yes| EDA[EDA Agent]
    CLEAN_OK -->|No - Partial| EDA
    CLEAN_OK -->|No - Fatal| ERROR
    
    EDA --> EDA_OK{EDA Success?}
    EDA_OK -->|Yes| VIZ[Visualization Agent]
    EDA_OK -->|No| RETRY_EDA{Retries < 3?}
    RETRY_EDA -->|Yes| EDA
    RETRY_EDA -->|No| ERROR
    
    VIZ --> INSIGHT[Insight Agent]
    INSIGHT --> CONSULTANT[Consultant Agent]
    CONSULTANT --> REPORT_NEEDED{Report Requested?}
    REPORT_NEEDED -->|Yes| REPORT[Report Agent]
    REPORT_NEEDED -->|No| COMPLETE
    REPORT --> COMPLETE([Complete])
    ERROR --> COMPLETE
```

## 10.2 Analysis Workflow State Schema

```python
class AnalysisState(TypedDict):
    # Input
    analysis_id: str
    dataset_id: str
    project_id: str
    user_id: str
    analysis_types: List[str]
    config: Dict[str, Any]
    
    # Processing state
    current_step: str
    progress_pct: int
    
    # Data
    raw_dataframe_path: str
    cleaned_dataframe_path: str
    
    # Agent outputs
    cleaning_report: Optional[Dict]
    eda_report: Optional[Dict]
    chart_configs: Optional[List[Dict]]
    insights: Optional[List[Dict]]
    consultant_memo: Optional[str]
    report_path: Optional[str]
    
    # Error handling
    errors: List[str]
    warnings: List[str]
    retry_counts: Dict[str, int]
    
    # Metadata
    started_at: str
    completed_at: Optional[str]
```

## 10.3 Chat Workflow Graph

```mermaid
graph TD
    START([User Message]) --> CLASSIFY[Classify Intent]
    CLASSIFY -->|Simple Q&A| RETRIEVE[Retrieve from ChromaDB]
    CLASSIFY -->|SQL Query| SQL_AGENT[SQL Agent]
    CLASSIFY -->|Chart Request| VIZ_AGENT[Visualization Agent]
    CLASSIFY -->|Complex Analysis| ANALYSIS_AGENT[EDA/Insight Agent]
    
    RETRIEVE --> GENERATE[Generate Response]
    SQL_AGENT --> GENERATE
    VIZ_AGENT --> GENERATE
    ANALYSIS_AGENT --> GENERATE
    
    GENERATE --> FORMAT[Format with Citations]
    FORMAT --> SAVE[Save to Chat History]
    SAVE --> RESPOND([Return to User])
```

## 10.4 Human Approval Flow (COA)

```mermaid
graph TD
    COA_REQUEST[COA Action Requested] --> APPROVAL_CHECK{Auto-Allow?}
    APPROVAL_CHECK -->|Always Allow Rule| EXECUTE[Execute Action]
    APPROVAL_CHECK -->|Session Allow| EXECUTE
    APPROVAL_CHECK -->|Manual Required| NOTIFY[Send Approval Notification]
    
    NOTIFY --> WAIT[Wait for User Decision]
    WAIT -->|Allow Once| EXECUTE
    WAIT -->|Allow For Session| SAVE_SESSION[Save Session Rule]
    WAIT -->|Always Allow| SAVE_ALWAYS[Save Permanent Rule]
    WAIT -->|Deny| DENY[Log Denial + Skip]
    WAIT -->|Timeout 5min| AUTO_DENY[Auto-Deny + Notify]
    
    SAVE_SESSION --> EXECUTE
    SAVE_ALWAYS --> EXECUTE
    EXECUTE --> LOG[Audit Log Entry]
    DENY --> LOG
    AUTO_DENY --> LOG
    LOG --> COMPLETE([Complete])
```

## 10.5 Retry and Error Recovery Strategy

| Scenario | Strategy | Max Attempts |
|---------|---------|-------------|
| Gemini API rate limit (429) | Exponential backoff: 2s, 4s, 8s | 3 |
| Gemini API server error (500) | Fixed retry: 5s delay | 3 |
| Gemini timeout | Re-invoke with truncated input | 2 |
| pandas MemoryError | Chunk processing (10k rows/chunk) | 2 |
| Database connection error | Reconnect with 3s delay | 5 |
| ChromaDB timeout | Skip RAG, use raw data instead | 1 |
| File not found | Re-fetch from S3 | 2 |
| Agent partial failure | Log warning, continue with partial results | N/A |

---

# 11. Data Analysis Engine

## 11.1 Data Profiling

The profiling engine runs immediately after upload, before any agent processes the data.

**Profile Outputs Per Column:**

| Metric | Numeric | Categorical | Date | Text | Boolean |
|--------|---------|------------|------|------|---------|
| Count | ✅ | ✅ | ✅ | ✅ | ✅ |
| Null count + % | ✅ | ✅ | ✅ | ✅ | ✅ |
| Unique count | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mean | ✅ | ❌ | ❌ | ❌ | ❌ |
| Std Dev | ✅ | ❌ | ❌ | ❌ | ❌ |
| Min/Max | ✅ | ❌ | ✅ | ❌ | ❌ |
| P25/P50/P75 | ✅ | ❌ | ❌ | ❌ | ❌ |
| Skewness | ✅ | ❌ | ❌ | ❌ | ❌ |
| Top 5 values | ❌ | ✅ | ❌ | ❌ | ✅ |
| Date range | ❌ | ❌ | ✅ | ❌ | ❌ |
| Avg word length | ❌ | ❌ | ❌ | ✅ | ❌ |

## 11.2 Missing Value Strategies

| Strategy | Condition | Action |
|---------|-----------|--------|
| Drop row | Row null ratio > 80% | Remove row |
| Drop column | Column null ratio > 50% AND not critical | Remove column + warn |
| Mean imputation | Numeric, null < 20%, distribution normal | Fill with mean |
| Median imputation | Numeric, null < 20%, distribution skewed | Fill with median |
| Mode imputation | Categorical, null < 30% | Fill with mode |
| Forward fill | Time-series column | Forward fill |
| Constant fill | Boolean column | Fill with False |
| Flag column | Any | Add `_is_null` indicator column |

## 11.3 Outlier Detection

Three methods used in parallel:
1. **IQR Method:** Values outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR] flagged as outliers
2. **Z-Score Method:** |z| > 3.0 flagged as statistical outliers
3. **Isolation Forest:** ML-based multivariate outlier detection (for datasets >1000 rows)

Outliers are **flagged** by default, not removed. Users choose the action (remove/cap/keep).

## 11.4 Correlation Analysis

- **Pearson:** Linear relationships between numeric pairs
- **Spearman:** Rank-order correlation (robust to outliers)
- **Point-Biserial:** Numeric vs Binary
- **Cramér's V:** Categorical vs Categorical
- Correlation threshold alerts: |r| > 0.85 flagged as high correlation

## 11.5 Segmentation Engine

Uses K-Means clustering with automatic cluster count selection via:
- **Elbow Method:** Plot WCSS vs k (2–10)
- **Silhouette Score:** Select k with highest average silhouette
- **Gap Statistic:** Statistical benchmark comparison

Output includes:
- Cluster assignment per row
- Cluster centroid values
- Cluster size distribution
- AI-generated description per cluster ("Cluster 2: High-value, low-frequency buyers")

## 11.6 RFM Analysis

Requires: customer ID column, transaction date column, monetary value column

**Steps:**
1. Calculate R (Recency: days since last purchase), F (Frequency: purchase count), M (Monetary: total spend)
2. Score each dimension 1–5 (quintile-based)
3. Assign segment labels: Champions, Loyal, At Risk, Can't Lose, Lost
4. Generate segment size stats and average RFM scores per segment
5. AI narrative: "Your Champions represent X% of customers but Y% of revenue"

## 11.7 Cohort Analysis

Requires: user ID column, first-action date, event date

**Output:**
- Cohort retention matrix (week/month × cohort group)
- Retention heatmap chart config
- Average retention by period
- Drop-off inflection points identified

## 11.8 Market Basket Analysis

Uses Apriori algorithm (mlxtend library):
- Minimum support: 0.01
- Minimum confidence: 0.5
- Minimum lift: 1.0
- Output: association rules ranked by lift, top 20 rules surfaced as insights

---

# 12. Visualization Engine

## 12.1 KPI Card Specification

Each KPI card displays:
- Metric name
- Current value (formatted: $ for currency, % for rates, K/M/B for large numbers)
- Period comparison (vs last period: ▲ 12.3% or ▼ 5.1%)
- Sparkline (7-point mini chart)
- Color coding: green (positive), red (negative), neutral (grey)

KPI cards are auto-generated based on:
- Numeric columns with date dimension → time-based KPIs
- Aggregate functions (sum, mean, count) on key columns

## 12.2 Chart Specifications

### Recharts JSON Config Structure (Standard)
```json
{
  "id": "uuid",
  "chart_type": "bar|line|scatter|heatmap|histogram|box|pie|area",
  "title": "string",
  "caption": "AI-generated insight",
  "data": [...],
  "config": {
    "x_key": "column_name",
    "y_keys": ["column_name"],
    "color_scheme": "default|blue|green|diverging",
    "show_legend": true,
    "show_grid": true,
    "animation": true
  },
  "dimensions": { "width": "100%", "height": 350 }
}
```

## 12.3 Dashboard Layout System

Dashboards use a 12-column grid system. Widgets are positioned using:
```json
{
  "widget_id": "uuid",
  "type": "kpi_card|chart|insight_panel|data_table",
  "position": { "x": 0, "y": 0, "w": 4, "h": 2 },
  "config": {}
}
```

## 12.4 Drill-Down Specification

Charts support drill-down via onClick handlers:
- Bar chart segment clicked → filtered dataset view
- Line chart point clicked → row-level data panel
- Heatmap cell clicked → column pair scatter plot

## 12.5 Export Capabilities

| Format | Method | Resolution |
|--------|--------|-----------|
| PNG | html2canvas / server-side matplotlib | 2x retina (1920px wide) |
| SVG | Direct Recharts SVG export | Vector |
| PDF (chart) | Embedded in report PDF | 300 DPI |
| CSV (data) | Raw pandas to CSV | — |

---

# 13. Forecasting Engine

## 13.1 Model Selection Framework

```mermaid
flowchart TD
    START[Forecasting Request] --> CHECK_DATES{Date Column Present?}
    CHECK_DATES -->|No| NO_TS[Regression Only Mode]
    CHECK_DATES -->|Yes| CHECK_LEN{Rows > 100?}
    CHECK_LEN -->|No| LINEAR[Linear Regression]
    CHECK_LEN -->|Yes| CHECK_SEASON{Seasonality Detected?}
    CHECK_SEASON -->|Yes + >365 rows| PROPHET[Prophet Model]
    CHECK_SEASON -->|No| CHECK_FEATS{Multiple Features?}
    CHECK_FEATS -->|Yes| XGBOOST[XGBoost Model]
    CHECK_FEATS -->|No| PROPHET
```

## 13.2 Prophet Engine

**Inputs Required:**
- `ds` column: datetime
- `y` column: numeric target

**Configuration:**
```python
ProphetConfig:
  yearly_seasonality: "auto"
  weekly_seasonality: "auto"
  daily_seasonality: False
  changepoint_prior_scale: 0.05  # tunable
  seasonality_prior_scale: 10.0
  interval_width: 0.95  # 95% CI
  growth: "linear"  # or "logistic"
```

**Outputs:** forecast DataFrame with `ds`, `yhat`, `yhat_lower`, `yhat_upper`, `trend`, `weekly`, `yearly`

**Evaluation:** 20% holdout, compute MAPE, MAE, RMSE on holdout

## 13.3 XGBoost Engine

**Feature Engineering Applied:**
- Lag features: t-1, t-7, t-14, t-30
- Rolling mean: 7-day, 30-day
- Date features: day_of_week, month, quarter, is_weekend
- Target encoding for categoricals

**Configuration:**
```python
XGBConfig:
  n_estimators: 200
  max_depth: 6
  learning_rate: 0.05
  subsample: 0.8
  colsample_bytree: 0.8
  early_stopping_rounds: 20
```

## 13.4 Evaluation Metrics

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| MAPE | mean(|actual - forecast| / actual) × 100 | % error (lower = better) |
| MAE | mean(|actual - forecast|) | Absolute units error |
| RMSE | sqrt(mean((actual - forecast)²)) | Penalizes large errors |
| R² | 1 - SS_res/SS_tot | Variance explained (1 = perfect) |

**Quality Thresholds:**
| Rating | MAPE |
|--------|------|
| Excellent | < 5% |
| Good | 5–15% |
| Acceptable | 15–25% |
| Poor | > 25% |

---

# 14. Reporting Engine

## 14.1 PDF Report Structure

Generated using **ReportLab** with custom styles:

**Page Layout:** A4, 25mm margins all sides, header/footer with logo + page numbers

**Section Specifications:**

| Section | Content | Page Estimate |
|---------|---------|--------------|
| Cover Page | Title, dataset, date, logo | 1 |
| Table of Contents | Auto-generated | 1 |
| Executive Summary | 300–500 words, 3–5 key bullets | 1–2 |
| Dataset Overview | Profile stats table, quality score visual | 1–2 |
| Key Insights | Top 5 insights, each with supporting chart | 3–5 |
| Detailed Analysis | Column-by-column EDA, correlation heatmap | 2–5 |
| Forecasting Results | Forecast chart, metrics table, explanation | 1–2 |
| Anomaly Report | Anomaly table, timeline chart | 1 |
| Recommendations | Prioritized action table | 1 |
| Appendix | Raw statistics, full correlation matrix | 1–3 |

## 14.2 PPTX Report Structure

Generated using **python-pptx** with a professional slide template:

**Slide Layout:**

| Slide | Content |
|-------|---------|
| 1 | Title Slide: Dataset name, date, project |
| 2 | Agenda / Table of Contents |
| 3 | Executive Summary (bullet points) |
| 4 | Dataset Overview (stats table) |
| 5–7 | Top 3 Key Insights (one per slide, with chart) |
| 8–10 | EDA Highlights (3 key charts) |
| 11 | Forecast Chart (if applicable) |
| 12 | Recommendations (3-column table) |
| 13 | Thank You / Contact |

## 14.3 Executive Summary Writing

The executive summary is written by the Report Agent using this prompt structure:
- Input: All insights + EDA report + dataset context
- Output: 3 paragraphs: (1) What the data shows, (2) Key risks/opportunities, (3) Recommended next actions
- Tone: Professional, non-technical, executive-appropriate
- Model: Gemini 2.5 Pro

---

# 15. Chat With Data

## 15.1 RAG Architecture

```mermaid
graph TB
    subgraph "Indexing (One-time on Upload)"
        DF[DataFrame] --> CHUNK[Chunking Strategy]
        CHUNK --> SUMMARY_CHUNK[Statistical Summaries]
        CHUNK --> ROW_CHUNK[Row Samples - 500 rows random]
        CHUNK --> COL_CHUNK[Column Descriptions]
        SUMMARY_CHUNK --> EMBED[Gemini Embeddings]
        ROW_CHUNK --> EMBED
        COL_CHUNK --> EMBED
        EMBED --> CHROMA[(ChromaDB Collection)]
    end

    subgraph "Query Time"
        USER_Q[User Question] --> Q_EMBED[Embed Question]
        Q_EMBED --> RETRIEVE[Top-K Retrieval k=10]
        CHROMA --> RETRIEVE
        RETRIEVE --> RERANK[Rerank by Relevance]
        RERANK --> CONTEXT[Build Context Window]
        CONTEXT --> HISTORY[+ Chat History]
        HISTORY --> GEMINI[Gemini 2.5 Pro]
        GEMINI --> RESPONSE[Response + Citations]
    end
```

## 15.2 Chunking Strategy

| Chunk Type | Content | Metadata |
|-----------|---------|---------|
| Column summary | "Column 'revenue' is numeric. Mean: $12,450. Range: $0–$250,000. 5 nulls." | column_name, type |
| Row sample | Serialized row dict (25 rows per chunk) | row_indices |
| Aggregate fact | "Total revenue: $1.2M. Top region: West ($450K)" | aggregation_type |
| Dataset summary | Overall profile paragraph | dataset_level |

## 15.3 Context Memory Management

```
Session starts → empty history

Messages 1–20: Full conversation kept in state

Message 21+:
  - Messages 1–15 → summarize via Gemini Flash
  - Keep summary + messages 16–current
  - New context = summary + last 5 messages + RAG results
```

## 15.4 Question Classification

Before routing to retrieval or SQL, questions are classified:

| Class | Example | Handler |
|-------|---------|---------|
| Statistical fact | "What is the average revenue?" | RAG + Aggregation |
| Row lookup | "Show me rows where sales > 10000" | SQL Agent |
| Trend question | "Is revenue growing over time?" | EDA cached results |
| Forecast question | "What will revenue be next month?" | Forecasting Agent |
| Chart request | "Show me a bar chart of sales by region" | Visualization Agent |
| General BI | "What should I focus on first?" | Insight/Consultant Agent |

---

# 16. File Management System

## 16.1 Upload Flow

```mermaid
sequenceDiagram
    participant U as User
    participant FE as Frontend
    participant API as FastAPI
    participant VALID as Validator
    participant S3 as File Storage
    participant Q as Celery Queue
    participant W as Worker

    U->>FE: Select file
    FE->>FE: Client-side validation (size, extension)
    FE->>API: POST /datasets/upload (multipart)
    API->>VALID: Validate file
    VALID->>VALID: Check MIME type vs extension
    VALID->>VALID: Check file size <= 500MB
    VALID->>VALID: Scan for malicious content
    VALID-->>API: Validation result
    API->>S3: Save raw file (with UUID filename)
    API->>DB: Create dataset record (status=processing)
    API->>Q: Enqueue parse task
    API-->>FE: 202 + dataset_id
    
    W->>Q: Dequeue parse task
    W->>S3: Download file
    W->>W: Parse to pandas DataFrame
    W->>W: Detect column types
    W->>W: Generate profile
    W->>DB: Save profile + update status=ready
    W->>Q: Enqueue embedding task
    W-->>FE: WebSocket: dataset_ready event
```

## 16.2 File Validation Rules

| Check | Rule | Action on Fail |
|-------|------|----------------|
| Extension | .csv, .xlsx, .xls, .pdf, .pptx | Reject with error |
| MIME type | Must match extension | Reject |
| File size | Max 500MB | Reject with 413 |
| Empty file | Size > 0 bytes | Reject |
| Malicious content | No executable content in XLSX macros | Reject |
| CSV encoding | UTF-8, Latin-1, CP1252 | Auto-detect, fail if unknown |
| XLSX corruption | File must open without error | Reject |
| Column count | Minimum 2 columns | Warn |
| Row count | Minimum 10 rows for analysis | Warn |

## 16.3 Excel Multi-Sheet Handling

1. On upload, detect all sheets
2. Return sheet list to user
3. User selects one or multiple sheets
4. If multiple: offer join/union/separate options
5. Each sheet processed as a separate dataset OR merged

## 16.4 Supported File Types Summary

| Type | Max Size | Notes |
|------|---------|-------|
| CSV | 500MB | Auto-encoding detection |
| XLSX / XLS | 100MB | Multi-sheet support |
| PDF | 50MB | Text extraction only (for chat/analysis) |
| PPTX | 50MB | Text extraction for context |

---

# 17. SQL Integration

## 17.1 Connection Flow

```mermaid
sequenceDiagram
    participant U as User
    participant API as FastAPI
    participant VAULT as Secrets Vault
    participant DB_CONN as DB Connection

    U->>API: POST /datasets/connect-db (credentials)
    API->>API: Validate connection params
    API->>VAULT: Encrypt and store password
    API->>DB_CONN: Test connection (timeout 10s)
    DB_CONN-->>API: Connection status
    API->>DB_CONN: Fetch schema (table names, columns, types)
    DB_CONN-->>API: Schema JSON
    API-->>U: Connection created + schema preview
```

## 17.2 Supported Database Configurations

| Database | Driver | Port (Default) | Connection String Template |
|---------|--------|----------|--------------------------|
| PostgreSQL | psycopg2 | 5432 | `postgresql://user:pass@host:port/db` |
| MySQL | PyMySQL | 3306 | `mysql+pymysql://user:pass@host:port/db` |
| SQLite | Built-in | N/A | `sqlite:///path/to/file.db` |

## 17.3 SQL Security Architecture

**Mandatory Security Controls:**
1. **Read-Only Transactions:** Every query executed inside `BEGIN READ ONLY; ... ROLLBACK;`
2. **Allowlist Validation:** Parser checks for presence of forbidden keywords before execution
3. **Query Timeout:** 30-second timeout enforced at connection level
4. **Schema-Only Sharing:** Database schema (not data) passed to Gemini for query generation
5. **Credential Encryption:** Passwords encrypted with AES-256 before storage
6. **Parameterized Queries:** All queries use parameter binding to prevent injection
7. **Row Limit:** Results capped at 10,000 rows; streaming for larger results

**Forbidden SQL Keywords (Hard Reject):**
```
DROP, DELETE, TRUNCATE, ALTER, UPDATE, INSERT, CREATE, GRANT, 
REVOKE, EXECUTE, CALL, EXEC, XP_, SP_, INFORMATION_SCHEMA.*, 
pg_read_file, LOAD DATA, OUTFILE
```

## 17.4 Natural Language to SQL Flow

1. User asks: "What are the top 10 customers by revenue last quarter?"
2. SQL Agent receives: schema JSON + question
3. Gemini Pro generates SQL
4. Safety validator scans generated SQL
5. If safe: execute via read-only connection
6. Return DataFrame + explain query in plain English
7. Offer to save as a named query or add to dashboard

---

# 18. Power BI Integration

## 18.1 Integration Architecture

Power BI integration operates via the Power BI REST API and requires user OAuth credentials.

**Supported Actions:**
- Export dashboard as Power BI `.pbix` dataset
- Push dataset to Power BI workspace
- Create report from AI-BIOS analysis results
- Sync forecasting results to Power BI dataset

## 18.2 Export Workflow

```mermaid
sequenceDiagram
    participant U as User
    participant AIBIOS as AI-BIOS API
    participant PBI as Power BI API

    U->>AIBIOS: Request Power BI export
    AIBIOS->>AIBIOS: Format dataset as Power BI-compatible JSON
    AIBIOS->>AIBIOS: Build .pbix manifest
    AIBIOS->>PBI: POST /datasets (OAuth2 Bearer)
    PBI-->>AIBIOS: dataset_id
    AIBIOS->>PBI: POST /reports (bind to dataset)
    PBI-->>AIBIOS: report_url
    AIBIOS-->>U: Power BI report URL
```

## 18.3 Dataset Publishing Format

AI-BIOS exports datasets in Power BI's push dataset format:
- Tables defined with column names and Power BI data types
- Rows pushed in batches of 1000
- Maximum 75MB per dataset push
- Relationships between tables declared in schema

---

# 19. Computer Operator Agent

## 19.1 Overview and Safety Philosophy

The Computer Operator Agent (COA) is the most security-critical component of AI-BIOS. It bridges the AI platform with local desktop applications. The guiding principle is:

> **The COA NEVER acts autonomously. Every action MUST pause and wait for explicit human approval before execution. This is architecturally enforced, not merely policy.**

## 19.2 Capability Matrix

| Capability | Target Application | Risk Level |
|-----------|-------------------|-----------|
| Open application | VS Code, Power BI, Excel, MySQL Workbench, Browser | Low |
| Open specific file | Any supported app | Medium |
| Run a script | Python, PowerShell, Bash | High |
| Execute SQL in workbench | MySQL Workbench | High |
| Export data to Excel | Excel | Medium |
| Open URL in browser | Chrome/Edge/Firefox | Low-Medium |
| Navigate to URL | Browser | Medium |
| Fill web form | Browser | High |
| Run workflow (multi-step) | Any combination | Critical |

## 19.3 COA Architecture

```mermaid
graph TB
    subgraph "AI-BIOS Backend"
        USER_REQ[User Request to COA] --> PLANNER[Action Planner<br/>Gemini 2.5 Pro]
        PLANNER --> ACTION_LIST[Action Sequence]
        ACTION_LIST --> APPROVAL_MGR[Approval Manager]
    end

    subgraph "Approval System"
        APPROVAL_MGR --> NOTIFY_UI[Push Notification<br/>to Frontend]
        NOTIFY_UI --> APPROVAL_DIALOG[Approval Dialog<br/>in Browser]
        APPROVAL_DIALOG --> USER_DECISION{User Decision}
        USER_DECISION -->|Allow| PERMISSION_STORE[(Permission Store)]
        USER_DECISION -->|Deny| DENY_LOG[Log Denial]
        PERMISSION_STORE --> EXECUTOR[Action Executor]
    end

    subgraph "Desktop Layer (Local Agent)"
        EXECUTOR --> LOCAL_AGENT[Local Python Agent<br/>pyautogui / subprocess]
        LOCAL_AGENT --> APP[Target Application]
        LOCAL_AGENT --> RESULT[Execution Result]
        RESULT --> AUDIT_LOG[(Audit Log)]
    end
```

## 19.4 Approval Dialog Specification

The approval dialog is a modal presented in the browser UI. It is blocking — no other UI interaction is possible until a decision is made.

**Dialog Content:**

```
┌─────────────────────────────────────────────────┐
│  🤖 Computer Operator Agent — Action Request     │
├─────────────────────────────────────────────────┤
│  Agent:           Computer Operator Agent        │
│  Requested By:    Analysis Workflow              │
│  Action:          Open Excel and export dataset  │
│  Target App:      Microsoft Excel                │
│  Reason:          Export cleaned sales data      │
│                   for client presentation        │
│  Expected Result: Excel opens with sales.xlsx    │
│  Risk Level:      🟡 Medium                      │
│                                                  │
│  ┌──────────┬──────────┬──────────┬───────────┐ │
│  │Allow Once│Allow     │ Always   │   Deny    │ │
│  │          │Session   │  Allow   │           │ │
│  └──────────┴──────────┴──────────┴───────────┘ │
│                                                  │
│  ⏱ Auto-deny in: 4:32                           │
└─────────────────────────────────────────────────┘
```

## 19.5 Permission Scope Definitions

| Scope | Duration | Stored In | Revocable |
|-------|---------|-----------|----------|
| Allow Once | Single execution | RAM | N/A (single use) |
| Allow For Session | Until browser tab closes | Session storage | Yes (end session) |
| Always Allow | Permanent | PostgreSQL `coa_permissions` | Yes (admin panel) |
| Deny | Single decision | Audit log only | N/A |

## 19.6 Auto-Deny Rules

The system auto-denies any pending COA action if:
- User does not respond within **5 minutes**
- User navigates away from the approval dialog
- Browser tab is closed
- Session token expires
- The action was flagged as **Critical** risk (always manual regardless)

## 19.7 COA Action Schema

```python
class COAAction:
    id: UUID
    agent_name: str = "computer_operator_agent"
    action_type: COAActionType  # enum
    target_application: str
    action_params: Dict[str, Any]
    reason: str  # AI-generated human-readable reason
    expected_outcome: str
    risk_level: RiskLevel  # low|medium|high|critical
    rollback_strategy: Optional[str]
    timeout_seconds: int = 30
```

## 19.8 Rollback Strategies

| Action | Rollback Strategy |
|--------|------------------|
| Open file | Close the opened file |
| Run script | Kill process by PID |
| Export to Excel | Delete created file |
| Fill web form | Navigate back |
| Multi-step workflow | Reverse steps in order |

**Rollback Trigger:** User can request rollback from the COA Actions History panel within 5 minutes of execution.

## 19.9 Local Agent Architecture

The COA requires a local Python agent (`aibios-local-agent`) running on the user's desktop:
- Communicates with AI-BIOS backend via WebSocket (authenticated)
- Receives action payloads (signed with HMAC-SHA256)
- Uses `pyautogui`, `subprocess`, `win32com` (Windows), `applescript` (macOS)
- Reports back execution status and screenshots

**Local Agent Security:**
- Only connects to authenticated AI-BIOS backend
- Actions validated against allowlist before execution
- No action executed without approval token from backend
- All actions logged locally and synced to backend

## 19.10 Audit Log Schema for COA

Every COA action generates an immutable audit entry:
```json
{
  "action_id": "uuid",
  "user_id": "uuid",
  "action_type": "string",
  "target_application": "string",
  "action_params": {...},
  "approval_scope": "once|session|always",
  "approved_at": "ISO8601",
  "executed_at": "ISO8601",
  "execution_result": "success|failed|rolled_back",
  "error_message": "string|null",
  "screenshot_path": "string|null",
  "ip_address": "string",
  "session_id": "string"
}
```

---

# 20. Security Architecture

## 20.1 OWASP Top 10 Mitigations

| OWASP Risk | Mitigation |
|-----------|-----------|
| A01: Broken Access Control | RBAC enforced at API + DB layer, RLS in PostgreSQL |
| A02: Cryptographic Failures | AES-256 at rest, TLS 1.3 in transit, bcrypt passwords |
| A03: Injection | Parameterized queries, SQL allowlist for COA, Pydantic input validation |
| A04: Insecure Design | Threat modeling per phase, principle of least privilege |
| A05: Security Misconfiguration | Hardened Docker images, secrets in environment variables |
| A06: Vulnerable Components | Dependabot alerts, `pip-audit` in CI/CD |
| A07: Auth & Session Failures | Short-lived JWTs (15min), refresh token rotation, brute force lockout |
| A08: Software & Data Integrity | HMAC-signed COA action tokens, signed Docker images |
| A09: Logging Failures | Immutable audit log, centralized logging to Loki |
| A10: SSRF | Allowlisted outbound domains, no user-supplied URLs in backend requests |

## 20.2 Secrets Management

| Secret Type | Storage Method |
|------------|---------------|
| DATABASE_URL | Railway/Vercel environment variable |
| GEMINI_API_KEY | Railway environment variable, never in code |
| JWT_SECRET | Railway environment variable, rotated quarterly |
| DB connection passwords | AES-256 encrypted in PostgreSQL, key in env |
| SMTP credentials | Environment variable |
| Power BI OAuth tokens | Encrypted in PostgreSQL |

**Rules:**
- No secrets in source code, ever
- No secrets in Docker images
- No secrets logged
- `.env` files are `.gitignored`

## 20.3 File Upload Security

- All uploaded files stored with UUID names (no original filename on disk)
- XLSX files scanned for VBA macros before processing (if found: strip or reject)
- PDF files processed in sandboxed subprocess
- Upload directory is NOT served directly — always served through signed URLs with TTL

## 20.4 Agent Safety Controls

- SQL Agent: read-only mode enforced at connection level
- COA: every action requires explicit human approval token
- All agents: maximum token output limit enforced
- All agents: hallucination mitigation via structured output schemas
- Prompt injection protection: user input sanitized before embedding in prompts
- System prompts stored server-side only, never exposed to client

## 20.5 API Security

- Rate limiting per user and per IP (see Section 8.4)
- CORS configured to allow only frontend domain
- All endpoints require authentication except auth endpoints
- Request size limits: 500MB for file uploads, 10KB for JSON bodies
- API versioning prevents abrupt breaking changes

---

# 21. Performance Architecture

## 21.1 Caching Strategy

| Cache Target | TTL | Key Pattern | Invalidation |
|-------------|-----|-------------|-------------|
| Dataset profile | 24 hours | `profile:{dataset_id}` | On dataset update |
| Analysis results | 7 days | `analysis:{analysis_id}` | On analysis re-run |
| Chart configs | 24 hours | `charts:{analysis_id}` | On analysis update |
| User project list | 5 minutes | `projects:{user_id}` | On project create/delete |
| DB schema | 1 hour | `schema:{connection_id}` | On connection update |
| Chat embeddings | 30 days | ChromaDB collection | On dataset delete |

## 21.2 Celery Task Routing

```python
task_routes = {
    "tasks.parse_file": {"queue": "high_priority"},
    "tasks.run_analysis": {"queue": "compute"},
    "tasks.generate_embeddings": {"queue": "ai"},
    "tasks.generate_report": {"queue": "reports"},
    "tasks.run_forecast": {"queue": "compute"},
    "tasks.send_notification": {"queue": "low_priority"},
}
```

**Worker Pool Configuration:**
| Queue | Workers | Concurrency |
|-------|---------|-------------|
| high_priority | 2 | 4 |
| compute | 4 | 2 |
| ai | 2 | 1 |
| reports | 2 | 2 |
| low_priority | 1 | 4 |

## 21.3 Pagination Standards

All list endpoints use cursor-based pagination:
```json
{
  "items": [...],
  "pagination": {
    "has_next": true,
    "has_prev": false,
    "next_cursor": "base64_encoded_cursor",
    "limit": 20
  }
}
```

## 21.4 Large File Processing

Files > 50MB processed in streaming chunks:
1. Read CSV in 50k-row chunks
2. Profile each chunk, accumulate statistics
3. Merge chunk statistics using Welford's algorithm for running mean/std
4. Write cleaned chunks to new file
5. Memory usage capped at 2GB per worker

## 21.5 Database Query Optimization

- Eager loading: Use SQLAlchemy `selectinload()` for related objects
- N+1 prevention: All list queries use JOINs or batch fetching
- Query analysis: `EXPLAIN ANALYZE` run on all new queries during development
- Slow query log: PostgreSQL `log_min_duration_statement = 500ms`

---

# 22. Monitoring & Observability

## 22.1 Logging Architecture

**Log Levels by Component:**

| Component | Level | Output |
|----------|-------|--------|
| API requests | INFO | Structured JSON to stdout |
| Agent actions | INFO | PostgreSQL `agent_logs` table |
| Auth events | WARN+ | Audit log + stdout |
| Errors | ERROR | stdout + Sentry |
| SQL queries | DEBUG | Dev only |
| Celery tasks | INFO | stdout + flower |

**Structured Log Format:**
```json
{
  "timestamp": "ISO8601",
  "level": "INFO",
  "service": "fastapi",
  "request_id": "uuid",
  "user_id": "uuid|null",
  "method": "POST",
  "path": "/api/v1/analyses/run",
  "status_code": 202,
  "duration_ms": 45,
  "message": "Analysis task queued"
}
```

## 22.2 Metrics (Prometheus)

Key metrics exposed at `/metrics`:

| Metric | Type | Labels |
|--------|------|--------|
| `http_requests_total` | Counter | method, path, status |
| `http_request_duration_seconds` | Histogram | method, path |
| `active_analyses` | Gauge | status |
| `celery_task_duration_seconds` | Histogram | task_name |
| `gemini_api_calls_total` | Counter | model, status |
| `gemini_tokens_used_total` | Counter | model |
| `file_upload_size_bytes` | Histogram | file_type |
| `rag_retrieval_latency_seconds` | Histogram | — |
| `coa_actions_total` | Counter | action_type, status |

## 22.3 Health Check Endpoints

| Endpoint | Checks |
|---------|--------|
| `GET /health` | App running |
| `GET /health/db` | PostgreSQL connection |
| `GET /health/redis` | Redis connection |
| `GET /health/chroma` | ChromaDB connection |
| `GET /health/celery` | Celery worker ping |

## 22.4 Alerting Rules

| Alert | Condition | Severity |
|-------|-----------|---------|
| API error rate high | > 5% 5xx in 5 min | Critical |
| Analysis failure rate | > 10% failed in 1 hour | Warning |
| Celery queue depth | > 100 pending tasks | Warning |
| Database connections | > 80% pool used | Warning |
| Memory usage | > 85% of container limit | Critical |
| Gemini API errors | > 5 consecutive failures | Critical |
| COA unapproved timeout | Any 5min auto-deny | Info |

---

# 23. Testing Strategy

## 23.1 Testing Pyramid

```mermaid
graph TB
    E2E["E2E Tests<br/>(Playwright)<br/>~20 tests<br/>Critical user journeys"]
    INTEGRATION["Integration Tests<br/>(pytest + TestClient)<br/>~150 tests<br/>API + DB + Agents"]
    UNIT["Unit Tests<br/>(pytest)<br/>~500 tests<br/>Services, utilities, validators"]
    
    E2E --> INTEGRATION --> UNIT
```

## 23.2 Unit Test Coverage Requirements

| Module | Minimum Coverage |
|--------|----------------|
| Services layer | 90% |
| Analysis engines | 85% |
| Forecasting engines | 90% |
| Security/auth | 95% |
| Agents (tool functions) | 80% |
| API schemas/validators | 90% |
| File validators | 95% |

## 23.3 Integration Test Scenarios

| Scenario | What Is Tested |
|---------|---------------|
| Upload CSV → profile generated | File upload + parse + profile pipeline |
| Upload XLSX multi-sheet → select sheet | Sheet detection + selection |
| Run EDA analysis → results saved | Full analysis workflow |
| Generate PDF report | Report agent + ReportLab output |
| Chat message with RAG | Embedding + retrieval + Gemini response |
| COA action → approval required → execute | Full approval flow |
| DB connect → schema fetch → query | SQL agent end-to-end |
| JWT login → refresh → protected route | Auth flow |
| Forecast run → Prophet → results | Forecasting pipeline |

## 23.4 Agent Testing Strategy

Each agent is tested with:
1. **Happy path:** Normal inputs → expected output structure
2. **Malformed input:** Missing columns, wrong types → graceful error
3. **Large input:** 100k rows → completes within timeout
4. **Empty dataset:** 0 rows → informative error
5. **Retry test:** Simulate Gemini failure → verify retry behavior
6. **Partial failure:** One tool fails → rest of agent continues

**AI Output Evaluation:**
- Insights are evaluated for relevance using a separate Gemini call (LLM-as-judge)
- Chart configs are validated against Recharts schema
- SQL queries are validated for safety and syntactic correctness
- Report text is checked for minimum word count and section completeness

## 23.5 E2E Test Scenarios (Playwright)

1. Register → Login → Create Project → Upload CSV → View Profile
2. Run Full Analysis → View Dashboard → Export PDF
3. Connect PostgreSQL → Ask Natural Language Question → Get Chart
4. Run Forecast → View Chart → Export PPTX
5. Admin: Create User → Assign Role → View Audit Log
6. COA: Request action → Approve → Verify execution logged
7. Chat: Multi-turn conversation → Follow-up maintains context
8. Share Dashboard → Public URL → Viewer access

## 23.6 Security Testing

| Test Type | Tool | Frequency |
|-----------|------|-----------|
| SAST | Bandit (Python), ESLint security plugin | Every PR |
| Dependency scan | pip-audit, npm audit | Daily |
| SQL injection test | Custom test suite | Every PR |
| Auth bypass test | Custom test suite | Every PR |
| File upload fuzzing | Manual + automated | Monthly |
| OWASP ZAP scan | ZAP (automated) | Weekly on staging |

---

# 24. CI/CD Pipeline

## 24.1 GitHub Actions Workflow

```yaml
# .github/workflows/ci.yml
Triggers: push to main, pull_request to main

Jobs:
  1. lint-and-type-check
     - Frontend: ESLint + TypeScript tsc
     - Backend: ruff, mypy
  
  2. unit-tests
     - Backend: pytest with coverage report
     - Frontend: Jest unit tests
     - Minimum coverage: 80%
  
  3. security-scan
     - bandit (backend)
     - pip-audit
     - npm audit
     - Snyk (if configured)
  
  4. build-docker
     - Build backend image
     - Build frontend image
     - Tag with git SHA
  
  5. integration-tests
     - Spin up docker-compose test stack
     - Run pytest integration tests
     - Tear down
  
  6. e2e-tests (main branch only)
     - Deploy to staging
     - Run Playwright tests
     - Tear down
  
  7. deploy-staging (main branch, after all tests pass)
     - Deploy backend to Railway staging
     - Deploy frontend to Vercel preview
  
  8. deploy-production (manual trigger + tag)
     - Deploy backend to Railway production
     - Deploy frontend to Vercel production
     - Run smoke tests
     - Notify Slack
```

## 24.2 Docker Build Specifications

**Backend Dockerfile (multi-stage):**
```
Stage 1: python:3.12-slim — Install build dependencies
Stage 2: python:3.12-slim — Copy only runtime deps
  - Run as non-root user (uid 1000)
  - EXPOSE 8000
  - HEALTHCHECK via /health
  - No secrets baked in
```

**Frontend Dockerfile (multi-stage):**
```
Stage 1: node:20-alpine — npm install + next build
Stage 2: node:20-alpine — Copy .next/standalone
  - Run as non-root user
  - EXPOSE 3000
  - HEALTHCHECK via /api/health
```

## 24.3 Environment Strategy

| Environment | Backend | Frontend | Database |
|------------|---------|---------|---------|
| Local Dev | Docker Compose | `next dev` | Local PostgreSQL |
| PR Preview | — | Vercel Preview | Staging Neon branch |
| Staging | Railway staging service | Vercel Preview | Staging Neon DB |
| Production | Railway production | Vercel Production | Production Neon DB |

---

# 25. Deployment Architecture

## 25.1 Production Architecture Diagram

```mermaid
graph TB
    subgraph "Users"
        U[Browser / Mobile]
    end

    subgraph "Vercel Edge (Free Tier)"
        EDGE[Edge Network]
        NEXT_PROD[Next.js App<br/>Serverless Functions]
    end

    subgraph "Railway (Hobby $5/mo)"
        API_SVC[FastAPI Service<br/>512MB RAM]
        WORKER_SVC[Celery Worker<br/>512MB RAM]
        REDIS_SVC[Redis Service<br/>256MB RAM]
        CHROMA_SVC[ChromaDB Service<br/>256MB RAM]
    end

    subgraph "Neon PostgreSQL (Free Tier)"
        NEON[(PostgreSQL<br/>0.5 GB Storage)]
    end

    subgraph "File Storage"
        LOCAL_FS[Railway Persistent Volume<br/>1GB Free]
    end

    U --> EDGE
    EDGE --> NEXT_PROD
    NEXT_PROD --> API_SVC
    API_SVC --> REDIS_SVC
    API_SVC --> NEON
    API_SVC --> CHROMA_SVC
    API_SVC --> LOCAL_FS
    WORKER_SVC --> REDIS_SVC
    WORKER_SVC --> NEON
    WORKER_SVC --> LOCAL_FS
```

## 25.2 Cost Estimate

| Service | Tier | Monthly Cost |
|---------|------|-------------|
| Vercel | Hobby (Free) | $0 |
| Railway | Hobby | $5 |
| Neon PostgreSQL | Free | $0 |
| Redis (Railway) | Included | $0 |
| ChromaDB (Railway) | Included in Railway | $0 |
| Gemini API | Pay-per-use | ~$20–50/mo (moderate use) |
| Domain | Namecheap | ~$1/mo |
| **Total MVP** | | **~$26–56/mo** |

**Scale-Up Cost Estimate (500 users):**
| Service | Tier | Monthly Cost |
|---------|------|-------------|
| Vercel | Pro | $20 |
| Railway | Pro | $20 |
| Neon | Launch ($19) | $19 |
| Redis | Upstash | $10 |
| ChromaDB | Self-hosted | $0 |
| Gemini API | High volume | ~$200/mo |
| **Total Scale** | | **~$269/mo** |

## 25.3 Local Development Setup

**Prerequisites:** Docker Desktop, Node.js 20, Python 3.12

**Steps:**
```
1. Clone repository
2. cp .env.example .env (fill in GEMINI_API_KEY, DATABASE_URL)
3. docker-compose up -d (starts PostgreSQL, Redis, ChromaDB)
4. cd backend && pip install -r requirements.txt
5. alembic upgrade head (run migrations)
6. uvicorn app.main:app --reload (start API on :8000)
7. cd frontend && npm install
8. npm run dev (start Next.js on :3000)
```

---

# 26. Phase-by-Phase Roadmap

## PHASE 1: Core MVP (Weeks 1–8)

### Objectives
Deliver a working end-to-end flow: Upload CSV → Auto-profile → Run EDA → View Dashboard → Download PDF Report.

### Features Delivered
- User registration, login, JWT auth
- Project creation and management
- CSV and XLSX file upload with validation
- Automated data profiling (column stats, types, nulls)
- Data Cleaning Agent (basic: type coercion, null handling)
- EDA Agent (distributions, correlations)
- Visualization Agent (5 chart types: bar, line, scatter, pie, heatmap)
- Basic dashboard with auto-generated charts
- KPI cards (3 auto-selected metrics)
- Insight Agent (5 insights minimum)
- PDF report generation (basic template)
- User settings (name, email, password change)
- Responsive frontend (desktop + tablet)

### Deliverables
- Working web application deployed on Vercel + Railway
- Database schema fully migrated
- All Phase 1 APIs implemented and documented
- 80% unit test coverage on Phase 1 code
- Basic README with setup instructions

### Tasks

**Backend:**
- [ ] Project scaffolding (FastAPI, folder structure, Docker)
- [ ] Database schema + Alembic migrations
- [ ] Auth endpoints (register, login, refresh, logout)
- [ ] File upload endpoint + validation
- [ ] CSV/XLSX parser service
- [ ] Data profiler service
- [ ] Data Cleaning Agent
- [ ] EDA Agent
- [ ] Visualization Agent (5 chart types)
- [ ] Insight Agent (basic)
- [ ] PDF Report Generator (basic)
- [ ] Celery setup (file processing tasks)
- [ ] WebSocket for progress events
- [ ] Redis caching for analysis results

**Frontend:**
- [ ] Next.js 15 scaffolding + ShadCN setup
- [ ] Auth pages (login, register)
- [ ] Dashboard layout (sidebar, topbar)
- [ ] File upload page with drag-and-drop
- [ ] Dataset profile page
- [ ] Dashboard page (charts grid + KPI cards)
- [ ] Analysis status page with progress bar
- [ ] PDF download button
- [ ] Settings page

### Acceptance Criteria
- [ ] User can register, log in, and access dashboard
- [ ] CSV upload completes in < 30 seconds for files < 50MB
- [ ] Data profile appears within 2 minutes of upload
- [ ] EDA analysis completes within 3 minutes for 10MB CSV
- [ ] Dashboard shows minimum 5 charts and 3 KPI cards
- [ ] PDF report downloads successfully and contains all sections
- [ ] All Phase 1 endpoints return correct HTTP status codes
- [ ] Unit test suite passes with > 80% coverage

### Risks
| Risk | Probability | Mitigation |
|------|------------|-----------|
| Gemini API quota limits | Medium | Implement rate limiting + queuing |
| Large file parsing memory | Medium | Chunked processing implemented |
| PDF rendering issues | Low | Test with ReportLab early |

---

## PHASE 2: Advanced Analytics (Weeks 9–14)

### Objectives
Add forecasting, anomaly detection, chat with data, and advanced EDA features.

### Features Delivered
- Forecasting Agent (Prophet, XGBoost, Linear Regression)
- Anomaly Detection (IQR, Z-Score, Isolation Forest)
- Segmentation Engine (K-Means)
- Correlation Analysis (Pearson + Spearman + heatmap)
- Chat With Data (RAG pipeline, ChromaDB, Gemini)
- PPTX Report Generation
- Advanced chart types: histogram, box plot, area chart
- Forecast chart with confidence intervals
- Dataset management (rename, delete, re-upload)

### Acceptance Criteria
- [ ] Forecast completes within 5 minutes for 1-year daily data
- [ ] Chat answers relevant to dataset within 5 seconds
- [ ] Chat maintains context across 20 turns
- [ ] Anomalies detected and highlighted in dataset view
- [ ] PPTX report downloads with all charts embedded
- [ ] Segmentation produces 2–10 clusters with AI descriptions

---

## PHASE 3: Multi-Agent System (Weeks 15–22)

### Objectives
Deploy the full LangGraph multi-agent orchestration. Connect PostgreSQL, MySQL, SQLite databases. Enable SQL natural language queries.

### Features Delivered
- LangGraph workflow engine (full state machine)
- All 10 core agents deployed (Agents 1–10)
- SQL Agent with database connections (PostgreSQL, MySQL, SQLite)
- Executive Consultant Agent
- Report Agent (PDF + PPTX with full template)
- Agent progress tracking (real-time via WebSocket)
- Agent retry + error recovery
- Agent log viewer in admin panel
- RBAC full implementation (Admin, Analyst, Viewer)
- Audit logs
- Notification system
- RFM Analysis, Cohort Analysis, Market Basket Analysis
- Power BI integration (basic export)

### Acceptance Criteria
- [ ] Full LangGraph analysis workflow completes without manual intervention
- [ ] SQL Agent generates correct SQL for 90%+ of test questions
- [ ] SQL Agent NEVER executes destructive queries
- [ ] RBAC enforced on all endpoints (verified by penetration test)
- [ ] Audit log records all agent actions
- [ ] All 11 agents pass agent test suite
- [ ] LangGraph retries on transient failures (verified by test)

---

## PHASE 4: Computer Operator Agent (Weeks 23–30)

### Objectives
Deploy the COA with the full approval system. Local desktop agent. Audit trails.

### Features Delivered
- COA Planning Agent (Gemini 2.5 Pro)
- Approval Dialog UI (blocking modal)
- Permission scope management (Once, Session, Always, Deny)
- COA Admin panel (pending approvals, history, revoke)
- Local Python agent for desktop automation
- WebSocket-based COA ↔ backend communication
- Auto-deny on timeout
- Rollback system
- Full COA audit log
- COA Action History viewer

### Acceptance Criteria
- [ ] NO COA action executes without explicit user approval
- [ ] Auto-deny fires at exactly 5 minutes
- [ ] Approval dialog shows all required fields
- [ ] Permission scopes persist correctly (session, always)
- [ ] Admin can view and revoke all permissions
- [ ] Rollback executed within 5 minutes of action
- [ ] Local agent communicates securely with backend
- [ ] Full audit trail persists for 90 days

---

## PHASE 5: Enterprise Features (Weeks 31–40)

### Objectives
Multi-tenancy, SSO, advanced sharing, white-label, API access.

### Features Delivered
- Multi-tenant organization model
- SSO (Google OAuth, Microsoft SAML)
- Public dashboard sharing with token
- Embedded dashboard widget (iframe)
- REST API access with API keys
- Webhook system (analysis complete, alert triggers)
- Custom branding (logo, colors per organization)
- Data retention policies
- Export to Google Sheets
- Scheduled report delivery (email)
- Advanced billing and subscription management
- Usage analytics dashboard (for admins)

---

# 27. Cursor Development Rules

## 27.1 Cursor Agent Instructions

> **READ THIS FIRST:** This document (`AI_BIOS_MASTER.md`) is the SINGLE SOURCE OF TRUTH. When implementing any feature, always verify it against this document. If something is not in this document, ask before building. Do not make architectural decisions not specified here.

## 27.2 Coding Standards

### Python (Backend)
- Python version: **3.12 strictly**
- Formatter: **ruff** (replaces black + isort + flake8)
- Type hints: **required on all function signatures**
- Docstrings: **Google style** on all public functions and classes
- Import order: stdlib → third-party → local
- Max line length: 100 characters
- No `print()` statements — use `logging` module exclusively
- No mutable default arguments in function signatures
- All database queries through repository layer only (no raw queries in routes/services)

### TypeScript (Frontend)
- TypeScript strict mode: **enabled** (`"strict": true` in tsconfig.json)
- No `any` type unless absolutely unavoidable (comment justification required)
- All API calls through the centralized `lib/api-client.ts`
- All state via Zustand stores (no prop drilling beyond 2 levels)
- Components: functional only (no class components)
- Props: always define interface, never inline type
- File naming: `PascalCase.tsx` for components, `camelCase.ts` for utilities
- No direct `localStorage` access — use store wrappers

## 27.3 Architecture Rules

1. **Never mix concerns:** Routes call Services. Services call Repositories. Repositories call Database. Agents are called by Services only.
2. **No business logic in routes:** Routes validate input, call service, return response.
3. **No database calls outside repositories:** Repositories are the only layer that imports SQLAlchemy models.
4. **No Gemini calls outside agents:** All AI model calls happen inside agent classes only.
5. **No secrets in code:** All credentials from environment variables via `app/config.py`.
6. **All file paths relative to project root:** Never hardcode absolute paths.
7. **COA actions MUST go through ApprovalManager:** Never execute desktop actions directly.

## 27.4 Folder Rules

- New features: create new module in appropriate folder, never add to existing overcrowded file
- Agent files: one file per agent in `backend/app/agents/`
- New DB model: create in `backend/app/models/`, add migration immediately
- New API endpoint: add to appropriate router in `backend/app/api/v1/`
- New Pydantic schema: add to `backend/app/schemas/`
- New React component: add to most specific subfolder in `frontend/components/`
- New hook: add to `frontend/hooks/`
- New store: add to `frontend/stores/`

## 27.5 Naming Conventions

| Entity | Convention | Example |
|--------|-----------|---------|
| Python classes | PascalCase | `DataCleaningAgent` |
| Python functions | snake_case | `run_eda_analysis()` |
| Python files | snake_case | `data_cleaning_agent.py` |
| React components | PascalCase | `ApprovalDialog.tsx` |
| React hooks | camelCase + `use` prefix | `useApproval.ts` |
| TypeScript interfaces | PascalCase + `I` prefix (optional) or descriptive | `DatasetProfile`, `IAnalysisResult` |
| API endpoints | lowercase, hyphens | `/api/v1/chat-sessions` |
| DB table names | snake_case, plural | `chat_sessions` |
| DB column names | snake_case | `created_at`, `user_id` |
| Env variables | SCREAMING_SNAKE_CASE | `GEMINI_API_KEY` |
| Celery tasks | snake_case in module | `run_analysis_task` |

## 27.6 Security Requirements (Non-Negotiable)

1. Every new endpoint must have authentication dependency unless explicitly marked `public`
2. Every new endpoint must have RBAC check via `rbac.check_permission()`
3. All file uploads must pass through the file validator before any processing
4. All SQL passed to database must go through parameterized query builder
5. COA actions must include approval token in request
6. All user inputs sanitized before inclusion in Gemini prompts
7. Passwords hashed with bcrypt (min 12 rounds), never stored plain

## 27.7 Testing Requirements

1. Every new service function must have at least one unit test
2. Every new API endpoint must have at least one integration test
3. Every agent must have a happy-path test and a failure-path test
4. Tests must not call real Gemini API — mock with `unittest.mock.patch`
5. Tests must not use production database — use pytest fixtures with test DB
6. Test file names: `test_{module_name}.py`
7. Minimum test coverage enforced in CI (see Section 23.2)

## 27.8 Phase Gating

Cursor must implement features strictly in phase order:

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5
```

Do not begin Phase 2 features until Phase 1 acceptance criteria are met. Cross-phase code that belongs to a future phase should be stubbed with `raise NotImplementedError("Phase N feature")`.

## 27.9 Commit Message Format

```
type(scope): short description

Types: feat, fix, refactor, test, docs, chore, security
Scopes: auth, datasets, analysis, agents, coa, frontend, db, ci

Examples:
feat(agents): add EDA Agent with correlation analysis
fix(auth): resolve refresh token rotation race condition
test(coa): add COA approval flow integration tests
security(sql): enforce read-only transactions in SQL Agent
```

---

# 28. Final Completion Checklist

Use this checklist to verify completeness after each phase and before production release.

## 28.1 Phase 1 Checklist

### Infrastructure
- [ ] Docker Compose runs all services locally without errors
- [ ] Backend starts and `/health` returns 200
- [ ] Frontend builds without TypeScript errors
- [ ] All environment variables documented in `.env.example`
- [ ] Alembic migrations run cleanly on fresh database
- [ ] CI/CD pipeline runs without failures

### Authentication
- [ ] `POST /api/v1/auth/register` creates user with hashed password
- [ ] `POST /api/v1/auth/login` returns access + refresh tokens
- [ ] `POST /api/v1/auth/refresh` issues new access token
- [ ] `POST /api/v1/auth/logout` invalidates refresh token
- [ ] Protected endpoints return 401 without token
- [ ] RBAC returns 403 for insufficient role

### File Management
- [ ] CSV upload validates file extension and MIME type
- [ ] XLSX upload with multiple sheets returns sheet list
- [ ] Files > 500MB rejected with 413 error
- [ ] Files stored with UUID names, not original names
- [ ] Upload progress communicated via WebSocket
- [ ] Profile generated within 2 minutes

### Data Analysis
- [ ] Data Cleaning Agent handles: nulls, type mismatches, duplicates
- [ ] EDA Agent produces: distributions, correlations, descriptive stats
- [ ] Visualization Agent generates: bar, line, scatter, pie, heatmap
- [ ] Insight Agent produces minimum 5 insights per dataset
- [ ] Analysis results persisted to PostgreSQL
- [ ] Analysis results cached in Redis

### Reporting
- [ ] PDF report generates successfully for all Phase 1 data types
- [ ] PDF contains: cover, summary, overview, insights, charts, recommendations
- [ ] PDF download works from frontend
- [ ] Report generation completes within 5 minutes

### Frontend
- [ ] Login page functional with error handling
- [ ] Register page with validation
- [ ] Dashboard layout with sidebar navigation
- [ ] File upload page with drag-and-drop and progress
- [ ] Dataset profile page with column stats
- [ ] Dashboard page renders charts and KPI cards
- [ ] Analysis status page with real-time progress
- [ ] Responsive on desktop and tablet (768px+)

## 28.2 Phase 2 Checklist

### Forecasting
- [ ] Prophet model trains and forecasts for daily time series
- [ ] XGBoost model trains and forecasts with features
- [ ] Linear regression forecasts for simple trends
- [ ] Auto model selection applies correct decision rules
- [ ] Forecast chart shows confidence intervals
- [ ] Evaluation metrics (MAPE, MAE, RMSE) calculated and displayed
- [ ] Forecast results exportable as CSV
- [ ] Forecast explanation generated in plain English

### Chat With Data
- [ ] ChromaDB collection created on dataset upload
- [ ] Embeddings generated for statistical summaries + row samples
- [ ] Chat session created per dataset
- [ ] Questions answered with relevant source citations
- [ ] Context maintained across 20 turns
- [ ] Context summarized beyond 20 turns
- [ ] Chart generated from chart-request questions
- [ ] SQL queries routed to SQL Agent correctly
- [ ] Messages rated thumbs up/down

### Advanced Analytics
- [ ] Anomaly detection: IQR + Z-Score + Isolation Forest
- [ ] Anomalies highlighted in dataset view
- [ ] K-Means segmentation with auto cluster count
- [ ] Segment AI descriptions generated
- [ ] Cohort retention matrix calculated
- [ ] PPTX report generates with all charts embedded
- [ ] PPTX downloads successfully

## 28.3 Phase 3 Checklist

### LangGraph
- [ ] Analysis workflow graph runs all agents in sequence
- [ ] State passed correctly between agents
- [ ] Retry logic fires on transient AI errors
- [ ] Partial failures degrade gracefully (warn, don't fail)
- [ ] Workflow progress reported via WebSocket in real-time
- [ ] Error recovery returns meaningful user-facing message

### SQL Integration
- [ ] PostgreSQL connection established and tested
- [ ] MySQL connection established and tested
- [ ] SQLite connection established and tested
- [ ] Credentials encrypted before storage
- [ ] Read-only transactions enforced
- [ ] Forbidden keywords hard-rejected before execution
- [ ] Natural language → SQL accuracy > 90% on test set
- [ ] Query results returned as DataFrame
- [ ] Query explanation generated

### RBAC & Admin
- [ ] Admin can create/edit/delete users
- [ ] Admin can assign roles
- [ ] Analyst cannot access admin endpoints (403 verified)
- [ ] Viewer cannot run analyses (403 verified)
- [ ] Audit log records all CRUD operations
- [ ] Audit log records all agent actions
- [ ] Audit log UI in admin panel shows 90 days

## 28.4 Phase 4 Checklist

### Computer Operator Agent
- [ ] NO action executes without approval token
- [ ] Approval dialog shows all required fields (agent, action, reason, target, outcome)
- [ ] Approval dialog is blocking (no background interaction)
- [ ] Risk level displayed with color coding
- [ ] Allow Once: action fires once, approval not saved
- [ ] Allow For Session: approval persists until tab close
- [ ] Always Allow: approval saved to database
- [ ] Deny: action not executed, denial logged
- [ ] Auto-deny fires at exactly 5 minutes
- [ ] Countdown timer displayed in dialog
- [ ] Admin can view all pending approvals
- [ ] Admin can view full approval history
- [ ] Admin can revoke Always Allow permissions
- [ ] Rollback available within 5 minutes of execution
- [ ] Rollback result logged in audit trail
- [ ] Local agent communicates over authenticated WebSocket
- [ ] Local agent validates approval token before execution

## 28.5 Phase 5 Checklist

### Enterprise Features
- [ ] Organization model supports multiple teams under one org
- [ ] Google OAuth login functional
- [ ] Public dashboard share link works without login
- [ ] Embedded dashboard iframe renders correctly
- [ ] REST API access with API keys functional
- [ ] Webhook fires on analysis complete event
- [ ] Scheduled PDF report delivery via email
- [ ] Custom branding (logo, primary color) per organization
- [ ] Usage analytics dashboard shows requests, analyses, users

## 28.6 Security Checklist (Pre-Production)

- [ ] All secrets in environment variables (grep codebase for hardcoded secrets)
- [ ] CORS configured to production domain only
- [ ] TLS 1.3 enforced (verify with SSL Labs)
- [ ] SQL injection tests pass (all 50 test cases)
- [ ] XSS tests pass on all input fields
- [ ] CSRF protection on state-changing endpoints
- [ ] File upload: MIME type bypass test passes
- [ ] Auth: brute force lockout after 10 failed attempts
- [ ] JWT: expired tokens rejected
- [ ] JWT: tampered tokens rejected
- [ ] RBAC: all role boundaries tested
- [ ] COA: impossible to execute without approval token (unit test)
- [ ] `pip-audit` passes with 0 known vulnerabilities
- [ ] `npm audit` passes with 0 critical vulnerabilities
- [ ] Bandit scan: 0 high severity findings

## 28.7 Performance Checklist (Pre-Production)

- [ ] API p95 response time < 500ms (load test)
- [ ] CSV parse (10MB) < 30 seconds
- [ ] Full EDA analysis (10MB CSV) < 3 minutes
- [ ] PDF report generation < 5 minutes
- [ ] Chat response (simple) < 5 seconds
- [ ] Forecast (1-year daily) < 5 minutes
- [ ] Dashboard page load < 2 seconds
- [ ] Redis cache hit rate > 70% for analysis results
- [ ] No memory leaks in Celery workers (monitor for 24h)
- [ ] Database connection pool < 80% utilization under load

## 28.8 Documentation Checklist

- [ ] README.md with full local setup instructions
- [ ] API documentation available at `/docs` (Swagger UI)
- [ ] All environment variables documented in `.env.example`
- [ ] Agent architecture documented with diagrams
- [ ] COA approval system documented for end users
- [ ] Deployment guide for Railway + Vercel
- [ ] Database migration guide
- [ ] Contributing guidelines (`CONTRIBUTING.md`)



---

# 29. Detailed API Schema Reference

## 29.1 Projects API

### Create Project
```
POST /api/v1/projects
Authorization: Bearer <token>

Request Body:
{
  "name": string          // required, min 2, max 100 chars
  "description": string   // optional, max 500 chars
  "settings": {
    "timezone": string    // optional, e.g. "Asia/Kolkata"
    "currency": string    // optional, e.g. "USD", "INR"
    "industry": string    // optional, e.g. "retail", "fintech", "healthcare"
  }
}

Response 201:
{
  "id": uuid,
  "name": string,
  "description": string,
  "owner_id": uuid,
  "status": "active",
  "settings": {...},
  "member_count": 1,
  "dataset_count": 0,
  "created_at": ISO8601,
  "updated_at": ISO8601
}
```

### List Projects
```
GET /api/v1/projects?cursor=<base64>&limit=20&sort=updated_desc

Response 200:
{
  "items": [
    {
      "id": uuid,
      "name": string,
      "description": string,
      "status": string,
      "dataset_count": integer,
      "last_activity": ISO8601,
      "role": "owner|analyst|viewer",
      "created_at": ISO8601
    }
  ],
  "pagination": {
    "has_next": boolean,
    "next_cursor": string | null,
    "limit": integer
  }
}
```

### Update Project
```
PATCH /api/v1/projects/{project_id}

Request Body (all optional):
{
  "name": string,
  "description": string,
  "settings": {...}
}
```

### Add Project Member
```
POST /api/v1/projects/{project_id}/members

Request Body:
{
  "email": string,         // existing user email
  "role": "analyst|viewer"
}

Response 201:
{
  "user_id": uuid,
  "email": string,
  "full_name": string,
  "role": string,
  "joined_at": ISO8601
}
```

## 29.2 Dashboard API

### Create Dashboard
```
POST /api/v1/projects/{project_id}/dashboards

Request Body:
{
  "name": string,
  "layout": {
    "columns": 12,
    "row_height": 80
  },
  "widgets": [
    {
      "id": string,
      "type": "kpi_card|chart|insight_panel|data_table|text",
      "position": { "x": 0, "y": 0, "w": 4, "h": 2 },
      "config": {
        // type-specific config
      }
    }
  ]
}
```

### Generate Auto-Dashboard from Analysis
```
POST /api/v1/analyses/{analysis_id}/generate-dashboard

Response 201:
{
  "dashboard_id": uuid,
  "dashboard_url": string,
  "widget_count": integer
}
```

### Share Dashboard (Generate Public Link)
```
POST /api/v1/dashboards/{dashboard_id}/share

Request Body:
{
  "expires_in_days": integer | null  // null = no expiry
}

Response 200:
{
  "share_url": "https://aibios.app/shared/<token>",
  "share_token": string,
  "expires_at": ISO8601 | null
}
```

## 29.3 Admin API

### List All Users
```
GET /api/v1/admin/users?page=1&limit=20&role=analyst&search=john

Response 200:
{
  "items": [
    {
      "id": uuid,
      "email": string,
      "full_name": string,
      "role": string,
      "is_active": boolean,
      "subscription_tier": string,
      "last_login": ISO8601,
      "created_at": ISO8601
    }
  ],
  "total": integer,
  "pagination": {...}
}
```

### Update User Role
```
PATCH /api/v1/admin/users/{user_id}

Request Body:
{
  "role": "admin|analyst|viewer",
  "is_active": boolean,
  "subscription_tier": "free|analyst|team|enterprise"
}
```

### Get Audit Logs
```
GET /api/v1/admin/audit-logs
  ?user_id=<uuid>
  &action=<string>
  &resource_type=<string>
  &from=<ISO8601>
  &to=<ISO8601>
  &severity=info|warn|error
  &cursor=<base64>
  &limit=50

Response 200:
{
  "items": [
    {
      "id": uuid,
      "user_id": uuid,
      "user_email": string,
      "action": string,
      "resource_type": string,
      "resource_id": uuid,
      "ip_address": string,
      "severity": string,
      "metadata": {...},
      "created_at": ISO8601
    }
  ],
  "pagination": {...}
}
```

### System Stats (Admin Dashboard)
```
GET /api/v1/admin/stats

Response 200:
{
  "total_users": integer,
  "active_users_30d": integer,
  "total_projects": integer,
  "total_datasets": integer,
  "total_analyses": integer,
  "total_reports_generated": integer,
  "total_chat_messages": integer,
  "storage_used_bytes": integer,
  "gemini_tokens_used_30d": integer,
  "pending_coa_approvals": integer,
  "failed_analyses_7d": integer
}
```

## 29.4 Notification API

```
GET /api/v1/notifications?unread_only=true&limit=20

Response 200:
{
  "items": [
    {
      "id": uuid,
      "type": "analysis_complete|analysis_failed|report_ready|coa_pending|system",
      "title": string,
      "body": string,
      "is_read": boolean,
      "metadata": {
        "analysis_id": uuid,     // for analysis notifications
        "report_id": uuid,       // for report notifications
        "coa_action_id": uuid    // for COA notifications
      },
      "created_at": ISO8601
    }
  ],
  "unread_count": integer
}

PATCH /api/v1/notifications/{id}/read
PATCH /api/v1/notifications/read-all
```

---

# 30. Complete Environment Variables Reference

## 30.1 Backend Environment Variables

```bash
# ─── Application ─────────────────────────────────────────────
APP_NAME=AI-BIOS
APP_ENV=development                    # development | staging | production
APP_VERSION=1.0.0
DEBUG=true                             # false in production
SECRET_KEY=<random-64-char-hex>        # used for misc signing
LOG_LEVEL=INFO                         # DEBUG | INFO | WARNING | ERROR

# ─── API Server ──────────────────────────────────────────────
API_HOST=0.0.0.0
API_PORT=8000
API_PREFIX=/api/v1
ALLOWED_ORIGINS=http://localhost:3000  # comma-separated in production
MAX_REQUEST_SIZE_MB=500

# ─── Database ────────────────────────────────────────────────
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/aibios
DATABASE_POOL_SIZE=10
DATABASE_MAX_OVERFLOW=20
DATABASE_POOL_TIMEOUT=30

# ─── Redis ───────────────────────────────────────────────────
REDIS_URL=redis://localhost:6379/0
REDIS_CACHE_TTL=86400                  # 24 hours default

# ─── Authentication ──────────────────────────────────────────
JWT_SECRET_KEY=<random-64-char-hex>
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
PASSWORD_HASH_ROUNDS=12

# ─── AI / Gemini ─────────────────────────────────────────────
GEMINI_API_KEY=<your-gemini-api-key>
GEMINI_PRO_MODEL=gemini-2.5-pro
GEMINI_FLASH_MODEL=gemini-2.5-flash
GEMINI_MAX_RETRIES=3
GEMINI_TIMEOUT_SECONDS=60
GEMINI_MAX_OUTPUT_TOKENS=8192

# ─── ChromaDB ────────────────────────────────────────────────
CHROMA_HOST=localhost
CHROMA_PORT=8001
CHROMA_COLLECTION_PREFIX=aibios_

# ─── Celery ──────────────────────────────────────────────────
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2
CELERY_TASK_SERIALIZER=json
CELERY_RESULT_EXPIRES=86400

# ─── File Storage ────────────────────────────────────────────
STORAGE_BACKEND=local                  # local | s3
STORAGE_LOCAL_PATH=/app/uploads
MAX_UPLOAD_SIZE_MB=500
ALLOWED_UPLOAD_EXTENSIONS=.csv,.xlsx,.xls,.pdf,.pptx

# S3 (if STORAGE_BACKEND=s3)
S3_BUCKET_NAME=aibios-uploads
S3_REGION=ap-south-1
AWS_ACCESS_KEY_ID=<key>
AWS_SECRET_ACCESS_KEY=<secret>

# ─── Email (Notifications) ───────────────────────────────────
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=noreply@aibios.app
SMTP_PASSWORD=<smtp-password>
EMAIL_FROM_NAME=AI-BIOS
EMAIL_FROM_ADDRESS=noreply@aibios.app

# ─── Encryption (for DB credentials) ────────────────────────
ENCRYPTION_KEY=<fernet-key-32-bytes-base64>

# ─── Rate Limiting ───────────────────────────────────────────
RATE_LIMIT_ENABLED=true
RATE_LIMIT_STORAGE_URL=redis://localhost:6379/3

# ─── COA ─────────────────────────────────────────────────────
COA_APPROVAL_TIMEOUT_SECONDS=300       # 5 minutes
COA_LOCAL_AGENT_WS_SECRET=<hmac-secret>

# ─── Monitoring ──────────────────────────────────────────────
SENTRY_DSN=                            # optional
PROMETHEUS_ENABLED=true
```

## 30.2 Frontend Environment Variables

```bash
# ─── App ─────────────────────────────────────────────────────
NEXT_PUBLIC_APP_NAME=AI-BIOS
NEXT_PUBLIC_APP_URL=http://localhost:3000
NEXT_PUBLIC_API_URL=http://localhost:8000

# ─── WebSocket ───────────────────────────────────────────────
NEXT_PUBLIC_WS_URL=ws://localhost:8000/ws

# ─── Feature Flags ───────────────────────────────────────────
NEXT_PUBLIC_ENABLE_COA=true
NEXT_PUBLIC_ENABLE_POWER_BI=false
NEXT_PUBLIC_ENABLE_SSO=false

# ─── Analytics ───────────────────────────────────────────────
NEXT_PUBLIC_POSTHOG_KEY=                # optional
NEXT_PUBLIC_POSTHOG_HOST=https://app.posthog.com
```

---

# 31. Pydantic Schema Definitions (Complete Reference)

## 31.1 Auth Schemas

```python
# schemas/auth.py

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    full_name: str = Field(min_length=2, max_length=100)

    @validator('password')
    def password_strength(cls, v):
        # Must contain: uppercase, lowercase, digit, special char
        if not re.search(r'[A-Z]', v): raise ValueError('Password needs uppercase')
        if not re.search(r'[a-z]', v): raise ValueError('Password needs lowercase')
        if not re.search(r'\d', v):    raise ValueError('Password needs digit')
        return v

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserPublicSchema

class RefreshRequest(BaseModel):
    refresh_token: str

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirm(BaseModel):
    token: str
    new_password: str = Field(min_length=8, max_length=128)
```

## 31.2 Dataset Schemas

```python
# schemas/dataset.py

class DatasetStatus(str, Enum):
    UPLOADING = "uploading"
    PROCESSING = "processing"
    READY = "ready"
    ERROR = "error"

class ColumnType(str, Enum):
    NUMERIC = "numeric"
    CATEGORICAL = "categorical"
    DATE = "date"
    TEXT = "text"
    BOOLEAN = "boolean"
    UNKNOWN = "unknown"

class ColumnStatistics(BaseModel):
    mean: Optional[float] = None
    std: Optional[float] = None
    min: Optional[float] = None
    max: Optional[float] = None
    p25: Optional[float] = None
    p50: Optional[float] = None
    p75: Optional[float] = None
    skewness: Optional[float] = None
    kurtosis: Optional[float] = None
    top_values: Optional[List[Dict[str, Any]]] = None
    date_min: Optional[str] = None
    date_max: Optional[str] = None
    avg_word_count: Optional[float] = None

class ColumnProfile(BaseModel):
    name: str
    detected_type: ColumnType
    null_count: int
    null_pct: float
    unique_count: int
    sample_values: List[Any]
    statistics: ColumnStatistics
    has_outliers: bool = False
    outlier_count: int = 0

class DatasetProfileResponse(BaseModel):
    dataset_id: UUID
    row_count: int
    column_count: int
    file_size_bytes: int
    quality_score: float = Field(ge=0, le=100)
    columns: List[ColumnProfile]
    warnings: List[str] = []
    profiled_at: datetime

class DBConnectionRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    db_type: Literal["postgresql", "mysql", "sqlite"]
    host: Optional[str] = None
    port: Optional[int] = Field(None, ge=1, le=65535)
    database_name: str
    username: Optional[str] = None
    password: Optional[str] = None
    file_path: Optional[str] = None   # SQLite only

    @root_validator
    def validate_connection_type(cls, values):
        db_type = values.get('db_type')
        if db_type in ('postgresql', 'mysql'):
            if not values.get('host'): raise ValueError('host required')
            if not values.get('username'): raise ValueError('username required')
            if not values.get('password'): raise ValueError('password required')
        elif db_type == 'sqlite':
            if not values.get('file_path'): raise ValueError('file_path required for SQLite')
        return values
```

## 31.3 Analysis Schemas

```python
# schemas/analysis.py

class AnalysisType(str, Enum):
    EDA = "eda"
    CLEANING = "cleaning"
    CORRELATIONS = "correlations"
    ANOMALIES = "anomalies"
    SEGMENTATION = "segmentation"
    RFM = "rfm"
    COHORT = "cohort"
    RETENTION = "retention"
    CHURN = "churn"
    MARKET_BASKET = "market_basket"

class AnalysisStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class EDAConfig(BaseModel):
    depth: Literal["standard", "deep"] = "standard"
    include_narrative: bool = True

class CleaningConfig(BaseModel):
    strategy: Literal["auto", "conservative", "aggressive"] = "auto"
    drop_null_threshold: float = Field(0.5, ge=0, le=1)
    fix_types: bool = True
    remove_duplicates: bool = True

class SegmentationConfig(BaseModel):
    n_clusters: Optional[int] = Field(None, ge=2, le=10)
    features: Optional[List[str]] = None   # columns to use

class RFMConfig(BaseModel):
    date_column: str
    value_column: str
    id_column: str

class AnalysisRunRequest(BaseModel):
    dataset_id: UUID
    analysis_types: List[AnalysisType] = [AnalysisType.EDA]
    config: Dict[str, Any] = {}

class AnalysisStatusResponse(BaseModel):
    analysis_id: UUID
    status: AnalysisStatus
    progress_pct: int = Field(ge=0, le=100)
    current_agent: Optional[str]
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    estimated_completion: Optional[datetime]
    error: Optional[str]

class InsightSchema(BaseModel):
    id: str
    title: str
    description: str
    type: Literal["opportunity", "risk", "anomaly", "trend"]
    confidence: float = Field(ge=0, le=1)
    supporting_data: Dict[str, Any] = {}
    recommended_action: str
    priority: Literal["high", "medium", "low"]

class AnalysisResultResponse(BaseModel):
    analysis_id: UUID
    dataset_id: UUID
    status: AnalysisStatus
    analysis_types: List[str]
    cleaning_report: Optional[Dict[str, Any]]
    eda_report: Optional[Dict[str, Any]]
    insights: Optional[List[InsightSchema]]
    chart_configs: Optional[List[Dict[str, Any]]]
    consultant_memo: Optional[str]
    duration_seconds: Optional[float]
    created_at: datetime
    completed_at: Optional[datetime]
```

## 31.4 COA Schemas

```python
# schemas/coa.py

class COAActionType(str, Enum):
    OPEN_APPLICATION = "open_application"
    OPEN_FILE = "open_file"
    RUN_SCRIPT = "run_script"
    EXECUTE_SQL = "execute_sql"
    EXPORT_TO_EXCEL = "export_to_excel"
    OPEN_URL = "open_url"
    FILL_FORM = "fill_form"
    RUN_WORKFLOW = "run_workflow"

class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ApprovalStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    DENIED = "denied"
    AUTO_DENIED = "auto_denied"
    EXPIRED = "expired"

class ApprovalScope(str, Enum):
    ONCE = "once"
    SESSION = "session"
    ALWAYS = "always"

class COAActionSchema(BaseModel):
    id: UUID
    agent_name: str
    action_type: COAActionType
    target_application: str
    reason: str
    expected_outcome: str
    action_params: Dict[str, Any]
    risk_level: RiskLevel
    approval_status: ApprovalStatus
    rollback_strategy: Optional[str]
    timeout_seconds: int = 300
    created_at: datetime

class COAApproveRequest(BaseModel):
    scope: ApprovalScope

class COARollbackRequest(BaseModel):
    reason: str
```

---

# 32. LangGraph State Machines (Extended)

## 32.1 Full Analysis State Machine

```mermaid
stateDiagram-v2
    [*] --> Initializing
    Initializing --> ValidatingDataset : start
    ValidatingDataset --> DataCleaning : valid
    ValidatingDataset --> Failed : invalid
    
    DataCleaning --> DataCleaning : retry (max 3)
    DataCleaning --> EDAAnalysis : success
    DataCleaning --> EDAAnalysis : partial_success
    DataCleaning --> Failed : fatal_error
    
    EDAAnalysis --> EDAAnalysis : retry (max 3)
    EDAAnalysis --> Visualization : success
    EDAAnalysis --> Failed : fatal_error
    
    Visualization --> InsightGeneration : success
    Visualization --> InsightGeneration : partial (no charts)
    
    InsightGeneration --> ConsultantAnalysis : success
    InsightGeneration --> ConsultantAnalysis : partial
    
    ConsultantAnalysis --> ReportGeneration : report_requested
    ConsultantAnalysis --> Completed : no_report
    
    ReportGeneration --> ReportGeneration : retry (max 2)
    ReportGeneration --> Completed : success
    ReportGeneration --> CompletedWithWarnings : partial
    
    Failed --> [*]
    Completed --> [*]
    CompletedWithWarnings --> [*]
```

## 32.2 Full LangGraph Node Implementations Specification

Each LangGraph node is a Python function with signature:
```python
async def node_name(state: AnalysisState) -> AnalysisState:
    """
    Node description.
    
    Args:
        state: Current analysis state
        
    Returns:
        Updated state with new fields populated
    """
```

### Node: `validate_dataset`
- Fetch dataset record from DB
- Verify file exists in storage
- Verify row_count > 0
- Verify at least 2 columns exist
- Set `state["current_step"] = "validating"`
- On fail: set `state["errors"]` and route to `END`

### Node: `run_data_cleaning`
- Load DataFrame from storage path
- Instantiate `DataCleaningAgent`
- Call `agent.run(state)`
- Save cleaned DataFrame to temporary path
- Update `state["cleaned_dataframe_path"]`
- Update `state["cleaning_report"]`
- Update progress to 20%

### Node: `run_eda`
- Load cleaned DataFrame
- Instantiate `EDAAgent`
- Call `agent.run(state)`
- Update `state["eda_report"]`
- Update `state["chart_specs"]` (raw specs, not yet rendered)
- Update progress to 45%

### Node: `run_visualization`
- Instantiate `VisualizationAgent`
- Process chart specs from EDA report
- Generate Recharts configs
- Optionally render to PNG via matplotlib
- Update `state["chart_configs"]`
- Save chart configs to DB
- Update progress to 60%

### Node: `run_insight_generation`
- Instantiate `InsightAgent`
- Synthesize EDA + cleaning + charts
- Generate 5–10 prioritized insights
- Update `state["insights"]`
- Update progress to 75%

### Node: `run_consultant_analysis`
- Instantiate `ConsultantAgent`
- Generate strategic memo
- Update `state["consultant_memo"]`
- Update progress to 85%

### Node: `generate_report`
- Instantiate `ReportAgent`
- Compile all state data
- Generate PDF via `pdf_generator.py`
- Generate PPTX via `pptx_generator.py`
- Save file paths to DB
- Update `state["report_path"]`
- Update progress to 100%

### Node: `handle_error`
- Log error details
- Update analysis status to `failed`
- Send failure notification to user
- Preserve partial results if available

### Conditional Edges (Router Functions)

```python
def route_after_cleaning(state: AnalysisState) -> str:
    if state.get("errors") and len(state["errors"]) > 3:
        return "handle_error"
    return "run_eda"  # proceed even with partial cleaning

def route_after_consultant(state: AnalysisState) -> str:
    if "report" in state.get("analysis_types", []):
        return "generate_report"
    return END

def route_after_report(state: AnalysisState) -> str:
    if state.get("errors"):
        return "completed_with_warnings"
    return END
```

## 32.3 Chat Workflow State

```python
class ChatState(TypedDict):
    session_id: str
    dataset_id: str
    user_id: str
    
    # Current turn
    user_message: str
    message_intent: str        # classified intent
    
    # Retrieval
    retrieved_chunks: List[Dict]
    retrieved_context: str
    
    # Agent outputs
    sql_result: Optional[DataFrame]
    chart_config: Optional[Dict]
    
    # Response
    response_text: str
    sources: List[Dict]
    
    # History
    conversation_history: List[Dict]
    context_summary: Optional[str]
    turn_count: int
```

### Chat Workflow Nodes

| Node | Input | Output |
|------|-------|--------|
| `classify_intent` | user_message | message_intent |
| `retrieve_context` | user_message + dataset_id | retrieved_chunks |
| `route_to_sql` | classified as SQL | sql_result |
| `route_to_viz` | classified as chart | chart_config |
| `generate_response` | all context | response_text + sources |
| `update_history` | response_text | updated conversation_history |
| `maybe_summarize` | turn_count > 15 | context_summary |

---

# 33. Frontend Component Specifications

## 33.1 FileDropzone Component

**File:** `components/upload/FileDropzone.tsx`

**Behavior:**
- Accepts drag-and-drop OR click-to-browse
- Shows file type icons (CSV, XLSX) and accepted formats
- Validates file type client-side before upload
- Shows upload progress bar (byte-level via XHR)
- Shows error state for invalid files
- Shows success state with file name + size

**Props:**
```typescript
interface FileDropzoneProps {
  projectId: string
  onUploadComplete: (datasetId: string) => void
  onError: (error: string) => void
  maxSizeMB?: number        // default 500
  acceptedTypes?: string[]  // default ['.csv', '.xlsx', '.xls']
  disabled?: boolean
}
```

**States:**
- `idle`: Default drop target
- `dragging`: Highlighted border on drag-over
- `uploading`: Progress bar visible
- `success`: Green checkmark + file details
- `error`: Red border + error message

## 33.2 ApprovalDialog Component

**File:** `components/coa/ApprovalDialog.tsx`

This is the most security-critical frontend component. It must be:
- Rendered as a portal (above all other UI)
- Non-dismissible except by explicit button click
- Countdownable (shows seconds remaining to auto-deny)
- Accessible (keyboard navigable, screen reader labeled)

**Props:**
```typescript
interface ApprovalDialogProps {
  action: COAActionSchema
  onDecision: (decision: ApprovalDecision) => void
}

type ApprovalDecision = {
  action_id: string
  decision: 'allow_once' | 'allow_session' | 'always_allow' | 'deny'
}
```

**Risk Level Visual Indicators:**
| Level | Color | Icon |
|-------|-------|------|
| low | Green (emerald-500) | ✅ |
| medium | Yellow (amber-500) | ⚠️ |
| high | Orange (orange-500) | 🔶 |
| critical | Red (red-600) | 🚨 |

**Countdown Logic:**
- Timer starts at 300 seconds (5 minutes)
- Displayed as `MM:SS` format
- Red warning at < 60 seconds
- Dialog shakes animation at < 30 seconds
- Auto-fires `onDecision({ decision: 'deny' })` at 0

## 33.3 KPI Card Component

**File:** `components/dashboard/KPICard.tsx`

```typescript
interface KPICardProps {
  title: string
  value: number | string
  format: 'number' | 'currency' | 'percentage' | 'duration'
  currency?: string         // default 'USD'
  previousValue?: number
  trend?: 'up' | 'down' | 'neutral'
  sparklineData?: number[]  // last 7 data points
  isLoading?: boolean
}
```

**Formatting Rules:**
- Numbers: 1,234,567 → "1.23M" (K/M/B abbreviation)
- Currency: 12450.50 → "$12.5K" (respects currency symbol)
- Percentage: 0.1234 → "12.3%"
- Duration: 3665 seconds → "1h 1m"

**Trend Indicators:**
- Positive trend: green arrow up ↑ + green percentage
- Negative trend: red arrow down ↓ + red percentage
- Context-aware: for metrics like "churn rate", down = positive (configurable)

## 33.4 ChatWindow Component

**File:** `components/chat/ChatWindow.tsx`

**Architecture:**
```
ChatWindow
  ├── ContextPanel (pinned data sources)
  ├── MessagesContainer
  │   ├── ChatMessage (user)
  │   ├── ChatMessage (assistant)
  │   │   ├── MessageText (markdown-rendered)
  │   │   ├── SourceCitations (expandable)
  │   │   └── InlineChart (if chart_data present)
  │   └── TypingIndicator (streaming)
  └── ChatInput
      ├── TextArea (auto-resize)
      ├── SendButton
      └── ActionBar (clear, export)
```

**Message Streaming:**
- Connect to WebSocket on session open
- Stream tokens character by character
- Markdown rendering updates live during stream
- Auto-scroll to bottom during streaming
- Stop streaming button visible during generation

**Source Citation Display:**
```
[1] Column: revenue | Rows: 142, 289, 301 | Confidence: 94%
[2] Aggregate: SUM(revenue) WHERE region='West' = $2.3M
```
Expandable to show exact cell values.

## 33.5 AgentStatusPanel Component

**File:** `components/agents/AgentStatusPanel.tsx`

Shows real-time agent progress for running analyses.

```
Analysis Running...  ████████████░░░░░░ 60%

✅  Data Cleaning Agent      12.3s
✅  EDA Agent                45.1s
🔄  Visualization Agent      running...
⏳  Insight Agent            pending
⏳  Report Agent             pending
```

- Updates via WebSocket events
- Agent icons indicate status: ✅ complete, 🔄 running, ❌ failed, ⏳ pending
- Clicking a completed agent shows its output summary
- Failed agents show error message + retry button

---

# 34. Celery Task Specifications

## 34.1 Task: `parse_uploaded_file`

```
Queue: high_priority
Timeout: 600 seconds
Max Retries: 3

Input:
  - dataset_id: UUID
  - file_path: str
  - file_type: "csv" | "xlsx"
  - sheet_name: str | None

Steps:
  1. Download file from storage
  2. Parse with pandas (detect encoding for CSV)
  3. For XLSX: validate requested sheet exists
  4. Detect column types per column
  5. Run quick profile (10-second cap)
  6. Save profile to DB
  7. Update dataset status to "ready"
  8. Enqueue generate_embeddings task

On Failure:
  - Update dataset status to "error"
  - Save error message
  - Notify user via WebSocket

Retry Conditions:
  - RetryableError: file temporarily unavailable (3 retries)
  - NON-retryable: malformed file, encoding error
```

## 34.2 Task: `run_analysis_workflow`

```
Queue: compute
Timeout: 1800 seconds (30 minutes)
Max Retries: 1 (LangGraph handles internal retries)

Input:
  - analysis_id: UUID
  - state: Dict (initial AnalysisState)

Steps:
  1. Initialize LangGraph workflow
  2. Run workflow graph to completion
  3. Persist all results to DB
  4. Update analysis status to "completed"
  5. Notify user via WebSocket + notification

On Failure:
  - Update analysis status to "failed"
  - Save error details + partial results
  - Notify user
  - Log to Sentry if production
```

## 34.3 Task: `generate_embeddings`

```
Queue: ai
Timeout: 600 seconds
Max Retries: 3

Input:
  - dataset_id: UUID
  - file_path: str

Steps:
  1. Load DataFrame
  2. Generate column description chunks
  3. Sample 500 random rows, serialize as text chunks
  4. Generate aggregate fact chunks
  5. Call Gemini embeddings API (batch of 100)
  6. Upsert into ChromaDB collection
  7. Update dataset record: embeddings_ready = true

Rate Limiting:
  - Max 100 embedding requests per minute
  - Sleep between batches if needed
```

## 34.4 Task: `generate_pdf_report`

```
Queue: reports
Timeout: 600 seconds
Max Retries: 2

Input:
  - report_id: UUID
  - analysis_id: UUID

Steps:
  1. Fetch analysis results from DB
  2. Download chart PNG images from storage
  3. Initialize ReportLab PDF canvas
  4. Render cover page
  5. Render table of contents
  6. Render executive summary
  7. Render each insight section with charts
  8. Render appendix tables
  9. Save PDF to storage
  10. Update report record with pdf_path
  11. Send ready notification
```

## 34.5 Task: `run_forecast`

```
Queue: compute
Timeout: 900 seconds
Max Retries: 2

Input:
  - forecast_id: UUID
  - dataset_id: UUID
  - target_column: str
  - date_column: str
  - horizon_days: int
  - model_preference: str

Steps:
  1. Load DataFrame
  2. Validate date and target columns
  3. Run model selection logic
  4. Train selected model
  5. Generate forecast
  6. Calculate evaluation metrics on holdout
  7. Generate Recharts config for forecast chart
  8. Save forecast DataFrame as CSV
  9. Update forecast record with results
  10. Notify user
```

## 34.6 Celery Beat Scheduled Tasks

```python
CELERYBEAT_SCHEDULE = {
    # Clean up expired temp files every hour
    "cleanup-temp-files": {
        "task": "tasks.cleanup_temp_files",
        "schedule": crontab(minute=0),   # every hour
    },
    
    # Expire old auto-deny COA pending actions
    "expire-coa-actions": {
        "task": "tasks.expire_pending_coa_actions",
        "schedule": crontab(minute="*/5"),  # every 5 minutes
    },
    
    # Archive old audit logs to cold storage
    "archive-audit-logs": {
        "task": "tasks.archive_old_audit_logs",
        "schedule": crontab(hour=2, minute=0),   # daily at 2am
    },
    
    # Send scheduled reports (Phase 5)
    "send-scheduled-reports": {
        "task": "tasks.send_scheduled_reports",
        "schedule": crontab(minute=0),   # every hour, checks due reports
    },
    
    # Health-check all DB connections
    "health-check-db-connections": {
        "task": "tasks.health_check_db_connections",
        "schedule": crontab(minute="*/15"),  # every 15 minutes
    },
}
```

---

# 35. Database Migration Strategy

## 35.1 Alembic Configuration

```python
# alembic/env.py key configuration
target_metadata = Base.metadata
version_locations = "alembic/versions"
```

All migrations use Alembic with the following conventions:

**Naming:** `<timestamp>_<description>.py`
Example: `20240601_120000_create_users_table.py`

**Migration Safety Rules:**
1. Never drop columns in production without a two-phase migration
2. New NOT NULL columns must have a DEFAULT value
3. Large table operations must use `CONCURRENTLY` index builds
4. All migrations must be reversible (`downgrade()` must restore prior state)
5. Foreign key additions include `ON DELETE` behavior explicitly

## 35.2 Migration Sequence (Phase 1)

```
Migration 001: Create users table
Migration 002: Create projects table
Migration 003: Create project_members table
Migration 004: Create datasets table
Migration 005: Create db_connections table
Migration 006: Create analyses table
Migration 007: Create visualizations table
Migration 008: Create dashboards table
Migration 009: Create reports table
Migration 010: Create chat_sessions table
Migration 011: Create chat_messages table
Migration 012: Create agent_logs table
Migration 013: Create audit_logs table
Migration 014: Create notifications table
Migration 015: Create permissions table
Migration 016: Add indexes (composite indexes from Section 6.2)
Migration 017: Create forecasts table (Phase 2)
Migration 018: Create coa_actions table (Phase 4)
```

## 35.3 Zero-Downtime Migration Protocol

For production deployments involving schema changes:

**Phase A — Backward-compatible changes:**
1. `git push` deploys new code with `alembic upgrade head`
2. New code handles both old and new schema
3. Migration runs with rolling deployment

**Phase B — Breaking changes (e.g., rename column):**
1. Step 1: Add new column with new name (migration)
2. Step 2: Deploy code that writes to BOTH columns
3. Step 3: Backfill new column with data from old column
4. Step 4: Deploy code that reads from new column only
5. Step 5: Drop old column (migration)

---

# 36. WebSocket Event Specification

## 36.1 WebSocket Connection

```
WS URL: ws://<host>/ws?token=<access_token>

Authentication:
  - Token passed as query parameter on connect
  - Server validates JWT on connection
  - Invalid token → close with code 4001

Heartbeat:
  - Server sends {"type": "ping"} every 30 seconds
  - Client must respond {"type": "pong"} within 10 seconds
  - Missed 3 pings → connection closed
```

## 36.2 Server → Client Events

| Event Type | Trigger | Payload |
|-----------|---------|---------|
| `analysis.progress` | Agent completes a step | `{ analysis_id, step, progress_pct, agent_name }` |
| `analysis.completed` | Full workflow done | `{ analysis_id, result_summary }` |
| `analysis.failed` | Workflow error | `{ analysis_id, error }` |
| `dataset.ready` | File parsed successfully | `{ dataset_id, row_count, column_count }` |
| `report.ready` | PDF/PPTX generated | `{ report_id, pdf_url, pptx_url }` |
| `forecast.completed` | Forecast done | `{ forecast_id, model_used, mape }` |
| `coa.approval_required` | COA action pending | `{ action_id, action_type, risk_level, expires_at }` |
| `coa.executed` | Action executed | `{ action_id, result }` |
| `coa.auto_denied` | Timeout expired | `{ action_id }` |
| `chat.token` | Streaming chat token | `{ session_id, message_id, token }` |
| `chat.message_complete` | Full message ready | `{ session_id, message_id, sources }` |
| `notification.new` | New notification | `{ notification_id, type, title }` |

## 36.3 Client → Server Events

| Event Type | Purpose | Payload |
|-----------|---------|---------|
| `ping` | Heartbeat response | `{}` |
| `subscribe.analysis` | Watch analysis | `{ analysis_id }` |
| `subscribe.chat` | Watch chat session | `{ session_id }` |
| `unsubscribe` | Stop watching | `{ resource_type, resource_id }` |

---

# 37. Data Flow Diagrams

## 37.1 CSV Upload → Analysis → Report Complete Flow

```mermaid
flowchart TD
    A[User Selects CSV] --> B[Client Validation\nsize, extension]
    B --> C[POST /datasets/upload\nmultipart/form-data]
    C --> D[FastAPI: Validate + Save to Storage]
    D --> E[DB: dataset status = uploading]
    E --> F[Celery: Enqueue parse_file task]
    F --> G[Return 202: dataset_id to client]
    
    G --> H[WS Event: upload_started]
    
    F --> I[Worker: Parse CSV with pandas]
    I --> J[Detect column types]
    J --> K[Run quick profile]
    K --> L[Save profile to DB]
    L --> M[DB: dataset status = ready]
    M --> N[WS Event: dataset.ready]
    M --> O[Celery: Enqueue generate_embeddings]
    
    N --> P[Client: Show Profile Page]
    
    P --> Q[User Clicks Run Analysis]
    Q --> R[POST /analyses/run]
    R --> S[DB: analysis status = pending]
    S --> T[Celery: Enqueue run_analysis_workflow]
    T --> U[Return 202: analysis_id]
    
    T --> V[Worker: Initialize LangGraph]
    V --> W[Data Cleaning Agent]
    W --> X[WS: analysis.progress 20%]
    X --> Y[EDA Agent]
    Y --> Z[WS: analysis.progress 45%]
    Z --> AA[Visualization Agent]
    AA --> BB[WS: analysis.progress 60%]
    BB --> CC[Insight Agent]
    CC --> DD[WS: analysis.progress 80%]
    DD --> EE[Consultant Agent]
    EE --> FF[Report Agent]
    FF --> GG[WS: analysis.completed]
    GG --> HH[Client: Show Dashboard + Download Links]
```

## 37.2 RAG Chat Query Flow

```mermaid
flowchart LR
    A[User Types Question] --> B[POST /chat/sessions/id/messages]
    B --> C[FastAPI: Save user message]
    C --> D[Enqueue chat processing]
    
    D --> E[Classify Intent\nGemini Flash]
    E --> F{Intent Type?}
    
    F -->|SQL Query| G[SQL Agent\nGenerate + Execute SQL]
    F -->|Chart Request| H[Visualization Agent\nGenerate Chart Config]
    F -->|Statistical Q| I[RAG Retrieval\nChromaDB Top-10]
    F -->|General BI| J[Insight Agent\nLookup cached results]
    
    I --> K[Rerank Results]
    K --> L[Build Context String]
    G --> L
    H --> L
    J --> L
    
    L --> M[Load Chat History\nlast 5 + summary]
    M --> N[Build Final Prompt]
    N --> O[Gemini 2.5 Pro\nStream response]
    
    O --> P[WS: Stream tokens]
    P --> Q[Client: Render live text]
    O --> R[WS: message_complete + sources]
    R --> S[Save message to DB]
    S --> T[Update turn count]
    T --> U{turn_count > 15?}
    U -->|Yes| V[Summarize old history\nGemini Flash]
    U -->|No| W[Done]
    V --> W
```

---

# 38. Reporting Engine — Extended Specification

## 38.1 ReportLab PDF Generator Specification

**File:** `backend/app/reporting/pdf_generator.py`

### Page Setup
```python
PAGE_CONFIG = {
    "pagesize": A4,
    "leftMargin": 25 * mm,
    "rightMargin": 25 * mm,
    "topMargin": 20 * mm,
    "bottomMargin": 20 * mm,
    "allowSplitting": 1,
}
```

### Style Definitions
```python
STYLES = {
    "h1": ParagraphStyle(
        name='Heading1',
        fontSize=24,
        textColor=HexColor('#1E293B'),
        spaceAfter=12,
        fontName='Helvetica-Bold'
    ),
    "h2": ParagraphStyle(
        name='Heading2',
        fontSize=16,
        textColor=HexColor('#334155'),
        spaceAfter=8,
    ),
    "body": ParagraphStyle(
        name='Body',
        fontSize=10,
        leading=14,
        textColor=HexColor('#475569'),
    ),
    "caption": ParagraphStyle(
        name='Caption',
        fontSize=8,
        textColor=HexColor('#94A3B8'),
        alignment=TA_CENTER,
    ),
    "insight_high": ParagraphStyle(
        name='InsightHigh',
        backColor=HexColor('#FEF3C7'),
        borderColor=HexColor('#F59E0B'),
        borderWidth=1,
    ),
}
```

### Chart Embedding Strategy
Charts from the Visualization Agent are saved as PNG files at 300 DPI using matplotlib.
Each chart embedded in the PDF is:
- Max width: page_width - margins = 165mm
- Max height: 80mm per chart
- Caption below chart in `caption` style
- Source attribution: "Generated by AI-BIOS Visualization Agent"

### Table Rendering
All data tables use ReportLab `Table` with:
- Alternating row shading: #F8FAFC / #FFFFFF
- Header row: background #1E293B, text white
- Borders: 0.5pt light grey
- Column auto-width based on content
- Max 10 columns before horizontal overflow warning

## 38.2 python-pptx Slide Generator Specification

**File:** `backend/app/reporting/pptx_generator.py`

### Master Template Specification
```python
PPTX_CONFIG = {
    "slide_width": Inches(13.33),
    "slide_height": Inches(7.5),
    "background_color": RGBColor(0xF8, 0xFA, 0xFC),   # near-white
    "accent_color": RGBColor(0x37, 0x63, 0xAD),         # professional blue
    "text_dark": RGBColor(0x1E, 0x29, 0x3B),
    "text_light": RGBColor(0x64, 0x74, 0x8B),
    "title_font": "Calibri",
    "body_font": "Calibri",
}
```

### Slide Layout Templates

**Title Slide:**
- Full-width header band in accent_color
- Dataset name in white H1
- Date + "Prepared by AI-BIOS" in white H3
- Logo bottom-right

**Content Slide:**
- Thin accent bar at top (8pt height)
- Slide title left-aligned, H2 dark
- Content area: flexible (text, chart, or table)
- Slide number bottom-right, accent color
- "AI-BIOS" watermark bottom-left, 6pt

**Chart Slide:**
- Title top
- Full-width chart image (embedded PNG)
- AI-generated insight caption below chart in italic

**Insight Slide:**
- Title top
- Three-column layout: Insight | Evidence | Recommendation
- Color-coded by priority: red/amber/green border

---

# 39. Forecasting Engine — Extended Implementation

## 39.1 Prophet Implementation Details

```python
class ProphetEngine:
    """
    Prophet-based time series forecasting.
    Handles: trend, seasonality, holidays, changepoints.
    """
    
    def prepare_dataframe(self, df: pd.DataFrame, date_col: str, target_col: str) -> pd.DataFrame:
        """
        Rename columns to Prophet's expected 'ds' and 'y'.
        Handle timezone: convert all datetimes to UTC naive.
        Handle zero/negative values for multiplicative mode.
        """
    
    def detect_seasonality(self, df: pd.DataFrame) -> Dict:
        """
        Use FFT to detect dominant periodicities.
        Return: { 'weekly': bool, 'yearly': bool, 'daily': bool }
        """
    
    def fit(self, train_df: pd.DataFrame, config: ProphetConfig) -> Prophet:
        """
        Fit Prophet model with config.
        Apply Indian or US holidays if locale detected.
        """
    
    def predict(self, model: Prophet, horizon: int, freq: str) -> pd.DataFrame:
        """
        Generate future dates + forecast.
        Return DataFrame with: ds, yhat, yhat_lower, yhat_upper,
          trend, trend_lower, trend_upper, weekly, yearly.
        """
    
    def evaluate(self, model: Prophet, test_df: pd.DataFrame) -> Dict:
        """
        Compute MAPE, MAE, RMSE on test set.
        Also compute coverage of prediction intervals.
        """
    
    def to_recharts(self, forecast_df: pd.DataFrame, actual_df: pd.DataFrame) -> Dict:
        """
        Convert forecast DataFrame to Recharts line chart config.
        Series: actual (solid), forecast (dashed), CI band (area).
        """
```

## 39.2 XGBoost Time Series Implementation

```python
class XGBoostTimeSeriesEngine:
    """
    XGBoost for multi-variate time series.
    Uses lag features + rolling statistics + date features.
    """
    
    def engineer_features(self, df: pd.DataFrame, target_col: str, date_col: str) -> pd.DataFrame:
        """
        Create features:
        - Lag features: t-1, t-3, t-7, t-14, t-28
        - Rolling mean/std: window 7, 14, 28
        - EWM: alpha 0.3
        - Day of week (0-6)
        - Day of month (1-31)
        - Month (1-12)
        - Quarter (1-4)
        - Is weekend (0/1)
        - Is month start/end (0/1)
        - Days since epoch (trend proxy)
        Remove rows with NaN from lag creation.
        """
    
    def walk_forward_predict(
        self, 
        model: XGBRegressor, 
        last_known: pd.DataFrame, 
        horizon: int
    ) -> pd.DataFrame:
        """
        Iterative walk-forward prediction.
        Each future step uses predictions from prior steps as lag features.
        Bootstrap resampling (100 iterations) for confidence intervals.
        """
```

## 39.3 Forecast Quality Assurance

Before returning any forecast to the user, the engine runs these checks:

| Check | Condition | Action |
|-------|-----------|--------|
| MAPE sanity | MAPE > 50% | Add warning: "Low confidence forecast" |
| Negative forecast | yhat < 0 for non-negative metric | Clip to 0 with warning |
| Flat forecast | All yhat values identical | Raise error: "Insufficient variance for forecasting" |
| Exploding forecast | Any yhat > 10× max historical | Cap at 3× max with warning |
| Missing CI | yhat_lower == yhat_upper | Widen CI using ±2 * RMSE |

---

# 40. Agent Prompts Reference

## 40.1 System Prompt Design Principles

All agent system prompts follow these rules:
1. **Role declaration first:** "You are a [role] agent in the AI-BIOS system."
2. **Capability scope:** Explicitly state what the agent CAN and CANNOT do.
3. **Output format:** Always specify exact JSON schema expected.
4. **Error behavior:** Instruct model to return partial results, not empty responses.
5. **No hallucination:** "Only report facts present in the provided data. Do not invent statistics."

## 40.2 EDA Agent System Prompt

```
You are the EDA Agent in the AI-BIOS Business Intelligence platform.

Your role: Analyze a dataset's statistical properties and produce a structured 
EDA report with both quantitative findings and a human-readable narrative.

You have access to the following pre-computed statistics:
{eda_statistics_json}

Instructions:
1. Identify the 3 most important statistical findings across all columns.
2. Identify any columns that may require special attention (high nulls, 
   unusual distributions, potential data quality issues).
3. Describe the overall data quality in one paragraph.
4. For each numeric column, describe its distribution characteristics.
5. Identify the most strongly correlated column pairs.
6. Suggest the top 3 most useful analyses to perform next on this data.

CRITICAL RULES:
- Only reference statistics present in the provided JSON. Do not invent values.
- All numeric values must be taken verbatim from the statistics JSON.
- Format your narrative to be readable by a non-technical business user.
- Do not use statistical jargon without explanation.

Output your response as valid JSON matching this exact schema:
{narrative_schema_json}
```

## 40.3 Insight Agent System Prompt

```
You are the Insight Agent in the AI-BIOS Business Intelligence platform.

Your role: Synthesize findings from multiple analysis agents into actionable 
business insights. You think like a senior data scientist who also understands 
business strategy.

Context provided:
- Dataset profile: {profile_summary}
- EDA findings: {eda_summary}
- Anomalies detected: {anomaly_summary}
- Correlation findings: {correlation_highlights}
- Industry context: {industry_hint}

Generate exactly {n_insights} business insights ranked by business impact.

For each insight, provide:
- title: Concise, action-oriented headline (max 10 words)
- description: 2-3 sentences explaining what the data shows
- type: one of: opportunity, risk, anomaly, trend
- confidence: float 0-1 based on statistical evidence strength
- supporting_data: key statistics that support this insight
- recommended_action: specific, achievable action (1-2 sentences)
- priority: high | medium | low

CRITICAL RULES:
- Only report insights supported by data in the provided context.
- Do not speculate beyond what the data shows.
- Prioritize insights with highest business impact, not just statistical significance.
- Write recommended_action in imperative, actionable language.

Respond with a JSON array of insight objects.
```

## 40.4 SQL Agent System Prompt

```
You are the SQL Agent in the AI-BIOS Business Intelligence platform.

Your role: Convert natural language questions into safe, read-only SQL queries 
for connected databases.

Database schema:
{schema_json}

Database type: {db_type}

Rules (STRICTLY ENFORCED — NEVER VIOLATE):
1. Generate ONLY SELECT statements. No INSERT, UPDATE, DELETE, DROP, ALTER, 
   TRUNCATE, CREATE, GRANT, REVOKE, EXEC, CALL.
2. Always use table aliases for clarity.
3. Always include a LIMIT clause (max 10000) unless user explicitly requests all.
4. Use parameterized patterns where possible.
5. If the question cannot be answered with available schema, say so clearly.
6. Do not reference tables or columns not present in the provided schema.

Output format (JSON):
{
  "sql": "string — the complete SQL query",
  "explanation": "string — plain English explanation of what the query does",
  "estimated_rows": integer — best guess at result count,
  "warnings": ["string"] — any caveats about the query
}
```

## 40.5 Chat Agent System Prompt

```
You are the Chat Agent in the AI-BIOS Business Intelligence platform.

Your role: Answer questions about the active dataset in a conversational, 
accurate, and helpful manner.

Active dataset: {dataset_name}
Dataset summary: {dataset_summary}

Retrieved context (from vector search):
{retrieved_chunks}

Conversation history:
{conversation_history}

Current question: {user_question}

Guidelines:
1. Answer based ONLY on the retrieved context and dataset summary.
2. If you cannot answer from the available context, say: "I don't have enough 
   data to answer that. You could try running a deeper analysis."
3. Always cite which column(s) or rows support your answer.
4. Keep answers concise (2-4 sentences for simple questions, up to 8 for complex).
5. If a chart would better answer the question, indicate: 
   [CHART_SUGGESTED: <chart_type>: <description>]
6. Maintain the conversational tone of prior messages in the session.
7. Use business-friendly language, not statistical jargon.

Format citations as: [Source: column_name | aggregate_type]
```

---

# 41. Security Threat Model

## 41.1 STRIDE Analysis

| Threat | Category | Asset | Mitigation |
|--------|---------|-------|-----------|
| Attacker steals JWT token | Spoofing | User identity | Short expiry (15min), HTTPS-only cookies option |
| Attacker modifies analysis result | Tampering | Analysis data | Database write protection via RBAC |
| Attacker gains access to another user's data | Spoofing | Dataset | RLS + project membership checks |
| User uploads malicious macro XLSX | Tampering | Backend server | XLSX macro stripping before processing |
| SQL injection via natural language | Tampering | Connected DB | SQL keyword allowlist + read-only transactions |
| Prompt injection in chat | Tampering | AI model | Input sanitization, system prompt server-side |
| COA executes without approval | Elevation of privilege | Desktop | Approval token required + HMAC signed |
| Agent log exposes DB credentials | Information disclosure | Secrets | Credentials never logged, encrypted at rest |
| Brute force login | Spoofing | Auth | Rate limiting + account lockout after 10 fails |
| SSRF via DB connection URL | Spoofing | Internal network | URL allowlist + host validation |
| Denial of Service via large file | DoS | Server | 500MB limit + async processing queue |
| Replay attack on COA token | Spoofing | COA system | JTI claim in token, single-use enforcement |

## 41.2 Prompt Injection Mitigation

Prompt injection occurs when user-supplied data contains instructions that manipulate the AI model. Mitigations:

1. **Structural separation:** User data is injected into prompts as JSON-encoded strings inside a `data:` key, never as free text that could be mistaken for instructions.
2. **Instruction boundary markers:** System prompts use explicit delimiters:
   ```
   <system_instructions>
   You are the EDA Agent...
   </system_instructions>
   <user_data>
   {user_data_json_encoded}
   </user_data>
   ```
3. **Output validation:** All agent outputs validated against Pydantic schema before use.
4. **No action from data:** Agents never execute code found in data fields.

## 41.3 File Upload Attack Vectors

| Attack | Vector | Defense |
|--------|--------|---------|
| MIME type spoofing | Rename .exe to .csv | MIME type detection from file content (python-magic) |
| Zip bomb | Compressed CSV expanding to 100GB | 500MB limit enforced post-decompression |
| XLSX macro | VBA macro in xlsx | openpyxl loaded in read-only mode; macros never executed |
| CSV injection | `=cmd|'/c calc'!A1` in cell value | Cells displayed as text, never executed |
| Path traversal | `../../etc/passwd` in filename | UUID filename assigned server-side; original name stored separately |
| Polyglot file | Valid PNG that is also valid CSV | Both MIME and extension validated |

---

# 42. Scalability Architecture (Future)

## 42.1 Horizontal Scaling Plan

```mermaid
graph TB
    subgraph "Load Balancer"
        LB[NGINX / Railway Load Balancer]
    end

    subgraph "API Tier (stateless)"
        API1[FastAPI Instance 1]
        API2[FastAPI Instance 2]
        API3[FastAPI Instance N]
    end

    subgraph "Worker Tier"
        W1[Celery Worker 1\ncompute queue]
        W2[Celery Worker 2\ncompute queue]
        W3[Celery Worker 3\nAI queue]
        W4[Celery Worker 4\nreports queue]
    end

    subgraph "Shared State"
        REDIS_CLUSTER[Redis Cluster\n3 nodes]
        PG_PRIMARY[(PostgreSQL Primary)]
        PG_REPLICA1[(Read Replica 1)]
        PG_REPLICA2[(Read Replica 2)]
        CHROMA_DIST[ChromaDB Distributed]
        S3_STORAGE[S3 Object Storage]
    end

    LB --> API1
    LB --> API2
    LB --> API3
    API1 & API2 & API3 --> REDIS_CLUSTER
    API1 & API2 & API3 --> PG_PRIMARY
    API1 & API2 & API3 --> PG_REPLICA1
    W1 & W2 & W3 & W4 --> REDIS_CLUSTER
    W1 & W2 & W3 & W4 --> PG_PRIMARY
    W1 & W2 --> S3_STORAGE
    API1 & API2 & API3 --> CHROMA_DIST
```

## 42.2 Scaling Triggers

| Metric | Scale-Out Trigger | Scale-In Trigger |
|--------|-----------------|-----------------|
| CPU (API) | > 70% for 2 min | < 30% for 10 min |
| CPU (Workers) | > 80% for 2 min | < 20% for 15 min |
| Memory (Workers) | > 80% | < 40% |
| Queue depth (compute) | > 50 tasks | < 5 tasks |
| Queue depth (AI) | > 20 tasks | < 3 tasks |
| DB connections | > 70% pool | < 30% pool |

## 42.3 Multi-Region Consideration (Phase 5+)

For enterprise customers requiring data residency:
- Deploy independent stacks per region: US, EU, APAC
- No cross-region data transfer for user data
- Shared: application code, Gemini API (Google manages)
- Isolated: PostgreSQL, ChromaDB, file storage per region
- Auth tokens region-scoped with `iss` claim indicating region

---

# 43. Error Recovery Runbook

## 43.1 Common Failure Scenarios and Responses

### Scenario 1: Gemini API Returns 429 (Rate Limit)

**Detection:** `google.api_core.exceptions.ResourceExhausted`

**Immediate Response:**
1. Celery task enters exponential backoff: wait 2s, 4s, 8s
2. After 3 retries: mark task as `failed_retriable`
3. Notify user: "Analysis temporarily delayed due to AI service load. Retrying automatically."
4. Re-queue task with 5-minute delay

**Prevention:** Implement token bucket rate limiter per Gemini model, track usage, pre-emptively throttle.

---

### Scenario 2: Large File Causes Worker OOM

**Detection:** Worker process killed (SIGKILL), task marked `REVOKED`

**Immediate Response:**
1. Celery detects worker death, marks task as `FAILURE`
2. Monitor detects: `task.retries == 0` + `OOMKilled`
3. Re-queue with chunked processing flag: `chunk_size=10000`
4. Notify user: "File is large; switching to chunked processing. This may take longer."

**Prevention:** Check file size before dispatch; route files > 100MB to dedicated high-memory worker.

---

### Scenario 3: Database Connection Pool Exhausted

**Detection:** `asyncpg.TooManyConnectionsError`

**Immediate Response:**
1. API returns 503 with `Retry-After: 5` header
2. Alert fires to monitoring channel
3. PgBouncer pool automatically queues excess connections
4. If > 30 seconds: page on-call engineer

**Prevention:** Connection pool sized to 80% of PostgreSQL `max_connections`; PgBouncer as connection pooler in front of Neon.

---

### Scenario 4: ChromaDB Collection Unavailable

**Detection:** `chromadb.errors.ChromaError` on query

**Immediate Response:**
1. Chat agent falls back to: use raw DataFrame stats (no RAG)
2. User notified: "Context search temporarily unavailable. Answering from dataset summary."
3. Retry ChromaDB connection every 30 seconds in background
4. Log to monitoring as WARNING (not critical — degraded mode)

---

### Scenario 5: COA Local Agent Disconnects During Execution

**Detection:** WebSocket closes with code 1006 mid-execution

**Immediate Response:**
1. Mark COA action as `execution_uncertain`
2. Immediately notify user: "Connection to your device was lost during execution. Please verify the action manually."
3. Do NOT re-attempt automatically
4. Require manual confirmation from user before retry
5. Log incident to audit log with `execution_result = 'uncertain'`

---

# 44. Testing Data Fixtures

## 44.1 Standard Test Datasets

The following test fixtures must be created in `backend/tests/fixtures/` and used across all tests:

| File | Description | Rows | Columns |
|------|-------------|------|---------|
| `small_clean.csv` | Perfect data, all types | 500 | 10 |
| `medium_nulls.csv` | 20% null values | 5,000 | 15 |
| `large_numeric.csv` | All numeric, no nulls | 50,000 | 20 |
| `timeseries_daily.csv` | Daily dates + revenue | 730 | 3 |
| `timeseries_weekly.csv` | Weekly sales data | 156 | 5 |
| `ecommerce_rfm.csv` | Customer, date, order | 10,000 | 4 |
| `multi_category.csv` | Mixed types, high cardinality | 2,000 | 12 |
| `outliers_heavy.csv` | 10% extreme outliers | 1,000 | 5 |
| `corrupt_types.csv` | Numbers stored as strings | 500 | 8 |
| `empty_dataset.csv` | Header only, 0 rows | 0 | 5 |
| `single_column.csv` | Only one column | 100 | 1 |

## 44.2 pytest Fixture Configuration

```python
# conftest.py

@pytest.fixture(scope="session")
def db_engine():
    """Create test database engine."""
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture
def db_session(db_engine):
    """Provide transactional test session — rolled back after each test."""
    connection = db_engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def test_user(db_session):
    user = User(
        email="test@example.com",
        hashed_password=hash_password("TestPass123!"),
        full_name="Test User",
        role="analyst"
    )
    db_session.add(user)
    db_session.commit()
    return user

@pytest.fixture
def test_project(db_session, test_user):
    project = Project(name="Test Project", owner_id=test_user.id)
    db_session.add(project)
    db_session.commit()
    return project

@pytest.fixture
def mock_gemini():
    """Mock all Gemini API calls."""
    with patch("app.agents.base_agent.GenerativeModel") as mock:
        mock.return_value.generate_content.return_value = MockGeminiResponse(
            text='{"status": "ok", "insights": []}'
        )
        yield mock
```

---

# 45. Accessibility (a11y) Requirements

## 45.1 WCAG 2.1 AA Compliance Targets

| Criterion | Target | Implementation |
|----------|--------|---------------|
| Color contrast (text) | ≥ 4.5:1 | Checked with axe-core in CI |
| Color contrast (large text) | ≥ 3:1 | Tailwind color palette verified |
| Keyboard navigation | All interactive elements | Focus traps in modals, skip links |
| Screen reader support | ARIA labels on all controls | Tested with NVDA + VoiceOver |
| Form labels | Every input labeled | ShadCN `<Label>` linked to input |
| Error identification | Color + text + icon | Never color-only |
| Resize text | Up to 200% without loss | Fluid typography (rem units) |
| Motion sensitivity | Respect `prefers-reduced-motion` | CSS media query + Framer Motion check |

## 45.2 Key Accessibility Implementations

### Approval Dialog (COA) — Critical
- `role="dialog"` + `aria-modal="true"` + `aria-labelledby` pointing to title
- Focus trapped inside dialog (Tab cycles through buttons only)
- First focusable element: "Deny" button (safest default)
- Escape key: triggers Deny action
- Countdown announced via `aria-live="polite"` every 60 seconds

### Charts
- All charts have `role="img"` + `aria-label` describing the chart
- Data tables provided as accessible alternative to charts
- Color palettes tested for colorblind-safe combinations (deuteranopia + protanopia)

### Data Tables
- `<th>` with scope attribute on all headers
- Sortable columns announced via `aria-sort`
- Pagination controls labeled with current page context

---

# 46. Internationalization (i18n) — Phase 5

## 46.1 i18n Architecture

While Phase 1–4 are English-only, the codebase must be i18n-ready from day one.

**Frontend (next-intl):**
- All user-facing strings extracted to `messages/{locale}.json`
- No hardcoded strings in JSX
- Date/time/number formatting via `Intl` browser APIs
- RTL layout support via Tailwind `rtl:` variant

**Backend:**
- All user-facing error messages use message keys, not hardcoded English
- Language preference stored in `users.preferences.locale`
- Email templates use locale-aware templates

**Initial Locales for Phase 5:**
- `en-US` (primary)
- `hi-IN` (Hindi — Indian market)
- `es-ES` (Spanish)
- `pt-BR` (Brazilian Portuguese)

---

# 47. SaaS Subscription & Billing Architecture

## 47.1 Feature Gating

Feature flags are checked at three layers:
1. **API middleware:** `check_subscription_feature(user, feature_name)` — 403 if not entitled
2. **Frontend:** Feature flags loaded on login, gates UI elements from rendering
3. **Celery tasks:** Check subscription before starting compute-heavy tasks

## 47.2 Feature Entitlement Matrix

| Feature | Free | Analyst | Team | Enterprise |
|---------|:----:|:-------:|:----:|:----------:|
| Projects | 1 | 10 | Unlimited | Unlimited |
| Datasets per project | 3 | 20 | Unlimited | Unlimited |
| Rows per dataset | 100K | 2M | 10M | Unlimited |
| Storage | 100MB | 5GB | 50GB | Custom |
| Analyses per month | 5 | Unlimited | Unlimited | Unlimited |
| Chat messages per day | 20 | 200 | Unlimited | Unlimited |
| PDF reports per month | 3 | 20 | Unlimited | Unlimited |
| PPTX reports per month | 1 | 10 | Unlimited | Unlimited |
| Forecasting | ❌ | ✅ | ✅ | ✅ |
| RFM / Cohort analysis | ❌ | ✅ | ✅ | ✅ |
| SQL Integration | ❌ | ✅ | ✅ | ✅ |
| Computer Operator Agent | ❌ | ❌ | ✅ | ✅ |
| Power BI Integration | ❌ | ❌ | ✅ | ✅ |
| Team members | 1 | 3 | 10 | Unlimited |
| API access | ❌ | ❌ | ✅ | ✅ |
| White-label | ❌ | ❌ | ❌ | ✅ |
| SSO | ❌ | ❌ | ❌ | ✅ |
| Audit logs (retention) | 7 days | 30 days | 90 days | 1 year |
| SLA | ❌ | ❌ | 99.5% | 99.9% |

## 47.3 Usage Metering

Usage is tracked in Redis counters (daily) and synced to PostgreSQL (hourly):

```python
# Redis key patterns
"usage:{user_id}:analyses:{YYYY-MM}"      → int
"usage:{user_id}:chat_messages:{YYYY-MM-DD}" → int
"usage:{user_id}:reports:{YYYY-MM}"       → int
"usage:{user_id}:storage_bytes"           → int (updated on upload/delete)
```

On limit breach:
- API returns 429 with `X-Limit-Resource: analyses` header
- User receives in-app notification with upgrade CTA
- Usage dashboard shows consumption graphs

---

# 48. Makefile Reference

```makefile
# Makefile — AI-BIOS development commands

.PHONY: help setup dev test lint migrate seed clean deploy-staging deploy-prod

help:           ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

setup:          ## First-time setup: install deps + setup DB
	cd backend && pip install -r requirements-dev.txt
	cd frontend && npm install
	docker-compose up -d postgres redis chromadb
	cd backend && alembic upgrade head
	cd backend && python scripts/seed_dev_data.py

dev:            ## Start all services in development mode
	docker-compose up -d postgres redis chromadb
	cd backend && uvicorn app.main:app --reload --port 8000 &
	cd backend && celery -A app.tasks.celery_app worker --loglevel=info &
	cd frontend && npm run dev

test:           ## Run all tests
	cd backend && pytest tests/ -v --cov=app --cov-report=html
	cd frontend && npm run test

lint:           ## Run linters
	cd backend && ruff check . && mypy app/
	cd frontend && npm run lint && npx tsc --noEmit

migrate:        ## Run pending migrations
	cd backend && alembic upgrade head

migrate-new:    ## Create new migration
	cd backend && alembic revision --autogenerate -m "$(name)"

seed:           ## Seed development database with sample data
	cd backend && python scripts/seed_dev_data.py

clean:          ## Remove generated files and caches
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	cd frontend && rm -rf .next node_modules/.cache

docker-build:   ## Build Docker images
	docker build -t aibios-backend:latest ./backend
	docker build -t aibios-frontend:latest ./frontend

docker-up:      ## Start full stack via Docker Compose
	docker-compose up --build

docker-down:    ## Stop all Docker services
	docker-compose down -v

deploy-staging: ## Deploy to staging (Railway + Vercel)
	railway up --environment staging
	vercel --prod=false

deploy-prod:    ## Deploy to production (requires confirmation)
	@echo "⚠️  Deploying to PRODUCTION. Are you sure? [y/N]" && read ans && [ $${ans:-N} = y ]
	railway up --environment production
	vercel --prod
```

---

# 49. Seed Data Script Specification

**File:** `backend/scripts/seed_dev_data.py`

The seed script creates a complete development environment with:

```
Users:
  - admin@aibios.dev   | password: Admin123!  | role: admin
  - analyst@aibios.dev | password: Test123!   | role: analyst
  - viewer@aibios.dev  | password: View123!   | role: viewer

Projects:
  - "Retail Analytics Demo"  (owner: analyst user)
  - "Finance Dashboard"      (owner: analyst user)

Datasets (pre-loaded from fixtures/):
  - "Q4 Sales Data"          → fixtures/timeseries_daily.csv
  - "Customer RFM"           → fixtures/ecommerce_rfm.csv
  - "Revenue by Region"      → fixtures/multi_category.csv

Pre-run Analyses:
  - EDA analysis on "Q4 Sales Data" (status: completed)
  - Forecast on "Q4 Sales Data"     (status: completed)

Chat Sessions:
  - One session on "Q4 Sales Data" with 5 example messages

Notifications:
  - 2 unread notifications for analyst user
```

---

# 50. Glossary

| Term | Definition |
|------|-----------|
| **Agent** | An AI-powered module responsible for a specific analytical task, powered b
| **Analysis** | A complete run of one or more agents against a dataset, producing insights, charts, and optionally a report |
| **ChromaDB** | The vector database used to store dataset embeddings for RAG-based chat queries |
| **COA** | Computer Operator Agent — the agent responsible for automating desktop application interactions with mandatory human approval |
| **Dataset** | An uploaded file (CSV/XLSX) or database connection that serves as input to analyses |
| **EDA** | Exploratory Data Analysis — statistical profiling of a dataset to understand distributions, relationships, and quality |
| **LangGraph** | The agent orchestration framework used to define multi-step, stateful AI workflows |
| **MAPE** | Mean Absolute Percentage Error — the primary accuracy metric for forecasting models |
| **Profile** | The statistical summary of a dataset generated immediately after upload: row counts, column types, null rates, distributions |
| **Project** | A container for datasets, analyses, dashboards, and reports belonging to a team or use case |
| **RAG** | Retrieval-Augmented Generation — technique of retrieving relevant data chunks from ChromaDB before generating AI responses |
| **RBAC** | Role-Based Access Control — permission system that controls what each user role can do |
| **RFM** | Recency, Frequency, Monetary — customer segmentation framework based on purchase behavior |
| **Single Source of Truth (SSOT)** | This document: `AI_BIOS_MASTER.md`. All implementation decisions reference it |
| **State** | The LangGraph state object passed between agent nodes, accumulating results as the workflow progresses |
| **Workflow** | A LangGraph graph definition that sequences agents to complete a complex multi-step task |

---

> **Document End**
>
> **AI_BIOS_MASTER.md — Version 1.0.0**
>
> **Total Sections: 50 | Estimated: 20,000+ words**
>
> This document is the SINGLE SOURCE OF TRUTH for AI-BIOS development.
> All agents (Cursor, Claude Code, OpenHands, Roo Code, Continue.dev, Cline) must treat this document as authoritative.
> Implement phase by phase. Reference checklists after every phase. Never deviate from the architecture without updating this document first.
>
> Build something extraordinary. 🚀






---

# 51. Agent Tool Definitions (Complete)

This section defines every tool available to each agent within the LangGraph framework. Tools are implemented as Python functions decorated with `@tool` from LangGraph/LangChain and registered in each agent's tool list.

## 51.1 Data Tools (`backend/app/tools/data_tools.py`)

```python
@tool
def load_dataframe(file_path: str, max_rows: int = 100000) -> dict:
    """
    Load a CSV or parquet file into a pandas DataFrame.
    Returns: { "shape": [rows, cols], "columns": [...], "dtypes": {...}, "sample": [...5 rows...] }
    """

@tool
def compute_descriptive_stats(file_path: str, columns: list[str] = None) -> dict:
    """
    Compute descriptive statistics for specified columns (or all if None).
    Returns per-column: mean, std, min, max, p25, p50, p75, skewness, kurtosis, null_count.
    """

@tool
def compute_correlation_matrix(file_path: str, method: str = "pearson") -> dict:
    """
    Compute correlation matrix. method: pearson | spearman | kendall
    Returns: { "matrix": {...}, "top_pairs": [{col_a, col_b, r}] }
    """

@tool
def detect_outliers(file_path: str, column: str, method: str = "iqr") -> dict:
    """
    Detect outliers in a numeric column.
    method: iqr | zscore | isolation_forest
    Returns: { "outlier_count": int, "outlier_pct": float, "outlier_indices": [...] }
    """

@tool
def impute_missing_values(file_path: str, strategy: dict) -> str:
    """
    Impute missing values per column.
    strategy: { "column_name": "mean|median|mode|ffill|constant", ... }
    Returns: path to imputed file.
    """

@tool
def remove_duplicates(file_path: str, subset: list[str] = None) -> dict:
    """
    Remove duplicate rows.
    Returns: { "rows_before": int, "rows_after": int, "duplicates_removed": int, "output_path": str }
    """

@tool
def cast_column_types(file_path: str, type_map: dict) -> str:
    """
    Cast columns to specified types.
    type_map: { "col_name": "int|float|datetime|str|bool", ... }
    Returns: path to recast file.
    """

@tool
def filter_rows(file_path: str, condition: str) -> str:
    """
    Filter rows using a pandas query string.
    condition: valid pandas .query() expression (e.g. "revenue > 1000 and region == 'West'")
    Returns: path to filtered file.
    """

@tool
def aggregate_data(file_path: str, group_by: list[str], agg_spec: dict) -> dict:
    """
    Group and aggregate data.
    agg_spec: { "revenue": "sum", "orders": "count", "avg_value": ["mean", "std"] }
    Returns: aggregated result as dict records.
    """

@tool
def sample_dataframe(file_path: str, n: int = 500, method: str = "random") -> dict:
    """
    Sample rows from a dataset.
    method: random | head | tail | stratified
    Returns: { "sample": [...rows...], "total_rows": int }
    """
```

## 51.2 Visualization Tools (`backend/app/tools/viz_tools.py`)

```python
@tool
def generate_histogram_config(file_path: str, column: str, bins: int = 20) -> dict:
    """
    Generate Recharts histogram configuration for a numeric column.
    Returns: Recharts BarChart config with bin edges and counts.
    """

@tool
def generate_bar_chart_config(
    file_path: str, x_col: str, y_col: str,
    agg: str = "sum", top_n: int = 15
) -> dict:
    """
    Generate a bar chart config for categorical X vs numeric Y.
    Returns: Recharts BarChart JSON config.
    """

@tool
def generate_line_chart_config(
    file_path: str, x_col: str, y_cols: list[str]
) -> dict:
    """
    Generate a multi-series line chart config.
    Returns: Recharts LineChart JSON config.
    """

@tool
def generate_scatter_config(
    file_path: str, x_col: str, y_col: str, color_col: str = None
) -> dict:
    """
    Generate a scatter plot config.
    Returns: Recharts ScatterChart JSON config.
    """

@tool
def generate_heatmap_config(file_path: str, correlation_matrix: dict) -> dict:
    """
    Convert a correlation matrix dict to a heatmap visualization config.
    Returns: custom Recharts-compatible heatmap config.
    """

@tool
def generate_pie_chart_config(
    file_path: str, label_col: str, value_col: str, top_n: int = 8
) -> dict:
    """
    Generate a pie/donut chart config for categorical data.
    Returns: Recharts PieChart JSON config.
    """

@tool
def render_chart_to_png(chart_config: dict, output_path: str, dpi: int = 150) -> str:
    """
    Render a chart config to a PNG file using matplotlib.
    Used for PDF report embedding.
    Returns: absolute path to rendered PNG.
    """
```

## 51.3 SQL Tools (`backend/app/tools/sql_tools.py`)

```python
@tool
def get_database_schema(connection_id: str) -> dict:
    """
    Fetch schema (table names, columns, types, row counts) from a connected DB.
    Never returns credentials. Returns schema JSON only.
    """

@tool
def execute_read_query(connection_id: str, sql: str, limit: int = 10000) -> dict:
    """
    Execute a validated SELECT query in read-only mode.
    Validates: no forbidden keywords, timeout 30s enforced.
    Returns: { "columns": [...], "rows": [...], "row_count": int, "truncated": bool }
    """

@tool
def validate_sql_safety(sql: str) -> dict:
    """
    Check SQL for forbidden keywords and injection patterns.
    Returns: { "is_safe": bool, "violations": [str], "cleaned_sql": str }
    """

@tool
def explain_query_plan(connection_id: str, sql: str) -> dict:
    """
    Run EXPLAIN on a query to estimate cost and row count.
    Returns: { "estimated_rows": int, "estimated_cost": float, "plan_text": str }
    """
```

## 51.4 File Tools (`backend/app/tools/file_tools.py`)

```python
@tool
def save_dataframe_to_parquet(df_path: str, output_path: str) -> str:
    """Save a processed DataFrame as parquet for efficient downstream use."""

@tool
def save_dataframe_to_csv(df_path: str, output_path: str) -> str:
    """Export a DataFrame to CSV for user download."""

@tool
def get_file_metadata(file_path: str) -> dict:
    """Return: { size_bytes, created_at, modified_at, extension }"""

@tool
def generate_signed_download_url(file_path: str, ttl_seconds: int = 3600) -> str:
    """Generate a time-limited download URL for a stored file."""
```

## 51.5 System Tools (`backend/app/tools/system_tools.py`)

```python
@tool
def emit_progress_event(analysis_id: str, step: str, progress_pct: int) -> bool:
    """Broadcast a progress update to WebSocket subscribers for this analysis."""

@tool
def create_notification(user_id: str, type: str, title: str, body: str, metadata: dict) -> str:
    """Create a notification record and emit WebSocket event. Returns notification_id."""

@tool
def log_agent_action(
    analysis_id: str, agent_name: str, action: str,
    input_data: dict, output_data: dict, status: str,
    duration_ms: float
) -> str:
    """Write an agent action record to the agent_logs table. Returns log_id."""

@tool
def get_cached_result(cache_key: str) -> dict | None:
    """Retrieve a cached analysis result from Redis. Returns None if not found."""

@tool
def set_cached_result(cache_key: str, data: dict, ttl: int = 86400) -> bool:
    """Store an analysis result in Redis cache with TTL."""
```

---

# 52. Detailed Phase Implementation Tasks

This section expands each phase roadmap with granular, ticket-level tasks ordered for sequential implementation by an AI coding agent.

## 52.1 Phase 1 — Granular Task Breakdown

### Sprint 1 (Week 1–2): Infrastructure & Auth

```
TASK-001: Initialize backend project structure per Section 5.3
  - Create all folders, __init__.py files
  - Configure pyproject.toml (ruff, mypy, pytest)
  - Set up alembic with env.py
  - Connect to Neon PostgreSQL via asyncpg

TASK-002: Implement Settings (pydantic-settings)
  - Create app/config.py with all env vars from Section 30.1
  - All secrets read from environment, never hardcoded
  - Validate on startup: missing required vars raise ValueError

TASK-003: Create all SQLAlchemy models (Phase 1 subset)
  - User, Project, ProjectMember, Dataset, Analysis,
    Visualization, Report, AgentLog, AuditLog, Notification
  - All models include created_at, updated_at via mixin
  - Run alembic autogenerate → verify migrations 001–016

TASK-004: Implement auth endpoints
  - POST /auth/register: hash password (bcrypt 12 rounds), create user
  - POST /auth/login: verify password, issue JWT pair
  - POST /auth/refresh: validate refresh token from Redis, issue new access
  - POST /auth/logout: delete refresh token from Redis allowlist
  - GET /auth/me: return current user from JWT claims

TASK-005: Implement JWT middleware
  - Dependency: get_current_user(token) → User
  - Dependency: require_role(roles: list[str])
  - Attach user to request state

TASK-006: Set up Redis client and connection pool
  - Cache client with get/set/delete helpers
  - Test connection on startup
  
TASK-007: Initialize Next.js 15 frontend
  - App Router structure per Section 5.2
  - Install: tailwindcss, shadcn/ui, framer-motion, recharts, zustand, axios
  - Configure shadcn components.json
  - Set up api-client.ts with Axios interceptors (auto-attach JWT, auto-refresh)
  - Set up auth-store.ts (Zustand)

TASK-008: Build auth pages
  - /login: email/password form, error handling, redirect on success
  - /register: form with client-side validation matching server rules
  - Middleware: redirect unauthenticated users to /login

TASK-009: Build dashboard shell layout
  - Sidebar with nav items: Projects, Settings
  - TopBar with user avatar dropdown (logout)
  - Responsive: sidebar collapses on mobile
```

### Sprint 2 (Week 3–4): File Upload & Profiling

```
TASK-010: Implement file upload endpoint
  - POST /api/v1/projects/{id}/datasets/upload
  - Multipart form handling
  - Validate: extension, MIME type (python-magic), size ≤ 500MB
  - Save file with UUID name to STORAGE_LOCAL_PATH
  - Create Dataset record (status=uploading)
  - Enqueue parse_uploaded_file Celery task
  - Return 202 + dataset_id

TASK-011: Implement parse_uploaded_file Celery task
  - Download file from storage path
  - Detect encoding for CSV (chardet)
  - Parse with pandas (handle bad lines gracefully)
  - Detect column types: numeric/categorical/date/text/boolean
  - Compute profile per Section 11.1
  - Save profile JSON to Dataset record
  - Update status to "ready"
  - Emit dataset.ready WebSocket event
  - Enqueue generate_embeddings task

TASK-012: Set up Celery with Redis broker
  - celery_app.py: configure broker, backend, serializer
  - Task routing per Section 34 queues
  - Test: enqueue dummy task, verify execution

TASK-013: Set up WebSocket manager
  - ws/manager.py: ConnectionManager class
    - connect(user_id, websocket)
    - disconnect(user_id, websocket)
    - broadcast_to_user(user_id, event_type, payload)
  - WS endpoint: /ws?token=<jwt>
  - Validate JWT on connect, store user_id → websocket mapping

TASK-014: Build FileDropzone frontend component
  - Drag-and-drop + click-to-browse
  - Client-side: extension + size validation
  - XHR upload with onprogress for byte-level progress bar
  - States: idle / dragging / uploading / success / error
  - On success: navigate to /projects/{id}/datasets/{datasetId}

TASK-015: Build dataset profile page
  - Fetch GET /api/v1/datasets/{id}/profile
  - Display: row count, column count, quality score, file size
  - ColumnProfileCard for each column (type badge, null%, unique count, stats)
  - Loading skeleton while profile is processing
  - WebSocket listener for dataset.ready event
```

### Sprint 3 (Week 5–6): Analysis Agents

```
TASK-016: Implement BaseAgent class
  - app/agents/base_agent.py
  - Abstract run(state) method
  - log_action() writes to agent_logs
  - Retry logic with exponential backoff
  - Timeout enforcement via asyncio.wait_for

TASK-017: Implement DataCleaningAgent
  - Strategies: auto/conservative/aggressive
  - Handle: nulls (impute/drop), duplicates, type coercion
  - Generate cleaning_report dict
  - Save cleaned DataFrame to new path
  - Tests: happy path, >50% nulls triggers conservative, fatal error recovery

TASK-018: Implement EDAAgent
  - Compute: distributions, skewness, kurtosis per numeric column
  - Compute: correlation matrix (Pearson + Spearman)
  - Identify: top correlated pairs, constant columns, high-null columns
  - Call Gemini Flash to generate narrative (structured JSON output)
  - Recommend chart types based on column types
  - Tests: all column types, empty columns, Gemini failure fallback

TASK-019: Implement VisualizationAgent
  - Consume chart_specs from EDA Agent
  - Generate Recharts JSON config per chart type
  - Render to PNG via matplotlib for PDF embedding
  - Tests: each chart type produces valid JSON, PNG file created

TASK-020: Implement InsightAgent
  - Synthesize EDA + cleaning reports
  - Call Gemini Pro with structured insight prompt (Section 40.3)
  - Parse response into List[InsightSchema]
  - Assign priority + confidence
  - Tests: 5+ insights generated, all fields populated

TASK-021: Implement LangGraph Analysis Workflow
  - workflows/analysis_workflow.py
  - Define all nodes per Section 32.2
  - Define conditional edges per Section 32.3
  - Compile graph with checkpointer for resume support
  - Tests: full workflow runs end-to-end, partial failure degrades gracefully

TASK-022: Implement run_analysis_workflow Celery task
  - Initialize state from DB
  - Run LangGraph workflow
  - Persist results to DB after each node (checkpointing)
  - Emit progress WebSocket events
  - On completion: update analysis status, emit analysis.completed

TASK-023: Build analysis status page (frontend)
  - Poll GET /analyses/{id}/status every 3 seconds (or WebSocket)
  - AgentStatusPanel component showing each agent step
  - Progress bar (0–100%)
  - Error display with retry button
```

### Sprint 4 (Week 7–8): Dashboard, Reporting, Phase 1 Polish

```
TASK-024: Implement Report Agent (basic PDF)
  - ReportLab setup per Section 38.1
  - Render: cover, summary, dataset overview, top 5 insights, charts
  - Embed chart PNGs
  - Save to storage, update report record
  - Return signed download URL

TASK-025: Implement generate_pdf_report Celery task
  - Trigger from analysis completion if report requested
  - Or: POST /reports/generate endpoint
  - Emit report.ready WebSocket event on completion

TASK-026: Build dashboard page (frontend)
  - Auto-fetch analysis results on completion
  - DashboardGrid layout (12-column grid)
  - KPI cards (auto-select top 3 numeric aggregates)
  - Chart grid (render Recharts configs from analysis result)
  - InsightPanel (top 5 insights with type badges)
  - Download PDF button

TASK-027: Build project list page
  - GET /api/v1/projects with pagination
  - ProjectCard: name, dataset count, last activity, member count
  - Create project modal (name, description, settings)

TASK-028: Complete Phase 1 acceptance criteria verification
  - Run all unit tests (target: >80% coverage)
  - Run integration tests for all Phase 1 flows
  - Manual QA: upload CSV → profile → analysis → dashboard → PDF download
  - Verify all WebSocket events fire correctly
  - Deploy to staging, run smoke tests
```

## 52.2 Phase 2 — Granular Task Breakdown

```
TASK-101: Implement ProphetEngine (forecasting/prophet_engine.py)
  - prepare_dataframe(), detect_seasonality(), fit(), predict(), evaluate()
  - to_recharts(): forecast line + CI area + actual line
  - Tests: daily/weekly/monthly data, horizon variations

TASK-102: Implement XGBoostTimeSeriesEngine
  - engineer_features() with all lag/rolling/date features
  - walk_forward_predict() with bootstrap CI
  - Tests: multi-feature dataset, missing intermediate dates

TASK-103: Implement ModelSelector
  - Apply decision logic per Section 39.1
  - Return recommended model with reasoning
  - Tests: verify each condition routes to correct model

TASK-104: Implement ForecastingAgent
  - Orchestrate ModelSelector → chosen engine
  - Run forecast quality gates (Section 39.4)
  - Generate Gemini Flash narrative
  - Save forecast results + chart config

TASK-105: Build forecasting page (frontend)
  - Column selector (numeric columns only)
  - Date column selector
  - Horizon slider: 7/14/30/60/90/180/365 days
  - Model preference toggle (auto / specific)
  - ForecastChart: actual + forecast + CI band (Recharts)
  - Metrics cards: MAPE, MAE, RMSE, model used
  - Export forecast CSV button

TASK-106: Implement AnomalyDetector (analysis/anomaly_detector.py)
  - IQR method: flag per column
  - Z-Score method: |z| > 3.0
  - Isolation Forest: multivariate (sklearn, datasets >1000 rows)
  - Output: anomaly_report dict + anomaly_df with is_anomaly flag

TASK-107: Implement SegmentationEngine
  - Elbow method + Silhouette score for k selection
  - K-Means clustering
  - Gemini Flash: generate cluster description for each segment
  - Output: cluster assignments + centroid values + descriptions

TASK-108: Set up ChromaDB
  - chroma_client.py: connect to ChromaDB service
  - create_dataset_collection(dataset_id): create or get collection
  - upsert_chunks(collection, chunks, embeddings): batch upsert
  - query(collection, query_embedding, top_k=10): similarity search

TASK-109: Implement generate_embeddings Celery task
  - Chunking per Section 15.2 (column summaries + row samples + aggregates)
  - Gemini embedding API (batch 100 chunks)
  - Upsert to ChromaDB collection
  - Mark dataset.embeddings_ready = true

TASK-110: Implement ChatAgent (basic)
  - Session management + history loading
  - Intent classification via Gemini Flash
  - ChromaDB retrieval (top-10)
  - Context building (retrieved + history)
  - Gemini Pro response generation
  - Source citation extraction

TASK-111: Build chat page (frontend)
  - ChatWindow component per Section 33.5
  - WebSocket connection for streaming tokens
  - Message bubble rendering with markdown
  - SourceCitations expandable component
  - Chat history sidebar (list of sessions)
  - New session button

TASK-112: Implement PPTX generator
  - python-pptx setup per Section 38.2
  - All slide types: Title, Content, Chart, Insight, Close
  - Chart PNG embedding
  - Save to storage, update report record

TASK-113: Build reports page (frontend)
  - List generated reports per project
  - ReportPreview thumbnail
  - PDF download + PPTX download buttons
  - Regenerate report button

TASK-114: Implement RFMEngine (analysis/rfm_engine.py)
  - Compute R/F/M per customer
  - Quintile scoring (1–5 per dimension)
  - Segment labeling: Champions, Loyal, At Risk, Can't Lose, Lost
  - Generate segment stats + Gemini narrative

TASK-115: Implement CohortEngine (analysis/cohort_engine.py)
  - Build cohort retention matrix
  - Output: heatmap config + average retention by period
  - Identify drop-off inflection points
```

## 52.3 Phase 3 — Granular Task Breakdown

```
TASK-201: Implement SQL Agent (agents/sql_agent.py)
  - get_database_schema tool integration
  - Gemini Pro SQL generation with schema context (Section 40.4)
  - validate_sql_safety tool before execution
  - execute_read_query in read-only transaction
  - Plain-English explanation generation
  - Tests: 20+ NL → SQL test cases, 100% forbidden keyword rejection

TASK-202: Implement DB connection endpoints
  - POST /datasets/connect-db: validate + encrypt password + test connection
  - GET /db-connections/{id}/schema: return schema JSON
  - DELETE /db-connections/{id}: remove + decrypt/delete credentials
  - Support: PostgreSQL (psycopg2), MySQL (pymysql), SQLite

TASK-203: Implement ConsultantAgent
  - Gemini Pro with business consultant persona
  - Strategic memo generation (opportunities, risks, priorities)
  - Simulated "what-if" scenario analysis
  - Output: consultant_memo markdown string

TASK-204: Full LangGraph integration test suite
  - Test each agent in isolation with mock Gemini
  - Test full workflow end-to-end with real data fixtures
  - Test retry behavior: simulate Gemini 429, verify backoff
  - Test partial failure: one agent fails, rest continue

TASK-205: Implement RBAC enforcement layer
  - rbac.py: check_permission(user, action, resource)
  - Apply to every endpoint via FastAPI dependency
  - Analyst cannot access /admin/* (403 verified)
  - Viewer cannot POST /analyses/run (403 verified)
  - Project membership checked for all /projects/{id}/* endpoints

TASK-206: Implement AuditLog service
  - Write to audit_logs on every: auth event, CRUD op, agent action
  - IP address captured from request headers (handle proxy forwarding)
  - Severity classification: info / warn / error
  - Admin API: GET /admin/audit-logs with filters

TASK-207: Implement Notification system
  - Create notification on: analysis complete/failed, report ready
  - WebSocket: emit notification.new event
  - API: GET /notifications, PATCH /notifications/{id}/read
  - Frontend: notification bell with unread count badge

TASK-208: Build admin panel (frontend)
  - User list table with role badge, status, last login
  - Edit user modal: change role, activate/deactivate
  - Audit log viewer: filterable by user, action, date range, severity
  - System stats cards (from GET /admin/stats)

TASK-209: Implement MarketBasketEngine
  - Apriori algorithm via mlxtend
  - Config: min_support=0.01, min_confidence=0.5, min_lift=1.0
  - Output: top 20 association rules ranked by lift
  - Format as InsightSchema items

TASK-210: Implement Power BI basic export
  - Format dataset as Power BI push dataset schema
  - POST to Power BI REST API with user OAuth token
  - Return Power BI report URL
  - OAuth token management (store encrypted in DB)
```

## 52.4 Phase 4 — COA Implementation Tasks

```
TASK-301: Implement COA Planning Agent
  - consultant_agent for action planning
  - Gemini Pro: decompose user request into ordered action list
  - Each action: type, target_app, params, reason, expected_outcome, risk_level
  - Output: List[COAAction]

TASK-302: Implement ApprovalManager service
  - Create COAAction record (status=pending)
  - Emit coa.approval_required WebSocket event
  - Start 300-second countdown timer (Celery Beat task checks every 30s)
  - On user decision: update record, emit result event
  - Auto-deny on timeout: expire_pending_coa_actions beat task

TASK-303: Implement ApprovalDialog frontend component
  - Portal rendering (above all UI, z-index: 9999)
  - All required fields displayed per Section 19.4
  - Risk level color coding
  - 300-second countdown with visual urgency effects
  - Four decision buttons: Allow Once, Allow Session, Always Allow, Deny
  - Keyboard accessible, focus trapped, aria-modal

TASK-304: Implement COA permission store
  - coa_permissions table (user_id, action_type, target_app, scope, expires_at)
  - check_permission(user_id, action): return scope if permitted
  - Session permissions: stored in Redis key coa_session:{session_id}:{action_hash}
  - Always permissions: stored in PostgreSQL coa_permissions

TASK-305: Implement COA executor (backend)
  - Receive approved action with approval_token
  - Validate HMAC signature on token
  - Mark token as used (single-use enforcement via Redis)
  - Emit action payload to local agent via WebSocket
  - Wait for execution result (30s timeout)
  - Save result to coa_actions record

TASK-306: Implement Local Python Agent (separate package: aibios-local-agent)
  - WebSocket client: connects to backend WS with auth token
  - Receive signed action payload
  - Validate HMAC signature before any execution
  - Route to handler: open_application / open_file / run_script / open_url / export_to_excel
  - Handlers use: subprocess, pyautogui (GUI), win32com (Windows Excel), applescript (macOS)
  - Report execution result + optional screenshot back to backend
  - Log all actions locally to ~/.aibios/agent.log

TASK-307: Implement COA rollback system
  - For each action type, define rollback handler
  - open_file → close file by process monitoring
  - export_to_excel → delete created file
  - run_script → kill process by PID
  - POST /coa/actions/{id}/rollback: trigger within 5-minute window
  - Log rollback result to audit log

TASK-308: Build COA admin panel (frontend)
  - Pending approvals list with real-time updates via WebSocket
  - Approval history table with filters
  - Revoke "Always Allow" permissions UI
  - Per-user COA permission summary

TASK-309: COA security test suite
  - Verify: zero actions execute without approval token
  - Verify: used approval tokens rejected on reuse
  - Verify: auto-deny fires at exactly 300 seconds
  - Verify: HMAC validation rejects tampered payloads
  - Verify: all COA actions appear in audit log
```

## 52.5 Phase 5 — Enterprise Features Tasks

```
TASK-401: Multi-tenant organization model
  - Add Organization table
  - User belongs to Organization
  - Project belongs to Organization
  - Org-level admin role

TASK-402: Google OAuth integration
  - NextAuth.js (frontend) + FastAPI OAuth callback
  - Map Google profile to User record
  - Handle existing accounts: link by email

TASK-403: Public dashboard sharing
  - Generate share_token (cryptographically random 32 bytes, URL-safe base64)
  - /shared/{token} public route (no auth required)
  - Token expiry enforcement

TASK-404: REST API key management
  - api_keys table: user_id, key_hash, name, last_used, created_at
  - Generate: 32-byte random key, store bcrypt hash
  - Authentication: Bearer sk-<key> header accepted alongside JWT
  - Rate limiting: separate bucket per API key

TASK-405: Webhook system
  - webhooks table: url, events[], secret, is_active
  - On analysis.completed: POST to registered URLs with HMAC-SHA256 signature
  - Retry failed webhooks: 3 attempts with exponential backoff
  - Delivery log per webhook

TASK-406: Scheduled report delivery
  - report_schedules table: report_template_id, cron_expression, recipients[], format
  - Celery Beat: check due schedules hourly
  - Generate report → send via email (SMTP) or Slack webhook

TASK-407: Usage analytics dashboard
  - Track: API calls/day, analyses/day, storage used/day
  - Frontend: line charts for usage over time
  - Admin view: org-level + user-level breakdown

TASK-408: Custom branding per organization
  - Store: logo_url, primary_color, org_name in Organization table
  - CSS variables injected based on org branding
  - Email templates use org branding
```

---

# 53. Component State Management Reference

## 53.1 Zustand Store Definitions

### auth-store.ts
```typescript
interface AuthState {
  user: User | null
  accessToken: string | null
  isAuthenticated: boolean
  isLoading: boolean
  
  login: (email: string, password: string) => Promise<void>
  logout: () => Promise<void>
  refreshToken: () => Promise<void>
  setUser: (user: User) => void
}
```

### dataset-store.ts
```typescript
interface DatasetState {
  datasets: Dataset[]
  activeDataset: Dataset | null
  isUploading: boolean
  uploadProgress: number
  
  fetchDatasets: (projectId: string) => Promise<void>
  uploadFile: (projectId: string, file: File) => Promise<string>
  setActiveDataset: (dataset: Dataset) => void
  deleteDataset: (id: string) => Promise<void>
}
```

### analysis-store.ts
```typescript
interface AnalysisState {
  analyses: Analysis[]
  activeAnalysis: Analysis | null
  runningAnalysisId: string | null
  agentProgress: AgentProgress[]
  
  runAnalysis: (datasetId: string, types: string[]) => Promise<string>
  pollStatus: (analysisId: string) => void
  setProgress: (step: string, pct: number, agent: string) => void
  fetchResults: (analysisId: string) => Promise<void>
}
```

### chat-store.ts
```typescript
interface ChatState {
  sessions: ChatSession[]
  activeSession: ChatSession | null
  messages: ChatMessage[]
  isStreaming: boolean
  streamingContent: string
  
  createSession: (datasetId: string) => Promise<string>
  sendMessage: (content: string) => Promise<void>
  appendStreamToken: (token: string) => void
  finalizeMessage: (message: ChatMessage) => void
  loadHistory: (sessionId: string) => Promise<void>
}
```

### approval-store.ts
```typescript
interface ApprovalState {
  pendingAction: COAAction | null
  approvalHistory: COAAction[]
  
  setPendingAction: (action: COAAction | null) => void
  submitDecision: (actionId: string, decision: ApprovalDecision) => Promise<void>
  fetchHistory: () => Promise<void>
}
```

---

# 54. Backend Service Layer Specifications

## 54.1 AuthService

```python
class AuthService:
    async def register(self, email: str, password: str, full_name: str) -> User:
        """
        1. Check email uniqueness
        2. Hash password with bcrypt (12 rounds)
        3. Create User record (role=analyst, tier=free)
        4. Write audit log: action=USER_REGISTERED
        5. Return created user
        Raises: EmailAlreadyExistsError
        """

    async def login(self, email: str, password: str) -> TokenPair:
        """
        1. Fetch user by email
        2. Verify password with bcrypt
        3. Check is_active=True
        4. Generate access_token (JWT, 15min)
        5. Generate refresh_token (JWT, 7d, store hash in Redis)
        6. Write audit log: action=USER_LOGIN, ip=request.client.host
        7. Return TokenPair
        Raises: InvalidCredentialsError, AccountInactiveError
        """

    async def refresh(self, refresh_token: str) -> str:
        """
        1. Decode refresh token
        2. Check hash exists in Redis allowlist
        3. Issue new access_token
        4. Optionally rotate refresh_token (sliding window)
        Raises: InvalidTokenError, TokenExpiredError
        """

    async def logout(self, refresh_token: str, user_id: UUID) -> None:
        """
        1. Delete refresh token hash from Redis
        2. Write audit log: action=USER_LOGOUT
        """
```

## 54.2 DatasetService

```python
class DatasetService:
    async def create_from_upload(
        self, project_id: UUID, file: UploadFile, user_id: UUID
    ) -> Dataset:
        """
        1. Validate file (extension, MIME via python-magic, size)
        2. Generate UUID filename
        3. Save to storage backend (local or S3)
        4. Create Dataset record (status=uploading)
        5. Enqueue parse_uploaded_file task
        6. Write audit log
        Raises: FileTooLargeError, InvalidFileTypeError, MaliciousFileError
        """

    async def create_from_db_connection(
        self, project_id: UUID, request: DBConnectionRequest, user_id: UUID
    ) -> DBConnection:
        """
        1. Test database connection (timeout 10s)
        2. Encrypt password with Fernet
        3. Fetch schema (tables, columns, types)
        4. Create DBConnection record
        5. Write audit log
        Raises: ConnectionFailedError, UnsupportedDatabaseError
        """

    async def get_profile(self, dataset_id: UUID) -> DatasetProfileResponse:
        """Check Redis cache first. If miss: fetch from DB."""

    async def delete(self, dataset_id: UUID, user_id: UUID) -> None:
        """
        1. Verify user has delete permission (owner or admin)
        2. Delete file from storage
        3. Delete ChromaDB collection
        4. Soft-delete Dataset record
        5. Write audit log
        """
```

## 54.3 AnalysisService

```python
class AnalysisService:
    async def run(
        self, dataset_id: UUID, analysis_types: list[str],
        config: dict, user_id: UUID
    ) -> Analysis:
        """
        1. Verify dataset exists and is status=ready
        2. Check subscription limits (analyses/month)
        3. Create Analysis record (status=pending)
        4. Build initial LangGraph state
        5. Enqueue run_analysis_workflow task
        6. Write audit log
        """

    async def get_results(self, analysis_id: UUID) -> AnalysisResultResponse:
        """Check Redis cache. If miss: load from DB. Cache result for 7 days."""

    async def get_status(self, analysis_id: UUID) -> AnalysisStatusResponse:
        """Fetch status + progress_pct + current_agent from DB. No cache."""
```

## 54.4 ChatService

```python
class ChatService:
    async def create_session(
        self, dataset_id: UUID, user_id: UUID
    ) -> ChatSession:
        """Create session, verify dataset has embeddings_ready=True"""

    async def send_message(
        self, session_id: UUID, content: str, user_id: UUID
    ) -> ChatMessage:
        """
        1. Save user message to DB
        2. Load conversation history + context_summary
        3. Enqueue process_chat_message task (async) OR run inline (sync)
        4. Return task reference (client polls or streams via WS)
        """

    async def process_message(self, session_id: UUID, message_id: UUID) -> None:
        """
        Called by Celery or inline:
        1. Classify intent (Gemini Flash)
        2. Route: RAG / SQL Agent / Viz Agent / Insight cache
        3. Build prompt with context + history
        4. Stream response via Gemini Pro
        5. Emit chat.token WS events during stream
        6. Save complete message + sources to DB
        7. Emit chat.message_complete WS event
        8. Update turn_count; if >15: summarize old history
        """
```

---

# 55. Error Code Catalog

Complete reference of all application error codes for frontend error handling.

| Code | HTTP | Message | Recovery |
|------|------|---------|---------|
| `AUTH_001` | 401 | Invalid or expired access token | Refresh token |
| `AUTH_002` | 401 | Refresh token invalid or expired | Re-login |
| `AUTH_003` | 403 | Insufficient permissions for this action | Show permission error |
| `AUTH_004` | 429 | Too many login attempts | Show lockout timer |
| `AUTH_005` | 409 | Email already registered | Show login link |
| `DATASET_001` | 413 | File exceeds 500MB limit | Show size limit message |
| `DATASET_002` | 422 | Unsupported file type | Show accepted types |
| `DATASET_003` | 422 | File appears to be corrupt or empty | Re-upload prompt |
| `DATASET_004` | 404 | Dataset not found | Redirect to project |
| `DATASET_005` | 422 | Dataset has no embeddings yet | "Still processing..." |
| `DATASET_006` | 503 | Database connection test failed | Show connection error |
| `ANALYSIS_001` | 422 | Dataset is not ready for analysis | Wait for processing |
| `ANALYSIS_002` | 409 | Analysis already running for this dataset | Show running analysis |
| `ANALYSIS_003` | 429 | Monthly analysis limit reached | Show upgrade prompt |
| `ANALYSIS_004` | 500 | Analysis workflow failed internally | Retry + contact support |
| `FORECAST_001` | 422 | No date column detected for forecasting | Column selection hint |
| `FORECAST_002` | 422 | Insufficient data for forecasting (<100 rows) | Data requirements hint |
| `FORECAST_003` | 422 | Target column contains no variance | Column advice |
| `CHAT_001` | 422 | Message too long (max 4000 chars) | Truncate hint |
| `CHAT_002` | 503 | AI service temporarily unavailable | Retry in 30s |
| `SQL_001` | 403 | SQL contains forbidden operation | Security message |
| `SQL_002` | 422 | SQL syntax error | Show corrected hint |
| `SQL_003` | 408 | Query timed out (30s limit) | Optimize query hint |
| `COA_001` | 403 | Action denied by user | Show denial message |
| `COA_002` | 408 | Approval timed out (auto-denied) | Re-request option |
| `COA_003` | 404 | Local agent not connected | Install agent instructions |
| `REPORT_001` | 500 | PDF generation failed | Retry + fallback |
| `RATE_001` | 429 | API rate limit exceeded | Show retry-after |

---

# 56. docker-compose.yml Reference

```yaml
# docker-compose.yml — Local development stack

version: '3.9'

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: aibios
      POSTGRES_USER: aibios
      POSTGRES_PASSWORD: aibios_dev_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U aibios"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s

  chromadb:
    image: chromadb/chroma:latest
    ports:
      - "8001:8000"
    volumes:
      - chroma_data:/chroma/chroma
    environment:
      CHROMA_SERVER_HOST: 0.0.0.0
      CHROMA_SERVER_HTTP_PORT: 8000
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/api/v1/heartbeat"]
      interval: 10s

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql+asyncpg://aibios:aibios_dev_password@postgres:5432/aibios
      REDIS_URL: redis://redis:6379/0
      CELERY_BROKER_URL: redis://redis:6379/1
      CHROMA_HOST: chromadb
      CHROMA_PORT: 8000
      STORAGE_BACKEND: local
      STORAGE_LOCAL_PATH: /app/uploads
    volumes:
      - ./backend:/app
      - uploads_data:/app/uploads
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      chromadb:
        condition: service_healthy
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

  worker:
    build: ./backend
    environment:
      DATABASE_URL: postgresql+asyncpg://aibios:aibios_dev_password@postgres:5432/aibios
      REDIS_URL: redis://redis:6379/0
      CELERY_BROKER_URL: redis://redis:6379/1
      CHROMA_HOST: chromadb
      CHROMA_PORT: 8000
      STORAGE_BACKEND: local
      STORAGE_LOCAL_PATH: /app/uploads
    volumes:
      - ./backend:/app
      - uploads_data:/app/uploads
    depends_on:
      - backend
    command: celery -A app.tasks.celery_app worker --loglevel=info -Q high_priority,compute,ai,reports,low_priority

  beat:
    build: ./backend
    volumes:
      - ./backend:/app
    depends_on:
      - worker
    command: celery -A app.tasks.celery_app beat --loglevel=info

  flower:
    build: ./backend
    ports:
      - "5555:5555"
    depends_on:
      - worker
    command: celery -A app.tasks.celery_app flower --port=5555

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:8000
      NEXT_PUBLIC_WS_URL: ws://localhost:8000/ws
    volumes:
      - ./frontend:/app
      - /app/node_modules
      - /app/.next
    command: npm run dev

volumes:
  postgres_data:
  redis_data:
  chroma_data:
  uploads_data:
```

---

# 57. GitHub Actions CI/CD Complete Specification

## 57.1 ci.yml — Pull Request Checks

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  backend-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install ruff mypy
      - run: ruff check backend/
      - run: mypy backend/app/ --ignore-missing-imports

  frontend-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: cd frontend && npm ci
      - run: cd frontend && npm run lint
      - run: cd frontend && npx tsc --noEmit

  backend-test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env: { POSTGRES_DB: aibios_test, POSTGRES_USER: aibios, POSTGRES_PASSWORD: test }
        ports: ['5432:5432']
      redis:
        image: redis:7
        ports: ['6379:6379']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: cd backend && pip install -r requirements-dev.txt
      - run: cd backend && pytest tests/ -v --cov=app --cov-report=xml --cov-fail-under=80
      - uses: codecov/codecov-action@v4

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install bandit pip-audit
      - run: bandit -r backend/app/ -ll
      - run: pip-audit -r backend/requirements.txt
      - run: cd frontend && npm audit --audit-level=high

  docker-build:
    runs-on: ubuntu-latest
    needs: [backend-lint, frontend-lint, backend-test]
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t aibios-backend:${{ github.sha }} ./backend
      - run: docker build -t aibios-frontend:${{ github.sha }} ./frontend

  integration-test:
    runs-on: ubuntu-latest
    needs: [docker-build]
    steps:
      - uses: actions/checkout@v4
      - run: docker-compose -f docker-compose.test.yml up -d
      - run: sleep 15  # wait for services
      - run: cd backend && pytest tests/integration/ -v
      - run: docker-compose -f docker-compose.test.yml down -v
```

## 57.2 deploy.yml — Staging & Production Deployment

```yaml
name: Deploy

on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Target environment'
        required: true
        default: 'staging'
        type: choice
        options: [staging, production]

jobs:
  deploy-backend:
    runs-on: ubuntu-latest
    environment: ${{ github.event.inputs.environment || 'staging' }}
    steps:
      - uses: actions/checkout@v4
      - uses: railwayapp/railway-cli@v1
        with:
          railway-token: ${{ secrets.RAILWAY_TOKEN }}
      - run: railway up --environment ${{ github.event.inputs.environment || 'staging' }}

  deploy-frontend:
    runs-on: ubuntu-latest
    needs: deploy-backend
    steps:
      - uses: actions/checkout@v4
      - uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: ${{ github.event.inputs.environment == 'production' && '--prod' || '' }}

  smoke-test:
    runs-on: ubuntu-latest
    needs: [deploy-backend, deploy-frontend]
    steps:
      - run: curl -f ${{ secrets.STAGING_API_URL }}/health
      - run: curl -f ${{ secrets.STAGING_URL }}
```

---

# 58. Requirements Files

## 58.1 backend/requirements.txt

```
# Web framework
fastapi==0.115.0
uvicorn[standard]==0.32.0
python-multipart==0.0.12

# Database
sqlalchemy[asyncio]==2.0.36
asyncpg==0.30.0
alembic==1.14.0

# Auth
passlib[bcrypt]==1.7.4
python-jose[cryptography]==3.3.0

# Cache & Queue
redis==5.2.0
celery[redis]==5.4.0

# AI
google-generativeai==0.8.3
langchain-core==0.3.20
langgraph==0.2.55
chromadb==0.5.20

# Data processing
pandas==2.2.3
numpy==2.1.3
scipy==1.14.1
scikit-learn==1.5.2
openpyxl==3.1.5
chardet==5.2.0

# Forecasting
prophet==1.1.6
xgboost==2.1.3
mlxtend==0.23.1

# Reporting
reportlab==4.2.5
python-pptx==1.0.2
matplotlib==3.9.3

# Security
python-magic==0.4.27
cryptography==43.0.3

# Utils
pydantic==2.9.2
pydantic-settings==2.6.1
python-dotenv==1.0.1
httpx==0.28.0
aiofiles==24.1.0
```

## 58.2 backend/requirements-dev.txt

```
# Testing
pytest==8.3.3
pytest-asyncio==0.24.0
pytest-cov==6.0.0
httpx==0.28.0  # for TestClient
factory-boy==3.3.1

# Linting
ruff==0.8.0
mypy==1.13.0

# Type stubs
types-redis==4.6.0.20241004
types-passlib==1.7.7.20240819
pandas-stubs==2.2.3.241126
```

## 58.3 frontend/package.json (key dependencies)

```json
{
  "dependencies": {
    "next": "15.0.3",
    "react": "19.0.0",
    "react-dom": "19.0.0",
    "typescript": "5.6.3",
    "tailwindcss": "3.4.15",
    "@radix-ui/react-dialog": "1.1.2",
    "@radix-ui/react-dropdown-menu": "2.1.2",
    "class-variance-authority": "0.7.1",
    "clsx": "2.1.1",
    "framer-motion": "11.11.17",
    "recharts": "2.13.3",
    "zustand": "5.0.1",
    "axios": "1.7.9",
    "sonner": "1.7.1",
    "date-fns": "4.1.0",
    "lucide-react": "0.462.0",
    "react-dropzone": "14.3.5",
    "react-markdown": "9.0.1",
    "remark-gfm": "4.0.0"
  },
  "devDependencies": {
    "@types/node": "22.9.1",
    "@types/react": "19.0.1",
    "eslint": "9.15.0",
    "eslint-config-next": "15.0.3",
    "@playwright/test": "1.48.2",
    "jest": "29.7.0",
    "@testing-library/react": "16.0.1"
  }
}
```

---

# 59. Monitoring Dashboard Specification

## 59.1 Key Dashboards to Build (Grafana or similar)

### Dashboard 1: System Health
- API request rate (req/s)
- API error rate (% 5xx)
- API p50/p95/p99 latency
- Active WebSocket connections
- Memory usage per service

### Dashboard 2: Analysis Pipeline
- Analysis jobs created/hour
- Analysis completion rate (%)
- Average analysis duration (minutes)
- Queue depth per Celery queue
- Agent-level success/failure rates

### Dashboard 3: AI Usage
- Gemini API calls/hour by model
- Gemini tokens consumed/hour
- Gemini error rate (429/500)
- Average Gemini latency
- ChromaDB query latency

### Dashboard 4: User Activity
- New registrations/day
- DAU/WAU/MAU
- Chat messages/hour
- Reports generated/day
- File uploads/hour + total storage used

### Dashboard 5: COA Operations
- Pending approvals (current)
- Approval rate (approved vs denied)
- Auto-deny rate (timeout)
- Actions executed/day by type
- Rollbacks executed/day

## 59.2 Alert Runbook

When an alert fires, the on-call engineer follows this runbook:

| Alert | First Action | Escalate If |
|-------|-------------|-------------|
| API error rate > 5% | Check error logs, identify endpoint | > 10% after 10min |
| Gemini 429 rate high | Check token usage, throttle if needed | Sustained > 30min |
| Queue depth > 100 | Scale up compute workers | Depth still rising |
| DB pool > 80% | Check for slow queries, kill if needed | Connections maxed out |
| Memory > 85% | Restart affected worker | OOM kill in last 5min |
| COA local agent lost | Alert user, mark actions as uncertain | > 1 hour offline |

---

# 60. Final Project Completion Criteria

## 60.1 Definition of Done (Per Feature)

A feature is considered DONE when ALL of the following are true:

- [ ] Code implemented following architecture in this document
- [ ] Unit tests written with >80% coverage for new code
- [ ] Integration test covers the happy path end-to-end
- [ ] Edge cases handled (empty input, large input, network failure)
- [ ] Error responses match the error catalog (Section 55)
- [ ] API documentation auto-generated (FastAPI /docs)
- [ ] Frontend component is accessible (keyboard nav + aria labels)
- [ ] Security controls verified (auth, RBAC, input validation)
- [ ] Code reviewed (or self-reviewed against Section 27 rules)
- [ ] Deployed to staging and smoke-tested

## 60.2 Definition of Done (Per Phase)

A phase is DONE when ALL of the following are true:

- [ ] All tasks in phase task breakdown completed
- [ ] All acceptance criteria in Section 26 met
- [ ] Phase-specific checklist in Section 28 fully checked
- [ ] No open P0 or P1 bugs
- [ ] Performance targets met (Section 28.7)
- [ ] Security checklist verified (Section 28.6)
- [ ] Staging deployment stable for 48 hours
- [ ] This document updated with any spec changes discovered during implementation

## 60.3 Production Launch Criteria

Before going live with real users, ALL of the following must be satisfied:

- [ ] Phase 1 and Phase 2 Definition of Done verified
- [ ] OWASP ZAP scan on staging: 0 critical, 0 high findings
- [ ] Load test: 50 concurrent users, all endpoints within SLA
- [ ] Disaster recovery tested: DB restore from backup in < 30 minutes
- [ ] SSL certificate valid and auto-renewing
- [ ] Error monitoring (Sentry) configured and tested
- [ ] Alerting rules configured and tested (Section 22.4)
- [ ] Privacy policy and Terms of Service pages live
- [ ] GDPR data deletion endpoint implemented and tested
- [ ] On-call rotation established with runbook access
- [ ] Domain configured with HTTPS redirect
- [ ] Analytics (PostHog) configured for usage tracking

---

> ═══════════════════════════════════════════════════════════
>
> **AI_BIOS_MASTER.md — VERSION 1.0.0 — FINAL**
>
> **60 Sections | ~33,000 words | Complete Engineering Blueprint**
>
> ═══════════════════════════════════════════════════════════
>
> SINGLE SOURCE OF TRUTH FOR AI-BIOS DEVELOPMENT
>
> Every decision, every file, every function, every test —
> reference this document first.
>
> Sections 1–28:  Core architecture and planning
> Sections 29–50: API schemas, env vars, component specs, tooling
> Sections 51–60: Agent tools, tasks, service specs, CI/CD, launch criteria
>
> Implementation order:
>   Phase 1 (Sec 52.1) → Phase 2 (Sec 52.2) → Phase 3 (Sec 52.3)
>   → Phase 4 (Sec 52.4) → Phase 5 (Sec 52.5)
>
> Verify against:
>   Section 28 checklist after every phase
>   Section 60 before production launch
>
> Build something extraordinary. 🚀
> ═══════════════════════════════════════════════════════════


---

# PART A — Project Management & Execution Standards

---

# A1. Three Mandatory Project Files

Every AI-BIOS development session must begin by reading these three files in order:

```
ai-bios/
├── AI_BIOS_MASTER.md                    ← Architecture SSOT (read first)
├── AI_BIOS_MASTER_LEARNING_EDITION.md   ← Learning-focused guide (read second if solo dev)
└── AI_BIOS_PROJECT_STATUS.md            ← Operational memory (read before every session)
```

| File | Purpose | Update Frequency |
|------|---------|-----------------|
| `AI_BIOS_MASTER.md` | Complete architecture, API specs, agent definitions, tool definitions, deployment plans. NEVER changes unless architecture changes. | Rare — only on architecture decisions |
| `AI_BIOS_MASTER_LEARNING_EDITION.md` | Learning-focused version with roadmap, tool guide, solo dev strategy. | On major learning milestones |
| `AI_BIOS_PROJECT_STATUS.md` | Current phase, sprint tasks, bugs, blockers, session log. THE operational brain. | After EVERY development session |

### Rule: Never Start Without Reading PROJECT_STATUS.md

Before writing a single line of code in any session:
1. Open `AI_BIOS_PROJECT_STATUS.md`
2. Find Current Phase and Current Sprint
3. Find first task with status `todo` or `in-progress`
4. Implement that task
5. Update the status file on completion

---

# A2. Quick Start — Resume Development

> Use this section whenever development is interrupted, a new AI coding agent session begins, or you return to the project after any break.

## Step-by-Step Resume Protocol

```
STEP 1: Read the master document
  → Open AI_BIOS_MASTER.md
  → Find the section matching your current phase
  → Refresh your memory on the architecture for that phase

STEP 2: Read the project status
  → Open AI_BIOS_PROJECT_STATUS.md
  → Note: Current Phase, Current Sprint, Overall Completion %
  → Note: Any open bugs or blockers

STEP 3: Find your next task
  → Go to "Current Sprint Tasks" table in PROJECT_STATUS.md
  → Find the first row with Status = "todo" or "in-progress"
  → That is your starting point

STEP 4: Verify environment
  → Run: docker-compose up -d (if services not running)
  → Run: curl http://localhost:8000/health (verify backend)
  → Open: http://localhost:3000 (verify frontend)
  → Run: pytest tests/ -x (verify no regressions)

STEP 5: Implement
  → Work on exactly one task at a time
  → Run tests after completing each task
  → Do not start the next task until current task tests pass

STEP 6: Update trackers
  → Mark completed task as "done" in PROJECT_STATUS.md
  → Append a session log entry
  → Commit code with descriptive message
  → Move to next task

STEP 7: End-of-session checklist
  → All completed tasks marked "done" in PROJECT_STATUS.md
  → No uncommitted code
  → Tests passing
  → Session log entry written
  → Next task clearly identified
```

## For AI Coding Agents (Cursor, Claude Code, OpenHands, Roo Code, Cline)

When an AI agent begins a session, it MUST:

```
1. READ AI_BIOS_MASTER.md — understand the full architecture
2. READ AI_BIOS_PROJECT_STATUS.md — understand current state
3. IDENTIFY the first unfinished task
4. IMPLEMENT only that task
5. RUN tests to verify
6. UPDATE AI_BIOS_PROJECT_STATUS.md
7. REPORT what was completed and what is next
```

An AI agent must NEVER:
- Skip reading the master document
- Assume previous session context
- Implement tasks from future phases
- Mark tasks complete without passing tests
- Deviate from the architecture in AI_BIOS_MASTER.md

---

# A3. Project Execution Rules

These rules are NON-NEGOTIABLE for all developers and all AI coding agents.

## Rule 1: Never Skip Phases

```
✅ Correct:  Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7
❌ Wrong:    Phase 1 → Phase 3 (skipping Phase 2)
❌ Wrong:    Starting Phase 3 while Phase 2 acceptance criteria are not met
```

Each phase builds infrastructure that the next phase depends on. Skipping creates architectural debt that is almost impossible to resolve later.

## Rule 2: Never Implement Future Phases Early

```
✅ Correct:  Implement COA Approval Dialog when Phase 6 begins
❌ Wrong:    Implementing COA Approval Dialog while in Phase 3
```

Future phase code written early will conflict with the infrastructure built in intervening phases.

## Rule 3: Always Update Project Status

After EVERY task completion:
```
1. Mark task as "done" in AI_BIOS_PROJECT_STATUS.md Current Sprint Tasks
2. Move task to Completed Tasks section
3. Update Overall Completion %
4. Append session log entry
5. Commit AI_BIOS_PROJECT_STATUS.md along with code changes
```

## Rule 4: Always Complete Acceptance Criteria

A phase is NOT complete until EVERY acceptance criterion in its checklist is met:
```
✅ Criterion met:  Write test → test passes → mark criterion checked
❌ Criterion skipped: "close enough" is not acceptable
❌ Criterion assumed: "it should work" is not verified
```

## Rule 5: Always Run Tests Before Moving On

```bash
# After every task:
cd backend && pytest tests/ -x --tb=short

# After every phase:
cd backend && pytest tests/ -v --cov=app --cov-report=term
cd frontend && npm run test
```

## Rule 6: Architecture Decisions Must Update the Master

If during implementation you discover a necessary architectural change:
```
1. Stop implementation
2. Update AI_BIOS_MASTER.md with the new decision
3. Document the change in AI_BIOS_PROJECT_STATUS.md Architecture Drift Tracker
4. Resume implementation using the updated spec
```

Do NOT silently deviate from the architecture without updating the master document.

## Rule 7: Commit Message Standard

```
Format: type(scope): description

Types:   feat | fix | test | refactor | docs | chore | security
Scopes:  auth | datasets | analysis | agents | coa | frontend | db | ci | langgraph | rag | forecast | report

Examples:
  feat(agents): implement InsightAgent with structured output schema
  feat(rag): add ChromaDB embedding pipeline with batch processing
  fix(langgraph): correct conditional routing after DataCleaningAgent
  test(sql): add 20 NL-to-SQL test cases with safety verification
  docs(status): update Phase 3 completion in PROJECT_STATUS.md
```

---

# A4. Reference Implementation Snippets

> These are reference examples — not full implementations. Use them as starting points and copy-paste foundations. Full implementation specs are in the numbered sections of this document.

---

## A4.1 Frontend Reference

### Next.js App Structure (`frontend/app/layout.tsx`)
```typescript
// Root layout — wraps all pages with auth provider and query client
import { Inter } from 'next/font/google'
import { Providers } from '@/components/providers'
import { Toaster } from '@/components/ui/sonner'

const inter = Inter({ subsets: ['latin'] })

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <Providers>
          {children}
          <Toaster position="bottom-right" richColors />
        </Providers>
      </body>
    </html>
  )
}
```

### API Client (`frontend/lib/api-client.ts`)
```typescript
import axios from 'axios'
import { useAuthStore } from '@/stores/auth-store'

const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  headers: { 'Content-Type': 'application/json' },
})

// Attach JWT to every request
apiClient.interceptors.request.use((config) => {
  const token = useAuthStore.getState().accessToken
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

// Auto-refresh on 401
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      const refreshed = await useAuthStore.getState().refreshToken()
      if (refreshed) return apiClient(error.config)
      useAuthStore.getState().logout()
    }
    return Promise.reject(error)
  }
)

export default apiClient
```

### Dashboard Layout (`frontend/app/(dashboard)/layout.tsx`)
```typescript
import { Sidebar } from '@/components/layout/Sidebar'
import { TopBar } from '@/components/layout/TopBar'

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="flex h-screen bg-slate-50 dark:bg-slate-950">
      <Sidebar />
      <div className="flex flex-1 flex-col overflow-hidden">
        <TopBar />
        <main className="flex-1 overflow-y-auto p-6">
          {children}
        </main>
      </div>
    </div>
  )
}
```

### KPI Card Component (`frontend/components/dashboard/KPICard.tsx`)
```typescript
import { TrendingUp, TrendingDown, Minus } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Sparklines, SparklinesLine } from 'react-sparklines'

interface KPICardProps {
  title: string
  value: number
  format: 'number' | 'currency' | 'percentage'
  previousValue?: number
  sparklineData?: number[]
}

export function KPICard({ title, value, format, previousValue, sparklineData }: KPICardProps) {
  const formatted = format === 'currency'
    ? `$${(value / 1000).toFixed(1)}K`
    : format === 'percentage'
    ? `${(value * 100).toFixed(1)}%`
    : value.toLocaleString()

  const delta = previousValue ? ((value - previousValue) / previousValue) * 100 : null

  return (
    <Card>
      <CardHeader className="pb-2">
        <CardTitle className="text-sm font-medium text-muted-foreground">{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{formatted}</div>
        {delta !== null && (
          <div className={`flex items-center text-xs mt-1 ${delta >= 0 ? 'text-emerald-600' : 'text-red-500'}`}>
            {delta >= 0 ? <TrendingUp className="h-3 w-3 mr-1" /> : <TrendingDown className="h-3 w-3 mr-1" />}
            {Math.abs(delta).toFixed(1)}% vs last period
          </div>
        )}
        {sparklineData && (
          <div className="mt-2">
            <Sparklines data={sparklineData} height={24}>
              <SparklinesLine color="#3b82f6" />
            </Sparklines>
          </div>
        )}
      </CardContent>
    </Card>
  )
}
```

### WebSocket Hook (`frontend/hooks/useWebSocket.ts`)
```typescript
import { useEffect, useRef, useCallback } from 'react'
import { useAuthStore } from '@/stores/auth-store'

type WSEvent = { type: string; payload: Record<string, unknown> }

export function useWebSocket(onMessage: (event: WSEvent) => void) {
  const ws = useRef<WebSocket | null>(null)
  const token = useAuthStore((s) => s.accessToken)

  const connect = useCallback(() => {
    if (!token) return
    ws.current = new WebSocket(`${process.env.NEXT_PUBLIC_WS_URL}?token=${token}`)

    ws.current.onmessage = (e) => {
      try { onMessage(JSON.parse(e.data)) } catch { /* ignore malformed */ }
    }

    ws.current.onclose = () => {
      // Reconnect after 3 seconds on unexpected close
      setTimeout(connect, 3000)
    }

    // Heartbeat
    const ping = setInterval(() => {
      if (ws.current?.readyState === WebSocket.OPEN) {
        ws.current.send(JSON.stringify({ type: 'ping' }))
      }
    }, 30000)

    ws.current.onclose = () => { clearInterval(ping); setTimeout(connect, 3000) }
  }, [token, onMessage])

  useEffect(() => { connect(); return () => ws.current?.close() }, [connect])
}
```

---

## A4.2 Backend Reference

### FastAPI App Entry (`backend/app/main.py`)
```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.v1.router import api_router
from app.api.websocket.handlers import ws_router
from app.db.session import engine
from app.db.base import Base
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.rate_limit_middleware import RateLimitMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown
    await engine.dispose()

app = FastAPI(
    title="AI-BIOS API",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggingMiddleware)
app.add_middleware(RateLimitMiddleware)

app.include_router(api_router, prefix="/api/v1")
app.include_router(ws_router)

@app.get("/health")
async def health():
    return {"status": "healthy", "version": settings.APP_VERSION}
```

### FastAPI Dependency Injection (`backend/app/dependencies.py`)
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import async_session_factory
from app.security.jwt_handler import decode_access_token
from app.db.repositories.user_repo import UserRepository
from app.models.user import User

security = HTTPBearer()

async def get_db() -> AsyncSession:
    async with async_session_factory() as session:
        yield session

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User:
    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid or expired token")
    user_repo = UserRepository(db)
    user = await user_repo.get_by_id(payload["sub"])
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="User not found or inactive")
    return user

def require_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Admin privileges required")
    return current_user
```

### JWT Handler (`backend/app/security/jwt_handler.py`)
```python
from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
from app.config import settings

ALGORITHM = "HS256"

def create_access_token(user_id: str, role: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(
        {"sub": user_id, "role": role, "exp": expire, "type": "access"},
        settings.JWT_SECRET_KEY,
        algorithm=ALGORITHM,
    )

def create_refresh_token(user_id: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    import secrets
    return jwt.encode(
        {"sub": user_id, "exp": expire, "jti": secrets.token_hex(16), "type": "refresh"},
        settings.JWT_SECRET_KEY,
        algorithm=ALGORITHM,
    )

def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            return None
        return payload
    except jwt.PyJWTError:
        return None
```

### Celery Task Example (`backend/app/tasks/analysis_tasks.py`)
```python
from celery import shared_task
from app.tasks.celery_app import celery_app
from app.workflows.analysis_workflow import build_analysis_graph
from app.db.repositories.analysis_repo import AnalysisRepository
from app.cache.client import redis_client
import logging

logger = logging.getLogger(__name__)

@celery_app.task(
    bind=True,
    max_retries=1,
    soft_time_limit=1800,
    time_limit=1900,
    queue="compute",
)
def run_analysis_workflow(self, analysis_id: str, initial_state: dict):
    """
    Execute full LangGraph analysis workflow for a dataset.
    Handles retry on transient failures. Saves results to DB on completion.
    """
    try:
        graph = build_analysis_graph()
        config = {"configurable": {"thread_id": analysis_id}}
        final_state = graph.invoke(initial_state, config=config)
        # Results persisted inside graph nodes themselves
        logger.info(f"Analysis {analysis_id} completed successfully")
        return {"status": "completed", "analysis_id": analysis_id}
    except Exception as exc:
        logger.error(f"Analysis {analysis_id} failed: {exc}")
        if self.request.retries < self.max_retries:
            raise self.retry(exc=exc, countdown=30)
        # Update DB status to failed
        raise
```

---

## A4.3 Database Reference

### SQLAlchemy Base Model (`backend/app/db/base.py`)
```python
from datetime import datetime, timezone
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Base(DeclarativeBase):
    pass

class TimestampMixin:
    """Add created_at and updated_at to any model."""
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(),
        onupdate=func.now(), nullable=False
    )
```

### User Model (`backend/app/models/user.py`)
```python
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base, TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False, default="user")
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
```

### Dataset Model (`backend/app/models/dataset.py`)
```python
from sqlalchemy import String, BigInteger, Integer, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base, TimestampMixin
import uuid

class Dataset(Base, TimestampMixin):
    __tablename__ = "datasets"

    project_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False, index=True)
    uploaded_by: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    source_type: Mapped[str] = mapped_column(String(20), nullable=False)  # csv | xlsx | postgresql | mysql | sqlite
    file_path: Mapped[str] = mapped_column(String(500), nullable=True)
    file_size: Mapped[int] = mapped_column(BigInteger, nullable=True)
    row_count: Mapped[int] = mapped_column(Integer, nullable=True)
    column_count: Mapped[int] = mapped_column(Integer, nullable=True)
    schema_info: Mapped[dict] = mapped_column(JSON, nullable=True)
    profile_summary: Mapped[dict] = mapped_column(JSON, nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="uploading")
    # status options: uploading | processing | ready | error
```

### Alembic Migration Example
```python
# alembic/versions/20240601_120000_create_users_table.py
"""Create users table

Revision ID: a1b2c3d4e5f6
Revises:
Create Date: 2024-06-01 12:00:00
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'a1b2c3d4e5f6'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('hashed_password', sa.String(255), nullable=False),
        sa.Column('full_name', sa.String(100), nullable=False),
        sa.Column('role', sa.String(20), nullable=False, server_default='user'),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    op.create_index('ix_users_email', 'users', ['email'])

def downgrade() -> None:
    op.drop_index('ix_users_email', table_name='users')
    op.drop_table('users')
```

---

## A4.4 LangGraph Reference

### Analysis State Definition (`backend/app/workflows/analysis_workflow.py`)
```python
from typing import TypedDict, Optional, List, Dict, Any
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

class AnalysisState(TypedDict):
    # Identity
    analysis_id: str
    dataset_id: str
    project_id: str
    user_id: str

    # Configuration
    analysis_types: List[str]
    config: Dict[str, Any]

    # Processing state
    current_step: str
    progress_pct: int
    errors: List[str]
    warnings: List[str]
    retry_counts: Dict[str, int]

    # Data paths
    raw_dataframe_path: str
    cleaned_dataframe_path: Optional[str]

    # Agent outputs (accumulated as workflow progresses)
    cleaning_report: Optional[Dict[str, Any]]
    eda_report: Optional[Dict[str, Any]]
    chart_specs: Optional[List[Dict[str, Any]]]
    chart_configs: Optional[List[Dict[str, Any]]]
    insights: Optional[List[Dict[str, Any]]]
    consultant_memo: Optional[str]
    report_path: Optional[str]

    # Metadata
    started_at: str
    completed_at: Optional[str]
```

### Agent Node Example (`backend/app/agents/eda_agent.py`)
```python
import logging
from app.workflows.analysis_workflow import AnalysisState
from app.agents.base_agent import BaseAgent
from app.tools.data_tools import compute_descriptive_stats, compute_correlation_matrix
from app.tools.system_tools import emit_progress_event, log_agent_action

logger = logging.getLogger(__name__)

class EDAAgent(BaseAgent):
    name = "eda_agent"
    model = "gemini-2.5-flash"
    timeout = 180

    async def run(self, state: AnalysisState) -> AnalysisState:
        logger.info(f"EDAAgent starting for analysis {state['analysis_id']}")
        start = time.time()

        try:
            # Run statistical analysis
            stats = compute_descriptive_stats(state["cleaned_dataframe_path"])
            corr = compute_correlation_matrix(state["cleaned_dataframe_path"])

            # Generate AI narrative
            narrative = await self._generate_narrative(stats, corr)

            # Update state
            state["eda_report"] = {
                "statistics": stats,
                "correlation_matrix": corr,
                "narrative": narrative,
                "chart_recommendations": self._recommend_charts(stats),
            }
            state["progress_pct"] = 45
            state["current_step"] = "eda_complete"

            await emit_progress_event(state["analysis_id"], "eda", 45)
            await log_agent_action(state["analysis_id"], self.name, "eda_complete",
                                   {}, state["eda_report"], "success", (time.time()-start)*1000)

        except Exception as e:
            logger.error(f"EDAAgent failed: {e}")
            state["errors"].append(f"EDA: {str(e)}")
            # Graceful degradation — do not re-raise; let workflow continue

        return state

# LangGraph node function (wraps agent)
async def run_eda(state: AnalysisState) -> AnalysisState:
    agent = EDAAgent()
    return await agent.run(state)
```

### Conditional Routing (`backend/app/workflows/analysis_workflow.py`)
```python
def route_after_cleaning(state: AnalysisState) -> str:
    """Route based on cleaning outcome. Proceed even with warnings."""
    if state.get("cleaned_dataframe_path"):
        return "run_eda"
    # Fatal: no cleaned data available
    return "handle_error"

def route_after_consultant(state: AnalysisState) -> str:
    """Route to report generation if requested, otherwise finish."""
    if "report" in state.get("analysis_types", []):
        return "generate_report"
    return END

def build_analysis_graph() -> StateGraph:
    graph = StateGraph(AnalysisState)

    # Register all nodes
    graph.add_node("validate_dataset", validate_dataset)
    graph.add_node("run_data_cleaning", run_data_cleaning)
    graph.add_node("run_eda", run_eda)
    graph.add_node("run_visualization", run_visualization)
    graph.add_node("run_insight_generation", run_insight_generation)
    graph.add_node("run_consultant_analysis", run_consultant_analysis)
    graph.add_node("generate_report", generate_report)
    graph.add_node("handle_error", handle_error)

    # Entry point
    graph.set_entry_point("validate_dataset")

    # Sequential edges
    graph.add_conditional_edges("validate_dataset",
        lambda s: "run_data_cleaning" if not s.get("errors") else "handle_error")
    graph.add_conditional_edges("run_data_cleaning", route_after_cleaning)
    graph.add_edge("run_eda", "run_visualization")
    graph.add_edge("run_visualization", "run_insight_generation")
    graph.add_edge("run_insight_generation", "run_consultant_analysis")
    graph.add_conditional_edges("run_consultant_analysis", route_after_consultant)
    graph.add_edge("generate_report", END)
    graph.add_edge("handle_error", END)

    # Compile with memory checkpointing for resumable workflows
    memory = MemorySaver()
    return graph.compile(checkpointer=memory)
```

---

## A4.5 RAG Reference

### Embedding Pipeline (`backend/app/services/embedding_service.py`)
```python
import google.generativeai as genai
from chromadb import AsyncHttpClient
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

class EmbeddingService:
    def __init__(self):
        self.chroma = AsyncHttpClient(
            host=settings.CHROMA_HOST, port=settings.CHROMA_PORT
        )

    async def create_dataset_collection(self, dataset_id: str):
        return await self.chroma.get_or_create_collection(
            name=f"dataset_{dataset_id}",
            metadata={"hnsw:space": "cosine"},
        )

    def _chunk_dataframe(self, df, dataset_id: str) -> list[dict]:
        """Generate text chunks from a DataFrame for embedding."""
        chunks = []

        # Chunk type 1: Column descriptions
        for col in df.columns:
            dtype = str(df[col].dtype)
            nulls = df[col].isna().sum()
            unique = df[col].nunique()
            desc = f"Column '{col}' ({dtype}): {nulls} nulls, {unique} unique values. "
            if df[col].dtype in ["int64", "float64"]:
                desc += f"Range: {df[col].min():.2f} to {df[col].max():.2f}. Mean: {df[col].mean():.2f}."
            chunks.append({"id": f"{dataset_id}_col_{col}", "text": desc, "type": "column"})

        # Chunk type 2: Row samples (batches of 25 rows)
        sample = df.sample(min(500, len(df)))
        for i in range(0, len(sample), 25):
            batch = sample.iloc[i:i+25]
            text = batch.to_dict(orient="records").__repr__()
            chunks.append({"id": f"{dataset_id}_rows_{i}", "text": text[:2000], "type": "rows"})

        # Chunk type 3: Aggregate facts
        for col in df.select_dtypes(include="number").columns:
            text = f"Total {col}: {df[col].sum():.2f}. Average {col}: {df[col].mean():.2f}."
            chunks.append({"id": f"{dataset_id}_agg_{col}", "text": text, "type": "aggregate"})

        return chunks

    async def embed_and_store(self, dataset_id: str, df) -> int:
        """Embed all dataset chunks and store in ChromaDB."""
        collection = await self.create_dataset_collection(dataset_id)
        chunks = self._chunk_dataframe(df, dataset_id)

        # Batch embed (100 per call to respect rate limits)
        for i in range(0, len(chunks), 100):
            batch = chunks[i:i+100]
            texts = [c["text"] for c in batch]
            result = genai.embed_content(
                model="models/text-embedding-004",
                content=texts,
                task_type="retrieval_document",
            )
            await collection.upsert(
                ids=[c["id"] for c in batch],
                documents=texts,
                embeddings=result["embedding"],
                metadatas=[{"type": c["type"]} for c in batch],
            )

        return len(chunks)

    async def query(self, dataset_id: str, question: str, top_k: int = 10) -> list[str]:
        """Retrieve top-k relevant chunks for a question."""
        collection = await self.create_dataset_collection(dataset_id)
        q_embedding = genai.embed_content(
            model="models/text-embedding-004",
            content=question,
            task_type="retrieval_query",
        )["embedding"]

        results = await collection.query(
            query_embeddings=[q_embedding],
            n_results=top_k,
        )
        return results["documents"][0]
```

---

## A4.6 Forecasting Reference

### Prophet Engine (`backend/app/forecasting/prophet_engine.py`)
```python
import pandas as pd
from prophet import Prophet
from app.forecasting.base import ForecastResult

class ProphetEngine:
    def prepare(self, df: pd.DataFrame, date_col: str, target_col: str) -> pd.DataFrame:
        prepared = df[[date_col, target_col]].copy()
        prepared.columns = ["ds", "y"]
        prepared["ds"] = pd.to_datetime(prepared["ds"])
        prepared = prepared.dropna().sort_values("ds")
        return prepared

    def fit_predict(self, df: pd.DataFrame, horizon: int, freq: str = "D") -> pd.DataFrame:
        model = Prophet(
            yearly_seasonality="auto",
            weekly_seasonality="auto",
            daily_seasonality=False,
            changepoint_prior_scale=0.05,
            interval_width=0.95,
        )
        model.fit(df)
        future = model.make_future_dataframe(periods=horizon, freq=freq)
        forecast = model.predict(future)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper", "trend"]]

    def evaluate(self, model_df: pd.DataFrame, actual_df: pd.DataFrame) -> dict:
        # 80/20 train/test split evaluation
        split = int(len(actual_df) * 0.8)
        test = actual_df.iloc[split:]
        # Run prediction on test portion
        preds = self.fit_predict(actual_df.iloc[:split], len(test))
        preds_test = preds.tail(len(test))
        mape = (abs(test["y"].values - preds_test["yhat"].values) / test["y"].values).mean() * 100
        mae = abs(test["y"].values - preds_test["yhat"].values).mean()
        return {"mape": round(mape, 2), "mae": round(mae, 2), "model": "prophet"}

    def to_recharts(self, forecast: pd.DataFrame, actual: pd.DataFrame) -> dict:
        """Convert forecast + actual to Recharts LineChart config."""
        actual_map = dict(zip(actual["ds"].astype(str), actual["y"]))
        data = []
        for _, row in forecast.iterrows():
            ds = str(row["ds"].date())
            data.append({
                "date": ds,
                "actual": actual_map.get(ds),
                "forecast": round(row["yhat"], 2),
                "lower": round(row["yhat_lower"], 2),
                "upper": round(row["yhat_upper"], 2),
            })
        return {
            "chart_type": "area",
            "data": data,
            "series": [
                {"key": "actual", "label": "Actual", "stroke": "#3b82f6"},
                {"key": "forecast", "label": "Forecast", "stroke": "#f59e0b", "strokeDasharray": "5 5"},
                {"key": "upper", "label": "Upper CI", "stroke": "#d1d5db", "fill": "#f3f4f6"},
                {"key": "lower", "label": "Lower CI", "stroke": "#d1d5db"},
            ],
        }
```

### XGBoost Engine (`backend/app/forecasting/xgboost_engine.py`)
```python
import pandas as pd
import numpy as np
from xgboost import XGBRegressor

class XGBoostTimeSeriesEngine:
    def engineer_features(self, df: pd.DataFrame, target_col: str, date_col: str) -> pd.DataFrame:
        df = df.copy()
        df[date_col] = pd.to_datetime(df[date_col])
        df = df.sort_values(date_col)
        y = df[target_col]

        # Lag features
        for lag in [1, 3, 7, 14, 28]:
            df[f"lag_{lag}"] = y.shift(lag)

        # Rolling statistics
        for window in [7, 14, 28]:
            df[f"roll_mean_{window}"] = y.shift(1).rolling(window).mean()
            df[f"roll_std_{window}"] = y.shift(1).rolling(window).std()

        # Date features
        df["day_of_week"] = df[date_col].dt.dayofweek
        df["month"] = df[date_col].dt.month
        df["quarter"] = df[date_col].dt.quarter
        df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)
        df["days_since_start"] = (df[date_col] - df[date_col].min()).dt.days

        return df.dropna()

    def fit(self, X: pd.DataFrame, y: pd.Series) -> XGBRegressor:
        model = XGBRegressor(
            n_estimators=200, max_depth=6, learning_rate=0.05,
            subsample=0.8, colsample_bytree=0.8,
            early_stopping_rounds=20, eval_metric="mae",
        )
        split = int(len(X) * 0.8)
        model.fit(X.iloc[:split], y.iloc[:split],
                  eval_set=[(X.iloc[split:], y.iloc[split:])],
                  verbose=False)
        return model
```

---

## A4.7 Reporting Reference

### PDF Generator (`backend/app/reporting/pdf_generator.py`)
```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.colors import HexColor

ACCENT = HexColor("#3B82F6")
DARK   = HexColor("#1E293B")
LIGHT  = HexColor("#94A3B8")

def build_pdf_report(output_path: str, data: dict) -> str:
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=25*mm, rightMargin=25*mm,
        topMargin=20*mm, bottomMargin=20*mm,
    )
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle("H1", fontSize=24, textColor=DARK, spaceAfter=12, fontName="Helvetica-Bold")
    h2 = ParagraphStyle("H2", fontSize=16, textColor=DARK, spaceAfter=8)
    body = ParagraphStyle("Body", fontSize=10, leading=14, textColor=HexColor("#475569"))

    story = []

    # Cover
    story.append(Paragraph(data["title"], h1))
    story.append(Paragraph(f"Dataset: {data['dataset_name']} | {data['date']}", body))
    story.append(Spacer(1, 12))

    # Executive Summary
    story.append(Paragraph("Executive Summary", h2))
    story.append(Paragraph(data["executive_summary"], body))
    story.append(Spacer(1, 12))

    # Insights
    for insight in data.get("insights", [])[:5]:
        story.append(Paragraph(f"• {insight['title']}", h2))
        story.append(Paragraph(insight["description"], body))
        story.append(Spacer(1, 6))

    # Charts (embedded PNGs)
    for chart_path in data.get("chart_paths", []):
        story.append(Image(chart_path, width=160*mm, height=80*mm))
        story.append(Spacer(1, 8))

    doc.build(story)
    return output_path
```

### PPTX Generator (`backend/app/reporting/pptx_generator.py`)
```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

ACCENT_RGB = RGBColor(0x3B, 0x82, 0xF6)
DARK_RGB   = RGBColor(0x1E, 0x29, 0x3B)

def build_pptx_report(output_path: str, data: dict) -> str:
    prs = Presentation()
    prs.slide_width  = Inches(13.33)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]  # blank

    def add_title_slide(title: str, subtitle: str):
        slide = prs.slides.add_slide(blank_layout)
        # Accent header band
        header = slide.shapes.add_shape(1, 0, 0, prs.slide_width, Inches(1.5))
        header.fill.solid(); header.fill.fore_color.rgb = ACCENT_RGB
        tf = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12), Inches(0.9)).text_frame
        tf.text = title
        tf.paragraphs[0].font.size = Pt(36)
        tf.paragraphs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        # Subtitle
        sub = slide.shapes.add_textbox(Inches(0.5), Inches(1.7), Inches(12), Inches(0.5)).text_frame
        sub.text = subtitle
        sub.paragraphs[0].font.size = Pt(16)
        sub.paragraphs[0].font.color.rgb = DARK_RGB

    def add_chart_slide(title: str, chart_path: str, caption: str):
        slide = prs.slides.add_slide(blank_layout)
        tf = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12), Inches(0.6)).text_frame
        tf.text = title; tf.paragraphs[0].font.size = Pt(20)
        slide.shapes.add_picture(chart_path, Inches(0.5), Inches(0.9), Inches(12), Inches(5.5))
        cap = slide.shapes.add_textbox(Inches(0.5), Inches(6.5), Inches(12), Inches(0.5)).text_frame
        cap.text = caption; cap.paragraphs[0].font.size = Pt(10)
        cap.paragraphs[0].font.color.rgb = RGBColor(0x64, 0x74, 0x8B)

    add_title_slide(data["title"], data["dataset_name"])
    for chart_path, caption in zip(data.get("chart_paths", []), data.get("chart_captions", [])):
        add_chart_slide("Analysis Result", chart_path, caption)

    prs.save(output_path)
    return output_path
```

---

## A4.8 Computer Operator Agent Reference

### COA Action Schema (`backend/app/schemas/coa.py`)
```python
from pydantic import BaseModel
from enum import Enum
from typing import Any, Optional
import uuid

class COAActionType(str, Enum):
    OPEN_APPLICATION  = "open_application"
    OPEN_FILE         = "open_file"
    RUN_SCRIPT        = "run_script"
    EXECUTE_SQL       = "execute_sql"
    EXPORT_TO_EXCEL   = "export_to_excel"
    OPEN_URL          = "open_url"
    FILL_FORM         = "fill_form"
    RUN_WORKFLOW      = "run_workflow"

class RiskLevel(str, Enum):
    LOW      = "low"
    MEDIUM   = "medium"
    HIGH     = "high"
    CRITICAL = "critical"

class ApprovalScope(str, Enum):
    ONCE    = "once"
    SESSION = "session"
    ALWAYS  = "always"

class COAActionRequest(BaseModel):
    action_type:        COAActionType
    target_application: str
    action_params:      dict[str, Any]
    reason:             str
    expected_outcome:   str
    risk_level:         RiskLevel
    rollback_strategy:  Optional[str] = None
    timeout_seconds:    int = 300

class COAApproveRequest(BaseModel):
    scope: ApprovalScope

class COAActionResponse(BaseModel):
    action_id:       uuid.UUID
    approval_status: str   # pending | approved | denied | auto_denied
    expires_at:      str   # ISO8601
```

### Approval Flow (`backend/app/services/approval_manager.py`)
```python
import asyncio, hmac, hashlib, secrets, json
from datetime import datetime, timedelta, timezone
from app.cache.client import redis_client
from app.api.websocket.manager import ws_manager
from app.config import settings

class ApprovalManager:
    TIMEOUT = 300  # 5 minutes

    async def request_approval(self, action: dict, user_id: str) -> str:
        """Create pending approval, notify user, start timeout countdown."""
        action_id = secrets.token_urlsafe(16)

        # Store pending action in Redis
        await redis_client.setex(
            f"coa:pending:{action_id}",
            self.TIMEOUT,
            json.dumps({**action, "action_id": action_id, "user_id": user_id}),
        )

        # Notify user via WebSocket
        await ws_manager.broadcast_to_user(user_id, "coa.approval_required", {
            "action_id": action_id,
            "action_type": action["action_type"],
            "target_application": action["target_application"],
            "reason": action["reason"],
            "expected_outcome": action["expected_outcome"],
            "risk_level": action["risk_level"],
            "expires_at": (datetime.now(timezone.utc) + timedelta(seconds=self.TIMEOUT)).isoformat(),
        })

        return action_id

    def generate_execution_token(self, action_id: str, user_id: str) -> str:
        """Generate HMAC-signed single-use token for local agent verification."""
        message = f"{action_id}:{user_id}:{secrets.token_hex(8)}"
        sig = hmac.new(
            settings.COA_LOCAL_AGENT_WS_SECRET.encode(),
            message.encode(),
            hashlib.sha256,
        ).hexdigest()
        return f"{message}:{sig}"

    def verify_execution_token(self, token: str) -> bool:
        """Verify HMAC signature on token. Returns False if tampered."""
        parts = token.rsplit(":", 1)
        if len(parts) != 2: return False
        message, sig = parts
        expected = hmac.new(
            settings.COA_LOCAL_AGENT_WS_SECRET.encode(),
            message.encode(), hashlib.sha256,
        ).hexdigest()
        return hmac.compare_digest(sig, expected)
```

---

## A4.9 Deployment Reference

### Docker Compose (Local Development)

```yaml
# docker-compose.yml — minimal local development stack
version: '3.9'

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: aibios
      POSTGRES_USER: aibios
      POSTGRES_PASSWORD: aibios_dev
    ports: ["5432:5432"]
    volumes: [postgres_data:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U aibios"]
      interval: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s

  chromadb:
    image: chromadb/chroma:latest
    ports: ["8001:8000"]
    volumes: [chroma_data:/chroma/chroma]

  backend:
    build: ./backend
    ports: ["8000:8000"]
    env_file: [.env]
    volumes: [./backend:/app, uploads:/app/uploads]
    depends_on:
      postgres: {condition: service_healthy}
      redis: {condition: service_healthy}
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

  worker:
    build: ./backend
    env_file: [.env]
    volumes: [./backend:/app, uploads:/app/uploads]
    command: celery -A app.tasks.celery_app worker --loglevel=info -Q high_priority,compute,ai,reports,low_priority

volumes:
  postgres_data:
  chroma_data:
  uploads:
```

### Environment Variables (`.env.example`)
```bash
# Application
APP_NAME=AI-BIOS
APP_ENV=development
DEBUG=true
LOG_LEVEL=INFO

# Database
DATABASE_URL=postgresql+asyncpg://aibios:aibios_dev@localhost:5432/aibios

# Redis
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2

# Auth
JWT_SECRET_KEY=CHANGE_ME_64_CHAR_HEX_STRING_HERE
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
PASSWORD_HASH_ROUNDS=12

# AI
GEMINI_API_KEY=your-gemini-api-key-here
GEMINI_PRO_MODEL=gemini-2.5-pro
GEMINI_FLASH_MODEL=gemini-2.5-flash

# ChromaDB
CHROMA_HOST=localhost
CHROMA_PORT=8001

# Storage
STORAGE_BACKEND=local
STORAGE_LOCAL_PATH=./uploads
MAX_UPLOAD_SIZE_MB=500

# Security
ENCRYPTION_KEY=CHANGE_ME_FERNET_KEY_HERE
ALLOWED_ORIGINS=http://localhost:3000

# COA
COA_APPROVAL_TIMEOUT_SECONDS=300
COA_LOCAL_AGENT_WS_SECRET=CHANGE_ME_HMAC_SECRET_HERE
```


---

> **AI_BIOS_MASTER.md — VERSION 1.0.0 → Updated with v1.1 Maintainability Standards**
> **60+ Sections | Reference Implementation Snippets | Project Execution Rules | Quick-Resume Protocol**
>
> SINGLE SOURCE OF TRUTH. Read this first. Update this when architecture changes.
> Build something extraordinary. 🚀


---

# A5. Root Project Structure (Updated with Mandatory Files)

Every AI-BIOS repository MUST have these three files at the root level.
They are mandatory project files, not optional documentation.

```
ai-bios/                                 ← Repository root
│
├── AI_BIOS_MASTER.md                    ← MANDATORY: Complete architecture SSOT
├── AI_BIOS_MASTER_LEARNING_EDITION.md   ← MANDATORY: Learning guide + solo dev strategy
├── AI_BIOS_PROJECT_STATUS.md            ← MANDATORY: Operational memory + session tracker
│
├── frontend/                            ← Next.js 15 application
│   ├── app/                             ← App Router pages
│   ├── components/                      ← Reusable components
│   ├── hooks/                           ← Custom React hooks
│   ├── lib/                             ← Client utilities (api-client.ts)
│   ├── stores/                          ← Zustand state stores
│   ├── types/                           ← TypeScript types
│   ├── public/                          ← Static assets
│   ├── next.config.ts
│   ├── tailwind.config.ts
│   ├── tsconfig.json
│   ├── components.json                  ← ShadCN config
│   └── package.json
│
├── backend/                             ← FastAPI application
│   ├── app/
│   │   ├── main.py                      ← FastAPI entry point
│   │   ├── config.py                    ← pydantic-settings
│   │   ├── dependencies.py              ← DI: get_db, get_current_user
│   │   ├── api/v1/                      ← API routers
│   │   ├── models/                      ← SQLAlchemy models
│   │   ├── schemas/                     ← Pydantic schemas
│   │   ├── services/                    ← Business logic
│   │   ├── agents/                      ← 11 AI agents
│   │   ├── workflows/                   ← LangGraph graphs
│   │   ├── tools/                       ← Agent tools
│   │   ├── analysis/                    ← Analysis engines
│   │   ├── forecasting/                 ← Forecasting engines
│   │   ├── reporting/                   ← PDF + PPTX generators
│   │   ├── db/                          ← Database layer
│   │   ├── cache/                       ← Redis client
│   │   ├── tasks/                       ← Celery tasks
│   │   ├── middleware/                  ← FastAPI middleware
│   │   ├── security/                    ← JWT, RBAC, audit
│   │   └── utils/                       ← Utilities
│   ├── tests/                           ← All tests
│   ├── alembic/                         ← DB migrations
│   ├── scripts/                         ← Dev scripts (seed, etc.)
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   ├── alembic.ini
│   └── Dockerfile
│
├── aibios-local-agent/                  ← Phase 6: Desktop automation agent
│   ├── agent/
│   │   ├── main.py                      ← Local agent entry point
│   │   ├── ws_client.py                 ← WebSocket client
│   │   ├── security.py                  ← HMAC token verification
│   │   └── handlers/                    ← Action handlers
│   │       ├── open_application.py
│   │       ├── open_file.py
│   │       ├── run_script.py
│   │       ├── open_url.py
│   │       └── export_to_excel.py
│   ├── requirements.txt
│   └── README.md
│
├── docker/                              ← Docker configurations
│   ├── backend.Dockerfile
│   └── frontend.Dockerfile
│
├── .github/
│   └── workflows/
│       ├── ci.yml                       ← PR checks
│       └── deploy.yml                   ← Staging + production deploy
│
├── scripts/                             ← Dev ops scripts
│   ├── setup.sh                         ← First-time setup
│   └── generate_secrets.py              ← JWT + Fernet key generation
│
├── docker-compose.yml                   ← Local development stack
├── docker-compose.prod.yml              ← Production stack
├── .env.example                         ← All required env vars (no secrets)
├── .gitignore                           ← Python + Node + secrets
├── Makefile                             ← Common commands
├── langgraph.json                       ← LangGraph Studio config
└── README.md                            ← Project overview + setup

```

## File Purpose Summary

| File | Read When | Updated When |
|------|-----------|-------------|
| `AI_BIOS_MASTER.md` | Start of every session (required) | Architecture changes only |
| `AI_BIOS_MASTER_LEARNING_EDITION.md` | Learning phase transitions | Learning approach changes |
| `AI_BIOS_PROJECT_STATUS.md` | Before every session (required) | After EVERY task completion |
| `.env` | Never committed | Locally only |
| `langgraph.json` | When adding new LangGraph graphs | Phase 3+ |

## langgraph.json Configuration

```json
{
  "dependencies": ["."],
  "graphs": {
    "analysis_workflow": "./app/workflows/analysis_workflow.py:build_analysis_graph",
    "chat_workflow":     "./app/workflows/chat_workflow.py:build_chat_graph",
    "forecast_workflow": "./app/workflows/forecast_workflow.py:build_forecast_graph",
    "coa_workflow":      "./app/workflows/coa_workflow.py:build_coa_graph"
  },
  "env": ".env"
}
```

Start LangGraph Studio:
```bash
cd backend
langgraph dev
# Open: http://localhost:8123
```



---

# A6. Project Context Loading Protocol

> Full protocol: AI_BIOS_MASTER_LEARNING_EDITION.md Section A6
> This summary applies to all AI coding agents working from this document.

## A6.1 Mandatory Pre-Implementation Inspection

Before generating or modifying any code, every AI tool MUST inspect:

| # | What to Inspect | Where | Compare Against |
|---|----------------|-------|----------------|
| 1 | Folder structure | `ls -R` from project root | Section A5 of this document |
| 2 | Existing source code | `backend/app/` + `frontend/` | Section 5 folder spec |
| 3 | Existing APIs | `backend/app/api/v1/*.py` | Section 7 API architecture |
| 4 | Existing DB models | `backend/app/models/` + `alembic/versions/` | Section 6 ER diagram |
| 5 | Existing LangGraph workflows | `backend/app/workflows/*.py` | Section 10 / Section 30 |
| 6 | Existing agents | `backend/app/agents/*.py` | Section 9 / Section 51 |
| 7 | Existing prompts | Agent files — system prompt strings | Section 31 |
| 8 | Current dependencies | `requirements.txt` + `package.json` | Section 41 |
| 9 | Project status | `AI_BIOS_PROJECT_STATUS.md` | Current phase, sprint, task |
| 10 | Git state | `git branch` + `git log --oneline -5` | Expected branch |

## A6.2 Architecture Drift Response

If the codebase differs from this document's specification:

```
Intentional deviation  →  Update AI_BIOS_MASTER.md + record in Drift Tracker
Accidental deviation   →  Fix the implementation + record in Drift Tracker
No deviation           →  Proceed with next task
```

Never proceed with a new task while unresolved drift exists.

---

# A7. AI Development Startup Checklist

> Mandatory before every coding session. No exceptions.

```
□ 1.  Read AI_BIOS_MASTER.md (this file) — architecture for current phase
□ 2.  Read AI_BIOS_MASTER_LEARNING_EDITION.md — learning context + tool assignments
□ 3.  Read AI_BIOS_PROJECT_STATUS.md — current operational state
□ 4.  Inspect project folder structure vs Section A5 spec
□ 5.  Inspect existing source code — do not regenerate what exists
□ 6.  Inspect current dependencies vs Section 41
□ 7.  Inspect current LangGraph workflows vs Section 10 (Phase 3+)
□ 8.  Determine active phase from PROJECT_STATUS.md
□ 9.  Determine active sprint from PROJECT_STATUS.md
□ 10. Determine active task — first "todo" in Current Sprint Tasks
```

Only after all 10 steps: begin implementation.

---

# A8. IDE Responsibility Matrix (Summary)

> Full specification: AI_BIOS_MASTER_LEARNING_EDITION.md Section A8

| Tool | Role | Primary Use | Avoid |
|------|------|-------------|-------|
| **Cursor** | Primary Software Engineer | FastAPI, Next.js, LangGraph, DB, refactoring | Long-form research, concept learning |
| **Antigravity** | Boilerplate Generator | CRUD APIs, schemas, models, UI scaffolding | Agent architecture, workflow design |
| **VS Code Copilot** | Micro Coding Assistant | Functions, unit tests, bug fixes, inline completion | Architecture decisions, multi-file features |
| **Claude** | Principal Architect | Architecture reviews, agent reviews, documentation | Large boilerplate generation |
| **ChatGPT** | Senior Systems Engineer | Debugging, tradeoff analysis, design discussions | AI-BIOS-specific architecture (no MASTER.md context) |
| **Gemini Chat** | Research Engineer | LangGraph learning, RAG learning, concept research | Code generation, architecture decisions |
| **Google AI Studio** | Prompt Engineering Lab | Agent prompts, system prompts, RAG prompts, output schema testing | Code generation |
| **LangGraph Studio** | Agent Observatory | Workflow debugging, state inspection, graph visualization | Writing code (not an IDE) |

### Free-Tier Escalation Chain

```
Implementation:  Cursor → Antigravity → VS Code Copilot
Architecture:    Claude → ChatGPT → Gemini Chat
Prompts:         Google AI Studio (always generous free tier)
Debugging:       LangGraph Studio (always free, local)
Learning:        Gemini Chat (always available, browser-based)
```

**Cost target: $0/month** during all development phases.

