import networkx as nx
import matplotlib.pyplot as plt
from WeightedGraph import WeightedGraph
from DirectedGraph import DirectedGraph
from UndirectedGraph import UndirectedGraph


class UndirectedGraphWithVisualisation(UndirectedGraph):
    def visualize(self):
        g = nx.Graph()

        for node in self.nodes:
            g.add_node(node)

        for edge, values in self.edges.items():
            for neighbor in values:
                g.add_edge(edge, neighbor)

        pos = nx.spring_layout(g)  # Позиции узлов для красивого размещения на графе
        nx.draw(g, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue", font_size=8,
                font_color="black", edge_color="gray")
        plt.show()


class DirectedGraphWithVisualisation(DirectedGraph):
    def visualize(self):
        g = nx.DiGraph()

        for node in self.nodes:
            g.add_node(node)

        for node, neighbors in self.edges.items():
            for neighbor in neighbors:
                g.add_edge(node, neighbor)

        pos = nx.spring_layout(g)

        nx.draw(g, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8,
                font_color='black')

        plt.show()


class WeightedGraphWithVisualization(WeightedGraph):
    def visualize(self):
        g = nx.Graph()
        for node in self.nodes:
            g.add_node(node)
        for edge, weight in self.weight.items():
            g.add_edge(*edge, weight=weight)

        pos = nx.spring_layout(g)
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw(g, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10)
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.show()
