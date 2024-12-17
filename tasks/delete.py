from db.db import TaskDB


def delete_task(id):
    """
    Deletes a task with the given ID from the task database.
    Args:
        id (int): The ID of the task to be deleted.
    Returns:
        None
    Prints:
        A success message if the task was deleted successfully.
        An error message if no task was found with the given ID.
    """
    
    delete = TaskDB().delete(id)
    if delete:
        print(f"Task deleted successfully ID({id})")
    else:
        print(f"Task not found with ID({id})")