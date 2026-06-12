# AI_BIOS_MASTER_LEARNING_EDITION.md
# AI Business Intelligence Operating System
## Learning Edition — Solo Developer Agentic AI Project

> **Version:** 1.1.0 — Learning Edition
> **Status:** Active Learning Project
> **Document Classification:** Solo Developer Learning Blueprint
> **Based On:** AI_BIOS_MASTER.md v1.0.0
> **Last Updated:** 2026-06-05
> **Total Learning Phases:** 7
> **Estimated Developer:** 1 Solo Developer

---

> ⚠️ **PURPOSE STATEMENT:** This is NOT a SaaS business project. This is a structured learning project designed to teach Agentic AI, LangGraph, RAG, multi-agent orchestration, forecasting, report generation, SQL agents, Computer Operator Agents, Power BI integration, and production-grade AI architecture — through building a real, working system.

> ⚠️ **AGENT INSTRUCTION:** This document is the SINGLE SOURCE OF TRUTH for AI-BIOS Learning Edition. Implement phase by phase. Reference the Learning Roadmap in Section L1 to understand what you are learning in each phase. Reference Section 28 checklists after completing each implementation phase.

---

## Table of Contents

### Learning-Specific Sections
- [L1. Project Purpose & Learning Goals](#l1-project-purpose--learning-goals)
- [L2. Learning Roadmap (7 Phases)](#l2-learning-roadmap-7-phases)
- [L3. Tool Usage Guide](#l3-tool-usage-guide)
- [L4. Solo Developer Implementation Strategy](#l4-solo-developer-implementation-strategy)
- [L5. Deployment Strategy (Learning → Portfolio → Desktop Agent)](#l5-deployment-strategy)
- [L6. Human Approval Layer](#l6-human-approval-layer)
- [L7. Simplified RBAC (Admin + User)](#l7-simplified-rbac)

### Core Architecture Sections (Preserved from v1.0.0)
1. [Executive Overview (Revised)](#1-executive-overview-revised)
2. [Functional Requirements](#2-functional-requirements)
3. [System Architecture](#3-system-architecture)
4. [Technology Decisions](#4-technology-decisions)
5. [Folder Structure](#5-folder-structure)
6. [Database Architecture](#6-database-architecture)
7. [API Architecture](#7-api-architecture)
8. [Authentication & Authorization](#8-authentication--authorization)
9. [Multi-Agent Architecture](#9-multi-agent-architecture)
10. [LangGraph Workflow](#10-langgraph-workflow)
11. [Data Analysis Engine](#11-data-analysis-engine)
12. [Visualization Engine](#12-visualization-engine)
13. [Forecasting Engine](#13-forecasting-engine)
14. [Reporting Engine](#14-reporting-engine)
15. [Chat With Data (RAG)](#15-chat-with-data-rag)
16. [File Management System](#16-file-management-system)
17. [SQL Integration](#17-sql-integration)
18. [Power BI Integration](#18-power-bi-integration)
19. [Computer Operator Agent](#19-computer-operator-agent)
20. [Security Architecture](#20-security-architecture)
21. [Performance Architecture](#21-performance-architecture)
22. [Monitoring & Observability](#22-monitoring--observability)
23. [Testing Strategy](#23-testing-strategy)
24. [CI/CD Pipeline](#24-cicd-pipeline)
25. [Implementation Phase Tasks](#25-implementation-phase-tasks)
26. [Cursor Development Rules](#26-cursor-development-rules)
27. [Completion Checklist](#27-completion-checklist)
28. [Agent Tool Definitions](#28-agent-tool-definitions)
29. [Pydantic Schema Reference](#29-pydantic-schema-reference)
30. [LangGraph State Machines (Extended)](#30-langgraph-state-machines-extended)
31. [Agent Prompts Reference](#31-agent-prompts-reference)
32. [WebSocket Event Specification](#32-websocket-event-specification)
33. [Data Flow Diagrams](#33-data-flow-diagrams)
34. [Reporting Engine Extended](#34-reporting-engine-extended)
35. [Forecasting Engine Extended](#35-forecasting-engine-extended)
36. [Security Threat Model](#36-security-threat-model)
37. [Error Recovery Runbook](#37-error-recovery-runbook)
38. [Backend Service Layer](#38-backend-service-layer)
39. [Environment Variables Reference](#39-environment-variables-reference)
40. [docker-compose.yml Reference](#40-docker-composeyml-reference)
41. [Requirements Files](#41-requirements-files)
42. [Glossary](#42-glossary)

---

# L1. Project Purpose & Learning Goals

## L1.1 What This Project Is

AI-BIOS Learning Edition is a solo developer project built for the explicit purpose of learning production-grade Agentic AI development. It is a complete, working Business Intelligence platform — not a toy or tutorial — but its primary purpose is to teach, not to generate revenue.

By building AI-BIOS Learning Edition from scratch, you will understand:

- How multi-agent systems are architectured and orchestrated
- How LangGraph manages state across complex multi-step AI workflows
- How RAG (Retrieval-Augmented Generation) works in a real application
- How to build SQL agents that safely query live databases
- How to build a Computer Operator Agent with human-in-the-loop approval
- How to connect AI systems to Power BI and other desktop applications
- How forecasting models (Prophet, XGBoost) are selected, trained, and evaluated
- How PDF and PPTX reports are generated programmatically from AI output
- How to design production-grade AI architectures that are secure and observable
- How to build tool-calling agents with structured output schemas
- How to design human-approval systems for autonomous AI actions

## L1.2 Primary Learning Objectives

| # | Learning Objective | Covered In Phase |
|---|-------------------|-----------------|
| 1 | FastAPI async architecture + Celery task queues | Phase 1 |
| 2 | Data profiling, EDA, pandas processing pipelines | Phase 2 |
| 3 | RAG architecture: ChromaDB + Gemini embeddings + retrieval | Phase 3 |
| 4 | LangGraph: state design, node routing, conditional edges | Phase 3 |
| 5 | Chat agent with context memory and source citations | Phase 3 |
| 6 | Forecasting: Prophet, XGBoost, model selection logic | Phase 4 |
| 7 | Report generation: ReportLab PDF + python-pptx PPTX | Phase 4 |
| 8 | Multi-agent orchestration: 11 agents coordinated by LangGraph | Phase 5 |
| 9 | SQL agent: NL-to-SQL with safety validation | Phase 5 |
| 10 | LangGraph Studio: visual debugging of agent workflows | Phase 5 |
| 11 | Computer Operator Agent: desktop automation + approval layer | Phase 6 |
| 12 | Human-in-the-loop: approval dialogs, permission scopes, audit trails | Phase 6 |
| 13 | Power BI integration: REST API, dataset publishing, OAuth | Phase 7 |
| 14 | Tool calling: structured tool definitions, tool routing | Phase 5 |

## L1.3 What This Project Is NOT

- ❌ Not a SaaS business (no pricing, no billing, no subscription tiers)
- ❌ Not a multi-tenant platform (no organizations, no enterprise SSO)
- ❌ Not a 20-engineer project (all decisions optimized for solo development)
- ❌ Not a production SaaS at this stage (learning first, portfolio second)
- ❌ Not a cloud-first system (local-first for learning, cloud optional for portfolio)

## L1.4 What You Will Have When Complete

A fully working AI-powered Business Intelligence platform that you:
- Built yourself, understanding every component
- Can explain to any interviewer or employer in depth
- Can deploy as a portfolio project
- Can extend into a real product if desired later
- Can use as a reference implementation for any future agentic AI project

---

# L2. Learning Roadmap (7 Phases)

## L2.1 Phase 1 — Backend Foundations

**Duration:** 2–3 weeks
**Focus:** Build the production-grade backend skeleton before adding any AI

### Concepts Learned
- FastAPI application structure and async architecture
- SQLAlchemy ORM models and Alembic migrations
- JWT authentication (access tokens + refresh tokens)
- Redis-based token storage and caching
- Celery task queue with Redis broker
- WebSocket manager for real-time events
- Repository pattern for database access
- Pydantic models for request/response validation
- Docker Compose for local service orchestration

### Technologies Learned
- **FastAPI** — async Python web framework
- **SQLAlchemy 2.0** — async ORM with PostgreSQL
- **Alembic** — database migration management
- **PostgreSQL** — relational database (via Docker)
- **Redis** — cache + message broker (via Docker)
- **Celery** — distributed task queue
- **JWT** — stateless authentication
- **Pydantic v2** — data validation and serialization
- **Docker Compose** — local multi-service environment

### Deliverables
- Running FastAPI application with all folder structure per Section 5
- All database models created with migrations
- Auth endpoints: register, login, refresh, logout
- JWT middleware with role checking
- Celery worker running background tasks
- WebSocket manager broadcasting events
- Redis cache + session store working
- `/health` endpoint for all services
- Running Next.js frontend shell with auth pages

### Acceptance Criteria
- [ ] `docker-compose up` starts all services (postgres, redis, chromadb)
- [ ] `POST /auth/register` creates a user with hashed password
- [ ] `POST /auth/login` returns access + refresh token pair
- [ ] `POST /auth/refresh` issues new access token from refresh token
- [ ] Protected endpoints return 401 without token
- [ ] Celery worker processes a test task successfully
- [ ] WebSocket sends a test event to connected client
- [ ] All database tables created via `alembic upgrade head`

### Recommended Resources
- FastAPI official docs: https://fastapi.tiangolo.com
- SQLAlchemy 2.0 async tutorial: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
- LangGraph docs (read ahead): https://langchain-ai.github.io/langgraph/
- Celery with Redis: https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html

### Key Learning Insight
> Phase 1 has zero AI. That is intentional. You must deeply understand the infrastructure before adding agents on top. Every agent, every workflow, every embedding runs on this foundation. If Phase 1 is weak, everything above it will be fragile.

---

## L2.2 Phase 2 — Dataset Intelligence

**Duration:** 2 weeks
**Focus:** Build the data ingestion, profiling, and cleaning pipeline

### Concepts Learned
- File parsing: CSV encoding detection, XLSX multi-sheet handling
- Data type inference: how to detect numeric/categorical/date/text/boolean
- Statistical profiling: distributions, null analysis, outlier detection
- Automated data cleaning: imputation strategies, duplicate removal
- Chunked processing for large files (memory management)
- Celery task design for async file processing
- WebSocket-driven progress reporting

### Technologies Learned
- **pandas** — DataFrame operations, type coercion, profiling
- **python-magic** — file MIME type detection
- **chardet** — CSV encoding auto-detection
- **openpyxl** — XLSX parsing
- **scipy** — statistical functions (skewness, kurtosis, IQR)
- **scikit-learn** — Isolation Forest for outlier detection
- **ydata-profiling** — extended dataset profiling

### Deliverables
- File upload endpoint with full validation pipeline
- CSV and XLSX parser with encoding detection
- Automated column type detection
- Statistical profiling per column (all metrics from Section 11.1)
- Data cleaning agent (nulls, duplicates, type coercion)
- Dataset profile API and frontend profile page
- Upload progress via WebSocket events
- ChromaDB dataset collection created on upload (even if not yet queried)

### Acceptance Criteria
- [ ] CSV upload completes in < 30s for files < 50MB
- [ ] XLSX multi-sheet detection and selection works
- [ ] Files > 500MB rejected with 413 error
- [ ] Profile generated with: row count, column count, null%, unique count, stats per column
- [ ] Quality score (0–100) calculated and displayed
- [ ] DataCleaningAgent handles nulls with correct strategy per column type
- [ ] Cleaned DataFrame saved and path stored in analysis state
- [ ] WebSocket emits `dataset.ready` event on profile completion

### Recommended Resources
- pandas User Guide: https://pandas.pydata.org/docs/user_guide/
- python-magic: https://github.com/ahupp/python-magic
- ydata-profiling: https://docs.profiling.ydata.ai/

### Key Learning Insight
> This phase teaches you how raw messy data becomes structured analysis-ready data. Every AI system that works with real-world data has a pipeline like this. Understanding it makes you a better AI engineer.

---

## L2.3 Phase 3 — RAG & Chat With Data

**Duration:** 3 weeks
**Focus:** Build the RAG pipeline and the Chat Agent — the core of the learning project

### Concepts Learned
- **RAG Architecture**: how to index, retrieve, and generate against a knowledge base
- **Embedding models**: how text is converted to vector representations
- **ChromaDB**: vector storage, collection management, similarity search
- **LangGraph basics**: state definition, nodes, edges, conditional routing
- **Intent classification**: using LLMs to route queries to the right handler
- **Context memory**: managing multi-turn conversation with summarization
- **Source citation**: linking AI responses back to specific data points
- **Streaming responses**: token-by-token output via WebSocket

### Technologies Learned
- **ChromaDB** — vector database for embeddings
- **Gemini Embeddings API** — text-to-vector conversion
- **LangGraph** — stateful agent workflow framework
- **LangGraph Studio** — visual debugging tool for agent graphs
- **Gemini 2.5 Flash** — fast, low-latency LLM for intent classification
- **Gemini 2.5 Pro** — high-quality LLM for complex reasoning

### LangGraph Concepts to Master in This Phase
1. `TypedDict` state definition — how state is typed and passed between nodes
2. `StateGraph` — defining the graph structure
3. `add_node()` — registering agent functions as nodes
4. `add_edge()` — defining sequential connections
5. `add_conditional_edges()` — routing based on state content
6. `compile()` — finalizing the graph for execution
7. `checkpointer` — persisting state for resumable workflows
8. LangGraph Studio — connecting local graph for visual debugging

### Deliverables
- `generate_embeddings` Celery task: chunks dataset → embeds → stores in ChromaDB
- Chat session management (create, load history, update)
- Intent classifier node (Gemini Flash)
- ChromaDB retrieval tool (top-10 semantic search)
- Context builder (retrieved chunks + conversation history)
- Chat Agent LangGraph graph (fully wired)
- Streaming response via WebSocket `chat.token` events
- Source citation extraction and display
- Context summarization when turn count > 15
- Chat UI: ChatWindow, ChatMessage, SourceCitations, streaming indicator

### Acceptance Criteria
- [ ] Dataset embeddings generated and stored in ChromaDB on upload
- [ ] Chat session created and history persisted to DB
- [ ] Intent correctly classified for: statistical Q, SQL query, chart request, general BI
- [ ] ChromaDB retrieval returns relevant chunks within 2 seconds
- [ ] Chat response streams token-by-token to frontend
- [ ] Sources cited in every response (column/row references)
- [ ] Context maintained across 15+ turns without losing coherence
- [ ] Context summarized and compressed when turn > 15
- [ ] LangGraph Studio shows the chat workflow graph visually

### Recommended Resources
- ChromaDB docs: https://docs.trychroma.com
- LangGraph getting started: https://langchain-ai.github.io/langgraph/tutorials/
- LangGraph Studio: https://github.com/langchain-ai/langgraph-studio
- RAG from scratch (YouTube): search "LangChain RAG from scratch"
- Gemini API embeddings: https://ai.google.dev/gemini-api/docs/embeddings

### Key Learning Insight
> RAG is the most important pattern in applied LLM engineering. Every enterprise AI system uses it. Building it yourself — with real chunking, real embeddings, real retrieval, and real response generation — is worth more than reading 10 tutorials about it.

---

## L2.4 Phase 4 — Forecasting & Reports

**Duration:** 2 weeks
**Focus:** Build the forecasting pipeline and automated report generation

### Concepts Learned
- **Time series analysis**: stationarity, seasonality detection, trend analysis
- **Prophet**: Facebook's time series model — configuration, fitting, prediction, CI
- **XGBoost for time series**: feature engineering, lag features, walk-forward prediction
- **Model selection logic**: rule-based framework for choosing the right model
- **Evaluation metrics**: MAPE, MAE, RMSE, R² — what they mean and when to use each
- **ReportLab**: programmatic PDF generation with custom layouts
- **python-pptx**: programmatic PPTX generation with slide templates
- **Chart embedding**: converting Recharts/matplotlib charts into report files

### Technologies Learned
- **Prophet** — time series forecasting by Meta
- **XGBoost** — gradient boosting for regression/forecasting
- **scikit-learn** — linear regression, preprocessing
- **ReportLab** — PDF generation
- **python-pptx** — PowerPoint generation
- **matplotlib** — chart rendering for PDF embedding

### Deliverables
- `ProphetEngine`: prepare, detect seasonality, fit, predict, evaluate, to_recharts
- `XGBoostTimeSeriesEngine`: feature engineering, walk-forward prediction, bootstrap CI
- `ModelSelector`: decision logic per Section 13/35
- `ForecastingAgent`: orchestrate model selection → train → forecast → quality gates → narrate
- `ReportAgent`: compile all analysis output into structured report
- PDF report with all sections (Section 14 / 34)
- PPTX presentation with all slide types (Section 14 / 34)
- Forecasting page UI: column selector, horizon slider, forecast chart, metrics
- Reports page UI: download PDF and PPTX

### Acceptance Criteria
- [ ] Prophet forecasts correctly on daily/weekly/monthly data
- [ ] XGBoost feature engineering creates all lag/rolling/date features
- [ ] Model selector applies correct logic for each data pattern
- [ ] MAPE, MAE, RMSE calculated on 20% holdout
- [ ] Forecast chart shows actual + predicted + 95% CI band
- [ ] Quality gates warn or error for flat/explosive/negative forecasts
- [ ] PDF generates with all sections, embedded charts at 300 DPI
- [ ] PPTX generates with all slide types, chart images embedded
- [ ] Both files download successfully from frontend

### Recommended Resources
- Prophet docs: https://facebook.github.io/prophet/docs/
- XGBoost time series tutorial: https://machinelearningmastery.com/xgboost-for-time-series-forecasting/
- ReportLab user guide: https://www.reportlab.com/docs/reportlab-userguide.pdf
- python-pptx docs: https://python-pptx.readthedocs.io/

### Key Learning Insight
> Forecasting and report generation are two of the highest-value skills in applied data science. When you complete this phase, you will be able to take any dataset, generate a statistically rigorous forecast, and produce a boardroom-quality PDF report — all programmatically. This is rare and extremely valuable.

---

## L2.5 Phase 5 — Multi-Agent System

**Duration:** 3–4 weeks
**Focus:** Wire all agents together with LangGraph — the peak learning objective

### Concepts Learned
- **Multi-agent orchestration**: how multiple AI agents cooperate on a single task
- **LangGraph advanced patterns**: subgraphs, parallel nodes, conditional fan-out
- **Agent state management**: how state accumulates and passes through a workflow
- **Agent retry and error recovery**: exponential backoff, partial failure handling
- **Tool calling**: structured tool definitions, tool routing, tool result handling
- **SQL agent safety**: read-only enforcement, keyword allowlisting, parameterized queries
- **Consultant agent**: strategic reasoning over structured analysis output
- **LangGraph Studio advanced**: debugging multi-agent graphs, inspecting state at each node

### Technologies Learned
- **LangGraph** — advanced: subgraphs, interrupt, human-in-the-loop primitives
- **LangGraph Studio** — advanced debugging
- **mlxtend** — Market Basket Analysis (Apriori)
- **psycopg2 / PyMySQL / sqlite3** — database drivers for SQL agent
- **Fernet** — symmetric encryption for DB credentials

### All 11 Agents Activated in This Phase
1. DataCleaningAgent ✅ (Phase 2 — now integrated into workflow)
2. EDAAgent ✅ (Phase 2 — now integrated)
3. VisualizationAgent ✅ (Phase 2 — now integrated)
4. ForecastingAgent ✅ (Phase 4 — now integrated)
5. InsightAgent — NEW this phase
6. ReportAgent ✅ (Phase 4 — now integrated)
7. ConsultantAgent — NEW this phase
8. SQLAgent — NEW this phase
9. DatasetAgent — NEW this phase
10. ChatAgent ✅ (Phase 3 — now in multi-agent graph)
11. ComputerOperatorAgent — Phase 6

### Deliverables
- Full LangGraph analysis workflow graph (all 11 agents wired)
- InsightAgent with structured insight output schema
- ConsultantAgent with strategic memo generation
- SQLAgent with NL-to-SQL, safety validation, execution
- DatasetAgent with schema detection and join suggestions
- Database connection endpoints (PostgreSQL, MySQL, SQLite)
- RFM Engine, Cohort Engine, Market Basket Engine
- Agent log viewer in admin UI
- LangGraph Studio connection confirmed: visual graph debugging working
- Full agent test suite (happy path + failure path per agent)

### Acceptance Criteria
- [ ] Full LangGraph analysis workflow runs end-to-end without error
- [ ] All 10 agents (excluding COA) execute in correct sequence
- [ ] LangGraph Studio shows the full workflow graph visually
- [ ] State is correctly accumulated and passed between all nodes
- [ ] Agent retry logic fires on simulated Gemini 429 error
- [ ] Partial failure in one agent does not abort remaining agents
- [ ] SQL agent generates correct SQL for 90%+ of test questions
- [ ] SQL agent NEVER executes DELETE/DROP/UPDATE (verified by test)
- [ ] RFM analysis produces segment assignments with AI descriptions
- [ ] Cohort retention matrix calculated and rendered as heatmap
- [ ] All 10 agents pass both happy-path and failure-path tests

### Recommended Resources
- LangGraph multi-agent tutorial: https://langchain-ai.github.io/langgraph/tutorials/multi_agent/
- LangGraph concepts: https://langchain-ai.github.io/langgraph/concepts/
- Tool calling with Gemini: https://ai.google.dev/gemini-api/docs/function-calling
- SQLGlot (SQL validation): https://github.com/tobymao/sqlglot

### Key Learning Insight
> Phase 5 is the hardest and most rewarding phase. When your LangGraph Studio shows 10 agents executing in sequence, state flowing correctly between nodes, and real business insights emerging from a CSV file — you will understand why multi-agent AI is the future of knowledge work.

---

## L2.6 Phase 6 — Computer Operator Agent

**Duration:** 2–3 weeks
**Focus:** Build the most unique component: a local desktop automation agent with human approval

### Concepts Learned
- **Desktop automation**: controlling GUI applications programmatically
- **Human-in-the-loop AI**: designing AI systems that pause for human approval
- **Approval workflows**: permission scopes, timeouts, audit trails
- **WebSocket-based control plane**: communicating between cloud and local agent
- **HMAC request signing**: ensuring action payloads are not tampered with
- **Process management**: launching, monitoring, and killing desktop processes
- **Rollback strategies**: undoing actions that were approved and executed
- **Local agent architecture**: building a standalone Python service that connects to a remote backend

### Technologies Learned
- **pyautogui** — cross-platform GUI automation
- **subprocess** — launching and managing external processes
- **win32com** (Windows) / **applescript** (macOS) — application-specific automation
- **HMAC-SHA256** — request signing for security
- **Playwright** (optional) — browser automation for web-based actions
- **WebSockets** — bidirectional communication between local agent and backend

### Deliverables
- COA Planning Agent (Gemini Pro action planner)
- ApprovalManager service (backend approval orchestration)
- `coa_actions` database table and migrations
- WebSocket approval flow (server → client dialog → server)
- ApprovalDialog frontend component (per Section L6 specification)
- Permission scope system (Once / Session / Always / Deny)
- Auto-deny timer (5 minutes with countdown UI)
- `aibios-local-agent` Python service (separate installable package)
- Action handlers: open_application, open_file, run_script, open_url, export_to_excel
- Rollback system (5-minute window per action)
- COA audit log viewer in admin UI
- Full COA test suite (zero actions without approval token — verified)

### Acceptance Criteria
- [ ] NO desktop action executes without an approval token (verified by unit test)
- [ ] Approval dialog appears for every COA action request
- [ ] Dialog shows: agent name, action, reason, expected outcome, risk level
- [ ] Allow Once: executes once, no scope saved
- [ ] Allow Session: scope persists until tab close (Redis)
- [ ] Always Allow: scope persisted to PostgreSQL
- [ ] Deny: action not executed, denial logged
- [ ] Auto-deny fires at exactly 300 seconds (verified by integration test)
- [ ] HMAC validation rejects tampered action payloads (verified by test)
- [ ] Rollback available within 5 minutes of execution
- [ ] All COA actions appear in audit log

### Recommended Resources
- pyautogui docs: https://pyautogui.readthedocs.io/
- python-dotenv for local agent config: https://pypi.org/project/python-dotenv/
- LangGraph human-in-the-loop: https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/
- HMAC in Python: https://docs.python.org/3/library/hmac.html

### Key Learning Insight
> The Computer Operator Agent is the most advanced and most unique component in this project. Almost no tutorials or courses teach this. When you build it, you will understand how to design AI systems that interact with the real world safely — with human oversight built into the architecture, not bolted on as an afterthought.

---

## L2.7 Phase 7 — Power BI Integration

**Duration:** 1–2 weeks
**Focus:** Connect AI-BIOS to Power BI via REST API

### Concepts Learned
- **Power BI REST API**: authentication, dataset publishing, report creation
- **OAuth 2.0 for Power BI**: device code flow for local desktop authentication
- **Push datasets**: how to programmatically push data to Power BI
- **Dataset schema translation**: mapping pandas DataFrames to Power BI table schemas
- **Report URL generation**: creating embeddable report URLs from published datasets

### Technologies Learned
- **Power BI REST API** — Microsoft's BI platform API
- **MSAL (Microsoft Authentication Library)** — OAuth 2.0 for Microsoft services
- **requests** — HTTP client for REST API calls

### Deliverables
- Power BI OAuth integration (device code flow)
- Dataset schema formatter (pandas → Power BI push format)
- Dataset publisher (push rows in 1000-row batches)
- Report creation from published dataset
- Power BI export button on dashboard/report pages
- Encrypted token storage in PostgreSQL

### Acceptance Criteria
- [ ] OAuth device code flow works: user authenticates in browser, token stored
- [ ] Dataset pushed to Power BI workspace successfully
- [ ] Power BI report URL returned and displayed to user
- [ ] Tokens encrypted before storage in database
- [ ] Expired tokens refreshed automatically

### Recommended Resources
- Power BI REST API: https://learn.microsoft.com/en-us/rest/api/power-bi/
- MSAL Python: https://github.com/AzureAD/microsoft-authentication-library-for-python
- Power BI push datasets: https://learn.microsoft.com/en-us/power-bi/developer/automation/api-dataset-properties

### Key Learning Insight
> Power BI integration teaches OAuth 2.0, REST API design patterns, and enterprise software integration — skills directly applicable to any Microsoft or enterprise cloud integration you will encounter in your career.

---

# L3. Tool Usage Guide

## L3.1 Overview

As a solo developer building a complex agentic AI system, you have access to multiple AI tools. Each tool has a distinct role. Using the right tool for the right task is a skill in itself.

```
Primary Development Tools:
  Cursor        → Code generation, architecture implementation, file editing
  LangGraph Studio → Agent graph visualization, state debugging, workflow testing
  Claude        → Architecture decisions, complex debugging, document generation
  ChatGPT       → Quick lookups, alternative explanations, brainstorming
  Gemini        → Integrated into the app (API) — also useful for prompt testing
  VS Code Copilot → Line-level autocomplete, minor edits when not in Cursor
```

## L3.2 Tool-by-Tool Specification

### Cursor
**Primary Responsibility:** The main development environment. All code lives here.

**Best Use Cases:**
- Implementing new files and modules (give it this document as context)
- Refactoring existing code based on architecture specs
- Writing Celery tasks, FastAPI endpoints, LangGraph nodes
- Writing React components and Zustand stores
- Running tests and fixing test failures
- Implementing entire phases from the task breakdown in Section 25

**Secondary Responsibility:**
- Architecture-aware code generation (with this document as `@MASTER` context)
- Database migration generation via alembic autogenerate
- Docker and config file management

**Do NOT use Cursor for:**
- High-level architecture decisions (use Claude for that)
- Understanding why something works (ask Claude or ChatGPT)
- Visual debugging of LangGraph workflows (use LangGraph Studio)
- Live API testing (use FastAPI /docs or Postman)

**Workflow Integration:**
```
1. Reference this document in Cursor: @AI_BIOS_MASTER_LEARNING_EDITION.md
2. Ask Cursor to implement specific tasks from Section 25
3. Run tests after each task
4. Commit when task acceptance criteria pass
```

---

### LangGraph Studio
**Primary Responsibility:** Visualize, debug, and test all LangGraph workflows

**Best Use Cases:**
- Seeing your agent graph as a visual diagram in real-time
- Inspecting state at each node during a workflow run
- Debugging why an agent is failing or routing incorrectly
- Testing individual nodes in isolation
- Watching state accumulate as the workflow progresses
- Interrupted workflow inspection (human-in-the-loop debugging)

**Secondary Responsibility:**
- Demonstrating workflows to others (screenshots for portfolio)
- Understanding LangGraph concepts visually before coding them

**Do NOT use LangGraph Studio for:**
- Writing code (use Cursor)
- Production execution (it's a development tool)
- Performance testing

**Setup:**
```bash
pip install langgraph-studio
# Connect to your local backend
# LangGraph Studio auto-discovers graphs in your workflows/ folder
```

**Workflow Integration:**
```
Phase 3+:
  1. Implement graph in Cursor
  2. Open LangGraph Studio → see graph rendered
  3. Run a test workflow
  4. Inspect state at each node
  5. Fix bugs in Cursor
  6. Repeat
```

---

### Claude (Anthropic)
**Primary Responsibility:** Architecture decisions, complex debugging, document updates

**Best Use Cases:**
- Understanding WHY a design decision was made in this document
- Debugging complex multi-agent coordination issues
- Updating this master document when specs change
- Understanding security implications of implementation choices
- Reviewing your LangGraph state design before implementing
- Writing prompt templates for agent system prompts
- Understanding RAG architecture decisions

**Secondary Responsibility:**
- Explaining LangGraph concepts at a deep level
- Reviewing agent retry and error recovery strategies
- Designing the COA approval workflow logic

**Do NOT use Claude for:**
- Line-by-line code generation of large files (use Cursor)
- Quick syntax lookups (use Copilot or ChatGPT)

**Workflow Integration:**
```
When stuck on architecture:
  → Paste relevant section from this doc into Claude
  → Ask your specific question
  → Update this doc if Claude reveals a spec gap
  → Implement in Cursor

Free tier limit hit:
  → Switch to ChatGPT for continued assistance
  → Or switch to Gemini for architecture questions
```

---

### ChatGPT (OpenAI)
**Primary Responsibility:** Quick lookups, alternative explanations, brainstorming

**Best Use Cases:**
- Quick Python/TypeScript syntax questions
- Alternative approaches to implementation problems
- Understanding a library or API you're unfamiliar with
- Debugging a specific error message
- Brainstorming test cases

**Secondary Responsibility:**
- Overflow from Claude when free tier limit is hit
- General programming questions not architecture-specific

**Do NOT use ChatGPT for:**
- This project's architecture (it doesn't know this document)
- LangGraph-specific debugging (Claude is better)
- Generating large amounts of boilerplate (use Cursor)

---

### Gemini (Google)
**Primary Responsibility:** The LLM powering the AI-BIOS application itself

**Also useful for:**
- Testing prompts before wiring them into agents
- Understanding Gemini API capabilities and limits
- Verifying model output format before implementing a Pydantic schema

**Do NOT use Gemini (chat) for:**
- This project's architecture (it doesn't know this document)
- Development workflow assistance

---

### VS Code Copilot
**Primary Responsibility:** Line-level autocomplete when not in Cursor

**Best Use Cases:**
- Minor edits to existing files
- Completing boilerplate within a known pattern
- Quick import suggestions

**Do NOT use Copilot for:**
- Large feature implementation (use Cursor)
- Architecture decisions

---

## L3.3 Recommended Development Workflow

```
Daily Development Loop:
─────────────────────────────────────────────────────
MORNING PLANNING (15 minutes)
  1. Review today's tasks from Section 25 phase breakdown
  2. Identify which tools you'll need:
     - Implementation → Cursor
     - LangGraph work → LangGraph Studio open alongside Cursor
     - Architecture question → Claude
     - Quick lookup → ChatGPT or Copilot

IMPLEMENTATION (2–4 hours)
  3. Open Cursor with this document as context
  4. Work on one task at a time
  5. After each task: run tests
  6. If LangGraph-related: confirm in LangGraph Studio

DEBUGGING (as needed)
  7. Agent not routing correctly → LangGraph Studio first
  8. Pydantic validation error → ChatGPT or Copilot
  9. Architecture confusion → Claude

END OF DAY (15 minutes)
  10. Commit all passing code
  11. Update task checkboxes in this document
  12. Note any spec gaps or questions for tomorrow
─────────────────────────────────────────────────────
```

## L3.4 Free Tier Limit Strategy

When any tool hits its free tier limit, follow this rotation:

| Primary Tool | Limit Hit | Switch To |
|-------------|-----------|-----------|
| Claude | Daily limit | ChatGPT GPT-4o |
| ChatGPT | Daily limit | Claude (if reset) or Gemini |
| Cursor | Context limit | Split into smaller tasks; clear context |
| Gemini API | Rate limit (429) | Exponential backoff in code (already designed in) |
| LangGraph Studio | N/A (local) | Always available |

**Key Rule:** Never let a tool limit block you. Every tool has a capable substitute for the day.

---

# L4. Solo Developer Implementation Strategy

## L4.1 Mindset

Building AI-BIOS Learning Edition as a solo developer requires a different approach than a 20-engineer team. You are the architect, the backend engineer, the frontend engineer, the DevOps engineer, the QA engineer, and the documentation writer — all at once.

This section gives you a realistic, sustainable strategy.

## L4.2 Recommended Implementation Sequence

Work through phases strictly in order. Each phase builds on the last. Do not start Phase 3 until Phase 2 acceptance criteria are met.

```
Week 1–2:   Phase 1 — Backend Foundation
             Focus: infrastructure, auth, database, Celery, WebSocket
             Goal:  docker-compose up + auth working + test passes

Week 3–4:   Phase 2 — Dataset Intelligence
             Focus: upload, parse, profile, clean
             Goal:  upload CSV → see profile page in browser

Week 5–7:   Phase 3 — RAG & Chat
             Focus: ChromaDB, embeddings, LangGraph basics, Chat Agent
             Goal:  ask a question about your data, get a cited answer

Week 8–9:   Phase 4 — Forecasting & Reports
             Focus: Prophet, XGBoost, PDF, PPTX
             Goal:  upload sales data → see forecast → download PDF

Week 10–13: Phase 5 — Multi-Agent System
             Focus: full LangGraph graph, 10 agents, SQL agent
             Goal:  LangGraph Studio shows all 10 agents in workflow

Week 14–16: Phase 6 — Computer Operator Agent
             Focus: local agent, approval dialog, desktop automation
             Goal:  AI requests to open Excel → approval dialog → Excel opens

Week 17–18: Phase 7 — Power BI Integration
             Focus: OAuth, REST API, dataset publishing
             Goal:  push dataset to Power BI workspace from AI-BIOS
```

## L4.3 Solo Developer Simplifications

The following enterprise features from v1.0.0 are REMOVED in the Learning Edition:

| Removed Feature | Reason |
|----------------|--------|
| SaaS pricing tiers | Not building a SaaS business |
| Subscription billing | Not needed for learning |
| Organization / multi-tenancy | Over-engineering for solo dev |
| Enterprise SSO (SAML/Google OAuth) | Not needed for local learning |
| White-labeling | Not applicable |
| Advanced RBAC (4 roles) | Simplified to Admin + User |
| Scheduled report email delivery | Nice-to-have, not core |
| i18n / multi-language | Not needed for learning |
| Usage metering / quotas | Not needed without SaaS billing |
| Webhook system | Phase 5+ feature, skip for now |

**What this means for you:** You write less boilerplate code and spend more time on the AI components that matter.

## L4.4 Simplified RBAC for Learning Edition

See Section L7 for full simplified RBAC specification.

## L4.5 Focus Priorities

When time is limited, prioritize in this order:

1. **LangGraph workflows** — the core learning objective
2. **RAG pipeline** — the most transferable skill
3. **Agent tool calling** — essential for all future agentic projects
4. **COA approval system** — unique and impressive
5. **Forecasting engine** — high business value
6. **Report generation** — tangible deliverable
7. **SQL agent** — broadly applicable
8. **Power BI integration** — enterprise credibility
9. **Frontend polish** — secondary to backend AI work

---

# L5. Deployment Strategy

## L5.1 Phase 1 Deployment — Learning Mode (Weeks 1–13)

All development runs locally. No cloud deployments. No cost.

```
┌─────────────────────────────────────────────────────────┐
│              LOCAL DEVELOPMENT STACK                     │
├─────────────────────────────────────────────────────────┤
│  Next.js Dev Server         → localhost:3000            │
│  FastAPI (uvicorn --reload)  → localhost:8000            │
│  PostgreSQL (Docker)         → localhost:5432            │
│  Redis (Docker)              → localhost:6379            │
│  ChromaDB (Docker)           → localhost:8001            │
│  Celery Worker (local)       → background process        │
│  Celery Flower               → localhost:5555            │
│  LangGraph Studio            → localhost:8123            │
├─────────────────────────────────────────────────────────┤
│  LLM API: Gemini (remote)    → api.googleapis.com        │
├─────────────────────────────────────────────────────────┤
│  TOTAL MONTHLY COST: $0 + Gemini API usage               │
│  (Gemini free tier: 15 req/min, 1M tokens/day — enough) │
└─────────────────────────────────────────────────────────┘
```

**Start command:**
```bash
make dev   # starts all Docker services + backend + frontend + celery
```

**Gemini Free Tier Strategy:**
- Use `gemini-2.5-flash` for all fast/simple tasks (intent classification, chart captions)
- Use `gemini-2.5-pro` only for deep analysis tasks (EDA narrative, insights, SQL gen)
- Implement retry with exponential backoff (already designed — Section 37)
- Queue AI-heavy tasks in Celery to naturally rate-limit parallel calls

---

## L5.2 Phase 2 Deployment — Portfolio Mode (After Phase 5 Complete)

Deploy the complete working system for public showcase. Target cost: $0/month.

```
┌────────────────────────────────────────────────────────────────────┐
│                     PORTFOLIO DEPLOYMENT                            │
├──────────────────────────┬─────────────────────────────────────────┤
│ Component                │ Service                                  │
├──────────────────────────┼─────────────────────────────────────────┤
│ Frontend (Next.js)       │ Vercel — Free Tier (Hobby)              │
│ Backend (FastAPI)        │ Render — Free Tier (750 hrs/month)      │
│ Database (PostgreSQL)    │ Neon — Free Tier (0.5 GB)              │
│ Vector DB (ChromaDB)     │ Render — Free Tier (same service)      │
│ Cache + Queue (Redis)    │ Upstash Redis — Free Tier (10k req/day)│
│ File Storage             │ Render Persistent Disk or Cloudflare R2 │
│ LLM (Gemini)             │ Gemini API — free tier                  │
├──────────────────────────┼─────────────────────────────────────────┤
│ TOTAL MONTHLY COST       │ ~$0 (within free tier limits)           │
└──────────────────────────┴─────────────────────────────────────────┘
```

**Render Free Tier Notes:**
- Service spins down after 15 minutes of inactivity
- First request after spin-down takes 30–60 seconds (cold start)
- Acceptable for portfolio demo — not for production SaaS
- Add a `/health` ping from UptimeRobot (free) to keep it warm

**Deployment Steps:**
```
1. Push backend to GitHub
2. Connect to Render → New Web Service → Docker deploy
3. Set all environment variables from Section 39
4. Push frontend to GitHub
5. Connect to Vercel → Import project → auto-deploy
6. Set NEXT_PUBLIC_API_URL to Render backend URL
7. Run database migrations: render run alembic upgrade head
8. Test all Phase 1–5 features on deployed version
```

---

## L5.3 Phase 3 Deployment — Hybrid Desktop Agent Mode (After Phase 6 Complete)

The Computer Operator Agent and Power BI Agent MUST run locally. They cannot run in the cloud.

```
┌────────────────────────────────────────────────────────────────────┐
│                HYBRID DEPLOYMENT ARCHITECTURE                       │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──── CLOUD (Vercel + Render + Neon) ──────────────────────────┐  │
│  │  Next.js Frontend                                             │  │
│  │  FastAPI Backend                                              │  │
│  │  PostgreSQL (Neon)                                            │  │
│  │  ChromaDB                                                     │  │
│  │  Redis (Upstash)                                              │  │
│  │  LangGraph workflows (all except COA)                        │  │
│  │  Gemini API calls                                             │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                          │ WebSocket (authenticated)                │
│  ┌──── LOCAL (Developer's Machine) ────────────────────────────┐   │
│  │  aibios-local-agent (Python service)                         │   │
│  │  Computer Operator Agent execution                           │   │
│  │  Power BI Agent execution                                    │   │
│  │  Excel Agent execution                                       │   │
│  │  VS Code Agent execution                                     │   │
│  │  pyautogui / subprocess / win32com / applescript             │   │
│  │  Human Approval Layer (browser dialog)                       │   │
│  │  Playwright (browser automation)                             │   │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

**Why Local-Only for COA:**
- Power BI Desktop cannot be remotely controlled from cloud infrastructure
- Excel automation requires local COM object access (Windows) or AppleScript (macOS)
- VS Code opens local files — cloud execution makes no sense
- Desktop automation tools (pyautogui) require display/screen access
- Security: desktop automation on a cloud server is both dangerous and useless

**Local Agent Installation:**
```bash
pip install aibios-local-agent
aibios-agent start --backend-url wss://your-render-backend.onrender.com/ws --token <your-jwt>
```

---

# L6. Human Approval Layer

## L6.1 Design Principle

> Every action taken by the Computer Operator Agent on the user's local machine MUST pause execution and wait for explicit human approval before proceeding. This is architecturally enforced, not a policy suggestion.

This principle is implemented at three levels:
1. **Backend:** No execution command sent to local agent without a signed approval token
2. **Local Agent:** Refuses to execute any action without a valid approval token (verified by HMAC)
3. **Frontend:** Approval dialog is blocking — no other UI interaction possible until decision made

## L6.2 Actions Requiring Approval

Every desktop action — without exception — requires approval:

| Action | Target Application | Risk Level |
|--------|------------------|-----------|
| Open application | VS Code, Power BI, Excel, MySQL Workbench, Browser | Low |
| Open specific file in app | Any application | Medium |
| Run Python script | Python interpreter | High |
| Run PowerShell/Bash script | Terminal | High |
| Execute SQL in workbench | MySQL Workbench | High |
| Export data to Excel | Microsoft Excel | Medium |
| Open URL in browser | Default browser | Low |
| Navigate to URL | Active browser | Medium |
| Fill in web form | Browser | High |
| Run multi-step workflow | Multiple applications | Critical |

## L6.3 Approval Dialog Specification

The approval dialog is a blocking modal rendered as a browser portal (z-index: 9999). It cannot be dismissed without making a decision.

```
┌──────────────────────────────────────────────────────────┐
│  🤖  Computer Operator Agent — Action Requested          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Agent:           Computer Operator Agent                │
│  Action:          Open Microsoft Excel                   │
│  Reason:          Export cleaned sales dataset for       │
│                   client presentation                    │
│  Expected Result: Excel opens with sales_clean.xlsx      │
│  Risk Level:      🟡 Medium                              │
│                                                          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────┐ ┌──────────────┐ ┌────────────┐ ┌──────┐ │
│  │Allow Once│ │Allow Session │ │Always Allow│ │ Deny │ │
│  └──────────┘ └──────────────┘ └────────────┘ └──────┘ │
│                                                          │
│  ⏱ Auto-deny in: 4:47                                   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**Dialog Fields (all required):**
- **Agent:** Always "Computer Operator Agent" (or sub-agent name)
- **Action:** Human-readable description of exactly what will happen
- **Reason:** Why the agent determined this action is needed
- **Expected Result:** What the user should see after execution
- **Risk Level:** Low (green) / Medium (amber) / High (orange) / Critical (red)
- **Countdown:** 5-minute timer; auto-deny on expiry

## L6.4 Approval Scopes

| Scope | Storage | Duration | Revocable |
|-------|---------|---------|-----------|
| **Allow Once** | RAM only | Single execution | N/A |
| **Allow For Session** | Redis key with TTL | Until tab closes or session ends | Yes (end session) |
| **Always Allow** | PostgreSQL `coa_permissions` | Permanent | Yes (admin panel) |
| **Deny** | Audit log only | N/A | N/A |

## L6.5 Auto-Deny Rules

The system automatically denies any pending action if:
- User does not respond within **5 minutes** (300 seconds)
- Browser tab is closed or navigated away from approval page
- JWT session expires during approval wait
- Action is flagged as **Critical** risk (always requires fresh manual approval)

Auto-deny fires a `coa.auto_denied` WebSocket event and logs the denial to the audit trail.

## L6.6 Audit Log Entry Schema

Every COA action — approved, denied, or auto-denied — generates an immutable audit entry:

```json
{
  "action_id": "uuid",
  "user_id": "uuid",
  "agent_name": "computer_operator_agent",
  "action_type": "open_application",
  "target_application": "Microsoft Excel",
  "action_params": { "file_path": "/home/user/sales_clean.xlsx" },
  "reason": "Export cleaned sales dataset",
  "expected_outcome": "Excel opens with sales_clean.xlsx",
  "risk_level": "medium",
  "approval_decision": "allow_once | allow_session | always_allow | deny | auto_denied",
  "approval_scope": "once",
  "approved_at": "2026-06-05T10:23:11Z",
  "executed_at": "2026-06-05T10:23:12Z",
  "execution_result": "success | failed | rolled_back | uncertain",
  "error_message": null,
  "rollback_available_until": "2026-06-05T10:28:12Z",
  "ip_address": "127.0.0.1",
  "session_id": "session-uuid"
}
```

## L6.7 Rollback System

Every executed COA action has a rollback handler available for 5 minutes:

| Action | Rollback |
|--------|---------|
| Open application | Close the opened application |
| Open file | Close the file (if still open) |
| Export to Excel | Delete the created file |
| Run script | Kill the process by PID |
| Open URL | Close the browser tab |
| Multi-step workflow | Execute rollback steps in reverse order |

Rollback is triggered by: `POST /api/v1/coa/actions/{id}/rollback`
Rollback result logged as `execution_result: "rolled_back"` in audit log.

---

# L7. Simplified RBAC

## L7.1 Learning Edition Role Model

The enterprise RBAC (Admin / Analyst / Viewer / super_admin) from v1.0.0 is simplified to two roles for the Learning Edition:

| Role | Description |
|------|-------------|
| `admin` | Full access to all features, including admin panel, audit logs, COA approvals, user management |
| `user` | Access to all core features: upload datasets, run analyses, chat, forecast, generate reports, connect databases |

## L7.2 Permissions Matrix (Simplified)

| Permission | admin | user |
|-----------|:-----:|:----:|
| Upload dataset | ✅ | ✅ |
| Delete dataset | ✅ | Own only |
| Run analysis | ✅ | ✅ |
| View analysis | ✅ | ✅ |
| Generate report | ✅ | ✅ |
| Chat with data | ✅ | ✅ |
| Connect database | ✅ | ✅ |
| Run forecast | ✅ | ✅ |
| Create project | ✅ | ✅ |
| Delete project | ✅ | Own only |
| Approve COA actions | ✅ | ✅ (own actions) |
| View audit logs | ✅ | ❌ |
| Manage users | ✅ | ❌ |
| Revoke COA permissions | ✅ | ❌ |
| View system stats | ✅ | ❌ |

## L7.3 JWT Claims (Simplified)

```json
{
  "sub": "user-uuid",
  "email": "user@example.com",
  "role": "admin | user",
  "iat": 1717000000,
  "exp": 1717000900,
  "jti": "unique-token-id"
}
```

## L7.4 FastAPI Role Dependency

```python
# Simple role check for Learning Edition
def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

def require_user(current_user: User = Depends(get_current_user)):
    # Any authenticated user passes
    return current_user
```

---

# 1. Executive Overview (Revised)

## 1.1 Project Vision

AI-BIOS Learning Edition is a complete, working AI-powered Business Intelligence platform built by a solo developer for the purpose of deeply learning Agentic AI, LangGraph, RAG systems, and production-grade AI architecture.

The system replicates the capabilities of:
- A Data Analyst (EDA, profiling, cleaning)
- A BI Analyst (dashboards, visualizations)
- A Data Scientist (forecasting, segmentation, anomaly detection)
- A Report Writer (PDF, PPTX automated reports)
- A SQL Analyst (natural language database queries)
- A Business Consultant (insights, strategic recommendations)
- A Dashboard Developer (interactive charts, KPI cards)
- A Desktop Automation Specialist (Computer Operator Agent)

## 1.2 Learning Goals

| Goal | Achieved By |
|------|-------------|
| Learn Agentic AI | 11 agents orchestrated by LangGraph |
| Learn LangGraph | Full stateful workflow with all node types |
| Learn RAG | ChromaDB + Gemini embeddings + retrieval |
| Learn tool calling | 20+ tools across all agents |
| Learn forecasting | Prophet + XGBoost + linear regression |
| Learn report generation | ReportLab PDF + python-pptx PPTX |
| Learn SQL agents | NL-to-SQL with safety validation |
| Learn COA + HITL | Desktop automation + human approval layer |
| Learn Power BI API | OAuth + REST API + dataset publishing |
| Learn AI architecture | Complete production-grade system design |

## 1.3 Technology Stack

| Layer | Technology | Learning Value |
|-------|-----------|---------------|
| Frontend | Next.js 15, TypeScript, TailwindCSS, ShadCN, Recharts | React + data viz |
| Backend | FastAPI, Python 3.12 | Async API design |
| AI/LLM | Gemini 2.5 Pro + Flash | Gemini API, model selection |
| Agent Framework | LangGraph | Core agentic AI learning |
| Task Queue | Celery + Redis | Async processing patterns |
| Database | PostgreSQL (Neon / local Docker) | Relational + JSONB |
| Vector DB | ChromaDB | RAG + embeddings |
| Desktop Agent | pyautogui + subprocess | Desktop automation |

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


# 25. Implementation Phase Tasks

> This section replaces the 20-engineer team roadmap with a solo developer task breakdown. Tasks are ordered for sequential implementation. Complete each phase's acceptance criteria before starting the next.


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


# 28. Agent Tool Definitions (Complete)

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


# 29. Pydantic Schema Reference

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


# 30. LangGraph State Machines (Extended)

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


# 31. Agent Prompts Reference

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


# 32. WebSocket Event Specification

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


# 33. Data Flow Diagrams

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


# 34. Reporting Engine Extended

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


# 35. Forecasting Engine Extended

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

# 36. Security Threat Model

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

# 37. Error Recovery Runbook

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


# 38. Backend Service Layer Specifications

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


# 39. Environment Variables Reference

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


# 40. docker-compose.yml Reference

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


# 41. Requirements Files

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


# 42. Glossary

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



---

# 43. LangGraph Studio Setup Guide

## 43.1 Installation

```bash
pip install langgraph-cli
pip install langgraph-sdk

# Install LangGraph Studio (macOS/Windows desktop app)
# Download from: https://github.com/langchain-ai/langgraph-studio/releases

# Or use the web-based developer UI (no install required):
# npx @langchain/langgraph-cli@latest studio
```

## 43.2 Connecting Your Project

Create `langgraph.json` in your backend root:

```json
{
  "dependencies": ["."],
  "graphs": {
    "analysis_workflow": "./app/workflows/analysis_workflow.py:graph",
    "chat_workflow": "./app/workflows/chat_workflow.py:graph",
    "forecast_workflow": "./app/workflows/forecast_workflow.py:graph",
    "coa_workflow": "./app/workflows/coa_workflow.py:graph"
  },
  "env": ".env"
}
```

## 43.3 Running LangGraph Studio

```bash
# Start your local FastAPI backend first
uvicorn app.main:app --reload

# In a new terminal, start LangGraph dev server
langgraph dev

# Open LangGraph Studio in browser: http://localhost:8123
# Or open the desktop app and connect to http://localhost:8123
```

## 43.4 What to Do in LangGraph Studio

For each phase that introduces a new LangGraph graph:

1. **See the graph visually**: click your workflow name in the left panel
2. **Run a test**: use the "Run" button with a sample state payload
3. **Step through nodes**: watch each node execute one at a time
4. **Inspect state**: click any node to see input state and output state
5. **Debug routing**: see which conditional edge was taken and why
6. **Test interrupts**: for COA workflows, see the graph pause at the approval interrupt

## 43.5 Debugging Tips

| Problem | LangGraph Studio Action |
|---------|------------------------|
| Agent routes to wrong node | Inspect state after classify step; check conditional edge logic |
| State field missing | Inspect node output; check TypedDict definition |
| Workflow stuck | Check for infinite loops in conditional edges |
| Agent retrying endlessly | Check retry count in state; verify backoff is incrementing |
| COA not pausing | Verify `interrupt_before` is set on approval node |

---

# 44. Development Environment Setup (Complete)

## 44.1 Prerequisites

```
Required:
  Python 3.12+          (pyenv recommended for version management)
  Node.js 20+           (nvm recommended)
  Docker Desktop        (for PostgreSQL + Redis + ChromaDB)
  Git                   (version control)

Recommended:
  Cursor                (primary IDE)
  LangGraph Studio      (agent debugging)
  Postman or Bruno      (API testing)
  TablePlus or DBeaver  (PostgreSQL GUI)
  RedisInsight          (Redis monitoring)
```

## 44.2 Initial Setup

```bash
# 1. Clone repository
git clone https://github.com/yourusername/ai-bios.git
cd ai-bios

# 2. Copy environment files
cp .env.example .env
# Edit .env: add your GEMINI_API_KEY

# 3. Start Docker services
docker-compose up -d postgres redis chromadb

# 4. Set up backend
cd backend
python -m venv venv
source venv/bin/activate          # macOS/Linux
# venv\Scripts\activate           # Windows
pip install -r requirements-dev.txt

# 5. Run migrations
alembic upgrade head

# 6. Seed development data
python scripts/seed_dev_data.py

# 7. Start backend
uvicorn app.main:app --reload --port 8000

# 8. In new terminal: start Celery worker
celery -A app.tasks.celery_app worker --loglevel=info -Q high_priority,compute,ai,reports,low_priority

# 9. Set up frontend (in new terminal)
cd ../frontend
npm install
npm run dev

# 10. In new terminal: start LangGraph Studio (Phase 3+)
cd ../backend
langgraph dev
```

## 44.3 Verify Setup

```bash
# Backend health
curl http://localhost:8000/health
# Expected: {"status": "healthy", "services": {"db": "ok", "redis": "ok", "chroma": "ok"}}

# Register test user
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"Test123!","full_name":"Test User"}'

# Frontend
open http://localhost:3000
# Expected: Login page renders
```

---

# 45. Solo Developer Git Workflow

## 45.1 Branch Strategy

As a solo developer, keep it simple:

```
main          → always working, deployed to portfolio
develop       → active development (default branch for local work)
feature/xxx   → individual features (optional, for complex multi-day work)
```

## 45.2 Commit Message Convention

```
feat(agents): implement EDA Agent with correlation analysis
feat(rag): add ChromaDB embedding pipeline
feat(coa): implement approval dialog with countdown timer
fix(auth): resolve refresh token rotation race condition
fix(langgraph): correct state routing after cleaning agent
test(sql): add 20 NL-to-SQL test cases
docs(master): update Phase 3 acceptance criteria
chore(deps): upgrade LangGraph to 0.2.55
```

## 45.3 Daily Commit Rule

Commit at least once per day with passing tests. Never leave uncommitted work that breaks the build overnight. The LangGraph state machine tests are your safety net.

---

> ════════════════════════════════════════════════════════════════
>
> **AI_BIOS_MASTER_LEARNING_EDITION.md — VERSION 1.1.0 — COMPLETE**
>
> **Solo Developer Agentic AI Learning Project**
>
> ════════════════════════════════════════════════════════════════
>
> SINGLE SOURCE OF TRUTH FOR AI-BIOS LEARNING EDITION
>
> ────────────────────────────────────────────────────────────────
> LEARNING PHASES:
>   Phase 1 (L2.1) → Backend Foundations          Weeks 1–2
>   Phase 2 (L2.2) → Dataset Intelligence         Weeks 3–4
>   Phase 3 (L2.3) → RAG & Chat With Data         Weeks 5–7
>   Phase 4 (L2.4) → Forecasting & Reports        Weeks 8–9
>   Phase 5 (L2.5) → Multi-Agent System           Weeks 10–13
>   Phase 6 (L2.6) → Computer Operator Agent      Weeks 14–16
>   Phase 7 (L2.7) → Power BI Integration         Weeks 17–18
> ────────────────────────────────────────────────────────────────
>
> DEPLOYMENT STRATEGY:
>   Weeks 1–13:  Local only ($0/month)
>   After Phase 5: Deploy to Vercel + Render + Neon ($0/month)
>   After Phase 6: Hybrid cloud + local desktop agent
>
> TOOL WORKFLOW:
>   Cursor (implement) → LangGraph Studio (debug) → Claude (architecture)
>   → ChatGPT (quick lookups) → Gemini (prompts + API)
>
> VERIFY AFTER EACH PHASE:
>   Section 27 Checklist + Phase acceptance criteria in Section L2
>


---

# PART A — Project Management & Execution Standards

---

# A1. Three Mandatory Project Files

Every AI-BIOS development session must begin by reading these three files in order:

```
ai-bios/
├── AI_BIOS_MASTER.md                    ← Full architecture SSOT (read first)
├── AI_BIOS_MASTER_LEARNING_EDITION.md   ← This file — learning guide + solo dev strategy
└── AI_BIOS_PROJECT_STATUS.md            ← Operational memory (read before every session)
```

| File | Purpose | Update Frequency |
|------|---------|-----------------|
| `AI_BIOS_MASTER.md` | Complete architecture, API specs, agent definitions, all technical depth | Rare — only on architecture decisions |
| `AI_BIOS_MASTER_LEARNING_EDITION.md` | Learning roadmap, tool guide, solo developer strategy, simplified RBAC | On learning milestones or approach changes |
| `AI_BIOS_PROJECT_STATUS.md` | Current phase, sprint tasks, bugs, blockers, session log — operational brain | After EVERY development session |

### Rule: Never Start a Session Without Reading PROJECT_STATUS.md

```
Before writing any code in any session:
  1. Open AI_BIOS_PROJECT_STATUS.md
  2. Note: Current Phase and Current Sprint
  3. Find first task with status = "todo" or "in-progress"
  4. Implement that task
  5. Update PROJECT_STATUS.md on completion
```

---

# A2. Quick Start — Resume Development

> Use this section when development is interrupted, a new AI agent session begins,
> or you return after any break — even a single day.

## Step-by-Step Resume Protocol

```
STEP 1: Orient yourself
  → Open AI_BIOS_MASTER_LEARNING_EDITION.md (this file)
  → Read Section L2 for the phase you are currently in
  → Refresh the concepts and technologies for that phase

STEP 2: Read operational state
  → Open AI_BIOS_PROJECT_STATUS.md
  → Note: Current Phase, Current Sprint, Overall Completion %
  → Note: Any open bugs or current blockers
  → Note: Last session's "Next Action" entry

STEP 3: Find your next task
  → Go to "Current Sprint Tasks" table in PROJECT_STATUS.md
  → Find the first row with Status = "todo" or "in-progress"
  → That is your starting point

STEP 4: Verify your local environment
  → docker-compose up -d
  → curl http://localhost:8000/health
  → open http://localhost:3000
  → pytest tests/ -x  (verify no regressions from last session)

STEP 5: Implement
  → Work on exactly one task at a time
  → Run tests after completing each task
  → Do not start the next task until current task's tests pass

STEP 6: Update trackers
  → Mark completed task as "done" in PROJECT_STATUS.md
  → Append a session log entry with: Date, Tool, Tasks, Files, Issues, Next
  → Commit: git commit -m "feat(scope): description" 
  → Push to GitHub

STEP 7: End-of-session checklist
  □ All completed tasks marked "done" in PROJECT_STATUS.md
  □ No uncommitted code
  □ Tests passing
  □ Session log entry written with "Next Action" clearly stated
  □ Next task identified and noted
```

## For AI Coding Agents (Cursor, Claude Code, OpenHands, Roo Code, Cline)

When an AI agent begins a new session it MUST follow this sequence:

```
1. READ AI_BIOS_MASTER.md           → understand full architecture
2. READ AI_BIOS_MASTER_LEARNING_EDITION.md → understand learning context
3. READ AI_BIOS_PROJECT_STATUS.md   → understand current operational state
4. IDENTIFY the first unfinished task in the Current Sprint Tasks table
5. IMPLEMENT only that specific task
6. RUN tests to verify completion
7. UPDATE AI_BIOS_PROJECT_STATUS.md with results
8. REPORT: what was completed, what files were modified, what is next
```

An AI agent MUST NEVER:
- Skip reading all three files before starting work
- Assume context from a previous session
- Implement tasks from future phases
- Mark tasks complete without passing tests
- Deviate from architecture in AI_BIOS_MASTER.md without updating it first

---

# A3. Project Execution Rules

These rules apply to all developers and all AI coding agents without exception.

## Rule 1: Never Skip Phases
```
✅ Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7
❌ Phase 1 → Phase 3  (infrastructure dependency broken)
❌ Starting Phase 4 while Phase 3 acceptance criteria are unmet
```

## Rule 2: Never Implement Future Phase Features Early
```
✅ Implement COA approval dialog when Phase 6 begins
❌ Building COA UI while still in Phase 3
   (Reason: Phase 4 and 5 change the state architecture COA depends on)
```

## Rule 3: Always Update PROJECT_STATUS.md After Every Task
```
After completing any task:
  1. Set task status = "done" in Current Sprint Tasks table
  2. Move it to Completed Tasks section
  3. Recalculate and update Overall Completion %
  4. Append session log entry
  5. Commit PROJECT_STATUS.md alongside code changes
```

## Rule 4: Acceptance Criteria Are Not Optional
```
✅ Write test → test passes → criterion checked
❌ "It should work" is not verified
❌ "Close enough" is not done
```

## Rule 5: Run Tests Before Moving On
```bash
# After every task:
cd backend && pytest tests/ -x --tb=short

# After every phase:
cd backend && pytest tests/ -v --cov=app --cov-report=term
cd frontend && npm run test
```

## Rule 6: Architecture Changes Must Update the Master
```
If you discover a necessary architecture change:
  1. Stop implementation
  2. Update AI_BIOS_MASTER.md with the decision
  3. Record change in AI_BIOS_PROJECT_STATUS.md Architecture Drift Tracker
  4. Resume implementation from updated spec
Never silently deviate from AI_BIOS_MASTER.md.
```

## Rule 7: Commit Message Standard
```
Format: type(scope): description

Types:   feat | fix | test | refactor | docs | chore | security
Scopes:  auth | datasets | analysis | agents | coa | frontend | db | langgraph | rag | forecast | report

Examples:
  feat(rag): implement ChromaDB embedding pipeline with batch processing
  feat(agents): add InsightAgent with structured JSON output schema  
  fix(langgraph): correct routing after DataCleaningAgent partial failure
  test(sql): add 20 NL-to-SQL test cases with safety keyword rejection
  docs(status): update Phase 3 completion in PROJECT_STATUS.md
```

---

# A4. Reference Implementation Snippets

> These are copy-paste foundations for the learning edition. Not full implementations —
> starting points designed to be used alongside this document in Cursor.
> Full specifications are in the numbered sections.

---

## A4.1 Frontend Reference

### API Client with Auto-Refresh (`frontend/lib/api-client.ts`)
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

### Auth Zustand Store (`frontend/stores/auth-store.ts`)
```typescript
import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import apiClient from '@/lib/api-client'

interface User { id: string; email: string; full_name: string; role: string }
interface AuthState {
  user: User | null
  accessToken: string | null
  isAuthenticated: boolean
  login: (email: string, password: string) => Promise<void>
  logout: () => Promise<void>
  refreshToken: () => Promise<boolean>
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      user: null,
      accessToken: null,
      isAuthenticated: false,

      login: async (email, password) => {
        const { data } = await apiClient.post('/auth/login', { email, password })
        set({ user: data.user, accessToken: data.access_token, isAuthenticated: true })
        localStorage.setItem('refresh_token', data.refresh_token)
      },

      logout: async () => {
        const refresh = localStorage.getItem('refresh_token')
        if (refresh) await apiClient.post('/auth/logout', { refresh_token: refresh }).catch(() => {})
        localStorage.removeItem('refresh_token')
        set({ user: null, accessToken: null, isAuthenticated: false })
      },

      refreshToken: async () => {
        try {
          const refresh = localStorage.getItem('refresh_token')
          if (!refresh) return false
          const { data } = await apiClient.post('/auth/refresh', { refresh_token: refresh })
          set({ accessToken: data.access_token })
          return true
        } catch { return false }
      },
    }),
    { name: 'auth-storage', partialize: (s) => ({ user: s.user }) }
  )
)
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
    const ping = setInterval(() => {
      if (ws.current?.readyState === WebSocket.OPEN)
        ws.current.send(JSON.stringify({ type: 'ping' }))
    }, 30000)
    ws.current.onclose = () => { clearInterval(ping); setTimeout(connect, 3000) }
  }, [token, onMessage])

  useEffect(() => { connect(); return () => ws.current?.close() }, [connect])
}
```

### Analysis Progress Store (`frontend/stores/analysis-store.ts`)
```typescript
import { create } from 'zustand'
import apiClient from '@/lib/api-client'

interface AgentStep { name: string; status: 'pending' | 'running' | 'done' | 'failed'; duration_ms?: number }
interface AnalysisState {
  activeAnalysisId: string | null
  progress: number
  agentSteps: AgentStep[]
  result: Record<string, unknown> | null
  runAnalysis: (datasetId: string, types: string[]) => Promise<string>
  setProgress: (step: string, pct: number, agent: string) => void
  fetchResult: (id: string) => Promise<void>
}

export const useAnalysisStore = create<AnalysisState>((set) => ({
  activeAnalysisId: null,
  progress: 0,
  agentSteps: [],
  result: null,

  runAnalysis: async (datasetId, types) => {
    const { data } = await apiClient.post('/analyses/run', { dataset_id: datasetId, analysis_types: types })
    set({ activeAnalysisId: data.analysis_id, progress: 0, agentSteps: [], result: null })
    return data.analysis_id
  },

  setProgress: (step, pct, agent) =>
    set((s) => ({
      progress: pct,
      agentSteps: s.agentSteps.map((a) =>
        a.name === agent ? { ...a, status: 'running' } : a.status === 'running' ? { ...a, status: 'done' } : a
      ),
    })),

  fetchResult: async (id) => {
    const { data } = await apiClient.get(`/analyses/${id}`)
    set({ result: data })
  },
}))
```

### COA Approval Dialog (`frontend/components/coa/ApprovalDialog.tsx`)
```typescript
'use client'
import { useEffect, useState } from 'react'
import { createPortal } from 'react-dom'
import { AlertTriangle, Shield, Clock } from 'lucide-react'
import { Button } from '@/components/ui/button'

interface COAAction {
  action_id: string; action_type: string; target_application: string
  reason: string; expected_outcome: string; risk_level: 'low' | 'medium' | 'high' | 'critical'
  expires_at: string
}

const riskConfig = {
  low:      { color: 'text-emerald-600', bg: 'bg-emerald-50', icon: '✅' },
  medium:   { color: 'text-amber-600',   bg: 'bg-amber-50',   icon: '⚠️' },
  high:     { color: 'text-orange-600',  bg: 'bg-orange-50',  icon: '🔶' },
  critical: { color: 'text-red-600',     bg: 'bg-red-50',     icon: '🚨' },
}

export function ApprovalDialog({ action, onDecision }: {
  action: COAAction
  onDecision: (decision: { action_id: string; decision: string }) => void
}) {
  const [seconds, setSeconds] = useState(300)
  const risk = riskConfig[action.risk_level]

  useEffect(() => {
    const t = setInterval(() => {
      setSeconds((s) => {
        if (s <= 1) { onDecision({ action_id: action.action_id, decision: 'deny' }); return 0 }
        return s - 1
      })
    }, 1000)
    return () => clearInterval(t)
  }, [action.action_id, onDecision])

  const mins = Math.floor(seconds / 60)
  const secs = seconds % 60

  return createPortal(
    <div className="fixed inset-0 z-[9999] flex items-center justify-center bg-black/60 backdrop-blur-sm"
      role="dialog" aria-modal="true" aria-labelledby="coa-title">
      <div className="w-full max-w-lg rounded-2xl bg-white shadow-2xl p-6 border border-slate-200">
        <div className="flex items-center gap-3 mb-4">
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-blue-100">
            <Shield className="h-5 w-5 text-blue-600" />
          </div>
          <div>
            <h2 id="coa-title" className="font-semibold text-slate-900">Computer Operator Agent</h2>
            <p className="text-xs text-slate-500">Action approval required</p>
          </div>
        </div>

        <div className="space-y-3 mb-6 rounded-lg border border-slate-100 bg-slate-50 p-4 text-sm">
          {[
            ['Action', action.action_type.replace(/_/g, ' ')],
            ['Target', action.target_application],
            ['Reason', action.reason],
            ['Expected result', action.expected_outcome],
          ].map(([label, value]) => (
            <div key={label} className="flex gap-2">
              <span className="w-32 shrink-0 font-medium text-slate-600">{label}:</span>
              <span className="text-slate-800">{value}</span>
            </div>
          ))}
          <div className="flex gap-2">
            <span className="w-32 shrink-0 font-medium text-slate-600">Risk level:</span>
            <span className={`font-semibold ${risk.color}`}>{risk.icon} {action.risk_level.toUpperCase()}</span>
          </div>
        </div>

        <div className="grid grid-cols-4 gap-2 mb-4">
          {(['allow_once', 'allow_session', 'always_allow', 'deny'] as const).map((d) => (
            <Button key={d} variant={d === 'deny' ? 'destructive' : 'outline'} size="sm"
              onClick={() => onDecision({ action_id: action.action_id, decision: d })}>
              {d === 'allow_once' ? 'Allow Once' : d === 'allow_session' ? 'Session' : d === 'always_allow' ? 'Always' : 'Deny'}
            </Button>
          ))}
        </div>

        <div className={`flex items-center gap-2 text-xs ${seconds < 60 ? 'text-red-500' : 'text-slate-500'}`}>
          <Clock className="h-3 w-3" />
          Auto-deny in: {mins}:{secs.toString().padStart(2, '0')}
        </div>
      </div>
    </div>,
    document.body
  )
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
from app.middleware.logging_middleware import LoggingMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup checks
    from app.db.session import engine
    from app.db.base import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    from app.db.session import engine as e
    await e.dispose()

app = FastAPI(title="AI-BIOS API", version="1.1.0", lifespan=lifespan)

app.add_middleware(CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(LoggingMiddleware)

app.include_router(api_router, prefix="/api/v1")
app.include_router(ws_router)

@app.get("/health")
async def health():
    return {"status": "healthy", "version": settings.APP_VERSION}
```

### FastAPI Dependencies (`backend/app/dependencies.py`)
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
    payload = decode_access_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = await UserRepository(db).get_by_id(payload["sub"])
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="User not found or inactive")
    return user

def require_admin(user: User = Depends(get_current_user)) -> User:
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return user
```

### JWT Handler (`backend/app/security/jwt_handler.py`)
```python
from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt, secrets
from app.config import settings

def create_access_token(user_id: str, role: str) -> str:
    exp = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode({"sub": user_id, "role": role, "exp": exp, "type": "access"},
                      settings.JWT_SECRET_KEY, algorithm="HS256")

def create_refresh_token(user_id: str) -> str:
    exp = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    return jwt.encode({"sub": user_id, "exp": exp, "jti": secrets.token_hex(16), "type": "refresh"},
                      settings.JWT_SECRET_KEY, algorithm="HS256")

def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
        return payload if payload.get("type") == "access" else None
    except jwt.PyJWTError:
        return None
```

### Celery App (`backend/app/tasks/celery_app.py`)
```python
from celery import Celery
from app.config import settings

celery_app = Celery(
    "aibios",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=[
        "app.tasks.analysis_tasks",
        "app.tasks.report_tasks",
        "app.tasks.forecast_tasks",
        "app.tasks.embedding_tasks",
    ]
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_routes={
        "app.tasks.analysis_tasks.*": {"queue": "compute"},
        "app.tasks.embedding_tasks.*": {"queue": "ai"},
        "app.tasks.report_tasks.*":   {"queue": "reports"},
        "app.tasks.forecast_tasks.*": {"queue": "compute"},
    },
    task_time_limit=1900,
    task_soft_time_limit=1800,
)
```

---

## A4.3 Database Reference

### TimestampMixin + Base (`backend/app/db/base.py`)
```python
import uuid
from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class TimestampMixin:
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
```

### Alembic Migration Pattern
```python
# alembic/versions/001_create_users_table.py
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    op.create_table("users",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("full_name", sa.String(100), nullable=False),
        sa.Column("role", sa.String(20), nullable=False, server_default="user"),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="true"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

def downgrade():
    op.drop_index("ix_users_email", "users")
    op.drop_table("users")
```

---

## A4.4 LangGraph Reference

### Analysis State (`backend/app/workflows/analysis_workflow.py`)
```python
from typing import TypedDict, Optional, List, Dict, Any
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

class AnalysisState(TypedDict):
    analysis_id: str
    dataset_id: str
    project_id: str
    user_id: str
    analysis_types: List[str]
    config: Dict[str, Any]
    current_step: str
    progress_pct: int
    errors: List[str]
    warnings: List[str]
    retry_counts: Dict[str, int]
    raw_dataframe_path: str
    cleaned_dataframe_path: Optional[str]
    cleaning_report: Optional[Dict[str, Any]]
    eda_report: Optional[Dict[str, Any]]
    chart_specs: Optional[List[Dict[str, Any]]]
    chart_configs: Optional[List[Dict[str, Any]]]
    insights: Optional[List[Dict[str, Any]]]
    consultant_memo: Optional[str]
    report_path: Optional[str]
    started_at: str
    completed_at: Optional[str]
```

### Node + Conditional Routing
```python
# Node function — each agent is wrapped as a node
async def run_eda(state: AnalysisState) -> AnalysisState:
    from app.agents.eda_agent import EDAAgent
    return await EDAAgent().run(state)

# Routing function
def route_after_cleaning(state: AnalysisState) -> str:
    if state.get("cleaned_dataframe_path"):
        return "run_eda"
    return "handle_error"

def route_after_consultant(state: AnalysisState) -> str:
    return "generate_report" if "report" in state.get("analysis_types", []) else END

# Graph assembly
def build_analysis_graph():
    g = StateGraph(AnalysisState)
    for name, fn in [
        ("validate_dataset",        validate_dataset),
        ("run_data_cleaning",       run_data_cleaning),
        ("run_eda",                 run_eda),
        ("run_visualization",       run_visualization),
        ("run_insight_generation",  run_insight_generation),
        ("run_consultant_analysis", run_consultant_analysis),
        ("generate_report",         generate_report),
        ("handle_error",            handle_error),
    ]:
        g.add_node(name, fn)

    g.set_entry_point("validate_dataset")
    g.add_conditional_edges("validate_dataset",
        lambda s: "run_data_cleaning" if not s.get("errors") else "handle_error")
    g.add_conditional_edges("run_data_cleaning", route_after_cleaning)
    g.add_edge("run_eda",                 "run_visualization")
    g.add_edge("run_visualization",       "run_insight_generation")
    g.add_edge("run_insight_generation",  "run_consultant_analysis")
    g.add_conditional_edges("run_consultant_analysis", route_after_consultant)
    g.add_edge("generate_report", END)
    g.add_edge("handle_error",    END)

    return g.compile(checkpointer=MemorySaver())
```

### Chat Workflow State
```python
class ChatState(TypedDict):
    session_id: str
    dataset_id: str
    user_id: str
    user_message: str
    message_intent: str          # statistical | sql | chart | general_bi
    retrieved_chunks: List[str]
    sql_result: Optional[Any]
    chart_config: Optional[Dict]
    response_text: str
    sources: List[Dict]
    conversation_history: List[Dict]
    context_summary: Optional[str]
    turn_count: int
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
        self.chroma = AsyncHttpClient(host=settings.CHROMA_HOST, port=settings.CHROMA_PORT)

    def _chunk_dataframe(self, df, dataset_id: str) -> list[dict]:
        chunks = []
        # Column descriptions
        for col in df.columns:
            desc = f"Column '{col}' ({df[col].dtype}): {df[col].isna().sum()} nulls, {df[col].nunique()} unique."
            if df[col].dtype in ["int64", "float64"]:
                desc += f" Mean: {df[col].mean():.2f}. Range: {df[col].min():.2f}–{df[col].max():.2f}."
            chunks.append({"id": f"{dataset_id}_col_{col}", "text": desc, "type": "column"})
        # Row samples (batches of 25)
        sample = df.sample(min(500, len(df)))
        for i in range(0, len(sample), 25):
            text = sample.iloc[i:i+25].to_dict(orient="records").__repr__()[:2000]
            chunks.append({"id": f"{dataset_id}_rows_{i}", "text": text, "type": "rows"})
        # Aggregate facts
        for col in df.select_dtypes(include="number").columns:
            chunks.append({"id": f"{dataset_id}_agg_{col}",
                           "text": f"Total {col}: {df[col].sum():.2f}. Avg: {df[col].mean():.2f}.",
                           "type": "aggregate"})
        return chunks

    async def embed_and_store(self, dataset_id: str, df) -> int:
        collection = await self.chroma.get_or_create_collection(f"dataset_{dataset_id}")
        chunks = self._chunk_dataframe(df, dataset_id)
        for i in range(0, len(chunks), 100):
            batch = chunks[i:i+100]
            result = genai.embed_content(model="models/text-embedding-004",
                                         content=[c["text"] for c in batch],
                                         task_type="retrieval_document")
            await collection.upsert(
                ids=[c["id"] for c in batch],
                documents=[c["text"] for c in batch],
                embeddings=result["embedding"],
                metadatas=[{"type": c["type"]} for c in batch],
            )
        return len(chunks)

    async def query(self, dataset_id: str, question: str, top_k: int = 10) -> list[str]:
        collection = await self.chroma.get_or_create_collection(f"dataset_{dataset_id}")
        q_emb = genai.embed_content(model="models/text-embedding-004",
                                     content=question,
                                     task_type="retrieval_query")["embedding"]
        results = await collection.query(query_embeddings=[q_emb], n_results=top_k)
        return results["documents"][0]
```

---

## A4.6 Forecasting Reference

### Prophet Engine
```python
import pandas as pd
from prophet import Prophet

class ProphetEngine:
    def prepare(self, df: pd.DataFrame, date_col: str, target_col: str) -> pd.DataFrame:
        out = df[[date_col, target_col]].copy()
        out.columns = ["ds", "y"]
        out["ds"] = pd.to_datetime(out["ds"])
        return out.dropna().sort_values("ds")

    def fit_predict(self, df: pd.DataFrame, horizon: int, freq: str = "D") -> pd.DataFrame:
        m = Prophet(yearly_seasonality="auto", weekly_seasonality="auto",
                    daily_seasonality=False, changepoint_prior_scale=0.05, interval_width=0.95)
        m.fit(df)
        future = m.make_future_dataframe(periods=horizon, freq=freq)
        fc = m.predict(future)
        return fc[["ds", "yhat", "yhat_lower", "yhat_upper", "trend"]]

    def to_recharts(self, forecast: pd.DataFrame, actual: pd.DataFrame) -> dict:
        actual_map = dict(zip(actual["ds"].astype(str), actual["y"]))
        data = [{"date": str(r.ds.date()), "actual": actual_map.get(str(r.ds.date())),
                 "forecast": round(r.yhat, 2), "lower": round(r.yhat_lower, 2),
                 "upper": round(r.yhat_upper, 2)} for _, r in forecast.iterrows()]
        return {"chart_type": "area", "data": data,
                "series": [{"key": "actual", "stroke": "#3b82f6"},
                            {"key": "forecast", "stroke": "#f59e0b", "strokeDasharray": "5 5"}]}
```

### XGBoost Engine
```python
import pandas as pd
from xgboost import XGBRegressor

class XGBoostTimeSeriesEngine:
    def engineer_features(self, df, target_col, date_col):
        df = df.copy().sort_values(date_col)
        y = df[target_col]
        for lag in [1, 3, 7, 14, 28]:
            df[f"lag_{lag}"] = y.shift(lag)
        for w in [7, 14, 28]:
            df[f"roll_mean_{w}"] = y.shift(1).rolling(w).mean()
        df["dow"]   = pd.to_datetime(df[date_col]).dt.dayofweek
        df["month"] = pd.to_datetime(df[date_col]).dt.month
        df["is_wknd"] = df["dow"].isin([5,6]).astype(int)
        return df.dropna()

    def fit(self, X, y):
        split = int(len(X) * 0.8)
        m = XGBRegressor(n_estimators=200, max_depth=6, learning_rate=0.05,
                         subsample=0.8, early_stopping_rounds=20)
        m.fit(X.iloc[:split], y.iloc[:split],
              eval_set=[(X.iloc[split:], y.iloc[split:])], verbose=False)
        return m
```

---

## A4.7 Reporting Reference

### PDF Generator
```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle

def build_pdf_report(output_path: str, data: dict) -> str:
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                            leftMargin=25*mm, rightMargin=25*mm,
                            topMargin=20*mm, bottomMargin=20*mm)
    h1 = ParagraphStyle("H1", fontSize=24, textColor=HexColor("#1E293B"), fontName="Helvetica-Bold")
    h2 = ParagraphStyle("H2", fontSize=16, textColor=HexColor("#334155"), spaceAfter=8)
    body = ParagraphStyle("Body", fontSize=10, leading=14, textColor=HexColor("#475569"))
    story = []
    story.append(Paragraph(data["title"], h1))
    story.append(Paragraph(f"Dataset: {data['dataset_name']} | {data['date']}", body))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Executive Summary", h2))
    story.append(Paragraph(data["executive_summary"], body))
    for insight in data.get("insights", [])[:5]:
        story.append(Paragraph(f"• {insight['title']}", h2))
        story.append(Paragraph(insight["description"], body))
    for chart_path in data.get("chart_paths", []):
        story.append(Image(chart_path, width=160*mm, height=80*mm))
    doc.build(story)
    return output_path
```

### PPTX Generator
```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def build_pptx_report(output_path: str, data: dict) -> str:
    prs = Presentation()
    prs.slide_width  = Inches(13.33)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]
    BLUE = RGBColor(0x3B, 0x82, 0xF6)
    DARK = RGBColor(0x1E, 0x29, 0x3B)

    # Title slide
    s = prs.slides.add_slide(blank)
    hdr = s.shapes.add_shape(1, 0, 0, prs.slide_width, Inches(1.5))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = BLUE
    tf = s.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12), Inches(0.9)).text_frame
    tf.text = data["title"]
    tf.paragraphs[0].font.size = Pt(36)
    tf.paragraphs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    # Chart slides
    for chart_path, caption in zip(data.get("chart_paths", []), data.get("chart_captions", [])):
        cs = prs.slides.add_slide(blank)
        cs.shapes.add_picture(chart_path, Inches(0.5), Inches(0.9), Inches(12), Inches(5.5))
        cap = cs.shapes.add_textbox(Inches(0.5), Inches(6.5), Inches(12), Inches(0.5)).text_frame
        cap.text = caption; cap.paragraphs[0].font.size = Pt(10)

    prs.save(output_path)
    return output_path
```

---

## A4.8 Computer Operator Agent Reference

### Action Request Schema
```python
from pydantic import BaseModel
from enum import Enum
from typing import Any, Optional

class COAActionType(str, Enum):
    OPEN_APPLICATION = "open_application"
    OPEN_FILE        = "open_file"
    RUN_SCRIPT       = "run_script"
    EXECUTE_SQL      = "execute_sql"
    EXPORT_TO_EXCEL  = "export_to_excel"
    OPEN_URL         = "open_url"
    FILL_FORM        = "fill_form"
    RUN_WORKFLOW     = "run_workflow"

class RiskLevel(str, Enum):
    LOW = "low"; MEDIUM = "medium"; HIGH = "high"; CRITICAL = "critical"

class ApprovalScope(str, Enum):
    ONCE = "once"; SESSION = "session"; ALWAYS = "always"

class COAActionRequest(BaseModel):
    action_type:        COAActionType
    target_application: str
    action_params:      dict[str, Any]
    reason:             str
    expected_outcome:   str
    risk_level:         RiskLevel
    rollback_strategy:  Optional[str] = None
    timeout_seconds:    int = 300
```

### Approval Manager
```python
import hmac, hashlib, secrets, json
from datetime import datetime, timedelta, timezone
from app.cache.client import redis_client
from app.api.websocket.manager import ws_manager
from app.config import settings

class ApprovalManager:
    TIMEOUT = 300

    async def request_approval(self, action: dict, user_id: str) -> str:
        action_id = secrets.token_urlsafe(16)
        await redis_client.setex(f"coa:pending:{action_id}", self.TIMEOUT,
                                  json.dumps({**action, "action_id": action_id, "user_id": user_id}))
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
        msg = f"{action_id}:{user_id}:{secrets.token_hex(8)}"
        sig = hmac.new(settings.COA_LOCAL_AGENT_WS_SECRET.encode(), msg.encode(), hashlib.sha256).hexdigest()
        return f"{msg}:{sig}"

    def verify_execution_token(self, token: str) -> bool:
        parts = token.rsplit(":", 1)
        if len(parts) != 2: return False
        msg, sig = parts
        expected = hmac.new(settings.COA_LOCAL_AGENT_WS_SECRET.encode(),
                            msg.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(sig, expected)
```

---

## A4.9 Deployment Reference

### docker-compose.yml (Local Development)
```yaml
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
      interval: 5s; retries: 5

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

### .env.example
```bash
APP_NAME=AI-BIOS
APP_ENV=development
DEBUG=true

DATABASE_URL=postgresql+asyncpg://aibios:aibios_dev@localhost:5432/aibios
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2

JWT_SECRET_KEY=CHANGE_ME_64_CHAR_HEX
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
PASSWORD_HASH_ROUNDS=12

GEMINI_API_KEY=your-gemini-api-key
GEMINI_PRO_MODEL=gemini-2.5-pro
GEMINI_FLASH_MODEL=gemini-2.5-flash

CHROMA_HOST=localhost
CHROMA_PORT=8001

STORAGE_BACKEND=local
STORAGE_LOCAL_PATH=./uploads
MAX_UPLOAD_SIZE_MB=500

ENCRYPTION_KEY=CHANGE_ME_FERNET_KEY
ALLOWED_ORIGINS=http://localhost:3000

COA_APPROVAL_TIMEOUT_SECONDS=300
COA_LOCAL_AGENT_WS_SECRET=CHANGE_ME_HMAC_SECRET

NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_WS_URL=ws://localhost:8000/ws
NEXT_PUBLIC_ENABLE_COA=true
```

---

> **AI_BIOS_MASTER_LEARNING_EDITION.md — VERSION 1.1.0 — COMPLETE**
> All project management, execution rules, quick-resume protocols, and reference snippets added.
> Three mandatory files: AI_BIOS_MASTER.md + AI_BIOS_MASTER_LEARNING_EDITION.md + AI_BIOS_PROJECT_STATUS.md
> Build something you understand completely. 🚀


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

> This protocol applies to every AI tool before any implementation task begins.
> No exceptions. No assumptions about unchanged architecture.

## A6.1 Why This Protocol Exists

Between development sessions:
- Files may have been created, moved, or deleted
- Dependencies may have been upgraded or changed
- LangGraph state schemas may have evolved
- Database models may have been altered via migrations
- Agent prompts may have been updated
- The implementation may have deviated from the specification in `AI_BIOS_MASTER.md`

An AI agent that writes code without first inspecting the current project state will produce code that conflicts with reality. This protocol prevents that.

## A6.2 Mandatory Pre-Implementation Inspection Checklist

Before generating or modifying a single line of code, every AI tool MUST complete this inspection:

```
□ 1. FOLDER STRUCTURE
      Command: list all files and directories from project root
      Purpose: understand what has been created vs what the spec requires
      Check:   does the actual structure match Section A5 (Root Project Structure)?

□ 2. EXISTING SOURCE CODE
      Inspect: backend/app/ — all existing modules, services, agents
      Inspect: frontend/ — all existing pages, components, stores, hooks
      Purpose: avoid regenerating code that already exists; avoid conflicting implementations

□ 3. EXISTING APIs
      Inspect: backend/app/api/v1/*.py — all implemented routers and endpoints
      Purpose: confirm which endpoints are implemented vs which are still planned
      Check:   do existing endpoints match the specs in Section 7 of AI_BIOS_MASTER.md?

□ 4. EXISTING DATABASE MODELS
      Inspect: backend/app/models/*.py
      Inspect: backend/alembic/versions/ — all migration files
      Purpose: know the current DB schema; avoid creating conflicting models
      Check:   do models match the ER diagram in Section 6 of AI_BIOS_MASTER.md?

□ 5. EXISTING LANGGRAPH WORKFLOWS
      Inspect: backend/app/workflows/*.py
      Purpose: understand current graph topology and state schemas
      Check:   does the graph match Section 10 / Section 30 of AI_BIOS_MASTER.md?

□ 6. EXISTING AGENTS
      Inspect: backend/app/agents/*.py
      Purpose: understand which of the 11 agents are implemented
      Check:   do agent tools and outputs match Section 9 / Section 51 of AI_BIOS_MASTER.md?

□ 7. EXISTING PROMPTS
      Inspect: any system prompt strings in agent files or prompt template files
      Purpose: avoid duplicating or overwriting existing prompt engineering
      Check:   do prompts follow the structure in Section 31 of AI_BIOS_MASTER.md?

□ 8. CURRENT DEPENDENCIES
      Inspect: backend/requirements.txt (or pyproject.toml)
      Inspect: frontend/package.json
      Purpose: confirm actual library versions vs locked versions in STATUS.md
      Check:   are all required packages from Section 41 of AI_BIOS_MASTER.md present?

□ 9. CURRENT PROJECT STATUS
      Read:    AI_BIOS_PROJECT_STATUS.md — Current Phase, Sprint, open tasks, blockers
      Purpose: understand operational state before touching any code

□ 10. CURRENT GIT BRANCH
       Command: git branch --show-current (if git available)
       Command: git log --oneline -5 (last 5 commits)
       Purpose: confirm you are on the correct branch and understand recent changes
```

## A6.3 Architecture Comparison Step

After completing the inspection, perform this comparison before writing code:

```
PLANNED (from AI_BIOS_MASTER.md)    vs    ACTUAL (from codebase inspection)
────────────────────────────────         ──────────────────────────────────
Folder structure per Section A5          → Actual folders found on disk
Models per Section 6 (ER diagram)        → Actual SQLAlchemy models
API endpoints per Section 7              → Actual FastAPI routers
LangGraph state per Section 30           → Actual TypedDict definitions
Agent tools per Section 28               → Actual @tool functions
Dependencies per Section 41              → Actual requirements.txt
```

**If differences are found:**

1. Document the drift in `AI_BIOS_PROJECT_STATUS.md` → Architecture Drift Tracker
2. Determine which is authoritative: specification or implementation
3. If implementation intentionally diverges → update `AI_BIOS_MASTER.md` first
4. If implementation accidentally diverges → fix the implementation
5. Only then proceed with the new task

**Decision rule:**

```
Implementation intentionally diverged  →  Update MASTER.md, record in Drift Tracker
Implementation accidentally diverged   →  Fix implementation, record in Drift Tracker
No drift found                         →  Proceed with next task
```

## A6.4 Reporting Format

When an AI agent completes the context loading protocol, it should produce a brief status report before coding:

```
CONTEXT LOADING REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Current Phase:     Phase X — [Name]
Current Sprint:    Sprint Y — [Goal]
Current Task:      TASK-XXX — [Description]

Folder Structure:  ✅ Matches spec / ⚠️ Drift found (detail)
Models:            ✅ Matches spec / ⚠️ Drift found (detail)
APIs:              ✅ Matches spec / ⚠️ Drift found (detail)
LangGraph:         ✅ Matches spec / ⚠️ N/A (not yet implemented)
Agents:            ✅ Matches spec / ⚠️ N/A
Dependencies:      ✅ All present / ⚠️ Missing: [package list]
Git Branch:        main / develop / feature/xxx

Architecture Drift: None / [Description of drift found]
Action Before Coding: [None needed / Update MASTER.md / Fix implementation]

Ready to implement: TASK-XXX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

# A7. AI Development Startup Checklist

> Run this checklist at the beginning of every coding session, every time, with every tool.

```
BEFORE WRITING ANY CODE:

  □ Step 1:  Read AI_BIOS_MASTER.md
             Focus on the section matching your current phase
             Refresh architecture, API specs, agent definitions

  □ Step 2:  Read AI_BIOS_MASTER_LEARNING_EDITION.md
             Confirm which learning phase you are in
             Confirm tool usage for today (Section A8 IDE Responsibility Matrix)

  □ Step 3:  Read AI_BIOS_PROJECT_STATUS.md
             Note: Current Phase, Sprint, Milestone
             Note: Open bugs and blockers
             Note: Last session's "Next Action"

  □ Step 4:  Inspect project folder structure
             List actual files on disk
             Compare to Section A5 (Root Project Structure)

  □ Step 5:  Inspect current codebase
             Scan backend/app/ and frontend/ for existing implementations
             Do not regenerate what already exists

  □ Step 6:  Inspect current dependencies
             Check requirements.txt and package.json
             Compare to Section 41 of AI_BIOS_MASTER.md

  □ Step 7:  Inspect current LangGraph workflows
             Check backend/app/workflows/*.py (if Phase 3+)
             Understand current graph topology

  □ Step 8:  Determine active phase
             AI_BIOS_PROJECT_STATUS.md → "Current Phase" field

  □ Step 9:  Determine active sprint
             AI_BIOS_PROJECT_STATUS.md → "Current Sprint" field

  □ Step 10: Determine active task
             AI_BIOS_PROJECT_STATUS.md → Current Sprint Tasks → first "todo" or "in-progress"

ONLY THEN begin implementation.
```

**Time estimate for checklist:** 10–15 minutes. Non-negotiable. This prevents hours of rework.

---

# A8. IDE Responsibility Matrix

> Use the right tool for the right task. Switching tools unnecessarily wastes free-tier limits.
> Follow the escalation chain when a tool's free tier is exhausted.

## A8.1 Tool Assignments

### 🖥️ Cursor — Primary Software Engineer

| Attribute | Detail |
|-----------|--------|
| **Role** | Primary Software Engineer |
| **Scope** | All implementation across the full project lifecycle |

**Use Cursor for:**
- FastAPI endpoint implementation (routers, schemas, services, repositories)
- Next.js pages, layouts, and App Router structure
- React components, Zustand stores, custom hooks
- LangGraph workflow graph assembly (`build_analysis_graph()`, etc.)
- SQLAlchemy model definitions and Alembic migration generation
- Celery task implementation
- Database repository pattern implementation
- Code refactoring and cleanup
- Implementing tasks directly from the Section 25 task breakdown

**Do NOT use Cursor for:**
- Long-form architecture research or learning (use Gemini Chat)
- Understanding new concepts before implementing (use Gemini Chat or ChatGPT first)
- Prompt engineering for agents (use Google AI Studio first)
- Debugging complex multi-agent LangGraph state issues (use LangGraph Studio + Claude)

**Free-tier management:**
- Attach `@AI_BIOS_MASTER.md` and `@AI_BIOS_PROJECT_STATUS.md` as context every session
- Implement one task at a time to stay within context window
- When context limit hit: start a fresh Cursor session with new task + fresh context

---

### ⚡ Antigravity — Boilerplate Generator

| Attribute | Detail |
|-----------|--------|
| **Role** | Boilerplate Generator |
| **Scope** | Scaffolding repetitive code patterns |

**Use Antigravity for:**
- CRUD API generation (create endpoint + schema + service + repo in one shot)
- Pydantic schema generation from a table description
- SQLAlchemy model generation from column descriptions
- Repository pattern boilerplate
- Next.js UI page scaffolding (forms, tables, list pages)
- Test file boilerplate generation

**Do NOT use Antigravity for:**
- Agent architecture design or LangGraph workflow design
- Complex multi-agent orchestration code
- Security-sensitive code (JWT, HMAC, approval flows) — use Cursor with MASTER.md
- Anything requiring understanding of the full system architecture

**When Cursor limits hit → Switch to Antigravity for:** any task that is primarily scaffolding or CRUD without complex business logic.

---

### 🔧 VS Code Copilot — Micro Coding Assistant

| Attribute | Detail |
|-----------|--------|
| **Role** | Micro Coding Assistant |
| **Scope** | Small, inline assistance within existing code |

**Use Copilot for:**
- Completing individual functions within an existing file
- Writing unit tests for a specific function
- Quick bug fixes within a known pattern
- Import statement completion
- Docstring generation

**Do NOT use Copilot for:**
- Architecture decisions or multi-file feature implementation
- Understanding new LangGraph concepts
- Writing new agents from scratch (use Cursor with MASTER.md)

---

### 🏛️ Claude — Principal Architect

| Attribute | Detail |
|-----------|--------|
| **Role** | Principal Architect |
| **Scope** | Architecture, review, and documentation |

**Use Claude for:**
- Architecture decisions not covered by AI_BIOS_MASTER.md
- Agent design review before implementation
- LangGraph workflow design review (state schema, routing logic)
- Security architecture review (COA approval flows, JWT design)
- Review of completed agent implementations
- Documentation generation and MASTER.md updates
- When a task requires understanding the full system before deciding how to implement

**Do NOT use Claude for:**
- Line-by-line code generation of large files (use Cursor)
- Routine boilerplate (use Antigravity or Copilot)

**Session protocol with Claude:**
```
1. Paste the relevant MASTER.md section as context
2. Describe the specific architecture question or review request
3. Implement the decision in Cursor
4. Update AI_BIOS_MASTER.md if the decision changes the spec
```

---

### 🔍 ChatGPT — Senior Systems Engineer

| Attribute | Detail |
|-----------|--------|
| **Role** | Senior Systems Engineer |
| **Scope** | Debugging, tradeoff analysis, learning support |

**Use ChatGPT for:**
- Debugging a specific error that Cursor cannot resolve
- Design discussions: comparing two implementation approaches
- Tradeoff analysis: library A vs library B for a specific use case
- Understanding error messages from pandas, LangGraph, or Celery
- When Claude free tier is exhausted and you need architecture input

**Do NOT use ChatGPT for:**
- AI-BIOS-specific architecture decisions (it doesn't know MASTER.md)
- Generating large amounts of boilerplate (use Antigravity)

---

### 🔬 Gemini Chat — Research Engineer

| Attribute | Detail |
|-----------|--------|
| **Role** | Research Engineer |
| **Scope** | Learning and concept research |

**Use Gemini Chat for:**
- Learning LangGraph concepts before implementing (e.g., "explain StateGraph conditional edges")
- Learning RAG architecture patterns before building the pipeline
- Learning Prophet/XGBoost time series patterns
- Understanding Agentic AI design patterns
- Reviewing your implementation approach against best practices
- Learning ChromaDB collection management

**Do NOT use Gemini Chat for:**
- Code generation for AI-BIOS (use Cursor)
- Architecture decisions (use Claude)

---

### 🧪 Google AI Studio — Prompt Engineering Laboratory

| Attribute | Detail |
|-----------|--------|
| **Role** | Prompt Engineering Laboratory |
| **Scope** | Agent system prompt development and testing |

**Use Google AI Studio for:**
- Writing and iterating EDA Agent system prompts before wiring into code
- Writing and iterating Insight Agent prompts
- Writing and iterating SQL Agent safety prompts
- Writing Chat Agent persona and RAG prompts
- Writing Consultant Agent strategic reasoning prompts
- Writing Report Agent executive summary prompts
- Testing structured JSON output schemas from agents
- Iterating on forecast explanation prompts

**Workflow:**
```
1. Open Google AI Studio
2. Set model: Gemini 2.5 Pro (or Flash for fast iteration)
3. Write draft system prompt
4. Run test inputs against it
5. Iterate until output matches Pydantic schema
6. Copy finalized prompt into agent file in Cursor
7. Write test to verify agent output format
```

**Do NOT use AI Studio for:**
- Code generation
- Architecture decisions

---

### 🔭 LangGraph Studio — Agent Observatory

| Attribute | Detail |
|-----------|--------|
| **Role** | Agent Observatory |
| **Scope** | Workflow debugging, state inspection, agent testing |

**Use LangGraph Studio for:**
- Visualizing the analysis workflow graph after implementation
- Inspecting state at each node during a test run
- Debugging why a conditional edge routes to the wrong node
- Testing human-in-the-loop interrupt behavior (COA approval flow)
- Verifying agent retry behavior after simulated Gemini failure
- Testing individual agents in isolation
- Demonstrating the multi-agent workflow (portfolio screenshots)

**Do NOT use LangGraph Studio for:**
- Writing code (it is not a coding IDE)
- Production execution (development tool only)

**Setup reminder:**
```bash
cd backend
langgraph dev
# Open http://localhost:8123
```

---

## A8.2 Tool Escalation Chain

When a tool hits its free-tier limit, follow this escalation:

```
PRIMARY:   Cursor (implementation)
    ↓ limit hit
SECONDARY: Antigravity (scaffolding + CRUD)
    ↓ limit hit
TERTIARY:  VS Code Copilot (inline micro-tasks)

PRIMARY:   Claude (architecture)
    ↓ limit hit
SECONDARY: ChatGPT (debugging + design)
    ↓ limit hit
TERTIARY:  Gemini Chat (research mode)

ALWAYS AVAILABLE (local, no limits):
  LangGraph Studio
  Docker + PostgreSQL + Redis + ChromaDB
  Gemini API (rate-limited but not hard-blocked)
```

## A8.3 Free-Tier Development Strategy

The entire AI-BIOS project must be buildable using free-tier resources only.

| Rule | Detail |
|------|--------|
| **1. Cursor first** | All implementation starts in Cursor. Attach MASTER.md as context every session. |
| **2. Cursor limit → Antigravity** | When Cursor context/request limit hit: switch to Antigravity for scaffolding and CRUD-level tasks |
| **3. Antigravity limit → Copilot** | When Antigravity limit hit: use VS Code Copilot for small inline tasks that don't require full project context |
| **4. Claude for architecture** | Architecture reviews, agent design, workflow reviews, and documentation. Claude free tier resets daily. |
| **5. ChatGPT for debugging** | Specific error messages, tradeoff analysis, design discussions when Claude limit is hit |
| **6. Gemini Chat for learning** | Learn concepts before implementing. Never blocked — always available via browser |
| **7. AI Studio for prompts** | Prompt engineering laboratory. Free tier is generous — use for all agent prompt development |
| **8. LangGraph Studio for validation** | Always free (local). Use for every LangGraph graph you implement — mandatory validation step |

**Cost target: $0/month during Phases 1–7 development** (Gemini API free tier: 15 req/min, 1M tokens/day — sufficient for learning-pace development)

---

# A9. Development Environment — Active State

> This section is updated at the start of each session to reflect the current environment.

| Field | Current Value |
|-------|--------------|
| **Current IDE** | Cursor |
| **Current Model** | *(update each session)* |
| **Current Module** | *(update each session — e.g., `backend/app/api/v1/auth.py`)* |
| **Current Phase** | Phase 1 — Backend Foundations |
| **Current Sprint** | Sprint 1 — Infrastructure & Auth |
| **Current Task** | TASK-001 — Initialize backend project structure |
| **Next Recommended Tool** | Cursor (implementation) |
| **Reason** | All Phase 1 tasks are implementation — Cursor is primary tool |

**Instructions:** Update this table at the start of every session. If switching tools mid-session, update "Current IDE" and "Next Recommended Tool" to reflect the switch and the reason.

