class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent_list = []
        self.visited = False


class Graph:
    def depth_first_search(self, node, traversal_list):
        if node is None:
            return
        node.visited = True
        traversal_list.append(node.value)
        for adjacent_node in node.adjacent_list:
            if adjacent_node.visited is False:
                self.depth_first_search(adjacent_node, traversal_list)
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
    print(f"DFS Traversal: {graph.depth_first_search(node1, [])}")


if __name__ == '__main__':
    main()
