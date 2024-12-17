from enum import Enum

class TaskStatus(str, Enum):
    """
    Enum representing the status of a task.

    Attributes:
        TODO (str): Represents a task that is yet to be started.
        DONE (str): Represents a task that has been completed.
        IN_PROGRESS (str): Represents a task that is currently in progress.
    """
    TODO = "todo"
    DONE = "done"
    IN_PROGRESS = "in-progress"