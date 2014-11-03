class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self,node_a, node_b):
        if node_a not in self.graph:
            self.graph[node_a] = [node_b]
        elif (node_a in self.graph) and (node_b not in self.graph[node_a]):
            self.graph[node_a].append(node_b)

    def print_graph(self):
        print(self.graph)

    def get_neighbours_for(self, node):
        return self.graph[node]

    def path_between(self, node_a, node_b):
        for neighbours in self.graph[node_a]:
            if neighbours in self.graph:
                if node_b in self.graph[neighbours]:
                    return True
        return False

    def to_str(self):
        for item in self.graph:
            return "{} ---> {}".format(item, self.get_neighbours_for(item))

graf = DirectedGraph()

graf.add_edge('a', 'b')
graf.add_edge('b', 'e')
graf.add_edge('d', 'c')
graf.add_edge('e', 'c')
graf.add_edge('c', 'd')
graf.add_edge('a', 'e')
graf.add_edge('c', 'd')

graf.print_graph()
print(graf.get_neighbours_for('c'))
print(graf.path_between('a', 'd'))