class Node:
    def __init__(self, value):
        self.value = value  # Store the node's value
        self.next = None    # Reference to the next node, initially None

class StackUsingLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None (empty stack)
        self.count = 0    # Keep track of the number of elements in the stack

    def push(self, item):
        new_node = Node(item)    # Create a new node with the given item
        new_node.next = self.head  # Set the new node's next to the current head
        self.head = new_node     # Update the head to be the new node
        self.count += 1          # Increment the count of elements
        # Time complexity: O(1)

    def pop(self):
        if not self.is_empty():
            removed_node = self.head  # Store the current head node
            self.head = self.head.next  # Update the head to the next node
            self.count -= 1  # Decrement the count of elements
            return removed_node.value  # Return the value of the removed node
        return None  # Return None if the stack is empty
        # Time complexity: O(1)

    def peek(self):
        if not self.is_empty():
            return self.head.value  # Return the value of the head node without removing it
        return None  # Return None if the stack is empty
        # Time complexity: O(1)

    def is_empty(self):
        return self.head is None  # Stack is empty if there's no head node
        # Time complexity: O(1)

    def size(self):
        return self.count  # Return the count of elements
        # Time complexity: O(1)