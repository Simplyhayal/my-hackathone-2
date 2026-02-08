"""
Business logic for the Todo application
"""

from typing import List, Optional
from src.models.task import Task


class TodoService:
    """
    Service class containing all business logic for task management
    """
    
    def __init__(self):
        self.tasks: List[Task] = []
        self._next_id = 1
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task with a unique ID
        
        Args:
            title: Required task title
            description: Optional task description
            
        Returns:
            The newly created Task object
        """
        if not title.strip():
            raise ValueError("Title is required")
            
        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip() if description else None,
            completed=False
        )
        self.tasks.append(task)
        self._next_id += 1
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks
        
        Returns:
            List of all Task objects
        """
        return self.tasks.copy()
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task by ID
        
        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)
            
        Returns:
            Updated Task object or None if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None
            
        if title is not None:
            task.title = title.strip()
        if description is not None:
            task.description = description.strip() if description else description
            
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID
        
        Args:
            task_id: ID of the task to delete
            
        Returns:
            True if task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
            
        self.tasks.remove(task)
        return True
    
    def mark_task_completed(self, task_id: int, completed: bool = True) -> Optional[Task]:
        """
        Mark a task as complete or incomplete
        
        Args:
            task_id: ID of the task to update
            completed: Whether the task is completed (default True)
            
        Returns:
            Updated Task object or None if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None
            
        task.completed = completed
        return task
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID
        
        Args:
            task_id: ID of the task to find
            
        Returns:
            Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None