# Mark Task Complete/Incomplete Feature Specification

## Feature Name
Mark Task Complete/Incomplete

## Objective
Allow users to toggle the completion status of a task by its ID.

## Inputs
- Task ID (required integer)
- Desired status (complete/incomplete)

## Expected Behavior
- System locates task by ID in memory
- Updates the completion status of the task
- Preserves other task attributes (ID, title, description)
- Provides confirmation of status change

## Constraints
- Task ID must exist in the system
- Operation should fail gracefully if ID doesn't exist
- Only affects completion status, not other attributes

## Output
- Success message confirming status update
- Display of task with new status
- Error message if task ID doesn't exist