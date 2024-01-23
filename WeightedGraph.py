import numpy as np
import random
from DirectedGraph import DirectedGraph


class WeightedGraph(DirectedGraph):
    def __init__(self, node, probability=None):
        super().__init__(node)
        self.weight = {}
        if probability is not None:
            for i in range(1, node + 1):
                for j in range(1, node + 1):
                    if i != j and random.random() < probability:
                        rand = random.randint(1, 200)
                        self.add_weighted_edge(i, j, rand)

    def delete_node(self, node):
        super().delete_node(node)
        for key in list(self.weight.keys()):
            if node in key:
                self.weight.pop(key)

    def delete_edge(self, first, second):
        res = super().delete_edge(first, second)
        if res:
            self.weight.pop((first, second))

    def add_weighted_edge(self, first, second, weight_g):
        super().add_edges(first, second)
        if (first, second) not in self.weight:
            self.weight[(first, second)] = weight_g
        else:
            if self.weight[(first, second)] == weight_g:
                print("This edge is already exist")
            else:
                self.weight[(first, second)] = weight_g
                print(f"The weight of this edge {first, second} was updated")

    def switch_to_matrix(self):
        self.matrix = np.zeros((len(self.nodes), len(self.nodes)))
        for key, values in self.weight.items():
            node1, node2 = key
            value = values
            self.matrix[node1 - 1][node2 - 1] = value
