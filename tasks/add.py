
from db.model import Task
from db.db import TaskDB
import datetime

from utils.enums import TaskStatus

def add_task(description):
    """
    Adds a new task with the given description to the task database.

    Args:
        description (str): The description of the task to be added.

    Returns:
        None

    Prints:
        A success message with the ID of the added task.
    """
    task = TaskDB().create(Task(None, description, TaskStatus.TODO.value, datetime.datetime.now().__str__(), datetime.datetime.now().__str__()))
    print(f"Task added successfully (ID: {task.id})")