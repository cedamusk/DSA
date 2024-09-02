class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store stack items

    def push(self, item):
        self.items.append(item)  # Add item to the top of the stack (end of the list)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the top item
        return None  # Return None if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top item without removing it
        return None  # Return None if the stack is empty

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack has no items

    def size(self):
        return len(self.items)  # Return the number of items in the stack

# Initialize stack to manage seismic events
# Using a stack ensures we process the most recent events first (Last-In-First-Out)
seismic_stack = Stack()

# Recording seismic events
# Each event is represented as a string with magnitude and location information
seismic_stack.push("Event 1: Magnitude 4.2 - Location A")
seismic_stack.push("Event 2: Magnitude 5.1 - Location B")
seismic_stack.push("Event 3: Magnitude 6.3 - Location C")

# Analyzing the most recent seismic event
# The peek() method allows us to see the latest event without removing it from the stack
print(f"Most recent event: {seismic_stack.peek()}")  # Output: Event 3: Magnitude 6.3 - Location C

# Removing the analyzed event
# Once an event is analyzed, we can remove it from the stack using pop()
analyzed_event = seismic_stack.pop()
print(f"Analyzed event: {analyzed_event}")  # Output: Event 3: Magnitude 6.3 - Location C

# Checking the remaining events
# The size() method gives us a quick count of unanalyzed events
print(f"Number of remaining events: {seismic_stack.size()}")  # Output: 2

# Checking if there are any events left to analyze
# The is_empty() method helps us determine if we've processed all events
print(f"Are there any events left? {not seismic_stack.is_empty()}")  # Output: True