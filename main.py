from visualize import *

c_nodes = 6
graph = UndirectedGraph(c_nodes)
print("Undirected Graph")
graph.add_edges(1, 3)
graph.add_edges(2, 3)
graph.add_edges(4, 1)
graph.add_edges(1, 5)
graph.add_edges(3, 5)
graph.switch_to_matrix()
print("Nodes:", graph.nodes)
print("Edges:", graph.edges)
print(graph.matrix)
graph.delete_node(4)
graph.delete_edge(1, 3)
print("Updated nodes:", graph.nodes)
print("Updated edges:", graph.edges)
graph.switch_to_matrix()
print(graph.matrix)

print("--------------------------------")
print("Directed Graph")
c_nodes = 7
graph = DirectedGraph(c_nodes)
graph.add_edges(1, 3)
graph.add_edges(3, 1)
graph.add_edges(5, 4)
graph.add_edges(2, 3)
graph.add_edges(2, 1)
graph.add_edges(4, 1)
print(graph.nodes)
print(graph.edges)
graph.switch_to_matrix()
print(graph.matrix)
graph.add_node(8)
graph.add_edges(2, 8)
graph.switch_to_matrix()
print("Updated nodes:", graph.nodes)
print("Updated edges:", graph.edges)
print(graph.matrix)
print("-------------------------------")

print("Weighted-directed Graph")
c_nodes = 10
graph = WeightedGraph(c_nodes, 0.3)
print(graph.nodes)
print(graph.edges)
graph.switch_to_matrix()
print(graph.matrix)

c_nodes = 5
g = DirectedGraphWithVisualisation(c_nodes, 0.2)
g.visualize()
if g.has_cycle():
    print("He has a cycle")
    print("Nodes:", g.nodes)
    print("Edges:", g.edges)
else:
    print("He hasn't a cycle")
    print("Nodes:", g.nodes)
    print("Edges:", g.edges)
    topological_order = g.topological_sort()
    print("Topological order:", topological_order)
    demoucron_order = g.demoucron_sort()
    print("Demoucron order:", demoucron_order)