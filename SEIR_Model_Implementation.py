import networkx as nx
import matplotlib.pyplot as plt

data = open('edgesList.csv', 'r')
graphType = nx.DiGraph()

g = nx.parse_edgelist(data, delimiter=',', create_using=graphType,
                      nodetype=str)
nx.draw(g)
plt.savefig("filename.png")