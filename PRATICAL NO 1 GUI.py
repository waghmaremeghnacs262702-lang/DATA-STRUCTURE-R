
import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks


class StudentADT:
    def __init__(self):
        self.students = []

    def create(self, roll, name, marks):
        for student in self.students:
            if student.roll_no == roll:
                return False

        self.students.append(Student(roll, name, marks))
        return True

    def update(self, roll, name, marks):
        for student in self.students:
            if student.roll_no == roll:
                student.name = name
                student.marks = marks
                return True

        return False

    def delete(self, roll):
        for student in self.students:
            if student.roll_no == roll:
                self.students.remove(student)
                return True

        return False

adt = StudentADT()

def create_student():

    roll_text = entry_roll.get().strip()
    name = entry_name.get().strip()
    marks_text = entry_marks.get().strip()

    if roll_text == "":
        messagebox.showerror("Error", "Please enter Roll No")
        return

    if name == "":
        messagebox.showerror("Error", "Please enter Name")
        return

    if marks_text == "":
        messagebox.showerror("Error", "Please enter Marks")
        return

    try:
        roll = int(roll_text)
        marks = float(marks_text)

        if marks < 0 or marks > 100:
            messagebox.showerror("Error", "Marks must be between 0 and 100")
            return

    except ValueError:
        messagebox.showerror(
            "Error",
            "Roll No must be an integer and Marks must be a number"
        )
        return

    if adt.create(roll, name, marks):
        messagebox.showinfo("Success", "Student created successfully!")
        display_students()
        clear_entries()
    else:
        messagebox.showerror("Error", "Roll No already exists")


def display_students():

    listbox.delete(0, tk.END)

    if len(adt.students) == 0:
        listbox.insert(tk.END, "No students found.")
        return

    for student in adt.students:
        data = (
            f"Roll No: {student.roll_no}    "
            f"Name: {student.name}    "
            f"Marks: {student.marks}"
        )

        listbox.insert(tk.END, data)
        
def update_student():

    roll_text = entry_roll.get().strip()
    name = entry_name.get().strip()
    marks_text = entry_marks.get().strip()

    if roll_text == "":
        messagebox.showerror("Error", "Please enter Roll No")
        return

    if name == "":
        messagebox.showerror("Error", "Please enter Name")
        return

    if marks_text == "":
        messagebox.showerror("Error", "Please enter Marks")
        return

    try:
        roll = int(roll_text)
        marks = float(marks_text)

        if marks < 0 or marks > 100:
            messagebox.showerror("Error", "Marks must be between 0 and 100")
            return

    except ValueError:
        messagebox.showerror("Error", "Enter valid data")
        return

    if adt.update(roll, name, marks):
        messagebox.showinfo("Success", "Student updated successfully!")
        display_students()
        clear_entries()
    else:
        messagebox.showerror("Error", "Student not found")


def delete_student():

    roll_text = entry_roll.get().strip()

    if roll_text == "":
        messagebox.showerror("Error", "Please enter Roll No")
        return

    try:
        roll = int(roll_text)
    except ValueError:
        messagebox.showerror("Error", "Roll No must be a number")
        return

    if adt.delete(roll):
        messagebox.showinfo("Success", "Student deleted successfully!")
        display_students()
        clear_entries()
    else:
        messagebox.showerror("Error", "Student not found")


def clear_entries():
    entry_roll.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_marks.delete(0, tk.END)



root = tk.Tk()
root.title("Student ADT")
root.geometry("550x600")

title = tk.Label(
    root,
    text="STUDENT ADT MANAGEMENT",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)


tk.Label(
    root,
    text="Roll No:",
    font=("Arial", 12)
).pack()

entry_roll = tk.Entry(
    root,
    width=25,
    font=("Arial", 12)
)
entry_roll.pack(pady=5)


tk.Label(
    root,
    text="Name:",
    font=("Arial", 12)
).pack()

entry_name = tk.Entry(
    root,
    width=25,
    font=("Arial", 12)
)
entry_name.pack(pady=5)


tk.Label(
    root,
    text="Marks:",
    font=("Arial", 12)
).pack()

entry_marks = tk.Entry(
    root,
    width=25,
    font=("Arial", 12)
)
entry_marks.pack(pady=5)


tk.Button(
    root,
    text="Create",
    width=20,
    command=create_student
).pack(pady=5)

tk.Button(
    root,
    text="Update",
    width=20,
    command=update_student
).pack(pady=5)

tk.Button(
    root,
    text="Delete",
    width=20,
    command=delete_student
).pack(pady=5)

tk.Button(
    root,
    text="Display",
    width=20,
    command=display_students
).pack(pady=5)


listbox = tk.Listbox(
    root,
    width=65,
    height=10,
    font=("Arial", 10)
)
listbox.pack(pady=20)


root.mainloop()
       
