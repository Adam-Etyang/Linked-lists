class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head is None

    # insert at end
    def append(self, data):
        new_node = Node(data)

        if self.isempty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # insert at start
    def prepend(self, data):
        new_node = Node(data)
        if self.isempty():
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    # insert at index
    def insert_at_index(self, data, index):
        new_node = Node(data)

        if index < 0:
            print("Index must be a positive number")
            return

        if index == 0:
            self.prepend(data)
            return

        current = self.head
        position = 0

        while current and position < index - 1:
            current = current.next
            position += 1

        if not current:
            print(f"Index {index} out of bounds")
            return

        new_node.next = current.next
        current.next = new_node

    # deleting a value
    def delete_value(self, key):
        if not self.isempty() and self.head.data == key:
            self.head = self.head.next
            print(f"Deleted node with value {key}")
            return

        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Key {key} not found in the list")
            return

        prev.next = current.next
        print(f"Deleted node with value {key}")

    # delete at index
    def delete_at_index(self, index):
        if index < 0:
            print("Index cannot be negative")
            return

        if self.isempty():
            print("The list is empty, please insert elements")
            return

        if index == 0:
            deleted_value = self.head.data
            self.head = self.head.next
            print(f"Deleted node at index 0 with value {deleted_value}")
            return

        current = self.head
        position = 0
        while current and position < index - 1:
            current = current.next
            position += 1

        if not current or not current.next:
            print(f"Index {index} is out of bounds")
            return

        deleted_value = current.next.data
        current.next = current.next.next
        print(f"Deleted node at index {index} with value {deleted_value}")

    def search(self, key):
        current = self.head
        position = 0

        while current:
            if current.data == key:
                print(f"Found value {key} at position {position}")
                return True
            current = current.next
            position += 1

        print(f"Value {key} not found in the list")
        return False

    # display
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "List is empty")

    # get length (utility method)
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


def menu():
    print("\n===== Linked List Operations =====")
    print("1. Display list")
    print("2. Insert element at index")
    print("3. Append element to list")
    print("4. Prepend element to list")
    print("5. Delete element")
    print("6. Delete element at index")
    print("7. Search for element in list")
    print("8. Get list length")
    print("9. Exit")
    print("=================================")


def main():
    llist = LinkedList()
    while True:
        menu()
        try:
            choice = int(input("Enter your choice (1-9): "))

            if choice == 1:
                print("\nCurrent list:")
                llist.display()

            elif choice == 2:
                index = int(input("Enter index: "))
                data = int(input("Enter data: "))
                llist.insert_at_index(data, index)
                print(f"Inserted {data} at index {index}")

            elif choice == 3:
                data = int(input("Enter data: "))
                llist.append(data)
                print(f"Appended {data} to the list")

            elif choice == 4:
                data = int(input("Enter data: "))
                llist.prepend(data)
                print(f"Prepended {data} to the list")

            elif choice == 5:
                data = int(input("Enter data to delete: "))
                llist.delete_value(data)

            elif choice == 6:
                index = int(input("Enter index to delete: "))
                llist.delete_at_index(index)

            elif choice == 7:
                element = int(input("Enter value to search: "))
                llist.search(element)

            elif choice == 8:
                length = llist.length()
                print(f"List length: {length}")

            elif choice == 9:
                print("Exiting program. Goodbye!")
                break

            else:
                print("Please enter a valid choice (1-9)")

        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()

