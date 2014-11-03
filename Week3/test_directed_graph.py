class DirectedGraph:

    def __init__(self,):
        self.graph = {}
        self.nodes = ['a', 'b', 'c', 'd', 'e']

    def add_edge(self, node_a, node_b):
        self.graph[node_a, node_b] = True

    def create_graph(self):
        for node_1 in self.nodes:
            for node_2 in self.nodes:
                self.graph[node_1, node_2] = False

    def print_graph(self):
        print(self.graph)

    def get_neighbours_for(self, node):
        neighbours = []

        for node_1 in self.nodes:
            for node_2 in self.nodes:
                if (node_1 == node or node_2 == node) and self.graph[node_1, node_2] is True:
                    if node_1 is not node:
                        neighbours.append(node_1)
                    else:
                        neighbours.append(node_2)

        return sorted(set(neighbours))

    def path_between(self, node_a, node_b, path = []):
        start = node_a
        path = path + [start]

        if node_a == node_b:
            return path

        else:
            for elements in self.nodes:
                if self.graph[start, elements] is True:
                    return path_between(elements, node_b)

        #if not graph.

graf = DirectedGraph()
graf.create_graph()
graf.add_edge('a', 'b')
graf.add_edge('b', 'e')
graf.add_edge('d', 'c')
graf.add_edge('e', 'c')
graf.add_edge('c', 'd')
graf.add_edge('a', 'e')
graf.add_edge('c', 'd')
graf.path_between('a', 'd', [""])

#graf.print_graph()
print(graf.get_neighbours_for('c'))
