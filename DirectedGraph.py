import random
from Graph import Graph


class DirectedGraph(Graph):
    def __init__(self, node, probability=None):
        super().__init__(node)
        self.weight = {}
        if probability is not None:
            for i in range(1, node + 1):
                for j in range(1, node + 1):
                    if i != j and random.random() < probability:
                        self.add_edges(i, j)

    def add_edges(self, first, second):
        if first and second in self.nodes:
            if first not in self.edges:
                self.edges[first] = [second]
            else:
                if second not in self.edges[first]:
                    self.edges[first].append(second)
            self.edges = dict(sorted(self.edges.items()))
