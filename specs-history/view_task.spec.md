# View Tasks Feature Specification

## Feature Name
View Tasks

## Objective
Display all tasks in the todo list with their details in a readable format.

## Inputs
- None (displays all tasks)

## Expected Behavior
- System retrieves all tasks from memory
- Displays each task with its ID, title, description, and completion status
- Shows all tasks in a clear, organized format
- Handles case when no tasks exist

## Constraints
- Data displayed from in-memory storage only
- No modifications to tasks during viewing
- Must handle empty task list gracefully

## Output
- Formatted list of all tasks showing ID, title, description, and status
- Message indicating no tasks exist if list is empty