import tkinter as tk
from tkinter import messagebox

SIZE = 10
hash_table = [None] * SIZE

def insert():
    try:
        key = int(entry.get())
        index = key % SIZE

        if hash_table[index] is None:
            hash_table[index] = key
            messagebox.showinfo(
                "Success",
                f"{key} inserted at index {index}"
            )
            entry.delete(0, tk.END)
            display_table()
        else:
            messagebox.showwarning(
                "Collision",
                f"Index {index} is already occupied!"
            )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def delete():
    try:
        key = int(entry.get())
        index = key % SIZE

        if hash_table[index] == key:
            hash_table[index] = None
            messagebox.showinfo(
                "Success",
                f"{key} deleted successfully."
            )
            entry.delete(0, tk.END)
            display_table()
        else:
            messagebox.showwarning(
                "Not Found",
                f"{key} not found in the hash table."
            )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


def traverse():
    display_table()


def display_table():
    output.delete("1.0", tk.END)

    output.insert(tk.END, "INDEX\tVALUE\n")
    output.insert(tk.END, "----------------\n")

    for i in range(SIZE):
        if hash_table[i] is None:
            output.insert(tk.END, f"{i}\tEmpty\n")
        else:
            output.insert(tk.END, f"{i}\t{hash_table[i]}\n")


def clear_table():
    global hash_table
    hash_table = [None] * SIZE
    display_table()
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Hash Table")
root.geometry("500x550")

title = tk.Label(
    root,
    text="HASH TABLE",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

label = tk.Label(
    root,
    text="Enter Key:",
    font=("Arial", 13)
)
label.pack()

entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=20
)
entry.pack(pady=10)

insert_button = tk.Button(
    root,
    text="Insert",
    font=("Arial", 12, "bold"),
    width=15,
    command=insert
)
insert_button.pack(pady=5)

delete_button = tk.Button(
    root,
    text="Delete",
    font=("Arial", 12, "bold"),
    width=15,
    command=delete
)
delete_button.pack(pady=5)

traverse_button = tk.Button(
    root,
    text="Traverse",
    font=("Arial", 12, "bold"),
    width=15,
    command=traverse
)
traverse_button.pack(pady=5)

clear_button = tk.Button(
    root,
    text="Clear Table",
    font=("Arial", 12, "bold"),
    width=15,
    command=clear_table
)
clear_button.pack(pady=5)

output_label = tk.Label(
    root,
    text="Hash Table:",
    font=("Arial", 14, "bold")
)
output_label.pack(pady=15)

output = tk.Text(
    root,
    height=15,
    width=35,
    font=("Courier", 12)
)
output.pack()

display_table()

root.mainloop()
