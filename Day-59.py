## 66.RED_BLACK TREE
class Node:
    def __init__(self, key, color, parent, left=None, right=None):
        self.key = key
        self.color = color  # "R" for red, "B" for black
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None, "B", None)
        self.root = self.NIL_LEAF

    def insert(self, key):
        new_node = Node(key, "R", None, self.NIL_LEAF, self.NIL_LEAF)
        if self.root == self.NIL_LEAF:
            self.root = new_node
            self.root.color = "B"
        else:
            parent, node = self._find_parent(self.root, key)
            if key == node.key:
                return  # Key already exists
            new_node.parent = parent
            if key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node
            self._insert_fixup(new_node)

    def _find_parent(self, node, key):
        if key < node.key:
            if node.left != self.NIL_LEAF:
                return self._find_parent(node.left, key)
        else:
            if node.right != self.NIL_LEAF:
                return self._find_parent(node.right, key)
        return node, self.NIL_LEAF

    def _insert_fixup(self, node):
        while node.parent.color == "R":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "R":
                    node.parent.color = "B"
                    uncle.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "R":
                    node.parent.color = "B"
                    uncle.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    self._left_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = "B"

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def inorder_traversal(self, node):
        if node != self.NIL_LEAF:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node == self.NIL_LEAF:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)


# Example usage:
if __name__ == "__main__":
    tree = RedBlackTree()
    keys = [10, 5, 20, 2, 6, 15, 25]

   
