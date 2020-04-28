import networkx as nx
import matplotlib.pyplot as plt

g = nx.erdos_renyi_graph(1259, 0.021)

print("Number of nodes is ", g.number_of_edges())
print("Number of edges is ", g.number_of_nodes())

nx.draw(g)
plt.show()