import time
from colorama import init, Fore, Style

init(autoreset=True)


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
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

   
    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Position cannot be negative.")

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

    
    def delete_node_at_beginning(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

   
    def delete_node_at_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.prev.next = None

   
    def delete_node_at_position(self, position):
        if position < 0:
            raise IndexError("Position cannot be negative.")

        if self.head is None:
            raise IndexError("List is empty.")

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

    
    def display_list(self):
        temp = self.head

        if temp is None:
            print(Fore.RED + "Doubly Linked List is empty.")
            return

        print(Fore.GREEN + "Doubly Linked List:")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

   
    def search_node(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

   
    def length_of_list(self):
        temp = self.head
        length = 0

        while temp:
            length += 1
            temp = temp.next

        return length



def display_menu():
    print("\n" + Style.BRIGHT + "===== Doubly Linked List Operations =====")
    print("1. " + Fore.BLUE + "Insert at beginning")
    print("2. " + Fore.BLUE + "Insert at end")
    print("3. " + Fore.BLUE + "Insert at position")
    print("4. " + Fore.BLUE + "Delete node at beginning")
    print("5. " + Fore.BLUE + "Delete node at end")
    print("6. " + Fore.BLUE + "Delete node at position")
    print("7. " + Fore.BLUE + "Display the list")
    print("8. " + Fore.BLUE + "Search for a node")
    print("9. " + Fore.BLUE + "Length of the list")
    print("10. " + Fore.RED + "Exit")



def main():
    linked_list = DoublyLinkedList()

    while True:
        display_menu()

        try:
            choice = int(input(Style.RESET_ALL + "\nEnter your choice: "))

           
            if choice == 1:
                data = int(input("Enter data to insert at beginning: "))
                linked_list.insert_at_beginning(data)
                print(Fore.GREEN + "Node inserted at beginning.")

           
            elif choice == 2:
                data = int(input("Enter data to insert at end: "))
                linked_list.insert_at_end(data)
                print(Fore.GREEN + "Node inserted at end.")

           
            elif choice == 3:
                data = int(input("Enter data to insert: "))
                position = int(
                    input("Enter position to insert (0-indexed): ")
                )

                linked_list.insert_at_position(data, position)

                print(
                    Fore.GREEN
                    + f"Node inserted at position {position}."
                )

            
            elif choice == 4:
                linked_list.delete_node_at_beginning()
                print(Fore.RED + "Node deleted at beginning.")

           
            elif choice == 5:
                linked_list.delete_node_at_end()
                print(Fore.RED + "Node deleted at end.")

           
            elif choice == 6:
                position = int(
                    input("Enter index of the node to delete: ")
                )

                linked_list.delete_node_at_position(position)

                print(
                    Fore.RED
                    + f"Node at index {position} deleted."
                )

            
            elif choice == 7:
                linked_list.display_list()

            
            elif choice == 8:
                data = int(input("Enter data to search: "))

                if linked_list.search_node(data):
                    print(Fore.GREEN + "Node found.")
                else:
                    print(Fore.RED + "Node not found.")

            
            elif choice == 9:
                print(
                    Fore.BLUE
                    + f"Length of the list: "
                    f"{linked_list.length_of_list()}"
                )

            
            elif choice == 10:
                print(Style.RESET_ALL + "Exiting...")
                break

            else:
                print(
                    Fore.YELLOW
                    + "Invalid choice. Please enter a valid option."
                )

        except ValueError:
            print(
                Fore.YELLOW
                + "Error: Please enter a valid integer."
            )

        except IndexError as e:
            print(Fore.RED + f"Error: {e}")

        except Exception as e:
            print(Fore.RED + f"Error: {e}")

        time.sleep(1)


if __name__ == "__main__":
    main()
