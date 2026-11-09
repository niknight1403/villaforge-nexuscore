from time import time
from functools import wraps

class TaskScheduler:
    def __init__(self):
        self.tasks = {}
        self.blocked_tasks = {}

    def schedule_task(self, task_id, func, *args, **kwargs):
        if task_id in self.blocked_tasks:
            raise Exception(f'Task {task_id} is blocked and requires manual intervention.')
        self.tasks[task_id] = {'func': func, 'args': args, 'kwargs': kwargs, 'start_time': time()}

    def run_task(self, task_id):
        if task_id not in self.tasks:
            raise Exception(f'Task {task_id} not found.')
        task = self.tasks[task_id]
        result = task['func'](*task['args'], **task['kwargs'])
        if result is False and task['start_time'] + 600 < time():
            self.block_task(task_id)

    def block_task(self, task_id):
        self.blocked_tasks[task_id] = True
        print(f'Task {task_id} blocked due to repeated failures.')

    def retry_task(self, task_id):
        if task_id in self.blocked_tasks:
            del self.blocked_tasks[task_id]
            print(f'Task {task_id} unblocked. Retry initiated.')
        else:
            print(f'Task {task_id} is not blocked. No retry needed.')
