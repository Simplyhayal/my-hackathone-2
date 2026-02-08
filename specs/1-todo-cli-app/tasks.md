# Tasks: Phase I – In-Memory Python CLI Todo Application

## Feature Overview

This feature implements the foundational MVP of "The Evolution of Todo" system - a command-line based Todo application that demonstrates clean architecture, modular design, and extensibility for future cloud-native and AI-driven phases. The application will run locally with in-memory storage and provide core task management capabilities.

## Dependencies

- User Story 2 (View Tasks) depends on User Story 1 (Add Task) for task creation
- User Story 3 (Update Task) depends on User Story 1 (Add Task) for existing tasks
- User Story 4 (Delete Task) depends on User Story 1 (Add Task) for existing tasks
- User Story 5 (Mark Complete/Incomplete) depends on User Story 1 (Add Task) for existing tasks

## Parallel Execution Examples

- User Story 3 (Update Task) and User Story 4 (Delete Task) can be worked on in parallel after User Story 1 is complete
- User Story 5 (Mark Complete/Incomplete) can be developed in parallel with User Story 3 and 4 after User Story 1 is complete

## Implementation Strategy

- MVP scope: Complete User Story 1 (Add Task) with minimal supporting infrastructure
- Incremental delivery: Each user story builds on the previous one
- Focus on clean architecture separation between models, services, and CLI

## Phase 1: Setup

- [X] T001 Create project structure with src/models, src/services, src/cli directories
- [X] T002 Set up Python project with proper module imports
- [X] T003 Create initial README.md with project overview

## Phase 2: Foundational

- [X] T004 [P] Create Task data model in src/models/task.py
- [X] T005 [P] Create TodoService class skeleton in src/services/todo_service.py
- [X] T006 [P] Create TodoCLI class skeleton in src/cli/menu.py
- [X] T007 Create main.py entry point with service and CLI initialization

## Phase 3: [US1] Add Task

- [X] T008 [US1] Implement add_task method in src/services/todo_service.py
- [X] T009 [US1] Add validation for required title in src/services/todo_service.py
- [X] T010 [US1] Implement unique ID generation in src/services/todo_service.py
- [X] T011 [US1] Set default completion status to False in src/services/todo_service.py
- [X] T012 [US1] Create add_task method in src/cli/menu.py
- [X] T013 [US1] Connect CLI add_task to service add_task in src/cli/menu.py
- [X] T014 [US1] Test adding tasks with valid inputs
- [X] T015 [US1] Test handling of empty title error

## Phase 4: [US2] View Tasks

- [X] T016 [US2] Implement get_all_tasks method in src/services/todo_service.py
- [X] T017 [US2] Create view_tasks method in src/cli/menu.py
- [X] T018 [US2] Format output with ID, title, description, and status in src/cli/menu.py
- [X] T019 [US2] Add visual indicators for completion status in src/cli/menu.py
- [X] T020 [US2] Handle case when no tasks exist in src/cli/menu.py
- [X] T021 [US2] Connect CLI view_tasks to service get_all_tasks in src/cli/menu.py
- [X] T022 [US2] Test viewing tasks when list is empty
- [X] T023 [US2] Test viewing multiple tasks with different statuses

## Phase 5: [US3] Update Task

- [X] T024 [US3] Implement update_task method in src/services/todo_service.py
- [X] T025 [US3] Validate task exists before updating in src/services/todo_service.py
- [X] T026 [US3] Allow partial updates (title or description only) in src/services/todo_service.py
- [X] T027 [US3] Preserve task ID and completion status during updates in src/services/todo_service.py
- [X] T028 [US3] Create update_task method in src/cli/menu.py
- [X] T029 [US3] Connect CLI update_task to service update_task in src/cli/menu.py
- [X] T030 [US3] Test updating existing task
- [X] T031 [US3] Test handling of non-existent task ID

## Phase 6: [US4] Delete Task

- [X] T032 [US4] Implement delete_task method in src/services/todo_service.py
- [X] T033 [US4] Handle case when task doesn't exist in src/services/todo_service.py
- [X] T034 [US4] Create delete_task method in src/cli/menu.py
- [X] T035 [US4] Connect CLI delete_task to service delete_task in src/cli/menu.py
- [X] T036 [US4] Test deleting existing task
- [X] T037 [US4] Test handling of non-existent task ID

## Phase 7: [US5] Mark Complete/Incomplete

- [X] T038 [US5] Implement mark_task_completed method in src/services/todo_service.py
- [X] T039 [US5] Toggle completion status based on input in src/services/todo_service.py
- [X] T040 [US5] Validate task exists before updating in src/services/todo_service.py
- [X] T041 [US5] Create mark_task_completed method in src/cli/menu.py
- [X] T042 [US5] Create mark_task_incomplete method in src/cli/menu.py
- [X] T043 [US5] Connect CLI mark methods to service mark_task_completed in src/cli/menu.py
- [X] T044 [US5] Test marking existing task as complete
- [X] T045 [US5] Test marking existing task as incomplete
- [X] T046 [US5] Test handling of non-existent task ID

## Phase 8: [US6] CLI Interface

- [X] T047 [US6] Implement main menu display in src/cli/menu.py
- [X] T048 [US6] Handle user input for menu selection in src/cli/menu.py
- [X] T049 [US6] Implement graceful handling of invalid commands in src/cli/menu.py
- [X] T050 [US6] Add help/usage information in src/cli/menu.py
- [X] T051 [US6] Handle keyboard interrupts (Ctrl+C) gracefully in src/cli/menu.py
- [X] T052 [US6] Test complete menu flow with all options

## Phase 9: Polish & Cross-Cutting Concerns

- [X] T053 Add error handling for invalid user inputs across all CLI methods
- [X] T054 Improve user feedback messages for all operations
- [X] T055 Add input validation for task titles and descriptions
- [X] T056 Test edge cases: very long titles/descriptions, special characters
- [X] T057 Update README.md with detailed usage instructions
- [X] T058 Perform end-to-end testing of all features
- [X] T059 Verify compliance with all non-functional requirements
- [X] T060 Final code review and documentation cleanup