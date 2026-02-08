---
id: 2
title: Update Project Constitution
stage: constitution
date_iso: 2026-01-24
surface: agent
model: Qwen Code
feature: todo-app
branch: main
user: Sabahat Ahmed
command: /sp.constitution
labels:
  - constitution
  - todo-app
  - architecture
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - .specify/memory/constitution.md
tests_yaml: []
prompt_text: |
  $ARGUMENTS

  You **MUST** consider the user input before proceeding (if not empty).

  ## Outline

  You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

  Follow this execution flow:

  1. Load the existing constitution template at `.specify/memory/constitution.md`.
     - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
     **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

  2. Collect/derive values for placeholders:
     - If user input (conversation) supplies a value, use it.
     - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
     - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
     - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
       - MAJOR: Backward incompatible governance/principle removals or redefinitions.
       - MINOR: New principle/section added or materially expanded guidance.
       - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
     - If version bump type ambiguous, propose reasoning before finalizing.

  3. Draft the updated constitution content:
     - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
     - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
     - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
     - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

  4. Consistency propagation checklist (convert prior checklist into active validations):
     - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
     - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
     - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
     - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
     - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

  5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
     - Version change: old → new
     - List of modified principles (old title → new title if renamed)
     - Added sections
     - Removed sections
     - Templates requiring updates (✅ updated / ⚠ pending) with file paths
     - Follow-up TODOs if any placeholders intentionally deferred.

  6. Validation before final output:
     - No remaining unexplained bracket tokens.
     - Version line matches report.
     - Dates ISO format YYYY-MM-DD.
     - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

  7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

  8. Output a final summary to the user with:
     - New version and bump rationale.
     - Any files flagged for manual follow-up.
     - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

  Formatting & Style Requirements:

  - Use Markdown headings exactly as in the template (do not demote/promote levels).
  - Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
  - Keep a single blank line between sections.
  - Avoid trailing whitespace.

  If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

  If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

  Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

  ---

  As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

  1) Determine Stage
     - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

  2) Generate Title and Determine Routing:
     - Generate Title: 3–7 words (slug for filename)
     - Route is automatically determined by stage:
       - `constitution` → `history/prompts/constitution/`
       - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
       - `general` → `history/prompts/general/`

  3) Create and Fill PHR (Shell first; fallback agent‑native)
     - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
     - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
     - If the script fails:
       - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
       - Allocate an ID; compute the output path based on stage from step 2; write the file
       - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

  4) Validate + report
     - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
     - On failure: warn, don't block. Skip only for `/sp.phr`.


  /sp.constitution @constitution.md
  Create this file and write the following content into it exactly as-is:

  You are an autonomous senior software engineer and product architect.

  You must NOT ask the user any clarification questions.
  You must make reasonable, standard, industry-accepted decisions yourself.

  PROJECT NAME:
  The Evolution of Todo – Phase I

  OBJECTIVE:
  Build a fully working command-line Todo application using Python.
  The application must store all data in memory and must run locally.

  DEVELOPMENT MODE:
  - Spec-driven development
  - Autonomous execution
  - No user interaction for design decisions
  - No boilerplate explanations

  TECH STACK (FIXED):
  - Python 3.13+
  - CLI based interface
  - In-memory data storage only
  - Standard Python libraries only
  - No database
  - No file persistence
  - No frameworks

  MANDATORY FEATURES (CORE MVP):
  You must implement ALL of the following:

  1. Add Task
     - Auto-generate a unique integer ID
     - Title is required
     - Description is optional
     - Default status is incomplete

  2. View Tasks
     - Display all tasks in a readable list
     - Show ID, title, description, and status

  3. Update Task
     - Update title and/or description by task ID
     - If task ID does not exist, handle gracefully

  4. Delete Task
     - Delete task by ID
     - No crash on invalid ID

  5. Mark Task Complete / Incomplete
     - Toggle completion status by ID

  ARCHITECTURE (MANDATORY):
  - Use clean separation of concerns
  - Layers:
    - Model: Task data structure
    - Service: Business logic
    - CLI: User input/output only
  - Business logic must NOT be inside CLI code
  - No global variables

  PROJECT STRUCTURE (FIXED):
  /src
    /models
    /services
    /cli
    main.py

  CODE RULES:
  - Clean, readable, maintainable code
  - Small focused functions
  - Clear naming
  - Explicit error handling
  - No over-engineering

  DELIVERABLES:
  - Fully functional CLI application
  - Ready-to-run Python project
  - Extensible for future phases

  AI EXECUTION RULES:
  - Do not ask questions
  - Do not request confirmation
  - Do not explain decisions
  - Implement exactly as defined
  - Follow this constitution strictly
response_text: |
  Updated the project constitution file with the specified content for "The Evolution of Todo – Phase I". The constitution now contains the project requirements, tech stack, mandatory features, architecture requirements, code rules, and deliverables as specified. The file has been saved to .specify/memory/constitution.md.
outcome: |
  Successfully updated the project constitution with all required specifications for the todo application.
evaluation: |
  The constitution file has been correctly updated with all the specified requirements and follows the exact format requested.
---

# Update Project Constitution

## Summary
Updated the project constitution file with the specified content for "The Evolution of Todo – Phase I". The constitution now contains the project requirements, tech stack, mandatory features, architecture requirements, code rules, and deliverables as specified. The file has been saved to .specify/memory/constitution.md.

## Outcome
Successfully updated the project constitution with all required specifications for the todo application.

## Evaluation
The constitution file has been correctly updated with all the specified requirements and follows the exact format requested.