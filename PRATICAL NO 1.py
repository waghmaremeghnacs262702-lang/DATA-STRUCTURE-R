

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")


class StudentADT:
    def __init__(self):
        self.students = []

    def create(self):
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = Student(roll, name, marks)
        self.students.append(student)
        print("Student created successfully!")

    def display(self):
        if not self.students:
            print("No students found.")
        else:
            print("\n--- Student Details ---")
            for student in self.students:
                student.display()

    
    def update(self):
        roll = int(input("Enter Roll No to update: "))

        for student in self.students:
            if student.roll_no == roll:
                student.name = input("Enter New Name: ")
                student.marks = float(input("Enter New Marks: "))
                print("Student updated successfully!")
                return

        print("Student not found.")

    def delete(self):
        roll = int(input("Enter Roll No to delete: "))

        for student in self.students:
            if student.roll_no == roll:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found.")


adt = StudentADT()

while True:
    print("\n===== STUDENT ADT =====")
    print("1. Create Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        adt.create()
    elif choice == "2":
        adt.display()
    elif choice == "3":
        adt.update()
    elif choice == "4":
        adt.delete()
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice!")
