print("Welcome to Task Management")

tasks_pro = ["Add task", "Update task", "Delete task"]
user_tasks = []

def select_pro():
    for i, task in enumerate(tasks_pro):
        print(f"{i+1} : {task}")
    option = input("What do you want to do? ").lower()
    return option

def more_task():
    option = input("Do you want more (y for yes, n for no)? ")
    if option.lower() in ["y", "yes"]:
            # option=select_pro()
            return True
            
    elif option.lower() in ["n", "no"]:
            return False
    else:
            print("Please enter 'y' for yes or 'n' for no: ")

def tasks_manage(option):
   
    while True:
        if option in ["1", "add"]:
            new_task = input("Enter task to add: ")
            user_tasks.append(new_task)
        elif option in ["2", "update"]:
            if user_tasks:
                for index, task in enumerate(user_tasks):
                    print(f"{index+1}.{task}")
                num = int(input("Enter number of task you want to update: ")) - 1
                if 0 <= num < len(user_tasks):
                    update_task = input("Enter new task: ")
                    user_tasks[num] = update_task
                    print("Task updated successfully")
                else:
                    print("Select correct task number")
            else:
                print("No tasks to update.")
        elif option in ["3", "delete"]:
            if user_tasks:
                for index, task in enumerate(user_tasks):
                    print(f"{index+1}.{task}")
                num = int(input("Enter number of task you want to delete: ")) - 1
                if 0 <= num < len(user_tasks):
                    del user_tasks[num]
                    print("Task deleted successfully")
                else:
                    print("Select correct task number")
            else:
                print("No tasks to delete.")
        else:
            print("Select a correct option.")
        
        if not more_task():
         break
        option=select_pro()
        tasks_manage(option)

# Start the task manager
option=select_pro()
tasks_manage(option)
print("Final tasks:", user_tasks)
