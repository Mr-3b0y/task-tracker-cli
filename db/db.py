import os
import json
import datetime
from .model import Task

class TaskDB:
    """
    A class to manage tasks in a JSON database.
    Methods
    -------
    __init__():
        Initializes the TaskDB instance and ensures the tasks.json file exists.
    __get_next_id():
        Returns the next available task ID.
    get_all():
        Returns all tasks in the database.
    get_by_id(id):
        Returns a task by its ID.
    create(task: Task):
        Creates a new task and adds it to the database.
    update_description(id, description):
        Updates the description of a task by its ID.
    update_status(id, status):
        Updates the status of a task by its ID.
    delete(id):
        Deletes a task by its ID.
    """
    def __init__(self):

        if not os.path.exists("db/tasks.json"):
            with open("db/tasks.json", "w") as f:
                json.dump({}, f)

        self.db: dict = dict(json.load(open("db/tasks.json")))
        
        
    def __get_next_id(self):
        return len(self.db.keys()) + 1 if self.db.keys() else 1

    def get_all(self):
        return self.db

    def get_by_id(self, id):
        return self.db.get(id)

    def create(self, task: Task):
        task.id = self.__get_next_id()
        self.db[task.id] = task.as_json()
        open("db/tasks.json", "w").write(json.dumps(self.db))
        self.db = json.dumps(self.db)
        return task

    def update_description(self, id, description):
        task = self.db.get(id)
        if task:
            task["description"] = description
            task["updatedAt"] = datetime.datetime.now().__str__()
            self.db[id] = task
            open("db/tasks.json", "w").write(json.dumps(self.db))
            return True
        return False
    
    def update_status(self, id, status):
        task = self.db.get(id)
        if task:
            task["status"] = status
            task["updatedAt"] = datetime.datetime.now().__str__()
            self.db[id] = task
            open("db/tasks.json", "w").write(json.dumps(self.db))
            return True
        return False

    def delete(self, id):
        if self.db.pop(id, None):
            open("db/tasks.json", "w").write(json.dumps(self.db))
            return True
        return False