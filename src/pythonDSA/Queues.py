# ============================================
# QUEUES IN PYTHON - DEMONSTRATION PROGRAM
# ============================================

print("\n============================")
print(" QUEUES IN PYTHON (FIFO) ")
print("============================\n")
print("A Queue follows FIFO principle: First In, First Out.\n")
print("Think of a queue as people standing in line in a supermarket.\n")

# -------------------------------------------------
# 1. Queue using Python List
# -------------------------------------------------
print("1️⃣ Queue Implementation using Python List\n")

queue = []

# Enqueue (append adds to the rear)
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after Enqueue (A, B, C):", queue)

# Peek
frontElement = queue[0]
print("Peek (Front element):", frontElement)

# Dequeue
poppedElement = queue.pop(0)
print("Dequeue (removed element):", poppedElement)
print("Queue after Dequeue:", queue)

# isEmpty
isEmpty = not bool(queue)
print("Is queue empty?", isEmpty)

# Size
print("Size of queue:", len(queue))

print("\n--- Important Note ---")
print("✅ Python lists make it simple to implement queues.")
print("❌ BUT dequeue (pop(0)) is inefficient since it shifts all remaining elements.")
print("❌ Not recommended for large queues.\n")


# -------------------------------------------------
# 2. Queue using Class with List internally
# -------------------------------------------------
print("2️⃣ Queue Implementation using Class (with List inside)\n")

class QueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Demo
myQueue = QueueList()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue after Enqueue:", myQueue.queue)
print("Peek:", myQueue.peek())
print("Dequeue:", myQueue.dequeue())
print("Queue after Dequeue:", myQueue.queue)
print("isEmpty:", myQueue.isEmpty())
print("Size:", myQueue.size())

print("\n--- Important Note ---")
print("✅ Using a class gives better design & encapsulation.")
print("✅ Easy to extend for queue-related functions.\n")


# -------------------------------------------------
# 3. Queue using Linked List
# -------------------------------------------------
print("3️⃣ Queue Implementation using Linked List\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:  # empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:  # queue became empty
            self.rear = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Demo
myLLQueue = LinkedListQueue()
myLLQueue.enqueue('A')
myLLQueue.enqueue('B')
myLLQueue.enqueue('C')

print("Queue represented as Linked List:")
myLLQueue.printQueue()

print("Peek:", myLLQueue.peek())
print("Dequeue:", myLLQueue.dequeue())
print("Queue after Dequeue:", end=" ")
myLLQueue.printQueue()
print("isEmpty:", myLLQueue.isEmpty())
print("Size:", myLLQueue.size())

print("\n--- Important Note ---")
print("✅ Linked List avoids shifting problem → Dequeue is efficient (O(1)).")
print("✅ Queue can grow/shrink dynamically.")
print("❌ Requires extra memory for pointers & longer implementation.\n")


# -------------------------------------------------
# 4. Common Applications of Queues
# -------------------------------------------------
print("4️⃣ Common Applications of Queues\n")
print("🔹 Task scheduling in operating systems")
print("🔹 Breadth-First Search (BFS) in graphs")
print("🔹 Message queues in distributed systems")
print("🔹 Job scheduling in printers / order processing\n")


# -------------------------------------------------
# END OF DEMO
# -------------------------------------------------
print("🎯 Demo Complete: Queues with Python (List, Class, Linked List)\n")
