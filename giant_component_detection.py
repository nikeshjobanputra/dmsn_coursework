import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# import os
# os.environ["PROJ_LIB"] = "C:\\Users\\Nikesh\\Anaconda3\\pkgs\\proj4-5.2.0-ha925a31_1\\Library\\share"
# from mpl_toolkits.basemap import Basemap as Basemap
import pygraphviz
from networkx.drawing.nx_agraph import graphviz_layout
layout = graphviz_layout

flight_data_col = ['Source', 'Destination']
# , 'Weight'
flight_data_df = pd.read_csv('flight_data.csv', names=flight_data_col, skiprows=[0])
flight_data_df['Source'] = flight_data_df['Source'].astype("string")
flight_data_df['Destination'] = flight_data_df['Destination'].astype("string")

# needs to be to changed to int for random graphs
# flight_data_df['Weight'] = flight_data_df['Weight'].astype("int")


print(flight_data_df)


graph = nx.from_pandas_edgelist(flight_data_df, source = 'Source', target = 'Destination')
# , edge_attr = True

# ,create_using = nx.DiGraph()
print("OG Graph Nodes",graph.number_of_nodes())
print("OG Graph Edges",graph.number_of_edges())

# print(graph)

# pos = layout(graph)
# nx.draw(graph, pos,
#             with_labels=False,
#             node_size=10
#            )
Gcc = sorted(nx.connected_components(graph), key=len, reverse=True)
G0 = graph.subgraph(Gcc[0])

print("Giant component with OG - nodes",G0.number_of_nodes())
print("Giant component with OG - edges",G0.number_of_edges())
# print("Graph OG - edges",graph.number_of_edges())






# nx.draw_networkx_edges(G0, pos, with_labels=False, edge_color='r', width=6.0)

# for Gi in Gcc[1:]:
#     if len(Gi) > 1:
#         nx.draw_networkx_edges(graph.subgraph(Gi), pos,
#                             with_labels=False,
#                             edge_color='r',
#                             alpha=0.3,
#                             width=5.0
#                             )

# plt.show()

# print("Edges",len(G0.edges))

# edges = graph.edges()
# edges=sorted(edges, reverse = True, key=lambda t: graph[t[0]][t[1]]['Weight'])

# edges=sorted(G.edges(data=True), key=lambda t: t[2].get('weight', 1))
# edges = sorted(edges, reverse = False, key = lambda t : graph.get_edge_data(t[0], t[1]))
# for i in range(3):

nodes = graph.nodes()
degrees = graph.degree()

degrees = sorted(degrees, reverse = True, key = lambda x: x[1])

# print(degrees)

i=0
data = []
data.append([G0.number_of_nodes(), G0.number_of_edges()])
while graph.number_of_edges() != 0:
    degrees = graph.degree()
    degrees = sorted(degrees, reverse = True, key = lambda x: x[1])

    numberOfNodes = graph.number_of_nodes()

    counter = 0
    for degree in degrees:
        graph.remove_node(degree[0])
        counter+=1

        if(counter == int(numberOfNodes * 0.1)):
            break

    Gcc = sorted(nx.connected_components(graph), key=len, reverse=True)
    G0 = graph.subgraph(Gcc[0])

    data.append([G0.number_of_nodes(), G0.number_of_edges()])

    print("Nodes in Giant component", i+1, "iteration", G0.number_of_nodes())
    print("Edges in Giant component", i+1, "iteration", G0.number_of_edges())
    # print("Edges for whole graph", i+1, "iteration", graph.number_of_edges())

    i+=1

# print(len(data))
df = pd.DataFrame(data, columns = ['Nodes', 'Edges'])
df.index.name = "Iteration"


print(df)

df.to_csv("task2_for_our_dataset.csv")

'''
i = 0
while graph.number_of_edges() != 0:
    edges = graph.edges()
    

    edges=sorted(edges, reverse = True, key=lambda t: graph[t[0]][t[1]]['Weight'])

    numberOfEdges = graph.number_of_edges()
    print(numberOfEdges)
    counter = 0
    for edge in edges:
        graph.remove_edge(edge[0],edge[1])
        counter+=1

        if counter == int(numberOfEdges * 0.1):
            print(counter)
            break

    Gcc = sorted(nx.connected_components(graph), key=len, reverse=True)
    G0 = graph.subgraph(Gcc[0])

    print("Giant component - Nodes for", i+1, "cut", G0.number_of_nodes())
    print("Giant component - Edges for", i+1, "cut", graph.number_of_edges())

    i+=1
'''
    

# edges=sorted(G.edges(data=True), key=lambda t: t[2].get('weight', 1))
# edges = sorted(edges, reverse = False, key = lambda t : graph.get_edge_data(t[0], t[1]))

'''

edges = graph.edges()
edges=sorted(edges, reverse = True, key=lambda t: graph[t[0]][t[1]]['Weight'])
counter = 0
for edge in edges:
    
    # print(graph[edge[0]][edge[1]]['Weight'])
    # print(graph.get_edge_data(edge[0],edge[1]))

    graph.remove_edge(edge[0],edge[1])

    counter+=1

    if counter == int(len(edges) * 0.1):
        print(counter)
        break

Gcc = sorted(nx.connected_components(graph), key=len, reverse=True)
G0 = graph.subgraph(Gcc[0])

print("Third",G0.number_of_nodes())
print("Third",graph.number_of_edges())

edges = graph.edges()
edges=sorted(edges, reverse = True, key=lambda t: graph[t[0]][t[1]]['Weight'])

# edges=sorted(G.edges(data=True), key=lambda t: t[2].get('weight', 1))
# edges = sorted(edges, reverse = False, key = lambda t : graph.get_edge_data(t[0], t[1]))
counter = 0
for edge in edges:
    
    # print(graph[edge[0]][edge[1]]['Weight'])
    # print(graph.get_edge_data(edge[0],edge[1]))

    graph.remove_edge(edge[0],edge[1])

    counter+=1

    if counter == int(len(edges) * 0.1):
        print(counter)
        break

Gcc = sorted(nx.connected_components(graph), key=len, reverse=True)
G0 = graph.subgraph(Gcc[0])

print("Fourth",G0.number_of_nodes())
print("Fourth",graph.number_of_edges())
'''



# edges=sorted(G0.edges(data=True), reverse=False ,key=lambda t: t[2].get('weight', 1))

# counter = 0
# for edge in edges:
#     counter+=1
#     if counter != int(len(edges) * 0.1):
#         print(graph[edge[0]][edge[1]]['weight'])
#         graph.remove_edge(edge[0], edge[1])
#     else:
#         break

# pos = layout(graph)
# nx.draw(graph, pos,
#             with_labels=False,
#             node_size=10
#            )
# Gcc = sorted(nx.connected_components(graph), key=len, reverse=True)
# G0 = graph.subgraph(Gcc[0])

# print("Second",G0.number_of_nodes())
# print("Second",graph.number_of_edges())





