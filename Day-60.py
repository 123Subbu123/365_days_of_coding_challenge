## 67.Binary Search Tree.
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_recursively(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursively(root.right, key)
        return root

    def delete(self, key):
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_recursively(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._min_value(root.right)
            root.right = self._delete_recursively(root.right, root.key)
        return root

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, root, key):
        if root is None or root.key == key:
            return root
        if root.key < key:
            return self._search_recursively(root.right, key)
        return self._search_recursively(root.left, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)

# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("In-order traversal:", bst.inorder_traversal())

    bst.delete(30)
    print("In-order traversal after deleting 30:", bst.inorder_traversal())

    key_to_search = 60
    result = bst.search(key_to_search)
    if result:
        print(f"Key {key_to_search} found in the tree.")
    else:
        print(f"Key {key_to_search} not found in the tree.")
