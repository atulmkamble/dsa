class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent_list = []
        self.visited = False


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


class Graph:
    @staticmethod
    def breadth_first_search(node):
        queue = Queue()
        queue.enqueue(node)
        node.visited = True
        traversal_list = []

        while len(queue.items) > 0:
            traversal_list.append(queue.peek())
            current_node = queue.dequeue()

            for adjacent_node in current_node.adjacent_list:
                if adjacent_node.visited is False:
                    queue.enqueue(adjacent_node)
                    adjacent_node.visited = True

        return traversal_list


def main():
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')
    node6 = Node('F')
    node7 = Node('G')

    # A is connected to B, C and D
    node1.adjacent_list.append(node2)
    node1.adjacent_list.append(node3)
    node1.adjacent_list.append(node4)
    # B is connected to E and F
    node2.adjacent_list.append(node5)
    node2.adjacent_list.append(node6)
    # D is connected to G
    node4.adjacent_list.append(node7)
    # C is connected to A
    node3.adjacent_list.append(node1)

    graph = Graph()
    print(f"BFS Traversal: {graph.breadth_first_search(node1)}")


if __name__ == '__main__':
    main()
