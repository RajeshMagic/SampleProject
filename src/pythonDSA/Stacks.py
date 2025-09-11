# ============================================
# STACKS IN PYTHON - DEMONSTRATION PROGRAM
# ============================================

print("\n============================")
print(" STACKS IN PYTHON (LIFO) ")
print("============================\n")
print("A stack follows LIFO principle: Last In, First Out.\n")

# -------------------------------------------------
# 1. Stack using Python List
# -------------------------------------------------
print("1️⃣ Stack Implementation using Python List\n")

stack = []

# Push (append)
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushes (A, B, C):", stack)

# Peek
topElement = stack[-1]
print("Peek (Top element):", topElement)

# Pop
poppedElement = stack.pop()
print("Pop element:", poppedElement)
print("Stack after Pop:", stack)

# isEmpty
isEmpty = not bool(stack)
print("Is stack empty?", isEmpty)

# Size
print("Size of stack:", len(stack))

print("\n--- Important Note ---")
print("✅ Python lists have built-in methods append() and pop() making them easy for stack operations.")
print("✅ But lists use contiguous memory blocks (array-like behavior).\n")


# -------------------------------------------------
# 2. Stack using Class with List internally
# -------------------------------------------------
print("2️⃣ Stack Implementation using Class (with List inside)\n")

class StackList:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Demo
myStack = StackList()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack after pushes:", myStack.stack)
print("Pop:", myStack.pop())
print("Stack after Pop:", myStack.stack)
print("Peek:", myStack.peek())
print("isEmpty:", myStack.isEmpty())
print("Size:", myStack.size())

print("\n--- Important Note ---")
print("✅ Using a class gives encapsulation (better design).")
print("✅ Easy to extend with extra stack-related functionality.\n")


# -------------------------------------------------
# 3. Stack using Linked List
# -------------------------------------------------
print("3️⃣ Stack Implementation using Linked List\n")

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print("None")

# Demo
myLLStack = LinkedListStack()
myLLStack.push('A')
myLLStack.push('B')
myLLStack.push('C')

print("Stack represented as Linked List:")
myLLStack.traverseAndPrint()

print("Peek:", myLLStack.peek())
print("Pop:", myLLStack.pop())
print("After Pop (Linked List stack):")
myLLStack.traverseAndPrint()
print("isEmpty:", myLLStack.isEmpty())
print("Size:", myLLStack.stackSize())

print("\n--- Important Note ---")
print("✅ Linked List allows dynamic memory usage (stack grows/shrinks easily).")
print("✅ No fixed size like arrays, but requires extra memory for 'next' pointers.")
print("✅ Implementation is longer and a bit harder to read.\n")


# -------------------------------------------------
# 4. Common Applications of Stacks
# -------------------------------------------------
print("4️⃣ Common Applications of Stacks\n")
print("🔹 Undo/Redo operations in text editors")
print("🔹 Browser history navigation (Back/Forward)")
print("🔹 Function call stack in programming languages")
print("🔹 Depth-First Search (DFS) in graphs")
print("🔹 Expression evaluation (infix to postfix conversion)\n")


# -------------------------------------------------
# END OF DEMO
# -------------------------------------------------
print("🎯 Demo Complete: Stacks with Python (List, Class, Linked List)\n")
