# Data Model: Phase I – In-Memory Python CLI Todo Application

## Task Entity

### Fields
- **id**: integer
  - Type: int
  - Constraints: Unique, Positive, Auto-generated
  - Description: Unique identifier for each task
  
- **title**: string
  - Type: str
  - Constraints: Required, Non-empty
  - Description: The main title or description of the task
  
- **description**: string
  - Type: Optional[str]
  - Constraints: Optional, Nullable
  - Description: Additional details about the task
  
- **completed**: boolean
  - Type: bool
  - Constraints: Required, Default: False
  - Description: Completion status of the task

### Relationships
- No relationships with other entities (standalone entity)

### Validation Rules
1. **Title Required**: Task title must be provided and non-empty
2. **Unique ID**: Each task must have a unique ID within the application
3. **Positive ID**: Task ID must be a positive integer
4. **Default Status**: New tasks have completed status set to False by default

### State Transitions
1. **New Task Creation**: 
   - Initial state: completed = False
   - Trigger: User adds a new task
   - Result: Task is created with unique ID and incomplete status

2. **Mark Complete**:
   - From state: completed = False
   - Trigger: User marks task as complete
   - To state: completed = True

3. **Mark Incomplete**:
   - From state: completed = True
   - Trigger: User marks task as incomplete
   - To state: completed = False

### Sample Representation
```python
{
    "id": 1,
    "title": "Complete project proposal",
    "description": "Finish writing the project proposal document",
    "completed": False
}
```

### Operations
1. **Create**: Add a new task with required fields
2. **Read**: Retrieve task information
3. **Update**: Modify task title, description, or completion status
4. **Delete**: Remove task from the system
5. **List**: Retrieve all tasks in the system