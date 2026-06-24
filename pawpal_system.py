from dataclasses import dataclass, field
from datetime import date


@dataclass
class Task:
    """Represent one pet care task."""

    title: str
    time: str
    duration_minutes: int
    priority: str = "medium"
    frequency: str = "once"
    due_date: date = field(default_factory=date.today)
    completed: bool = False

    def mark_complete(self):
        """Mark this task complete."""
        pass


@dataclass
class Pet:
    """Store pet details and assigned care tasks."""

    name: str
    species: str
    age: int | None = None
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        pass

    def incomplete_tasks(self):
        """Return this pet's incomplete tasks."""
        pass


@dataclass
class Owner:
    """Manage a pet owner's pets."""

    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        pass

    def all_tasks(self):
        """Return all tasks for every pet."""
        pass


class Scheduler:
    """Organize and manage tasks across an owner account."""

    def __init__(self, owner: Owner):
        """Create a scheduler for one owner."""
        self.owner = owner

    def sort_by_time(self, tasks=None):
        """Return tasks sorted by scheduled time."""
        pass

    def filter_tasks(self, pet_name=None, completed=None):
        """Filter tasks by pet name or completion status."""
        pass

    def detect_conflicts(self, tasks=None):
        """Return warnings for tasks scheduled at the same time."""
        pass

    def mark_task_complete(self, pet_name: str, task_title: str):
        """Mark a task complete and handle recurrence."""
        pass
