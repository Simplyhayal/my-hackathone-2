"""
Task data structure for the Todo application
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a task in the todo list
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False