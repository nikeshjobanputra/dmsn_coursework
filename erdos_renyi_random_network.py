import networkx as nx
import matplotlib.pyplot as plt
import csv

random_graph_1 = nx.erdos_renyi_graph(1259, 0.021)
random_graph_2 = nx.erdos_renyi_graph(1259, 0.021)
random_graph_3 = nx.erdos_renyi_graph(1259, 0.021)


print("Number of nodes for random_graph_1 is ", random_graph_1.number_of_edges())
print("Number of edges is random_graph_1 is ", random_graph_1.number_of_nodes())
print("\n")
print("Number of nodes for random_graph_2 is ", random_graph_2.number_of_edges())
print("Number of edges for random_graph_2 is ", random_graph_2.number_of_nodes())
print("\n")
print("Number of nodes for random_graph_3 is ", random_graph_3.number_of_edges())
print("Number of edges for random_graph_3 is ", random_graph_3.number_of_nodes())

list_of_edges_random_graph_1 = list(random_graph_1.edges())
list_of_edges_random_graph_2 = list(random_graph_2.edges())
list_of_edges_random_graph_3 = list(random_graph_3.edges())

with open('random_graph_1_data.csv', 'w') as f:
    w = csv.writer(f)
    for edge_list in list_of_edges_random_graph_1:
        w.writerow([edge_list[0],edge_list[1]])

with open('random_graph_2_data.csv', 'w') as f:
    w = csv.writer(f)
    for edge_list in list_of_edges_random_graph_2:
        w.writerow([edge_list[0],edge_list[1]])

with open('random_graph_3_data.csv', 'w') as f:
    w = csv.writer(f)
    for edge_list in list_of_edges_random_graph_3:
        w.writerow([edge_list[0],edge_list[1]])
    