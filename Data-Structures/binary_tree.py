class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(val)
                return
            elif not node.right:
                node.right = TreeNode(val)
                return
            else:
                queue.append(node.left)
                queue.append(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))


if __name__ == "__main__":
    bt = BinaryTree()
    for val in [10, 20, 30, 40, 50, 60]:
        bt.insert(val)
    print("Inorder:", end=" ")
    bt.inorder(bt.root)
    print("\nPreorder:", end=" ")
    bt.preorder(bt.root)
    print("\nPostorder:", end=" ")
    bt.postorder(bt.root)
    print(f"\nHeight: {bt.height(bt.root)}")
