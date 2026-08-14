import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Invalid position")

        if position == 0:
            self.insert_at_beginning(data)
            return

        temp = self.head

        for i in range(position - 1):
            if temp is None:
                raise IndexError("Position out of bounds")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds")

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            raise IndexError("List is empty")

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

        raise IndexError("Value not found")

    def delete_by_index(self, index):
        if self.head is None:
            raise IndexError("List is empty")

        if index < 0:
            raise IndexError("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(index - 1):
            if temp.next is None:
                raise IndexError("Index out of bounds")
            temp = temp.next

        if temp.next is None:
            raise IndexError("Index out of bounds")

        temp.next = temp.next.next

    def get_values(self):
        values = []
        temp = self.head

        while temp:
            values.append(temp.data)
            temp = temp.next

        return values


# ---------------- GUI ----------------

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Singly Linked List")
        self.root.geometry("1000x650")

        self.list = LinkedList()

        title = tk.Label(
            root,
            text="SINGLY LINKED LIST",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        # Input area
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(
            frame,
            text="Data:",
            font=("Arial", 12)
        ).grid(row=0, column=0, padx=5)

        self.data_entry = tk.Entry(
            frame,
            width=15,
            font=("Arial", 12)
        )
        self.data_entry.grid(row=0, column=1, padx=5)

        tk.Label(
            frame,
            text="Position / Index:",
            font=("Arial", 12)
        ).grid(row=0, column=2, padx=5)

        self.position_entry = tk.Entry(
            frame,
            width=15,
            font=("Arial", 12)
        )
        self.position_entry.grid(row=0, column=3, padx=5)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="Insert Beginning",
            width=20,
            height=2,
            command=self.insert_beginning
        ).grid(row=0, column=0, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="Insert End",
            width=20,
            height=2,
            command=self.insert_end
        ).grid(row=0, column=1, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="Insert at Position",
            width=20,
            height=2,
            command=self.insert_position
        ).grid(row=0, column=2, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="Delete by Value",
            width=20,
            height=2,
            command=self.delete_value
        ).grid(row=1, column=0, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="Delete by Index",
            width=20,
            height=2,
            command=self.delete_index
        ).grid(row=1, column=1, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="Display List",
            width=20,
            height=2,
            command=self.display_list
        ).grid(row=1, column=2, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="Clear List",
            width=20,
            height=2,
            command=self.clear_list
        ).grid(row=2, column=0, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="Exit",
            width=20,
            height=2,
            command=self.root.destroy
        ).grid(row=2, column=1, padx=8, pady=5)

        self.status = tk.Label(
            root,
            text="Ready",
            font=("Arial", 12, "bold")
        )
        self.status.pack(pady=5)

        # Canvas
        self.canvas = tk.Canvas(
            root,
            width=900,
            height=250,
            bg="white"
        )
        self.canvas.pack(pady=15)

    # ---------------- BUTTON FUNCTIONS ----------------

    def insert_beginning(self):
        try:
            data = int(self.data_entry.get())

            self.list.insert_at_beginning(data)

            self.status.config(
                text=f"{data} inserted at beginning"
            )

            self.data_entry.delete(0, tk.END)

            self.draw_list()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid number in Data."
            )

    def insert_end(self):
        try:
            data = int(self.data_entry.get())

            self.list.insert_at_end(data)

            self.status.config(
                text=f"{data} inserted at end"
            )

            self.data_entry.delete(0, tk.END)

            self.draw_list()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid number."
            )

    def insert_position(self):
        try:
            data = int(self.data_entry.get())
            position = int(self.position_entry.get())

            self.list.insert_at_position(
                data,
                position
            )

            self.status.config(
                text=f"{data} inserted at position {position}"
            )

            self.data_entry.delete(0, tk.END)
            self.position_entry.delete(0, tk.END)

            self.draw_list()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Enter valid numbers."
            )

        except IndexError as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def delete_value(self):
        try:
            value = int(self.data_entry.get())

            self.list.delete_by_value(value)

            self.status.config(
                text=f"{value} deleted"
            )

            self.data_entry.delete(0, tk.END)

            self.draw_list()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Enter a valid number."
            )

        except IndexError as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def delete_index(self):
        try:
            index = int(self.position_entry.get())

            self.list.delete_by_index(index)

            self.status.config(
                text=f"Node at index {index} deleted"
            )

            self.position_entry.delete(0, tk.END)

            self.draw_list()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Enter a valid index."
            )

        except IndexError as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def display_list(self):
        values = self.list.get_values()

        if not values:
            messagebox.showinfo(
                "Linked List",
                "Linked List is empty."
            )
            return

        messagebox.showinfo(
            "Linked List",
            " -> ".join(map(str, values)) + " -> NULL"
        )

        self.draw_list()

    def clear_list(self):
        self.list.head = None
        self.canvas.delete("all")

        self.status.config(
            text="Linked List cleared"
        )

    # ---------------- DRAW LIST ----------------

    def draw_list(self):
        self.canvas.delete("all")

        values = self.list.get_values()

        if not values:
            self.canvas.create_text(
                450,
                120,
                text="Linked List is Empty",
                font=("Arial", 20, "bold")
            )
            return

        x = 40
        y = 90

        for i, value in enumerate(values):

            # Node
            self.canvas.create_rectangle(
                x,
                y,
                x + 120,
                y + 60,
                width=2
            )

            # Data
            self.canvas.create_text(
                x + 45,
                y + 30,
                text=str(value),
                font=("Arial", 16, "bold")
            )

            # Next part
            self.canvas.create_line(
                x + 90,
                y,
                x + 90,
                y + 60,
                width=2
            )

            self.canvas.create_text(
                x + 105,
                y + 30,
                text="N",
                font=("Arial", 12)
            )

            # Index
            self.canvas.create_text(
                x + 60,
                y - 15,
                text=f"Index {i}",
                font=("Arial", 10, "bold")
            )

            # Arrow
            if i < len(values) - 1:
                self.canvas.create_line(
                    x + 120,
                    y + 30,
                    x + 180,
                    y + 30,
                    arrow=tk.LAST,
                    width=2
                )

            x += 180

        # NULL
        self.canvas.create_text(
            x,
            y + 30,
            text="NULL",
            font=("Arial", 14, "bold")
        )


# ---------------- RUN ----------------

root = tk.Tk()
app = App(root)
root.mainloop()
