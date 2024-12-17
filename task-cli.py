import argparse

from tasks import add_task, delete_task, get_tasks_list, update_task_description, update_task_status
from utils.enums import TaskStatus


def main():
    """
    Main function to handle command-line arguments for the Task Tracker CLI.
    This function parses the command-line arguments and calls the appropriate
    functions to add, update, delete, list, or change the status of tasks.
    Command-line arguments:
    -a, --add: Add a new task.
    -u, --update: Update an existing task. Requires two arguments: task ID and new task description.
    -d, --delete: Delete a task by its ID.
    -l, --list: List tasks. Optionally filter by status: "done", "in-progress", "todo", or "all".
    -md, --mark-done: Mark a task as done by its ID.
    -mp, --mark-in-progress: Mark a task as in progress by its ID.
    If no valid arguments are provided, the function prints a help message.
    """
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-a", "--add", help = "Add task")
    parser.add_argument("-u", "--update", nargs=2, metavar=('id', 'task'), help = "Update task")
    parser.add_argument("-d", "--delete", help = "Delete task")
    parser.add_argument("-l", "--list", nargs='?', const='all', choices=("done", "in-progress", "todo", "all"), help = "Get all tasks")
    parser.add_argument("-md", "--mark-done", help="Mark task as done")
    parser.add_argument("-mp", "--mark-in-progress", help="Mark task as in progress")
    
    args = parser.parse_args()
        
    if args.add:
        add_task(args.add)
    elif args.list:
        get_tasks_list(args.list)
    elif args.update:
        update_task_description(args.update[0], args.update[1])  
    elif args.delete:
        delete_task(args.delete)
    elif args.mark_done:
        update_task_status(args.mark_done, TaskStatus.DONE.value)
    elif args.mark_in_progress:
        update_task_status(args.mark_in_progress, TaskStatus.IN_PROGRESS.value)
    else:
        print("No valid arguments provided, please run the script with -h or --help for more information.")
        
        
if __name__ == "__main__":
    main()