from tkinter import *

root = Tk()
root.title("To-Do List Manager")
root.geometry("400x500")

tasks = []

def add_task():
    task = task_entry.get()
    if task:  
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, END)
    else:
        message_label.config(text="Task cannot be empty!", fg="red")

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()
        message_label.config(text="Task removed!", fg="green")
    else:
        message_label.config(text="Select a task to remove!", fg="red")

def clear_tasks():
    tasks.clear()
    update_task_list()
    message_label.config(text="All tasks cleared!", fg="green")

def update_task_list():
    task_list.delete(0, END)  
    for task in tasks:
        task_list.insert(END, task)
    message_label.config(text="")

Label(root, text="To-Do List Manager", font=("Arial", 20, "bold")).pack(pady=10)


task_entry = Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

Button(root, text="Add Task", font=("Arial", 12), command=add_task, bg="lightblue").pack(pady=5)
Button(root, text="Remove Task", font=("Arial", 12), command=remove_task, bg="lightblue").pack(pady=5)
Button(root, text="Clear Tasks", font=("Arial", 12), command=clear_tasks, bg="lightblue").pack(pady=5)

task_list = Listbox(root, font=("Arial", 14), width=30, height=15)
task_list.pack(pady=10)

message_label = Label(root, text="", font=("Arial", 12))
message_label.pack(pady=5)

root.mainloop()
