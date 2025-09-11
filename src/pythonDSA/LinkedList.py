# ================================================================
# LINKED LISTS IN PYTHON - DEMONSTRATION PROGRAM
# ================================================================

print("\n============================")
print(" LINKED LISTS IN PYTHON ")
print("============================\n")

print("🔹 A Linked List is a linear data structure made up of nodes.\n"
      "🔹 Each node contains data and a pointer (reference) to the next node.\n"
      "🔹 Unlike arrays, nodes are not stored contiguously in memory.\n")

print("Comparison: Arrays vs Linked Lists")
print("""
Arrays:
 - Built-in data structure in Python
 - Fixed size in memory
 - Elements stored contiguously
 - Fast random access
 - Insertion/Deletion costly (shifting needed)

Linked Lists:
 - User-defined data structure
 - Dynamic size
 - Nodes stored anywhere in memory (linked by pointers)
 - Extra memory for links
 - No random access (must traverse)
 - Insertion/Deletion efficient (O(1) if position is known)
""")

# -------------------------------------------------
# 1. Define Node class (Singly Linked List Node)
# -------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# -------------------------------------------------
# 2. Traversal of Linked List
# -------------------------------------------------
def traverseAndPrint(head):
    print("Traversing Linked List:")
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


print("\n1️⃣ Traversal of Linked List:\n")
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)

print("\n--- Important Note ---")
print("✅ Traversal requires following pointers until we hit 'null'.")
print("❌ Unlike arrays, we cannot directly access node[3] without traversing.\n")


# -------------------------------------------------
# 3. Find Lowest Value in Linked List
# -------------------------------------------------
def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue


print("2️⃣ Find the Lowest Value:\n")
print("Linked List:")
traverseAndPrint(node1)
print("Lowest value in the linked list is:", findLowestValue(node1))

print("\n--- Important Note ---")
print("✅ Linear search (O(n)) required because no random access in linked lists.\n")


# -------------------------------------------------
# 4. Delete a Node in Linked List
# -------------------------------------------------
def deleteSpecificNode(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next  # move head to next node

    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head  # node not found

    currentNode.next = currentNode.next.next
    return head


print("3️⃣ Delete a Node:\n")
print("Before deletion:")
traverseAndPrint(node1)

node1 = deleteSpecificNode(node1, node4)  # delete node with value 2

print("\nAfter deletion (deleted value 2):")
traverseAndPrint(node1)

print("\n--- Important Note ---")
print("✅ Before deleting, adjust links to avoid breaking the chain.")
print("✅ Head may change if first node is deleted.\n")


# -------------------------------------------------
# 5. Insert a Node at a Given Position
# -------------------------------------------------
def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head


print("4️⃣ Insert a Node:\n")
print("Original list:")
traverseAndPrint(node1)

newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)  # insert at 2nd position

print("\nAfter insertion (97 at position 2):")
traverseAndPrint(node1)

print("\n--- Important Note ---")
print("✅ Insertion only requires pointer adjustment (O(1)) if position is known.")
print("❌ If we need to find the position, traversal makes it O(n).\n")


# -------------------------------------------------
# 6. Time Complexity Notes
# -------------------------------------------------
print("5️⃣ Time Complexity of Linked List Operations\n")
print("""
🔸 Traversal/Search: O(n)  (must check each node)
🔸 Insertion: 
    - At beginning: O(1)
    - At end (if tail pointer exists): O(1), else O(n)
    - At position: O(n) (due to traversal)
🔸 Deletion: O(1) if node is known, else O(n) to find node
🔸 Arrays allow O(1) random access, Linked Lists do not
""")


# -------------------------------------------------
# END OF DEMO
# -------------------------------------------------
print("\n🎯 Demo Complete: Linked Lists in Python (Traversal, Min, Insert, Delete)\n")
