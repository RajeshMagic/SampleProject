# ================================================================
# PYTHON BINARY TREES - DEMONSTRATION
# ================================================================

print("\n==============================")
print("   BINARY TREES IN PYTHON")
print("==============================\n")

print("🔹 A Binary Tree is a hierarchical data structure where each node has max two children.")
print("🔹 It is widely used in searching, sorting, expression evaluation, and hierarchical storage.\n")

# ================================================================
# IMPLEMENTING A BINARY TREE
# ================================================================
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Build sample tree
root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

# Linking nodes
root.left = nodeA
root.right = nodeB
nodeA.left = nodeC
nodeA.right = nodeD
nodeB.left = nodeE
nodeB.right = nodeF
nodeF.left = nodeG

print("=== Binary Tree Example (Manual Construction) ===")
print("Root Node:", root.data)
print("Left Child of Root:", root.left.data)
print("Right Child of Root:", root.right.data)
print("Test: root.right.left.data =", root.right.left.data, "\n")

print("--- Important Note ---")
print("Each node has references to LEFT and RIGHT child nodes.")
print("This tree looks like:\n")
print("            R")
print("          /   \\")
print("         A     B")
print("        / \\   / \\")
print("       C   D E   F")
print("                /")
print("               G\n")

# ================================================================
# TREE TRAVERSALS (DFS and BFS)
# ================================================================

# Pre-order Traversal (Root → Left → Right)
def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=" ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

# In-order Traversal (Left → Root → Right)
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=" ")
    inOrderTraversal(node.right)

# Post-order Traversal (Left → Right → Root)
def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=" ")

# Breadth-First Search (Level Order)
from collections import deque
def bfsTraversal(node):
    if not node:
        return
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        print(curr.data, end=" ")
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

print("=== Traversals ===")
print("Pre-order Traversal  (DFS): ", end="")
preOrderTraversal(root)
print()

print("In-order Traversal   (DFS): ", end="")
inOrderTraversal(root)
print()

print("Post-order Traversal (DFS): ", end="")
postOrderTraversal(root)
print()

print("Breadth First Search (BFS): ", end="")
bfsTraversal(root)
print("\n")

print("--- Important Note ---")
print("✅ Pre-order: Root before children → Useful for copying tree, prefix expressions.")
print("✅ In-order: Left → Root → Right → Useful in BST for sorted order.")
print("✅ Post-order: Children before Root → Useful for deleting/freeing tree.")
print("✅ BFS: Visits level by level → Useful in shortest path problems.\n")

# ================================================================
# TYPES OF BINARY TREES (Conceptual Examples)
# ================================================================
print("=== Types of Binary Trees (Concepts) ===\n")

print("1. Balanced Binary Tree:")
print("   - Height difference between left & right subtree ≤ 1.")
print("   - Ensures efficiency in operations.\n")

print("2. Complete Binary Tree:")
print("   - All levels are full except possibly the last.")
print("   - Last level nodes are filled left to right.\n")

print("3. Full Binary Tree:")
print("   - Each node has 0 or 2 children.")
print("   - No node with only one child.\n")

print("4. Perfect Binary Tree:")
print("   - All internal nodes have exactly 2 children.")
print("   - All leaf nodes are on the same level.")
print("   - Also full, balanced, and complete.\n")

print("--- Important Note ---")
print("🌲 Binary Trees form the basis for advanced trees like BST, AVL, Heaps.")
print("🌲 Perfect & Complete trees are often represented efficiently using arrays.\n")

# ================================================================
# END OF DEMO
# ================================================================
print("🎯 Demo Complete: Binary Trees with Types & Traversals\n")
