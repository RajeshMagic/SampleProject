# ================================================================
# TREES IN PYTHON - DEMONSTRATION PROGRAM
# ================================================================

print("\n============================")
print(" TREES IN PYTHON ")
print("============================\n")

print("🔹 A Tree is a hierarchical data structure with nodes connected by edges.")
print("🔹 Unlike arrays and linked lists (linear structures), trees branch out.")
print("🔹 Applications: File systems, databases, routing, search, and priority queues.\n")

# ================================================================
# BASIC TREE NODE
# ================================================================
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None   # left child
        self.right = None  # right child

# ================================================================
# BINARY TREE TRAVERSALS (DFS: Preorder, Inorder, Postorder)
# ================================================================
def preorder(root):
    return [] if not root else [root.value] + preorder(root.left) + preorder(root.right)

def inorder(root):
    return [] if not root else inorder(root.left) + [root.value] + inorder(root.right)

def postorder(root):
    return [] if not root else postorder(root.left) + postorder(root.right) + [root.value]

print("=== Binary Tree Example ===")
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.left = TreeNode("F")
root.right.right = TreeNode("G")

print("Preorder Traversal  (Root → Left → Right):", preorder(root))
print("Inorder Traversal   (Left → Root → Right):", inorder(root))
print("Postorder Traversal (Left → Right → Root):", postorder(root), "\n")

print("--- Important Note ---")
print("Traversal is the foundation of working with trees. Preorder is used for copying trees,")
print("Inorder is used in BSTs to get sorted order, Postorder is used for deletion.\n")

# ================================================================
# BINARY SEARCH TREE (BST)
# ================================================================
class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return TreeNode(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

    def inorder_traversal(self, root):
        return inorder(root)

    def search(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self.search(root.left, value)
        return self.search(root.right, value)

print("=== Binary Search Tree (BST) ===")
bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    bst.root = bst.insert(bst.root, v)

print("Inorder Traversal (Sorted):", bst.inorder_traversal(bst.root))
print("Search 40 → Found?", bst.search(bst.root, 40) is not None)
print("Search 90 → Found?", bst.search(bst.root, 90) is not None, "\n")

print("--- Important Note ---")
print("✅ BST property: Left < Root < Right.")
print("✅ Inorder traversal of BST gives sorted output.")
print("✅ Search, Insert, Delete operations are O(log n) on average.\n")

# ================================================================
# AVL TREE (SELF-BALANCING BINARY SEARCH TREE)
# ================================================================
class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # track height for balancing

class AVLTree:
    def insert(self, root, value):
        # 1. Normal BST insertion
        if not root:
            return AVLNode(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # 2. Update height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # 3. Get balance factor
        balance = self.getBalance(root)

        # 4. Balance the tree with rotations
        # Left Left Case
        if balance > 1 and value < root.left.value:
            return self.rightRotate(root)
        # Right Right Case
        if balance < -1 and value > root.right.value:
            return self.leftRotate(root)
        # Left Right Case
        if balance > 1 and value > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Right Left Case
        if balance < -1 and value < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        return 0 if not root else root.height

    def getBalance(self, root):
        return 0 if not root else self.getHeight(root.left) - self.getHeight(root.right)

    def inorder(self, root):
        return [] if not root else self.inorder(root.left) + [root.value] + self.inorder(root.right)

print("=== AVL Tree (Self-Balancing BST) ===")
avl = AVLTree()
root_avl = None
nums = [10, 20, 30, 40, 50, 25]
for n in nums:
    root_avl = avl.insert(root_avl, n)

print("Inorder Traversal of AVL Tree:", avl.inorder(root_avl), "\n")

print("--- Important Note ---")
print("✅ AVL Tree is a self-balancing BST.")
print("✅ Height difference (balance factor) between left and right is max 1.")
print("✅ Provides guaranteed O(log n) for search, insert, delete.")
print("✅ Uses rotations (LL, RR, LR, RL) to maintain balance.\n")

# ================================================================
# COMPARISON WITH ARRAYS & LINKED LISTS
# ================================================================
print("=== Trees vs Arrays & Linked Lists ===")
print("""
Arrays:
- Fast random access (O(1)).
- Slow insertion/deletion (need shifting).

Linked Lists:
- Fast insertion/deletion (O(1)).
- Slow search (O(n)).

Trees (BST / AVL):
- Fast search, insert, delete (O(log n)).
- Flexible for hierarchical data.
""")

# ================================================================
# END OF DEMO
# ================================================================
print("\n🎯 Demo Complete: Trees in Python (Binary Tree, BST, AVL Tree)\n")
