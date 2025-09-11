# ================================================================
# PYTHON DEMO: AVL Trees (Self-Balancing Binary Search Tree)
# ================================================================
# AVL Tree = A Binary Search Tree that keeps itself balanced
# Invented in 1962 by Adelson-Velsky and Landis
#
# Key Concepts:
#  - Balance Factor = height(left subtree) - height(right subtree)
#  - If balance factor < -1 or > 1 → tree is unbalanced
#  - To fix imbalance, we perform rotations: LL, RR, LR, RL
#  - Time Complexity: O(log n) for search, insert, delete
# ================================================================

class TreeNode:
    """Node class for AVL Tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Default height when node created


# ==============================
# Utility Functions
# ==============================
def getHeight(node):
    """Return height of a node"""
    if not node:
        return 0
    return node.height

def getBalance(node):
    """Balance factor = height(left) - height(right)"""
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)


# ==============================
# Rotations
# ==============================
def rightRotate(y):
    """Right rotation (LL case fix)"""
    print(f"\n➡️ Performing RIGHT rotation on node [{y.data}] (LL case)")
    x = y.left
    T2 = x.right

    # Rotate
    x.right = y
    y.left = T2

    # Update heights
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))

    return x

def leftRotate(x):
    """Left rotation (RR case fix)"""
    print(f"\n➡️ Performing LEFT rotation on node [{x.data}] (RR case)")
    y = x.right
    T2 = y.left

    # Rotate
    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y


# ==============================
# Insert Function
# ==============================
def insert(node, data):
    """Insert a node into AVL Tree and balance it"""
    if not node:
        print(f"✅ Inserted [{data}] as a new leaf node.")
        return TreeNode(data)

    if data < node.data:
        print(f"Inserting [{data}] to LEFT of node [{node.data}]")
        node.left = insert(node.left, data)
    elif data > node.data:
        print(f"Inserting [{data}] to RIGHT of node [{node.data}]")
        node.right = insert(node.right, data)
    else:
        print(f"⚠️ Duplicate value [{data}] ignored (AVL only supports unique values)")
        return node

    # Update height
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))

    # Get balance factor
    balance = getBalance(node)
    print(f"Node [{node.data}] → Balance Factor = {balance}")

    # ==============================
    # Check Four Imbalance Cases
    # ==============================
    # Left Left (LL)
    if balance > 1 and data < node.left.data:
        return rightRotate(node)

    # Right Right (RR)
    if balance < -1 and data > node.right.data:
        return leftRotate(node)

    # Left Right (LR)
    if balance > 1 and data > node.left.data:
        print("\n➡️ Detected Left-Right (LR) case")
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # Right Left (RL)
    if balance < -1 and data < node.right.data:
        print("\n➡️ Detected Right-Left (RL) case")
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node


# ==============================
# Deletion Functions
# ==============================
def minValueNode(node):
    """Find inorder successor (smallest node in right subtree)"""
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, data):
    """Delete a node from AVL Tree"""
    if not node:
        return node

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        print(f"\n🗑️ Deleting node [{data}]")
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)

    if node is None:
        return node

    # Update height
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Balance cases
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node


# ==============================
# Traversal Functions
# ==============================
def inOrderTraversal(node):
    """InOrder Traversal (sorted order)"""
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=" ")
    inOrderTraversal(node.right)

def preOrderTraversal(node):
    """PreOrder Traversal (Root, Left, Right)"""
    if node is None:
        return
    print(node.data, end=" ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


# ==============================
# DEMONSTRATION
# ==============================
if __name__ == "__main__":
    print("\n==============================")
    print(" DEMO: AVL Tree in Python ")
    print("==============================\n")

    root = None
    letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']

    print("🔹 Inserting nodes to build AVL Tree...\n")
    for letter in letters:
        root = insert(root, letter)

    print("\n✅ InOrder Traversal (sorted):")
    inOrderTraversal(root)
    print("\n\n✅ PreOrder Traversal (shows tree structure):")
    preOrderTraversal(root)
    print("\n")

    print("\n==============================")
    print(" DEMO: Deletion in AVL Tree ")
    print("==============================\n")

    root = delete(root, 'H')   # Delete a node with children
    root = delete(root, 'C')   # Delete root node

    print("\n✅ InOrder Traversal after deletion:")
    inOrderTraversal(root)
    print("\n\n✅ PreOrder Traversal after deletion:")
    preOrderTraversal(root)
    print("\n")

    print("\n==============================")
    print(" IMPORTANT NOTES ")
    print("==============================")
    print("1. AVL Trees are always balanced (balance factor ∈ {-1,0,1}).")
    print("2. Operations (insert, delete, search) run in O(log n).")
    print("3. Four imbalance cases: LL, RR, LR, RL → fixed by rotations.")
    print("4. Compared to unbalanced BST (O(n)), AVL is much faster for large data.")
    print("5. Rotations maintain BST property + sorted InOrder traversal.\n")
