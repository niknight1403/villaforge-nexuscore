from time import time
from typing import Callable, Dict, List, Optional, Tuple

class Task:
    def __init__(self, task_id: str, task_function: Callable, max_retries: int = 2, timeout: int = 600):
        self.task_id = task_id
        self.task_function = task_function
        self.max_retries = max_retries
        self.timeout = timeout
        self.retry_count = 0
        self.last_attempt_time = 0
        self.status = 'PENDING'

    def execute(self):
        if self.status == 'BLOCKED':
            print(f'Task {self.task_id} is blocked. Manual intervention required.')
            return

        if time() - self.last_attempt_time < self.timeout:
            print(f'Task {self.task_id} is still within the timeout period. Retrying...')
            return

        try:
            self.task_function()
            self.retry_count = 0
            self.last_attempt_time = time()
            self.status = 'COMPLETED'
        except Exception as e:
            self.retry_count += 1
            self.last_attempt_time = time()
            if self.retry_count >= self.max_retries:
                self.status = 'BLOCKED'
                print(f'Task {self.task_id} has been blocked after {self.retry_count} retries. Error: {str(e)}')
            else:
                print(f'Task {self.task_id} failed. Retrying...')

class TaskScheduler:
    def __init__(self):
        self.tasks: Dict[str, Task] = {}

    def add_task(self, task_id: str, task_function: Callable, max_retries: int = 2, timeout: int = 600):
        if task_id in self.tasks:
            raise ValueError(f'Task {task_id} already exists.')
        self.tasks[task_id] = Task(task_id, task_function, max_retries, timeout)

    def execute_task(self, task_id: str):
        if task_id not in self.tasks:
            raise ValueError(f'Task {task_id} does not exist.')
        task = self.tasks[task_id]
        task.execute()

    def get_task_status(self, task_id: str) -> str:
        if task_id not in self.tasks:
            raise ValueError(f'Task {task_id} does not exist.')
        return self.tasks[task_id].status

    def get_all_task_statuses(self) -> Dict[str, str]:
        return {task_id: task.status for task_id, task in self.tasks.items()}}
