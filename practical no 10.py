# Basic Hash Table
SIZE = 10

hash_table = [None] * SIZE


# Insert an element
def insert(key):
    index = key % SIZE

    if hash_table[index] is None:
        hash_table[index] = key
        print(key, "inserted at index", index)
    else:
        print("Index", index, "is already occupied.")


# Delete an element
def delete(key):
    index = key % SIZE

    if hash_table[index] == key:
        hash_table[index] = None
        print(key, "deleted successfully.")
    else:
        print(key, "not found.")


# Traverse the hash table
def traverse():
    print("\nHash Table:")

    for i in range(SIZE):
        if hash_table[i] is not None:
            print("Index", i, ":", hash_table[i])
        else:
            print("Index", i, ": Empty")


# Main program
while True:
    print("\n--- Hash Table Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Traverse")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        insert(key)

    elif choice == 2:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 3:
        traverse()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
