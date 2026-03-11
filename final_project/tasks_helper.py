import json
import os


def load_tasks():
    tasks = []
    if not os.path.exists("tasks.txt"):
        return tasks
    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                tasks.append(json.loads(line))
    return tasks


def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(json.dumps(task) + "\n")
