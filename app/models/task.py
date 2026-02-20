from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    id: int
    description: str
    done: bool = False

class TaskModel:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, description: str) -> bool:
        desc = description.strip()
        if not desc:
            return False
        task = Task(id=self._next_id, description=desc)
        self._tasks.append(task)
        self._next_id += 1
        return True

    def get_all_tasks(self) -> List[Task]:
        return self._tasks.copy()

    def mark_done(self, task_id: int) -> bool:
        for task in self._tasks:
            if task.id == task_id:
                task.done = True
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        self._tasks = [t for t in self._tasks if t.id != task_id]
        return True