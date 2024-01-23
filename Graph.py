from abc import ABC, abstractmethod
import numpy as np


class Graph(ABC):
    def __init__(self, node):
        self.matrix = None
        self.nodes = set(range(1, node + 1))
        self.edges = {node: [] for node in self.nodes}

    @abstractmethod
    def add_edges(self, first, second):
        pass

    def add_weighted_edge(self, first, second, weight):
        pass

    def delete_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.edges.pop(node)
            for values in self.edges.values():
                while node in values:
                    values.remove(node)

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError("This node is already exists")
        else:
            self.nodes.add(node)
            print("Node was added")
            print(self.nodes)

    def delete_edge(self, first, second):
        if first and second in self.nodes:
            if second in self.edges[first]:
                values = self.edges[first]
                values.remove(second)
                return True
            else:
                print("There isn't this edge")
        else:
            raise ValueError("These nodes don't exist")

    def switch_to_matrix(self):
        self.matrix = np.zeros((len(self.nodes), len(self.nodes)))
        for key, values in self.edges.items():
            if values is not None:
                for i in values:
                    self.matrix[key - 1][i - 1] = 1

    def topological_sort(self):
        visited = set()
        stack = []

        def dfs(node):
            nonlocal visited
            visited.add(node)

            for neighbor in self.edges[node]:
                if neighbor not in visited:
                    dfs(neighbor)

            stack.append(node)

        for node in self.nodes:
            if node not in visited:
                dfs(node)

        return stack[::-1]

    def has_cycle(self):
        visited = set()
        stack = set()

        def dfs_cycle(node):
            nonlocal visited, stack
            visited.add(node)
            stack.add(node)

            for neighbor in self.edges[node]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor):
                        return True
                elif neighbor in stack:
                    return True

            stack.remove(node)
            return False

        for node in self.nodes:
            if node not in visited:
                if dfs_cycle(node):
                    return True

        return False

    def demoucron_sort(self):
        visited = set()
        result = []

        def dfs_demoucron(node):
            nonlocal visited, result
            visited.add(node)

            for neighbor in self.edges[node]:
                if neighbor not in visited:
                    dfs_demoucron(neighbor)

            result.append(node)

        for node in self.nodes:
            if node not in visited:
                dfs_demoucron(node)

        return result[::-1]
