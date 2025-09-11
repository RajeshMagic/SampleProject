"""
Binary Search Trees (BST) in Python
-----------------------------------
This program demonstrates:
- BST properties
- Traversals (In-order, Pre-order, Post-order)
- Searching, Insertion, Deletion
- Finding Minimum Node
- Balanced vs Unbalanced BST Concept
"""

# -------------------------
# Define Tree Node
# -------------------------
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# -------------------------
# Traversal Methods
# -------------------------
def inOrderTraversal(node):
    """In-order Traversal (Left -> Root -> Right)"""
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=" ")
    inOrderTraversal(node.right)

def preOrderTraversal(node):
    """Pre-order Traversal (Root -> Left -> Right)"""
    if node is None:
        return
    print(node.data, end=" ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def postOrderTraversal(node):
    """Post-order Traversal (Left -> Right -> Root)"""
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=" ")


# -------------------------
# Search in BST
# -------------------------
def search(node, target):
    """Search for a value in BST"""
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)


# -------------------------
# Insert in BST
# -------------------------
def insert(node, data):
    """Insert a new value into BST"""
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node


# -------------------------
# Find Minimum Node
# -------------------------
def minValueNode(node):
    """Finds the node with the minimum value"""
    current = node
    while current.left is not None:
        current = current.left
    return current


# -------------------------
# Delete Node from BST
# -------------------------
def delete(node, data):
    """Deletes a node from BST"""
    if not node:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Case 1: Node has no child
        if not node.left and not node.right:
            return None
        # Case 2: Node with one child
        elif not node.left:
            return node.right
        elif not node.right:
            return node.left
        # Case 3: Node with two children
        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)
    return node


# -------------------------
# Demonstration
# -------------------------
if __name__ == "__main__":
    print("\n========== Binary Search Tree (BST) Demonstration ==========\n")

    # Create BST manually
    root = TreeNode(13)
    root.left = TreeNode(7)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(14)
    root.right.right = TreeNode(19)
    root.right.right.left = TreeNode(18)

    print("BST Created with Root = 13\n")
    print("Important Note: In a BST, left child < parent < right child.\n")

    # Traversals
    print("In-order Traversal (Sorted Order): ", end="")
    inOrderTraversal(root)
    print("\n")

    print("Pre-order Traversal (Root before Children): ", end="")
    preOrderTraversal(root)
    print("\n")

    print("Post-order Traversal (Root after Children): ", end="")
    postOrderTraversal(root)
    print("\n")

    # Search Example
    print("\nSearching for value 13 in BST...")
    result = search(root, 13)
    if result:
        print("✔ Found node with value:", result.data)
    else:
        print("✘ Value not found in BST")

    # Insert Example
    print("\nInserting new value 10 into BST...")
    insert(root, 10)
    print("In-order Traversal after insertion: ", end="")
    inOrderTraversal(root)
    print("\n")

    # Find Minimum Value
    print("Finding the minimum value in BST...")
    print("✔ Minimum Value is:", minValueNode(root).data, "\n")

    # Delete Example
    print("Deleting node 15 (has two children)...")
    root = delete(root, 15)
    print("In-order Traversal after deletion: ", end="")
    inOrderTraversal(root)
    print("\n")

    # Balanced vs Unbalanced Tree
    print("\n========== Important Notes ==========")
    print("1. BST operations like Search, Insert, Delete are O(h), where h = tree height.")
    print("2. Balanced BST => h ≈ log₂n, making operations efficient (O(log n)).")
    print("3. Unbalanced BST => h ≈ n, making operations slow (O(n)).")
    print("4. AVL Trees are self-balancing BSTs, ensuring minimum height.\n")

    print("✅ Demonstration Completed.\n")
