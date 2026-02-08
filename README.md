# Phase I – In-Memory Python CLI Todo Application

A command-line based Todo application that demonstrates clean architecture, modular design, and extensibility for future cloud-native and AI-driven phases. The application runs locally with in-memory storage and provides core task management capabilities.

## Features

- Add tasks with unique IDs, titles, and optional descriptions
- View all tasks with their ID, title, description, and completion status
- Update existing tasks by ID
- Delete tasks by ID
- Mark tasks as complete or incomplete

## Prerequisites

- Python 3.13 or higher

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Run the application using Python:

```bash
python src/main.py
```

## Usage

The application provides a menu-driven interface:

1. **Add Task**: Create a new task with a title and optional description
2. **View Tasks**: Display all tasks with their details
3. **Update Task**: Modify an existing task's title or description
4. **Delete Task**: Remove a task by its ID
5. **Mark Task Complete**: Change a task's status to completed
6. **Mark Task Incomplete**: Change a task's status to incomplete
7. **Exit**: Close the application

## Architecture

The application follows a clean architecture pattern with three distinct layers:

- **Models**: Data structures (Task entity)
- **Services**: Business logic (TodoService)
- **CLI**: User interface (TodoCLI)

## Project Structure

```
src/
├── models/
│   └── task.py          # Task data structure
├── services/
│   └── todo_service.py  # Business logic
├── cli/
│   └── menu.py          # CLI interface
└── main.py              # Entry point
```

## Constraints

- In-memory data storage only (no persistence)
- Command-line interface only
- Uses only Python standard libraries
- No external dependencies

## License

This project is open source and available under the MIT License.