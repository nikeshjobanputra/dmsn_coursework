import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
os.environ["PROJ_LIB"] = "C:\\Users\\Nikesh\\Anaconda3\\pkgs\\proj4-5.2.0-ha925a31_1\\Library\\share"
from mpl_toolkits.basemap import Basemap as Basemap
import pygraphviz
from networkx.drawing.nx_agraph import graphviz_layout
layout = graphviz_layout

flight_data_col = ['Source', 'Destination']
flight_data_df = pd.read_csv('flight_data.csv', names=flight_data_col, skiprows=[0])
flight_data_df['Source'] = flight_data_df['Source'].astype("string")
flight_data_df['Destination'] = flight_data_df['Destination'].astype("string")

graph = nx.from_pandas_edgelist(flight_data_df, source = 'Source', target = 'Destination' ,create_using = nx.DiGraph())

pos = layout(graph)
Gcc = sorted(nx.connected_components(graph), key=len, reverse=True)
G0 = graph.subgraph(Gcc[0])
nx.draw_networkx_edges(G0, pos, with_labels=False, edge_color='r', width=6.0)

plt.show()