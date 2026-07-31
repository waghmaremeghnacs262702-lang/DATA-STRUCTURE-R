from tkinter import *
from tkinter import messagebox

queue = []

def enqueue():
    item = item_entry.get().strip()

    if item == "":
        messagebox.showerror("Error", "Please enter an item.")
        return

    try:
        priority = int(priority_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Priority must be an integer.")
        return

    queue.append((item, priority))
    queue.sort(key=lambda x: x[1])

    item_entry.delete(0, END)
    priority_entry.delete(0, END)

    display()

def dequeue():
    if not queue:
        messagebox.showinfo("Queue", "Queue is Empty")
    else:
        removed = queue.pop(0)
        messagebox.showinfo("Dequeued", f"Removed: {removed[0]}")

    display()

def display():
    listbox.delete(0, END)

    if not queue:
        listbox.insert(END, "Queue is Empty")
    else:
        for item, priority in queue:
            listbox.insert(END, f"{item} - Priority {priority}")

# Main Window
root = Tk()
root.title("Priority Queue using Tkinter")
root.geometry("400x350")

# Item
Label(root, text="Item").grid(row=0, column=0, padx=10, pady=10)

item_entry = Entry(root, width=25)
item_entry.grid(row=0, column=1)

# Priority
Label(root, text="Priority").grid(row=1, column=0, padx=10, pady=10)

priority_entry = Entry(root, width=25)
priority_entry.grid(row=1, column=1)

# Buttons
Button(root, text="Enqueue", width=12, command=enqueue).grid(row=2, column=0, pady=10)

Button(root, text="Dequeue", width=12, command=dequeue).grid(row=2, column=1, pady=10)

# Queue Display
Label(root, text="Priority Queue").grid(row=3, column=0, columnspan=2)

listbox = Listbox(root, width=40, height=10)
listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
