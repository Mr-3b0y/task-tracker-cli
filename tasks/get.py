from db.db import TaskDB


def get_tasks_list(args):
    """
    Retrieves and prints a list of tasks based on their status.
    Args:
        args (str): The status of tasks to filter by. Can be "in-progress", "done", or "todo".
                    If no status is provided, all tasks are listed.
    Returns:
        None
    Prints:
        A list of tasks with their details such as Task ID, Description, Status, Created At, and Last Updated.
        If no tasks are found, prints "No tasks found".
    """
    
    
    tasks = TaskDB().get_all()
    text = "Listing all tasks"
    if args == "in-progress":
        tasks = {key: value for key, value in tasks.items() if value["status"] == "in-progress"}
        text = "Listing in-progress tasks"
    elif args == "done":
        tasks = {key: value for key, value in tasks.items() if value["status"] == "done"}
        text = "Listing done tasks"
    elif args == "todo":
        tasks = {key: value for key, value in tasks.items() if value["status"] == "todo"}
        text = "Listing todo tasks"
        
    if tasks == {}:
        print("No tasks found")
        return
    
    print(text)
    for key, value in tasks.items():
        print(f"""
        Task ID: {key}
        Description: {value['description']}
        Status: {value['status']}
        Created At: {value['createdAt']}
        Last Updated: {value['updatedAt']}
        --------------------------------------------""")
        