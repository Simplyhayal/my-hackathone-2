"""
CLI interface for the Todo application
"""

import sys
from typing import Optional
from src.services.todo_service import TodoService


class TodoCLI:
    """
    Command-line interface for the Todo application
    """
    
    def __init__(self, service: TodoService):
        self.service = service
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n=== Todo Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print("========================")
    
    def get_user_choice(self) -> str:
        """Get user's menu choice"""
        try:
            choice = input("Enter your choice (1-7): ").strip()
            return choice
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)
    
    def add_task(self):
        """Handle adding a new task"""
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()
        
        if not title:
            print("Error: Title is required!")
            return
        
        description = input("Enter task description (optional): ").strip()
        description = description if description else None
        
        try:
            task = self.service.add_task(title, description)
            print(f"Task added successfully! ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def view_tasks(self):
        """Handle viewing all tasks"""
        print("\n--- All Tasks ---")
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            print("No tasks found.")
            return
        
        for task in tasks:
            status = "✓" if task.completed else "○"
            desc = f" - {task.description}" if task.description else ""
            print(f"{status} [{task.id}] {task.title}{desc}")
    
    def update_task(self):
        """Handle updating an existing task"""
        print("\n--- Update Task ---")
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        # Check if task exists
        existing_task = self.service.get_task_by_id(task_id)
        if not existing_task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        print(f"Current task: {existing_task.title}")
        if existing_task.description:
            print(f"Current description: {existing_task.description}")
        
        new_title = input("Enter new title (leave blank to keep current): ").strip()
        new_title = new_title if new_title else None
        
        new_description = input("Enter new description (leave blank to keep current): ").strip()
        new_description = new_description if new_description else None
        
        updated_task = self.service.update_task(task_id, new_title, new_description)
        if updated_task:
            print("Task updated successfully!")
        else:
            print(f"Error: Could not update task with ID {task_id}.")
    
    def delete_task(self):
        """Handle deleting a task"""
        print("\n--- Delete Task ---")
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        success = self.service.delete_task(task_id)
        if success:
            print(f"Task with ID {task_id} deleted successfully!")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    
    def mark_task_completed(self):
        """Handle marking a task as completed"""
        print("\n--- Mark Task Complete ---")
        self._mark_task_status(True)
    
    def mark_task_incomplete(self):
        """Handle marking a task as incomplete"""
        print("\n--- Mark Task Incomplete ---")
        self._mark_task_status(False)
    
    def _mark_task_status(self, completed: bool):
        """Helper method to mark task status"""
        try:
            task_id = int(input("Enter task ID: "))
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        task = self.service.mark_task_completed(task_id, completed)
        if task:
            status = "completed" if completed else "incomplete"
            print(f"Task with ID {task_id} marked as {status}!")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    
    def run(self):
        """Main loop for the CLI application"""
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.mark_task_completed()
            elif choice == '6':
                self.mark_task_incomplete()
            elif choice == '7':
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")