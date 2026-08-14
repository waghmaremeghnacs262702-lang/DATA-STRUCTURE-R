class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid position")

        self.items.insert(position, item)
        print("'" + item + "' inserted successfully.")

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid position")

        item = self.items.pop(position)
        print("'" + item + "' deleted successfully.")
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.items[-1]

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return " <- ".join(self.items)

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"

        return " <- ".join(reversed(self.items))


def stack_operations():

    stack = Stack()

    print("====================================")
    print("   INTERACTIVE STACK OPERATIONS")
    print("====================================")

    while True:

        print("\nCurrent Stack:", stack)
        print("1. Insert an item")
        print("2. Delete an item")
        print("3. Peek at the top item")
        print("4. Check if the stack is empty")
        print("5. Get the size of the stack")
        print("6. Traverse the stack")
        print("7. Quit")

        try:
            choice = int(input("Choose an operation (1-7): "))

        except ValueError:
            print("Please enter a number from 1 to 7.")
            continue

        
        if choice == 1:

            item = input("Enter an item to insert: ")

            try:
                position = int(
                    input("Enter position (0-based index): ")
                )

                stack.insert(item, position)

            except ValueError:
                print("Position must be an integer.")

            except IndexError as e:
                print(e)

        
        elif choice == 2:

            try:
                position = int(
                    input("Enter position to delete (0-based index): ")
                )

                stack.delete(position)

            except ValueError:
                print("Position must be an integer.")

            except IndexError as e:
                print(e)

       
        elif choice == 3:

            try:
                print("Top item:", stack.peek())

            except IndexError as e:
                print(e)

       
        elif choice == 4:

            if stack.is_empty():
                print("Is the stack empty? Yes")
            else:
                print("Is the stack empty? No")

        
        elif choice == 5:

            print("Size of the stack:", stack.size())

        
        elif choice == 6:

            try:
                print("Stack contents:", stack.traverse())

            except IndexError as e:
                print(e)

       
        elif choice == 7:

            print("Exiting the program. Goodbye!")
            break

        else:

            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    stack_operations()
