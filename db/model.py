

class Task():
    """
    A class used to represent a Task.
    Attributes
    ----------
    id : int
        The unique identifier for the task.
    description : str
        A brief description of the task.
    status : str
        The current status of the task (e.g., 'pending', 'completed').
    createdAt : str
        The timestamp when the task was created.
    updatedAt : str
        The timestamp when the task was last updated.
    Methods
    -------
    __init__(self, id, description, status, createdAt, updatedAt)
        Initializes a new Task instance with the given attributes.
    as_json(self)
        Returns a dictionary representation of the task suitable for JSON serialization.
    """
    
    id: int
    description: str
    status: str
    createdAt: str
    updatedAt: str
    
    
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        
    def as_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }