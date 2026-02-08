# Implementation Plan: Phase I – In-Memory Python CLI Todo Application

## Technical Context

- **Application Type**: Command-line interface (CLI) application
- **Programming Language**: Python 3.13+
- **Data Storage**: In-memory only (no persistence)
- **Architecture**: Clean architecture with separation of concerns (Model-Service-CLI)
- **Dependencies**: Standard Python libraries only (no external dependencies)
- **Target Platform**: Local execution
- **Development Approach**: Spec-driven development
- **Project Structure**: 
  - `/src/models/task.py` - Task data structure
  - `/src/services/todo_service.py` - Business logic
  - `/src/cli/menu.py` - CLI interface
  - `/src/main.py` - Entry point

## Constitution Check

- ✅ CLI-First Interface: All features accessible through CLI
- ✅ In-Memory Data Storage: Data stored in memory only, no persistence
- ✅ Clean Architecture Separation: Clear separation between Models, Services, and CLI
- ✅ Python Standard Library Only: Using only Python 3.13+ standard libraries
- ✅ Error Handling and Graceful Degradation: Proper error handling for invalid inputs
- ✅ Minimalist Design: Focused on core functionality without over-engineering

## Gates

- ✅ Architecture compliance: Follows three-layer architecture (Model-Service-CLI)
- ✅ Technology compliance: Uses only Python standard libraries
- ✅ Constraint compliance: In-memory storage, CLI interface only
- ✅ Quality compliance: Clean, readable, maintainable code with error handling

## Phase 0: Outline & Research

### Research Findings

#### Decision: Unique ID Generation Strategy
- **Chosen**: Integer counter starting from 1
- **Rationale**: Simple, efficient, and predictable for CLI application. Users can easily reference tasks by small integers.
- **Alternatives considered**: UUID (too complex for CLI), random integers (might have collisions), timestamp-based (unnecessarily complex)

#### Decision: Task Status Handling
- **Chosen**: Boolean field (True for completed, False for incomplete)
- **Rationale**: Simple and efficient for the binary nature of task completion
- **Alternatives considered**: String labels like "completed"/"incomplete" (more verbose), enum (overkill for binary state)

#### Decision: Error Handling Approach
- **Chosen**: Exceptions for invalid inputs, return codes for expected scenarios
- **Rationale**: Exceptions for truly exceptional circumstances (invalid data), return codes for expected scenarios (task not found)
- **Alternatives considered**: Only return codes (less Pythonic), only exceptions (could mask expected scenarios)

#### Decision: CLI Input/Output Formatting
- **Chosen**: List display with visual indicators for completion status
- **Rationale**: Simple and clear for CLI environment
- **Alternatives considered**: Table format (more complex), JSON output (less human-readable)

#### Decision: Folder Structure
- **Chosen**: Layered approach with separate directories for models, services, and CLI
- **Rationale**: Maintains clear separation of concerns as required by constitution
- **Alternatives considered**: Single file (violates separation requirement), additional subdirectories (over-engineering)

## Phase 1: Design & Contracts

### Data Model

#### Task Entity
- **id**: integer (unique, auto-generated)
- **title**: string (required, non-empty)
- **description**: string (optional, nullable)
- **completed**: boolean (default: False)

#### Validation Rules
- Task title must be provided and non-empty
- Task ID must be unique within the application
- Task ID must be positive integer

#### State Transitions
- New task: completed = False (default)
- Completed task: completed = True
- Incomplete task: completed = False

### API Contracts

#### Service Layer Interface (TodoService)

```python
class TodoService:
    def __init__(self):
        """Initialize the service with empty task list and ID counter"""
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task with unique ID and return the created task"""
    
    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks in the system"""
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """Update an existing task and return updated task or None if not found"""
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID and return True if successful, False otherwise"""
    
    def mark_task_completed(self, task_id: int, completed: bool = True) -> Optional[Task]:
        """Mark a task as complete/incomplete and return updated task or None if not found"""
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Find a task by its ID and return it or None if not found"""
```

### Quickstart Guide

1. Clone or download the repository
2. Ensure Python 3.13+ is installed
3. Run the application: `python src/main.py`
4. Use the menu to interact with the todo list:
   - Add tasks with titles and optional descriptions
   - View all tasks with their status
   - Update existing tasks
   - Delete tasks by ID
   - Mark tasks as complete/incomplete

## Phase 2: Implementation Approach

### Section Structure (Organized by Features)

#### 1. Add Task Feature
- Implemented `add_task` method in TodoService
- Handles validation for required title
- Generates unique ID automatically
- Sets default completion status to False

#### 2. View Tasks Feature
- Implemented `get_all_tasks` method in TodoService
- Formats output in CLI with clear visual indicators
- Handles case when no tasks exist

#### 3. Update Task Feature
- Implemented `update_task` method in TodoService
- Validates task exists before updating
- Allows partial updates (title or description only)

#### 4. Delete Task Feature
- Implemented `delete_task` method in TodoService
- Handles case when task doesn't exist
- Confirms deletion if requested

#### 5. Mark Complete/Incomplete Feature
- Implemented `mark_task_completed` method in TodoService
- Toggles completion status based on input
- Validates task exists before updating

### Quality Validation

#### Automated Checks
- Unit tests for each service method
- Test edge cases (invalid IDs, empty titles, etc.)
- Verify data integrity after operations

#### Manual Checks
- End-to-end testing via CLI interface
- Verify all menu options work correctly
- Test error handling with invalid inputs
- Confirm data persists correctly in memory during session

#### Feature Validation Against Acceptance Criteria
- Add: Verify tasks can be added with unique IDs and required titles
- View: Verify all tasks display with correct information
- Update: Verify tasks can be updated by ID
- Delete: Verify tasks can be deleted by ID
- Mark: Verify completion status can be toggled by ID

### Testing Strategy

#### Unit Tests for Services
- Test `add_task` with valid and invalid inputs
- Test `get_all_tasks` with empty and populated lists
- Test `update_task` with existing and non-existing tasks
- Test `delete_task` with existing and non-existing tasks
- Test `mark_task_completed` with existing and non-existing tasks

#### Manual Testing via CLI
- Full end-to-end flow testing
- Error condition testing
- Edge case validation

#### Edge Cases
- Adding task with empty title (should fail)
- Updating/deleting non-existing tasks (should handle gracefully)
- Viewing tasks when none exist (should show appropriate message)
- Marking non-existing tasks as complete (should handle gracefully)

## Implementation Timeline

1. **Day 1**: Complete data model and service layer implementation
2. **Day 2**: Implement CLI interface and integrate with services
3. **Day 3**: Testing, debugging, and documentation
4. **Day 4**: Final validation and preparation for demo