import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
        new_node.prev = temp

    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Invalid position.")

        if position == 0:
            self.insert_at_beginning(data)
            return

        if self.head is None:
            raise IndexError("Position out of bounds.")

        temp = self.head

        for _ in range(position):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds.")

        new_node = Node(data)

        new_node.next = temp
        new_node.prev = temp.prev

        if temp.prev:
            temp.prev.next = new_node

        temp.prev = new_node

    def delete_at_beginning(self):
        if self.head is None:
            raise IndexError("List is empty.")

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            raise IndexError("List is empty.")

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    def delete_at_position(self, position):
        if self.head is None:
            raise IndexError("List is empty.")

        if position < 0:
            raise IndexError("Invalid position.")

        temp = self.head

        for _ in range(position):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds.")

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def search(self, data):
        temp = self.head

        while temp:
            if temp.data == data:
                return True
            temp = temp.next

        return False

    def length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    def get_data(self):
        data = []
        temp = self.head

        while temp:
            data.append(temp.data)
            temp = temp.next

        return data

class DoublyLinkedListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Doubly Linked List - GUI")
        self.root.geometry("950x600")
        self.root.resizable(False, False)

        self.list = DoublyLinkedList()

        # Title
        title = tk.Label(
            root,
            text="DOUBLY LINKED LIST",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=15)

        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="Data:",
            font=("Arial", 12, "bold")
        ).grid(row=0, column=0, padx=5)

        self.data_entry = tk.Entry(
            input_frame,
            width=15,
            font=("Arial", 12)
        )
        self.data_entry.grid(row=0, column=1, padx=5)

        tk.Label(
            input_frame,
            text="Position:",
            font=("Arial", 12, "bold")
        ).grid(row=0, column=2, padx=5)

        self.position_entry = tk.Entry(
            input_frame,
            width=10,
            font=("Arial", 12)
        )
        self.position_entry.grid(row=0, column=3, padx=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="Insert Beginning",
            width=18,
            command=self.insert_beginning
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Insert End",
            width=18,
            command=self.insert_end
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Insert Position",
            width=18,
            command=self.insert_position
        ).grid(row=0, column=2, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Delete Beginning",
            width=18,
            command=self.delete_beginning
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Delete End",
            width=18,
            command=self.delete_end
        ).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Delete Position",
            width=18,
            command=self.delete_position
        ).grid(row=1, column=2, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Search",
            width=18,
            command=self.search
        ).grid(row=2, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Length",
            width=18,
            command=self.show_length
        ).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Clear",
            width=18,
            command=self.clear_list
        ).grid(row=2, column=2, padx=5, pady=5)

       
        self.canvas = tk.Canvas(
            root,
            width=900,
            height=230,
            bg="white",
            highlightthickness=1
        )
        self.canvas.pack(pady=15)

        
        self.status = tk.Label(
            root,
            text="Ready",
            font=("Arial", 12, "bold")
        )
        self.status.pack()

   

    def get_data(self):
        try:
            return int(self.data_entry.get())
        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid integer."
            )
            return None

    def get_position(self):
        try:
            return int(self.position_entry.get())
        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid position."
            )
            return None

    def insert_beginning(self):
        data = self.get_data()

        if data is None:
            return

        self.list.insert_at_beginning(data)
        self.update_display()

        self.status.config(
            text=f"{data} inserted at beginning."
        )

        self.data_entry.delete(0, tk.END)

    def insert_end(self):
        data = self.get_data()

        if data is None:
            return

        self.list.insert_at_end(data)
        self.update_display()

        self.status.config(
            text=f"{data} inserted at end."
        )

        self.data_entry.delete(0, tk.END)

    def insert_position(self):
        data = self.get_data()
        position = self.get_position()

        if data is None or position is None:
            return

        try:
            self.list.insert_at_position(data, position)

            self.update_display()

            self.status.config(
                text=f"{data} inserted at position {position}."
            )

            self.data_entry.delete(0, tk.END)
            self.position_entry.delete(0, tk.END)

        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def delete_beginning(self):
        try:
            self.list.delete_at_beginning()

            self.update_display()

            self.status.config(
                text="First node deleted."
            )

        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def delete_end(self):
        try:
            self.list.delete_at_end()

            self.update_display()

            self.status.config(
                text="Last node deleted."
            )

        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def delete_position(self):
        position = self.get_position()

        if position is None:
            return

        try:
            self.list.delete_at_position(position)

            self.update_display()

            self.status.config(
                text=f"Node at position {position} deleted."
            )

            self.position_entry.delete(0, tk.END)

        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def search(self):
        data = self.get_data()

        if data is None:
            return

        if self.list.search(data):
            messagebox.showinfo(
                "Search Result",
                f"{data} was found in the list."
            )
            self.status.config(
                text=f"{data} found."
            )
        else:
            messagebox.showwarning(
                "Search Result",
                f"{data} was not found."
            )
            self.status.config(
                text=f"{data} not found."
            )

    def show_length(self):
        length = self.list.length()

        messagebox.showinfo(
            "Length",
            f"Length of the list = {length}"
        )

        self.status.config(
            text=f"Length = {length}"
        )

    def clear_list(self):
        self.list = DoublyLinkedList()

        self.update_display()

        self.status.config(
            text="List cleared."
        )


    def update_display(self):
        self.canvas.delete("all")

        data = self.list.get_data()

        if not data:
            self.canvas.create_text(
                450,
                110,
                text="List is Empty",
                font=("Arial", 20, "bold")
            )
            return

        x = 30
        y = 80

        node_width = 90
        node_height = 60
        gap = 70

        for i, value in enumerate(data):

           
            self.canvas.create_rectangle(
                x,
                y,
                x + node_width,
                y + node_height,
                outline="black",
                width=2
            )

            
            self.canvas.create_text(
                x + node_width / 2,
                y + node_height / 2,
                text=str(value),
                font=("Arial", 16, "bold")
            )

            
            self.canvas.create_text(
                x + node_width / 2,
                y - 15,
                text=f"Index {i}",
                font=("Arial", 10)
            )

           
            if i < len(data) - 1:

               
                self.canvas.create_line(
                    x + node_width,
                    y + 20,
                    x + node_width + gap,
                    y + 20,
                    arrow=tk.LAST,
                    width=2
                )

                self.canvas.create_line(
                    x + node_width + gap,
                    y + 40,
                    x + node_width,
                    y + 40,
                    arrow=tk.LAST,
                    width=2
                )

            x += node_width + gap

            
            if x > 820:
                break


root = tk.Tk()

app = DoublyLinkedListGUI(root)

root.mainloop()
