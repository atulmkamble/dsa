class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def peek(self):
        if len(self.items) > 0:
            return self.items[0].value


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    @staticmethod
    def levelorder(start):
        queue = Queue()
        queue.enqueue(start)
        traversal_list = []

        while len(queue.items) > 0:
            traversal_list.append(queue.peek())
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal_list


def main():
    tree = BinaryTree(3)

    tree.root.left = Node(4)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(7)

    tree.root.right = Node(5)
    tree.root.right.left = Node(8)
    tree.root.right.right = Node(9)

    print('Root Node     :', tree.root.value)
    print('BFS Traversal :', tree.levelorder(tree.root))


if __name__ == '__main__':
    main()
