# Quickstart Guide: Phase I – In-Memory Python CLI Todo Application

## Prerequisites

- Python 3.13 or higher installed on your system

## Setup

1. Clone or download the repository to your local machine
2. Navigate to the project directory

## Running the Application

To start the Todo application, run the following command from the project root:

```bash
python src/main.py
```

## Using the Application

Once the application starts, you'll see the main menu:

```
=== Todo Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
========================
```

### Available Actions

#### 1. Add Task
- Select option 1 from the menu
- Enter a title for the task (required)
- Optionally enter a description
- The system will automatically assign a unique ID

#### 2. View Tasks
- Select option 2 from the menu
- All tasks will be displayed with their ID, title, description, and completion status
- Completed tasks are marked with ✓, incomplete with ○

#### 3. Update Task
- Select option 3 from the menu
- Enter the task ID you wish to update
- Enter new title or description (or leave blank to keep current values)

#### 4. Delete Task
- Select option 4 from the menu
- Enter the task ID you wish to delete
- Confirm the deletion

#### 5. Mark Task Complete
- Select option 5 from the menu
- Enter the task ID you wish to mark as complete

#### 6. Mark Task Incomplete
- Select option 6 from the menu
- Enter the task ID you wish to mark as incomplete

#### 7. Exit
- Select option 7 to quit the application

## Example Workflow

1. Start the application: `python src/main.py`
2. Add a task: Select 1, enter "Buy groceries", press Enter
3. View tasks: Select 2 to see your task with ID 1
4. Mark complete: Select 5, enter ID 1
5. Exit: Select 7 to quit

## Troubleshooting

- If you get a "Python not found" error, ensure Python 3.13+ is installed and in your PATH
- If the application crashes, ensure you're entering valid inputs (numbers for IDs, non-empty titles)
- For invalid task IDs, the application will display an appropriate error message

## Architecture Overview

The application follows a clean architecture pattern:
- **Models** (`src/models/task.py`): Defines the Task data structure
- **Services** (`src/services/todo_service.py`): Contains all business logic
- **CLI** (`src/cli/menu.py`): Handles user input and output
- **Main** (`src/main.py`): Entry point that connects all components