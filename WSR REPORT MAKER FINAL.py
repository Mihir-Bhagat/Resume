GADM Agent Creation Contest - Complete Summary
Header & Key Dates
Milestone	Date
Registration	Aug 24–28
Kickoff	Aug 31, 8AM IST
Submission Deadline	Sept 18, 8AM IST
Results	Sept 28
Section 1 - Purpose and Overview
Brainstorming and build activity for GADM-supported accounts

Build practical, low-cost agents using existing account tooling

Tools allowed: AI coding companions, Azure OpenAI, VS Code

Every submission must:
Map to an ITIL Service Operation pillar
Solve a real account problem
Produce measurable value
Include documentation for another practitioner to run it

Section 2 - Practitioner Quick Start (6 Steps)
Step	Action
1	Pick the pain point (triage, alerts, runbook, access, change risk)
2	Prove it matters using ticket volume, SLA impact, handle time
3	Define agent job in one sentence
4	Build minimum agent locally in VS Code
5	Measure returns - hours saved, efficiency gain
6	Submit branch with all required files
Section 3 - Full Timeline
Milestone	Date	Action
Announcement	Week of Aug 24	Form teams, identify problems
Registration	Aug 24–28	Register team, account, problem statement
Kickoff	Aug 31, 8AM IST	Build window opens
Build & Test	Aug 31–Sept 17	Design, build, test, refine, rehearse
Submission	Sept 18, 8AM IST	Push final branch to Azure DevOps
Demo Shortlisting	Sept 21–24	Live demos to judges
Results	Sept 28	Winners announced
Section 4 - Build Guidance
Required Stack
Microsoft Agent Framework

LangGraph

Google ADK

Agent Core

Azure OpenAI only (no other LLM)

SQLite

VS Code local development

Rules
Azure OpenAI is the only approved LLM runtime

SQLite for local state, memory, logs

AI coding tools only through account/project code

No secrets, production credentials, or sensitive data in commits

Repository Structure
team-name-agent/
  README.md
  agent_card.md
  value_case.md
  architecture.md
  requirements.txt
  .env.example
  src/main.py
  src/agent.py
  src/tools.py
  src/prompts.py
  src/guardrails.py
  src/telemetry.py
  src/storage.py
  data/sample_input.json
  data/sample_output.json
  tests/test_agent.py
  docs/demo_script.md
  logs/sample_run_log.json
Run Commands
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python src/main.py --input data/sample_input.json
Section 5 - Returns & Value Calculation
Metric	Definition	Example
Monthly Volume	Transactions agent can be applied to	1,200 incidents/month
Baseline Effort	Current human effort per transaction	12 minutes
Agent-Assisted Effort	Human effort after agent help	7 minutes
Effort Saved	Baseline minus assisted	5 minutes
Adoption Factor	Realistic usable volume %	60%
Hours Saved/Month	Volume x saved mins x adoption / 60	60 hours
Efficiency Gain	Saved mins / baseline mins	41.7%
Formula
Hours Saved = Monthly Volume x Adoption Factor x Effort Saved / 60
Efficiency Gain % = Effort Saved / Baseline Effort x 100
Annualized Hours = Hours Saved per Month x 12
Example: 1,200 x 60% x 5 mins / 60 = 60 hours saved/month

Section 6 - Guardrails & Observability
Minimum Guardrails
No secrets in code or prompts

Masked or sanitized sample data

Read-only or recommendation-only behavior

Input and output validation

Human review for low confidence

Error logging without sensitive data

Minimum Logs Required
Run ID and timestamp

Input type and action performed

Model deployment used

Latency and status

Token estimate or actual count

Human review flag and error category

Section 7 - Submission Checklist
✅ README with setup and run instructions

✅ Agent card with purpose, architecture, data sources, guardrails, limitations

✅ Value case with hours saved and efficiency gain

✅ Source code and .env.example with no secrets

✅ Sample input and sample output

✅ Demo script and architecture notes

✅ Token/cost summary if using fallback subscription

✅ Basic logs, telemetry, or screenshots showing execution

Section 8 - Judging Criteria
Criterion	Weight	What Judges Look For
Business Value	30%	Problem linkage, credible ROI, hours saved
Technical Implementation	25%	Sound architecture, working demo
Guardrails	20%	Validation, human-in-loop, token discipline
Observability	15%	Logs, telemetry, latency, token usage
Token Optimization	10%	Efficient prompts, context management
Section 9 - SDK Integration Readiness
Shortlisted agents may be evaluated for ADM AI Shift Platform SDK integration.

Requirements
✅ Defined input schema

✅ Defined output schema

✅ Agent logic separated from CLI/demo wrapper

✅ Tool calls modular and documented

✅ Prompts separated from orchestration

✅ Guardrails as reusable functions

✅ Structured logs and externalized secrets

✅ Can run with sample data without target-system dependency

Agent Flow
Input → Validate → Retrieve/Enrich → Reason/Generate → 
Validate Output → Human Review Flag → Log → Return Response
Section 10 - Prompt Pack for AI Coding Companions
Repository Scaffold Prompt
Create a Python agent project scaffold for an ITIL service 
operations agent. Run locally in VS Code, use Azure OpenAI 
for LLM calls, SQLite for local persistence. Include README, 
agent_card.md, value_case.md, src files, tests, sample data, 
and .env.example. Keep code minimal and readable.
First Agent Function Prompt
Implement an agent that accepts a JSON incident record with 
title, description, category, priority, error text, and notes. 
Validate required fields, call Azure OpenAI, return structured 
JSON with summary, likely category, recommended action, 
confidence, human_review_required, and rationale.
Section 11 - FAQ
Question	Answer
Must I use AI coding assistant?	No, it is optional
Can I use a different LLM?	No, Azure OpenAI only
Is multi-agent required?	No, use one agent if it fits
Can agent write to production?	No, read-only or recommendation only
Footer - Key Contacts
Role	Contact
Sponsorship	Global Head of ADM
Logistics	Account GADM Point of Contact
Team Formation	Local GADM Lead
