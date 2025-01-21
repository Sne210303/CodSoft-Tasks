import tkinter as tk
from tkinter import messagebox

def command_line_interface():
    tasks = []  # Initialize an empty task list
    print("----WELCOME TO THE TO-DO LIST----")
    
    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print("Your initial tasks are:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

    while True:
        try:
            operation = int(input("\nEnter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit/Stop\n"))
            if operation == 1:
                add_task_cli(tasks)
            elif operation == 2:
                update_task_cli(tasks)
            elif operation == 3:
                delete_task_cli(tasks)
            elif operation == 4:
                view_tasks_cli(tasks)
            elif operation == 5:
                print("Closing the program....")
                break
            else:
                print("Invalid Input. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

def view_tasks_cli(tasks):
    if tasks:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("\nNo tasks available.")

def add_task_cli(tasks):
    new_task = input("Enter the task you want to add: ")
    tasks.append(new_task)
    print(f"Task '{new_task}' has been successfully added.")

def update_task_cli(tasks):
    if not tasks:
        print("No tasks available to update.")
        return
    old_task = input("Enter the task name you want to update: ")
    if old_task in tasks:
        new_task = input("Enter the new task: ")
        tasks[tasks.index(old_task)] = new_task
        print(f"Task '{old_task}' has been updated to '{new_task}'.")
    else:
        print("Task not found.")

def delete_task_cli(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return
    del_task = input("Enter the task you want to delete: ")
    if del_task in tasks:
        tasks.remove(del_task)
        print(f"Task '{del_task}' has been deleted.")
    else:
        print("Task not found.")


def gui_interface():
    def add_task_gui():
        task = task_entry.get()
        if task:
            task_list.insert(tk.END, task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def delete_task_gui():
        selected_task = task_list.curselection()
        if selected_task:
            task_list.delete(selected_task)
        else:
            messagebox.showwarning("Selection Error", "No task selected to delete!")

    def update_task_gui():
        selected_task = task_list.curselection()
        if selected_task:
            new_task = task_entry.get()
            if new_task:
                task_list.delete(selected_task)
                task_list.insert(selected_task, new_task)
                task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "New task cannot be empty!")
        else:
            messagebox.showwarning("Selection Error", "No task selected to update!")

    def clear_all_tasks_gui():
        if task_list.size() > 0:
            task_list.delete(0, tk.END)
        else:
            messagebox.showinfo("Info", "No tasks to clear!")

    root = tk.Tk()
    root.title("To-Do List (GUI)")

    
    task_entry = tk.Entry(root, width=50)
    task_entry.pack(pady=5)

    
    add_button = tk.Button(root, text="Add Task", command=add_task_gui)
    add_button.pack(pady=5)

    update_button = tk.Button(root, text="Update Task", command=update_task_gui)
    update_button.pack(pady=5)

    delete_button = tk.Button(root, text="Delete Task", command=delete_task_gui)
    delete_button.pack(pady=5)

    clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks_gui)
    clear_button.pack(pady=5)

    
    task_list = tk.Listbox(root, width=50, height=15)
    task_list.pack(pady=10)

    root.mainloop()


def main():
    print("----WELCOME TO THE HYBRID TO-DO LIST APPLICATION----")
    print("Choose an interface:")
    print("1. Command-Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")

    while True:
        try:
            choice = int(input("Enter your choice (1 or 2): "))
            if choice == 1:
                command_line_interface()
                break
            elif choice == 2:
                gui_interface()
                break
            else:
                print("Invalid choice. Please enter 1 for CLI or 2 for GUI.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


main()
