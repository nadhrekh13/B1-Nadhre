import json
import os

def load_tasks():
    """Load tasks from tasks.txt file and return list of task dictionaries"""
    if not os.path.exists('tasks.txt'):
        return []
    
    tasks = []
    with open('tasks.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                task = json.loads(line)
                tasks.append(task)
    return tasks

def save_tasks(tasks):
    """Save entire task list to tasks.txt file as JSON lines"""
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(json.dumps(task) + '\n')
