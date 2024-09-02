class StackUsingList:
    def __init__(self):
        self.stack = []  # Initialize an empty list to store stack elements

    def push(self, item):
        self.stack.append(item)  # Add the item to the end of the list (top of the stack)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the last item (top of the stack)
        return None  # Return None if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Return the last item without removing it
        return None  # Return None if the stack is empty

    def is_empty(self):
        return len(self.stack) == 0  # Check if the stack is empty

    def size(self):
        return len(self.stack)  # Return the number of elements in the stack