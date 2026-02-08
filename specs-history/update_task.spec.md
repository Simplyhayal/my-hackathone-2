# Update Task Feature Specification

## Feature Name
Update Task

## Objective
Allow users to modify the title and/or description of an existing task by its ID.

## Inputs
- Task ID (required integer)
- New title (optional string)
- New description (optional string)

## Expected Behavior
- System locates task by ID in memory
- Updates specified fields (title and/or description)
- Preserves task ID and completion status
- Provides confirmation of update

## Constraints
- Task ID must exist in the system
- Operation should fail gracefully if ID doesn't exist
- Does not change task completion status
- Does not change task ID

## Output
- Success message confirming update
- Display of updated task details
- Error message if task ID doesn't exist