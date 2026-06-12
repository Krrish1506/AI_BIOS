# AI_BIOS_PROJECT_STATUS.md
# AI Business Intelligence Operating System
## Project Operational Memory & Status Tracker

> **Document Type:** Operational Memory — Read BEFORE every development session
> **Version:** 1.0.0
> **Project:** AI-BIOS (AI Business Intelligence Operating System)
> **Architecture SSOT:** AI_BIOS_MASTER.md
> **Learning Guide:** AI_BIOS_MASTER_LEARNING_EDITION.md
> **Last Updated:** 2026-06-12
> **Updated By:** Cursor (PROJECT_STATUS consistency update)

---

> ⚠️ **AGENT INSTRUCTION:** Every AI coding agent (Cursor, Claude Code, OpenHands, Roo Code, Cline, ChatGPT, Gemini) MUST read this file before starting any development work. Find the first task with status `todo` or `in-progress` and begin there. Update this file after every task.

---

## 📊 Project Overview

| Field | Value |
|-------|-------|
| **Project Name** | AI Business Intelligence Operating System (AI-BIOS) |
| **Edition** | Learning Edition v1.1.0 |
| **Current Phase** | Phase 1 — Backend Foundations |
| **Current Sprint** | Sprint 1 — Infrastructure & Auth |
| **Current Milestone** | M0: ✅ COMPLETE - Scaffolding & Structure | M1: Local Development Environment Running |
| **Overall Completion** | 8% (backend scaffold + config layer complete) |
| **Development Mode** | Local (docker-compose) |
| **Target Deployment** | Local → Vercel + Render + Neon |
| **Primary Developer** | Solo Developer |
| **AI Tools in Use** | Cursor, Claude, ChatGPT, LangGraph Studio |
| **Last Session Date** | 2026-06-12 |
| **Last Session Tool** | Cursor |
| **Next Immediate Action** | TASK-003: Create SQLAlchemy base + TimestampMixin |

---

## 🗺️ Progress Tracker

| Phase | Name | Status | Completion | Started | Completed |
|-------|------|--------|-----------|---------|-----------|
| **Phase 0** | Project Scaffolding & Structure | 🟢 Complete | 100% | 2026-06-12 | 2026-06-12 |
| **Phase 1** | Backend Foundations | 🟡 In Progress | 10% | 2026-06-12 | — |
| **Phase 2** | Dataset Intelligence | ⬜ Locked | 0% | — | — |
| **Phase 3** | RAG & Chat With Data | ⬜ Locked | 0% | — | — |
| **Phase 4** | Forecasting & Reports | ⬜ Locked | 0% | — | — |
| **Phase 5** | Multi-Agent System | ⬜ Locked | 0% | — | — |
| **Phase 6** | Computer Operator Agent | ⬜ Locked | 0% | — | — |
| **Phase 7** | Power BI Integration | ⬜ Locked | 0% | — | — |

**Legend:** 🔴 Not Started | 🟡 In Progress | 🟢 Complete | ⬜ Locked (previous phase incomplete)

---

## 📋 Current Sprint Tasks — Phase 1, Sprint 1

> Sprint Goal: Get the full local development stack running with auth working and tests passing.

| Task ID | Description | Status | Priority | Estimated | Notes |
|---------|-------------|--------|----------|-----------|-------|
| TASK-001 | Initialize backend project structure per Section 5.3 of MASTER.md | `done` | P0 | 2h | Folders, `__init__.py`, `pyproject.toml`, requirements scaffold |
| TASK-002 | Set up `app/config/` with pydantic-settings | `done` | P0 | 1h | Modular package: Application, Database, Redis, ChromaDB, Gemini, Security |
| TASK-003 | Create SQLAlchemy base + TimestampMixin | `todo` | P0 | 0.5h | `app/db/base.py` per reference snippet |
| TASK-004 | Create all Phase 1 SQLAlchemy models | `todo` | P0 | 3h | User, Project, ProjectMember, Dataset, Analysis, Visualization, Report, AgentLog, AuditLog, Notification |
| TASK-005 | Configure Alembic and run first migration | `todo` | P0 | 1h | `alembic init`, `env.py` async config, `alembic upgrade head` |
| TASK-006 | Set up docker-compose.yml | `todo` | P0 | 1h | postgres + redis + chromadb per Section 40 of MASTER.md |
| TASK-007 | Implement JWT handler (`app/security/jwt_handler.py`) | `todo` | P0 | 1h | create_access_token, create_refresh_token, decode_access_token |
| TASK-008 | Implement password handler (bcrypt 12 rounds) | `todo` | P0 | 0.5h | hash_password, verify_password |
| TASK-009 | Implement UserRepository (`app/db/repositories/user_repo.py`) | `todo` | P0 | 1h | get_by_id, get_by_email, create, update |
| TASK-010 | Implement AuthService (`app/services/auth_service.py`) | `todo` | P0 | 2h | register, login, refresh, logout with Redis token store |
| TASK-011 | Implement FastAPI dependencies (`app/dependencies.py`) | `todo` | P0 | 1h | get_db, get_current_user, require_admin |
| TASK-012 | Implement auth router (`app/api/v1/auth.py`) | `todo` | P0 | 2h | POST /register, /login, /refresh, /logout, GET /me |
| TASK-013 | Implement main FastAPI app (`app/main.py`) | `todo` | P0 | 1h | lifespan, CORS, middleware, router includes, /health |
| TASK-014 | Set up Celery app (`app/tasks/celery_app.py`) | `todo` | P0 | 1h | broker config, queue routing, task includes |
| TASK-015 | Set up Redis cache client (`app/cache/client.py`) | `todo` | P0 | 0.5h | async redis client wrapper |
| TASK-016 | Set up WebSocket manager (`app/api/websocket/manager.py`) | `todo` | P0 | 1.5h | connect, disconnect, broadcast_to_user |
| TASK-017 | Implement WebSocket endpoint (`/ws?token=<jwt>`) | `todo` | P0 | 1h | JWT validation on connect, ping/pong heartbeat |
| TASK-018 | Initialize Next.js 15 frontend per Section 5.2 | `todo` | P0 | 2h | App Router structure, TailwindCSS, ShadCN, Zustand |
| TASK-019 | Implement `lib/api-client.ts` with JWT interceptors | `todo` | P0 | 1h | Axios instance, request interceptor, 401 auto-refresh |
| TASK-020 | Implement `stores/auth-store.ts` | `todo` | P0 | 1h | login, logout, refreshToken, persist |
| TASK-021 | Build login page (`/login`) | `todo` | P0 | 2h | Form, validation, error handling, redirect |
| TASK-022 | Build register page (`/register`) | `todo` | P0 | 1.5h | Form, password strength, server errors |
| TASK-023 | Build dashboard shell layout (sidebar + topbar) | `todo` | P0 | 2h | Sidebar nav, TopBar with avatar, responsive |
| TASK-024 | Write auth unit tests | `todo` | P0 | 2h | register, login, refresh, invalid token, role check |
| TASK-025 | Run all Phase 1 acceptance criteria checks | `todo` | P0 | 1h | Verify every criterion in Section L2.1 |

---

## 📋 Sprint 2 Tasks — Phase 1 (Queued)

> Sprint Goal: File upload, parsing, profiling, and async Celery pipeline working.

| Task ID | Description | Status | Priority |
|---------|-------------|--------|----------|
| TASK-026 | Implement file upload endpoint with validation | `queued` | P0 |
| TASK-027 | Implement CSV/XLSX parser service | `queued` | P0 |
| TASK-028 | Implement data profiler (column types, null%, stats) | `queued` | P0 |
| TASK-029 | Implement `parse_uploaded_file` Celery task | `queued` | P0 |
| TASK-030 | Build FileDropzone React component | `queued` | P0 |
| TASK-031 | Build dataset profile page | `queued` | P0 |
| TASK-032 | Build project list + create project pages | `queued` | P1 |
| TASK-033 | Implement DataCleaningAgent (basic) | `queued` | P0 |
| TASK-034 | Write dataset upload integration tests | `queued` | P0 |

---

## ✅ Completed Tasks

> Tasks move here when status = "done" and tests pass.

| Task ID | Description | Completed | Session | Commit |
|---------|-------------|-----------|---------|--------|
| TASK-001 | Initialize backend project structure per Section 5.3 of MASTER.md | 2026-06-12 | GitHub Copilot | not committed yet |
| TASK-002 | Set up `app/config/` with pydantic-settings | 2026-06-12 | Cursor | not committed yet |

---

## 🐛 Open Bugs

| Bug ID | Description | Severity | Status | Phase | Reported |
|--------|-------------|----------|--------|-------|---------|
| — | No bugs reported yet | — | — | — | — |

---

## 🚧 Current Blockers

| # | Blocker | Impact | Owner | Resolution |
|---|---------|--------|-------|-----------|
| — | No blockers | — | — | — |

> **How to add a blocker:**
> When something prevents task completion, add it here immediately.
> Include: what is blocked, why, and what is needed to unblock it.

---

## ⚡ Next Immediate Actions

> Ordered checklist — do these in sequence in your next session.

```
[x] 1. Run: git init && create .gitignore (Python + Node)
[x] 2. Create root folder structure: ai-bios/ with frontend/ and backend/
[ ] 3. Copy .env.example → .env and fill in GEMINI_API_KEY
[ ] 4. Run: docker-compose up -d (postgres, redis, chromadb)
[ ] 5. Verify: docker ps shows all 3 containers healthy
[x] 6. TASK-001: Backend folder structure per Section 5.3 of MASTER.md — done
[x] 7. TASK-002: pydantic-settings config layer — done
[ ] 8. Begin TASK-003: Create SQLAlchemy base + TimestampMixin (`app/db/base.py`)
[ ] 9. Continue through Sprint 1 tasks in order
```

---

## 🔄 Resume Development Instructions

### For Human Developers

```
1. Open this file (AI_BIOS_PROJECT_STATUS.md)
2. Read "Project Overview" — note current phase and sprint
3. Read "Current Blockers" — clear any blockers first
4. Go to "Current Sprint Tasks" — find first row with status "todo" or "in-progress"
5. Open AI_BIOS_MASTER.md — find the section for your current phase
6. Read the relevant architecture section before implementing
7. Implement the task
8. Run: pytest tests/ -x
9. Mark task "done" in this file
10. Write a session log entry below
11. Commit: git commit -m "feat(scope): description"
```

### For AI Coding Agents

```
MANDATORY STARTUP SEQUENCE (never skip):
  Step 1: Read AI_BIOS_MASTER.md (full architecture)
  Step 2: Read AI_BIOS_MASTER_LEARNING_EDITION.md (learning context + solo dev strategy)
  Step 3: Read this file (AI_BIOS_PROJECT_STATUS.md) — current operational state

IDENTIFY your task:
  → Current Sprint Tasks table → first row with status "todo" or "in-progress"

IMPLEMENT:
  → One task at a time
  → Reference AI_BIOS_MASTER.md for architecture decisions
  → Use reference snippets in Section A4 of both master files
  → Follow folder structure in Section 5 of MASTER.md exactly

VERIFY:
  → pytest tests/ -x (backend)
  → npm run test (frontend, if applicable)
  → All acceptance criteria for the task must pass

UPDATE this file:
  → Set task status = "done"
  → Move task to Completed Tasks
  → Add session log entry
  → Update Overall Completion %

REPORT:
  → What was completed
  → What files were created or modified
  → What tests were written and passed
  → What the next task is
  → Any issues or blockers found
```

---

## 🤖 AI Coding Agent Instructions

### Cursor

```
Primary Role: All code implementation
Context: Always attach AI_BIOS_MASTER.md as @MASTER context
Workflow:
  1. Open AI_BIOS_MASTER.md in Cursor context
  2. Open AI_BIOS_PROJECT_STATUS.md for current task
  3. Implement task referencing MASTER.md for specs
  4. Run tests inline
  5. Update PROJECT_STATUS.md
Do NOT: Make architecture decisions without MASTER.md reference
Do NOT: Skip folder structure conventions in Section 5
```

### Claude Code / Claude

```
Primary Role: Architecture decisions, complex debugging, document updates
When to use:
  → Architecture question not answered by MASTER.md
  → Complex LangGraph routing issue
  → Debugging multi-agent state propagation
  → Updating MASTER.md or this file
  → Writing agent system prompts
Always: Reference specific section numbers from MASTER.md in your questions
Do NOT: Use for routine code generation (use Cursor instead)
```

### ChatGPT

```
Primary Role: Quick lookups, syntax questions, alternative approaches
When to use:
  → Specific Python/TypeScript error you can't resolve
  → Library-specific usage question
  → Alternative implementation approach
  → When Claude free tier is hit
Do NOT: Ask for architecture decisions (it doesn't know MASTER.md)
Do NOT: Ask for LangGraph-specific design advice (Claude is better)
```

### Gemini

```
Primary Role: The LLM powering the AI-BIOS application itself
Also useful:
  → Testing prompts before wiring into agents
  → Verifying model output format before writing Pydantic schemas
  → Understanding Gemini API capabilities and rate limits
Do NOT: Use for development workflow or architecture decisions
```

### GitHub Copilot / VS Code Copilot

```
Primary Role: Line-level autocomplete, minor edits
When to use:
  → Completing boilerplate in known patterns
  → Quick import suggestions
  → Minor edits to existing files
Do NOT: Use for large feature implementation (use Cursor instead)
```

### OpenHands / Roo Code / Cline

```
Primary Role: Autonomous multi-file implementation sessions
When to use:
  → Implementing a complete phase from the task breakdown
  → Large refactoring with multiple file changes
Mandatory startup:
  → Read all three project files before starting
  → Follow task order exactly
  → Never implement future phase features
  → Update PROJECT_STATUS.md after each completed task
```

---

## 📝 Development Session Log

> Append a new entry after EVERY development session. Never delete old entries.

### Session Template

```markdown
---
### Session: YYYY-MM-DD | Tool: [Cursor/Claude/ChatGPT/OpenHands]
**Duration:** X hours
**Tasks Completed:**
  - TASK-XXX: Description — ✅ done
  - TASK-XXX: Description — ✅ done

**Files Created:**
  - backend/app/path/to/file.py
  - frontend/src/path/to/file.tsx

**Files Modified:**
  - backend/app/path/to/existing.py (what changed)

**Tests Written:**
  - tests/unit/test_auth.py — X test cases, all passing
  - Coverage: X%

**Issues Found:**
  - Issue description (or "None")

**Architecture Notes:**
  - Any deviation from MASTER.md (or "None")
  - Any spec gap discovered

**Next Action:**
  - TASK-XXX: Exact description of what to do next

**Commit:** git commit hash or "not committed yet"
---
```

### Sessions

---
### Session: 2026-06-12 | Tool: Cursor
**Duration:** ~1 hour
**Tasks Completed:**
  - TASK-002: Configuration System (pydantic-settings) — ✅ done

**Context Loading Report:**
```
CONTEXT LOADING REPORT — 2026-06-12
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Current Phase:      Phase 1 — Backend Foundations
Current Sprint:     Sprint 1 — Infrastructure & Auth
Current Task:       TASK-002 — Configuration System

Folder Structure:   ✅ Matches Section 5.3 (scaffold complete)
Models:             🔲 Not yet built
APIs:               🔲 Not yet built
LangGraph:          🔲 Not yet built
Agents:             🔲 Not yet built
Dependencies:       ⚠️ Minimal scaffold only (fastapi, uvicorn); pydantic-settings required for config
Git Branch:         unknown | Last commit: unknown

Architecture Drift Found: config/ package vs MASTER.md app/config.py single file (documented in drift tracker)
Pre-Coding Action:        Proceed with user-specified modular package layout
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Files Created:**
  - backend/app/config/__init__.py
  - backend/app/config/settings.py

**Files Modified:**
  - AI_BIOS_PROJECT_STATUS.md (TASK-002 done, session log, next action)

**Tests Written:**
  - None (config import verified manually)

**Issues Found:**
  - requirements.txt lacks pydantic-settings (install manually until TASK-001 deps finalized)

**Architecture Notes:**
  - Implemented as `app/config/` package instead of single `app/config.py` per task spec; `from app.config import settings` preserved for A4.2 compatibility

**Next Action:**
  - TASK-003: Create SQLAlchemy base + TimestampMixin (`app/db/base.py`)

**Commit:** not committed yet
---

---
### Session: 2026-06-12 | Tool: Cursor
**Duration:** ~15 minutes
**Tasks Completed:**
  - PROJECT_STATUS consistency update — TASK-001 retroactively marked done

**Files Created:**
  - None

**Files Modified:**
  - AI_BIOS_PROJECT_STATUS.md (TASK-001 status, Completed Tasks, Next Immediate Actions, completion %)

**Tests Written:**
  - None

**Issues Found:**
  - TASK-001 was completed during scaffolding (2026-06-12) but left as `todo` in sprint table

**Architecture Notes:**
  - None (documentation-only correction)

**Next Action:**
  - TASK-003: Create SQLAlchemy base + TimestampMixin (`app/db/base.py`)

**Commit:** not committed yet
---

---

## 🏆 Milestone Tracker

| Milestone | Description | Target | Status | Completed |
|-----------|-------------|--------|--------|-----------|
| **M1** | Local development environment fully running | End of Week 1 | 🔴 Pending | — |
| **M2** | Auth endpoints working + tested | End of Week 1 | 🔴 Pending | — |
| **M3** | File upload → profile pipeline working | End of Week 3 | ⬜ Locked | — |
| **M4** | First LangGraph graph running in Studio | End of Week 6 | ⬜ Locked | — |
| **M5** | Chat with data working (RAG pipeline) | End of Week 7 | ⬜ Locked | — |
| **M6** | Forecast + PDF report generation working | End of Week 9 | ⬜ Locked | — |
| **M7** | All 10 agents in LangGraph Studio workflow | End of Week 13 | ⬜ Locked | — |
| **M8** | COA approval dialog + local agent working | End of Week 16 | ⬜ Locked | — |
| **M9** | Power BI dataset push working | End of Week 18 | ⬜ Locked | — |
| **M10** | Full system deployed to Vercel + Render | After M7 | ⬜ Locked | — |

---

## 🏗️ Architecture Drift Tracker

> Record ANY deviation from the architecture defined in AI_BIOS_MASTER.md.
> A deviation is not automatically bad — but it must be documented and the MASTER must be updated.

| Drift ID | Date | Section Affected | Original Spec | Actual Implementation | Reason | MASTER Updated? |
|----------|------|-----------------|---------------|----------------------|--------|-----------------|
| DRIFT-001 | 2026-06-12 | Section 5.3 | `app/config.py` single file | `app/config/` package with `settings.py` | Modular config per TASK-002 spec; import path unchanged | No |

### How to Use This Tracker

```
When you implement something differently than specified in MASTER.md:
  1. Add a row to this table immediately
  2. Update AI_BIOS_MASTER.md to reflect the new decision
  3. Mark "MASTER Updated?" = Yes
  4. Add a note in your session log

Examples of architecture drift to track:
  → Using a different library than specified (e.g., motor instead of asyncpg)
  → Adding a database table not in the ER diagram
  → Changing an API endpoint path or method
  → Using a different ChromaDB collection naming scheme
  → Changing the LangGraph state schema
```

---

## 💳 Technical Debt Tracker

> Record shortcuts, known issues, and things that need to be fixed in a future sprint.
> Technical debt is acceptable during learning — but must be tracked.

| Debt ID | Date | Description | Impact | Phase Introduced | Fix In Phase | Priority |
|---------|------|-------------|--------|-----------------|-------------|---------|
| — | — | — | — | — | — | — |

### Common Technical Debt to Watch For

```
→ Skipping input validation on non-critical fields
→ Using synchronous code where async should be used
→ Hardcoded values that should be configuration
→ Missing error handling on agent tool calls
→ Test coverage below 80% on a service
→ Using print() instead of logging
→ Missing database index on a frequently queried column
→ Not handling Gemini API rate limits properly
→ Missing WebSocket reconnection logic
→ Inadequate COA token expiry handling
```

---

## 📦 Dependency Versions (Locked)

> Record exact versions used. Update when you intentionally upgrade.

### Backend
| Package | Version | Locked On | Notes |
|---------|---------|-----------|-------|
| fastapi | 0.115.0 | — | — |
| uvicorn | 0.32.0 | — | — |
| sqlalchemy | 2.0.36 | — | Async mode |
| asyncpg | 0.30.0 | — | PostgreSQL driver |
| alembic | 1.14.0 | — | — |
| redis | 5.2.0 | — | — |
| celery | 5.4.0 | — | Redis broker |
| google-generativeai | 0.8.3 | — | Gemini API |
| langgraph | 0.2.55 | — | — |
| chromadb | 0.5.20 | — | — |
| pandas | 2.2.3 | — | — |
| prophet | 1.1.6 | — | — |
| xgboost | 2.1.3 | — | — |
| reportlab | 4.2.5 | — | PDF generation |
| python-pptx | 1.0.2 | — | PPTX generation |
| pydantic | 2.9.2 | — | v2 |
| pydantic-settings | 2.6.1 | — | — |
| passlib | 1.7.4 | — | bcrypt |
| python-jose | 3.3.0 | — | JWT |

### Frontend
| Package | Version | Locked On | Notes |
|---------|---------|-----------|-------|
| next | 15.0.3 | — | App Router |
| react | 19.0.0 | — | — |
| typescript | 5.6.3 | — | — |
| tailwindcss | 3.4.15 | — | — |
| framer-motion | 11.11.17 | — | — |
| recharts | 2.13.3 | — | — |
| zustand | 5.0.1 | — | — |
| axios | 1.7.9 | — | — |

---

## 🔐 Environment Setup Checklist

> Complete before first development session.

```
[ ] Python 3.12 installed (verify: python --version)
[ ] Node.js 20 installed (verify: node --version)
[ ] Docker Desktop installed and running
[ ] Git configured (name + email)
[ ] Cursor installed (primary IDE)
[ ] LangGraph Studio installed (for Phase 3+)

[ ] Repository initialized: git init
[ ] .env created from .env.example
[ ] GEMINI_API_KEY added to .env
[ ] JWT_SECRET_KEY generated (python -c "import secrets; print(secrets.token_hex(32))")
[ ] ENCRYPTION_KEY generated (python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")
[ ] COA_LOCAL_AGENT_WS_SECRET generated

[ ] docker-compose up -d (start postgres, redis, chromadb)
[ ] docker ps (verify all 3 containers running and healthy)
[ ] pip install -r requirements-dev.txt (in backend/)
[ ] npm install (in frontend/)
[ ] alembic upgrade head (run migrations after models created)
[ ] pytest tests/ (verify test suite works)
```

---

## 📈 Phase Completion Criteria Reference

> Quick reference — full criteria in AI_BIOS_MASTER_LEARNING_EDITION.md Section L2

### Phase 1 — Backend Foundations ✅ Criteria
```
[ ] docker-compose up starts all services without errors
[ ] POST /auth/register creates user with bcrypt hashed password
[ ] POST /auth/login returns access_token + refresh_token pair
[ ] POST /auth/refresh issues new access token from refresh token
[ ] POST /auth/logout invalidates refresh token in Redis
[ ] Protected endpoints return 401 without valid token
[ ] Admin endpoints return 403 for non-admin users
[ ] Celery worker processes test task successfully
[ ] WebSocket sends test event to connected authenticated client
[ ] All database tables created via alembic upgrade head
[ ] Login + Register pages functional in browser
[ ] Dashboard shell layout renders with sidebar navigation
[ ] Backend unit tests: pytest passes with >80% coverage
```

### Phase 2 — Dataset Intelligence ✅ Criteria
```
[ ] CSV upload completes in < 30s for files < 50MB
[ ] Files > 500MB rejected with 413 error
[ ] XLSX multi-sheet detection returns sheet list
[ ] Column type detection: numeric / categorical / date / text / boolean
[ ] Profile generated: row count, column count, null%, unique, stats per column
[ ] Quality score 0-100 calculated and displayed
[ ] DataCleaningAgent handles nulls with correct strategy per type
[ ] WebSocket emits dataset.ready event on profile completion
[ ] FileDropzone drag-and-drop upload works with progress bar
[ ] Dataset profile page displays all column cards
```

### Phase 3 — RAG & Chat ✅ Criteria
```
[ ] Embeddings generated and stored in ChromaDB on upload
[ ] Chat session created and history persisted to DB
[ ] Intent classified correctly for: statistical Q, SQL, chart, general
[ ] ChromaDB retrieval returns relevant chunks in < 2s
[ ] Chat response streams token-by-token to frontend
[ ] Sources cited in every response
[ ] Context maintained across 15+ turns
[ ] Context summarized when turn_count > 15
[ ] LangGraph Studio shows chat workflow graph visually
```

### Phase 4 — Forecasting & Reports ✅ Criteria
```
[ ] Prophet forecasts correctly on daily/weekly/monthly data
[ ] XGBoost feature engineering creates all lag/rolling/date features
[ ] Model selector applies correct logic for each data pattern
[ ] MAPE, MAE, RMSE calculated on 20% holdout
[ ] Forecast chart shows actual + predicted + 95% CI band
[ ] PDF generates with all sections and embedded charts at 300 DPI
[ ] PPTX generates with all slide types and embedded chart images
[ ] Both files download successfully from frontend
```

### Phase 5 — Multi-Agent System ✅ Criteria
```
[ ] Full LangGraph workflow runs end-to-end without error
[ ] All 10 agents execute in correct sequence
[ ] LangGraph Studio shows full workflow graph visually
[ ] State accumulates correctly through all nodes
[ ] Retry fires on simulated Gemini 429 error
[ ] Partial agent failure does not abort remaining agents
[ ] SQL agent generates correct SQL for 90%+ of test questions
[ ] SQL agent NEVER executes DELETE/DROP/UPDATE (test verified)
[ ] RFM analysis produces segment assignments with AI descriptions
[ ] All 10 agents pass happy-path AND failure-path tests
```

### Phase 6 — Computer Operator Agent ✅ Criteria
```
[ ] NO desktop action executes without approval token (unit test verified)
[ ] Approval dialog appears for every COA action request
[ ] Dialog shows: agent name, action, reason, expected outcome, risk level
[ ] Allow Once: executes once, no scope saved
[ ] Allow Session: scope persists in Redis until session ends
[ ] Always Allow: scope persisted to PostgreSQL
[ ] Deny: action not executed, denial logged to audit trail
[ ] Auto-deny fires at exactly 300 seconds (integration test verified)
[ ] HMAC validation rejects tampered action payloads (test verified)
[ ] Rollback available within 5 minutes of execution
[ ] All COA actions appear in audit log
```

### Phase 7 — Power BI ✅ Criteria
```
[ ] OAuth device code flow: user authenticates in browser, token stored
[ ] Dataset pushed to Power BI workspace successfully
[ ] Power BI report URL returned and displayed to user
[ ] Tokens encrypted before storage in database
[ ] Expired tokens refreshed automatically
```

---

> ═══════════════════════════════════════════════════════════════════════════
>
> **AI_BIOS_PROJECT_STATUS.md — v1.0.0**
>
> This is the OPERATIONAL MEMORY of the AI-BIOS project.
> Read it before every session. Update it after every task. Commit it with every push.
>
> Files to read in order:
>   1. AI_BIOS_MASTER.md               → Architecture
>   2. AI_BIOS_MASTER_LEARNING_EDITION.md → Learning strategy
>   3. AI_BIOS_PROJECT_STATUS.md (this) → Current state
>
> Current Phase: Phase 1 — Backend Foundations
> Next Action:   TASK-003 — Create SQLAlchemy base + TimestampMixin
>
> ═══════════════════════════════════════════════════════════════════════════


---

## ⚙️ Project Execution Rules (Quick Reference)

> Full rules in AI_BIOS_MASTER.md Section A3. This is the quick-reference version.

| Rule | What It Means |
|------|--------------|
| **Never skip phases** | Phase 1 → 2 → 3 → 4 → 5 → 6 → 7 in strict order |
| **Never implement future phases early** | No Phase 5 code while in Phase 2 |
| **Always update this file** | After every completed task — no exceptions |
| **Always complete acceptance criteria** | Write tests → tests pass → criterion checked |
| **Always run tests before moving on** | `pytest tests/ -x` after every task |
| **Architecture changes update MASTER.md** | Never silently deviate |
| **One task at a time** | Complete + test + commit before starting next |

### Quick Test Commands
```bash
# Backend unit tests (run after every task)
cd backend && pytest tests/ -x --tb=short

# Full backend test suite with coverage (run after every phase)
cd backend && pytest tests/ -v --cov=app --cov-report=term

# Frontend tests
cd frontend && npm run test

# Type checks
cd backend && mypy app/
cd frontend && npx tsc --noEmit

# Lint
cd backend && ruff check .
cd frontend && npm run lint
```

### Quick Service Commands
```bash
# Start all local services
docker-compose up -d

# Check service health
curl http://localhost:8000/health

# Start LangGraph Studio (Phase 3+)
cd backend && langgraph dev

# Celery worker
cd backend && celery -A app.tasks.celery_app worker --loglevel=info

# Celery Flower (task monitor)
cd backend && celery -A app.tasks.celery_app flower --port=5555
# Open: http://localhost:5555
```



---

## 🖥️ Active Development Environment

> Update this block at the START of every development session before writing any code.

| Field | Current Value |
|-------|--------------|
| **Current IDE** | Cursor |
| **Current Model** | Composer |
| **Current Module** | `backend/app/config/settings.py` |
| **Current Phase** | Phase 1 — Backend Foundations |
| **Current Sprint** | Sprint 1 — Infrastructure & Auth |
| **Current Task** | TASK-003 — Create SQLAlchemy base + TimestampMixin |
| **Next Recommended Tool** | Cursor |
| **Reason** | All Phase 1 Sprint 1 tasks are pure implementation |

**How to update:** At the start of each session, paste this table and fill in the current values. When switching tools mid-session (e.g., Cursor → Claude for an architecture review), update the Current IDE and Next Recommended Tool fields and add a note to your session log entry.

---

## 🔍 Project Context Loading Protocol

> Every AI tool MUST complete this inspection before generating or modifying any code.
> Failure to inspect leads to conflicting implementations and wasted effort.

### Pre-Implementation Inspection Checklist

```
□ 1. FOLDER STRUCTURE
      List all files from project root
      Compare to Section A5 of AI_BIOS_MASTER_LEARNING_EDITION.md

□ 2. EXISTING SOURCE CODE
      backend/app/ — what modules, services, agents exist?
      frontend/    — what pages, components, stores, hooks exist?
      Do NOT regenerate code that already exists.

□ 3. EXISTING APIs
      backend/app/api/v1/*.py — which endpoints are implemented?
      Compare to Section 7 of AI_BIOS_MASTER.md

□ 4. EXISTING DATABASE MODELS
      backend/app/models/*.py — which models are defined?
      backend/alembic/versions/ — which migrations have run?
      Compare to Section 6 (ER diagram) of AI_BIOS_MASTER.md

□ 5. EXISTING LANGGRAPH WORKFLOWS
      backend/app/workflows/*.py — which graphs are built?
      Compare to Section 10 / Section 30 of AI_BIOS_MASTER.md

□ 6. EXISTING AGENTS
      backend/app/agents/*.py — which of the 11 agents are implemented?
      Compare to Section 9 / Section 51 of AI_BIOS_MASTER.md

□ 7. EXISTING PROMPTS
      Scan agent files for system prompt strings
      Compare to Section 31 of AI_BIOS_MASTER.md

□ 8. CURRENT DEPENDENCIES
      backend/requirements.txt — are all required packages present?
      frontend/package.json — are all required packages present?
      Compare to Section 41 of AI_BIOS_MASTER.md

□ 9. CURRENT PROJECT STATUS
      Re-read this file (AI_BIOS_PROJECT_STATUS.md) fully
      Note: Current Phase, Sprint, open tasks, blockers, last session next action

□ 10. CURRENT GIT STATE
       git branch --show-current
       git log --oneline -5
       Confirm: correct branch, understand recent changes
```

### Architecture Comparison Step

After inspection, compare planned vs actual:

| Area | Planned (MASTER.md) | Actual (Codebase) | Drift? |
|------|--------------------|--------------------|--------|
| Folder structure | Section A5 | `ls -R` output | — |
| DB models | Section 6 ER diagram | `backend/app/models/` | — |
| API endpoints | Section 7 | `backend/app/api/v1/` | — |
| LangGraph state | Section 30 | `backend/app/workflows/` | — |
| Agent tools | Section 28 | `backend/app/agents/` | — |
| Dependencies | Section 41 | `requirements.txt` | — |

**If drift found:**
1. Add row to Architecture Drift Tracker (below)
2. Decide: fix implementation OR update MASTER.md
3. Record decision in session log
4. Only then proceed with the new task

### Context Loading Report Template

Paste this report at the top of your session log entry:

```
CONTEXT LOADING REPORT — [DATE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Current Phase:      Phase X — [Name]
Current Sprint:     Sprint Y — [Goal]
Current Task:       TASK-XXX — [Description]

Folder Structure:   ✅ Matches / ⚠️ [drift detail]
Models:             ✅ Matches / ⚠️ [drift detail] / 🔲 Not yet built
APIs:               ✅ Matches / ⚠️ [drift detail] / 🔲 Not yet built
LangGraph:          ✅ Matches / ⚠️ [drift detail] / 🔲 Not yet built
Agents:             ✅ Matches / ⚠️ [drift detail] / 🔲 Not yet built
Dependencies:       ✅ All present / ⚠️ Missing: [list]
Git Branch:         [branch name] | Last commit: [message]

Architecture Drift Found: None / [description]
Pre-Coding Action:        None / [Update MASTER.md / Fix implementation]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🤖 AI Development Startup Checklist

> Complete every step before writing code. This takes 10–15 minutes and prevents hours of rework.

```
MANDATORY STARTUP SEQUENCE:

  □ 1. Read AI_BIOS_MASTER.md
        → Focus on section for current phase
        → Refresh architecture, API specs, agent definitions for today's task

  □ 2. Read AI_BIOS_MASTER_LEARNING_EDITION.md
        → Confirm which learning phase
        → Confirm which tool to use today (Section A8 IDE Responsibility Matrix)
        → Confirm deployment mode (local/portfolio/hybrid)

  □ 3. Read AI_BIOS_PROJECT_STATUS.md (this file)
        → Current Phase, Sprint, Milestone
        → Open bugs and blockers
        → Last session's "Next Action"
        → Update Active Development Environment table above

  □ 4. Inspect project folder structure
        → List all files from root
        → Compare to spec in LEARNING_EDITION.md Section A5

  □ 5. Inspect current codebase
        → backend/app/ and frontend/ — what exists?
        → Do not regenerate existing code

  □ 6. Inspect current dependencies
        → requirements.txt and package.json
        → All required packages from AI_BIOS_MASTER.md Section 41 present?

  □ 7. Inspect current LangGraph workflows (Phase 3+)
        → backend/app/workflows/*.py
        → Current graph topology matches spec?

  □ 8. Determine active phase
        → "Current Phase" in Project Overview table above

  □ 9. Determine active sprint
        → "Current Sprint" in Project Overview table above

  □ 10. Determine active task
         → Current Sprint Tasks → first "todo" or "in-progress" row

ONLY AFTER ALL 10 STEPS: begin implementation.
```

