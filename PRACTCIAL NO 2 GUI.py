import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid position")
        self.items.insert(position, item)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid position")
        return self.items.pop(position)

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.is_empty():
            return "Stack is empty"
        return " <- ".join(self.items)



stack = Stack()

def insert_item():
    item = item_entry.get()

    if item == "":
        messagebox.showerror("Error", "Please enter an item.")
        return

    try:
        position = int(position_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Position must be an integer.")
        return

    try:
        stack.insert(item, position)
        messagebox.showinfo(
            "Success",
            "'" + item + "' inserted at position " + str(position)
        )

        item_entry.delete(0, tk.END)
        position_entry.delete(0, tk.END)

        update_stack()

    except IndexError as e:
        messagebox.showerror("Error", str(e))


def delete_item():
    try:
        position = int(position_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid position.")
        return

    try:
        item = stack.delete(position)

        messagebox.showinfo(
            "Success",
            "'" + item + "' deleted from position " + str(position)
        )

        position_entry.delete(0, tk.END)

        update_stack()

    except IndexError as e:
        messagebox.showerror("Error", str(e))


def peek_item():
    try:
        item = stack.peek()
        result_label.config(text="Top Item: " + item)
    except IndexError as e:
        messagebox.showerror("Error", str(e))


def check_empty():
    if stack.is_empty():
        result_label.config(text="Stack is Empty")
    else:
        result_label.config(text="Stack is Not Empty")


def get_size():
    result_label.config(text="Stack Size: " + str(stack.size()))


def traverse_stack():
    result_label.config(
        text="Stack: " + stack.traverse()
    )


def update_stack():
    stack_list.delete(0, tk.END)

    if stack.is_empty():
        stack_list.insert(tk.END, "Stack is Empty")
    else:
        
        for item in reversed(stack.items):
            stack_list.insert(tk.END, item)


def clear_all():
    stack.items.clear()
    item_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    result_label.config(text="Stack Cleared")
    update_stack()


def exit_program():
    root.destroy()



root = tk.Tk()
root.title("Stack ADT - Practical No. 2")
root.geometry("650x600")
root.resizable(False, False)



title_label = tk.Label(
    root,
    text="STACK ADT",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=15)


subtitle_label = tk.Label(
    root,
    text="Practical No. 2 - Data Structures",
    font=("Arial", 14)
)
subtitle_label.pack()



input_frame = tk.Frame(root)
input_frame.pack(pady=20)


tk.Label(
    input_frame,
    text="Enter Item:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=10)

item_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=20
)
item_entry.grid(row=0, column=1, padx=10, pady=10)


tk.Label(
    input_frame,
    text="Position:",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=10)

position_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=20
)
position_entry.grid(row=1, column=1, padx=10, pady=10)



button_frame = tk.Frame(root)
button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="Insert",
    width=15,
    command=insert_item
).grid(row=0, column=0, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Delete",
    width=15,
    command=delete_item
).grid(row=0, column=1, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Peek",
    width=15,
    command=peek_item
).grid(row=1, column=0, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Check Empty",
    width=15,
    command=check_empty
).grid(row=1, column=1, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Size",
    width=15,
    command=get_size
).grid(row=2, column=0, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Traverse",
    width=15,
    command=traverse_stack
).grid(row=2, column=1, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Clear Stack",
    width=15,
    command=clear_all
).grid(row=3, column=0, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Exit",
    width=15,
    command=exit_program
).grid(row=3, column=1, padx=5, pady=5)



tk.Label(
    root,
    text="Stack Contents (Top to Bottom)",
    font=("Arial", 14, "bold")
).pack(pady=10)


stack_list = tk.Listbox(
    root,
    font=("Arial", 14),
    width=30,
    height=8
)
stack_list.pack()



result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 13)
)
result_label.pack(pady=15)



update_stack()



root.mainloop()
