"""
Entry point for the Todo application
"""

from src.services.todo_service import TodoService
from src.cli.menu import TodoCLI


def main():
    """
    Main entry point for the application
    """
    # Initialize the service and CLI
    service = TodoService()
    cli = TodoCLI(service)
    
    # Run the CLI application
    cli.run()


if __name__ == "__main__":
    main()