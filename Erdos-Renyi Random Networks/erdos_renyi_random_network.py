import networkx as nx
import matplotlib.pyplot as plt

fourtyPercentProbabilityNetwork = nx.erdos_renyi_graph(10, 0.4)
print("Average clustering coefficient for 40% probability network is ", nx.average_clustering(fourtyPercentProbabilityNetwork))
print("Average path length for 40% probability network is ", nx.average_shortest_path_length(fourtyPercentProbabilityNetwork))

sixtyPercentProbabilityNetwork = nx.erdos_renyi_graph(10, 0.6)
print("Average clustering coefficient for 60% probability network is ", nx.average_clustering(sixtyPercentProbabilityNetwork))
print("Average path length for 60% probability network is ", nx.average_shortest_path_length(sixtyPercentProbabilityNetwork))

eightyPercentProbabilityNetwork = nx.erdos_renyi_graph(10, 0.8)
print("Average clustering coefficient for 80% probability network is ", nx.average_clustering(eightyPercentProbabilityNetwork))
print("Average path length for 80% probability network is ", nx.average_shortest_path_length(eightyPercentProbabilityNetwork))

nx.draw(eightyPercentProbabilityNetwork)
plt.show()