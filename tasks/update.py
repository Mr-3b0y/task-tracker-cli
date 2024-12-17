from db.db import TaskDB
from utils.enums import TaskStatus


def update_task_description(id, description):
    """
    Update the description of a task in the task database.

    Args:
        id (int): The unique identifier of the task to be updated.
        description (str): The new description for the task.

    Returns:
        None

    Prints:
        A success message if the task was updated successfully.
        An error message if the task with the given ID was not found.
    """
    if TaskDB().update_description(id, description):
        print(f"Task updated successfully ID({id})")
    else:
        print(f"Task not found with ID({id})")
        
        
def update_task_status(id, status):
    """
    Updates the status of a task in the TaskDB.

    Args:
        id (int): The unique identifier of the task.
        status (str): The new status of the task. Expected values are TaskStatus.IN_PROGRESS.value or TaskStatus.DONE.value.

    Returns:
        None

    Prints:
        A success message if the task status is updated successfully.
        An error message if the task with the given ID is not found.
    """
    if TaskDB().update_status(id, status):
        if  status == TaskStatus.IN_PROGRESS.value:
            print(f"Task marked as in progress successfully ID({id})")
        elif status == TaskStatus.DONE.value:
            print(f"Task marked as done successfully ID({id})")
    else:
        print(f"Task not found with ID({id})")