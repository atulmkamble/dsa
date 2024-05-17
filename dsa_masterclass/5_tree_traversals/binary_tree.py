class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def preorder(self, start, traversal_list):
        if start is None:
            return
        traversal_list.append(start.value)
        self.preorder(start.left, traversal_list)
        self.preorder(start.right, traversal_list)
        return traversal_list

    def inorder(self, start, traversal_list):
        if start is None:
            return
        self.inorder(start.left, traversal_list)
        traversal_list.append(start.value)
        self.inorder(start.right, traversal_list)
        return traversal_list

    def postorder(self, start, traversal_list):
        if start is None:
            return
        self.postorder(start.left, traversal_list)
        self.postorder(start.right, traversal_list)
        traversal_list.append(start.value)
        return traversal_list


def main():
    tree = BinaryTree(3)

    tree.root.left = Node(4)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(7)

    tree.root.right = Node(5)
    tree.root.right.left = Node(8)
    tree.root.right.right = Node(9)

    print('Root Node          :', tree.root.value)
    print('Preorder Traversal :', tree.preorder(tree.root, []))
    print('Inorder Traversal  :', tree.inorder(tree.root, []))
    print('Postorder Traversal:', tree.postorder(tree.root, []))


if __name__ == '__main__':
    main()
