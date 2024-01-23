from abc import ABC
import random
from Graph import Graph


class UndirectedGraph(Graph, ABC):
    def __init__(self, node, probability=False):
        super().__init__(node)
        if probability:
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

            if second not in self.edges:
                self.edges[second] = [first]
            else:
                if first not in self.edges[second]:
                    self.edges[second].append(first)

            self.edges = dict(sorted(self.edges.items()))
        else:
            raise ValueError("These nodes aren't exist! Try again. ")

    def delete_edge(self, first, second):
        res = super().delete_edge(first, second)
        if res:
            values = self.edges[second]
            values.remove(first)
