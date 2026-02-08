# Delete Task Feature Specification

## Feature Name
Delete Task

## Objective
Allow users to remove a task from the todo list by its ID.

## Inputs
- Task ID (required integer)

## Expected Behavior
- System locates task by ID in memory
- Removes the task from storage
- Confirms deletion to user

## Constraints
- Task ID must exist in the system
- Operation should fail gracefully if ID doesn't exist
- No recovery option after deletion

## Output
- Success message confirming deletion
- Error message if task ID doesn't exist