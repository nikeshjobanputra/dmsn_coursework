import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
# os.environ["PROJ_LIB"] = "C:\\Users\\Nikesh\\Anaconda3\\pkgs\\proj4-5.2.0-ha925a31_1\\Library\\share"
from mpl_toolkits.basemap import Basemap as Basemap

flight_data_col = ['Source', 'Destination']
flight_data_df = pd.read_csv('flight_data.csv', names=flight_data_col, skiprows=[0])
flight_data_df['Source'] = flight_data_df['Source'].astype("string")
flight_data_df['Destination'] = flight_data_df['Destination'].astype("string")

nodes_lat_long_col = ['Node', 'Airport Name', 'Lon', 'Lat']
nodes_lat_long_df = pd.read_csv('data.csv', names=nodes_lat_long_col, skiprows=[0])
nodes_lat_long_df['Node'] = nodes_lat_long_df['Node'].astype("string")
nodes_lat_long_df['Airport Name'] = nodes_lat_long_df['Airport Name'].astype("string")

graph = nx.from_pandas_edgelist(flight_data_df, source = 'Source', target = 'Destination' ,create_using = nx.DiGraph())

plt.figure(figsize = (10,6))

m = Basemap(projection='cyl', resolution='l',
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, )
mx, my = m(nodes_lat_long_df['Lon'].values, nodes_lat_long_df['Lat'].values)
pos = {}
for count, elem in enumerate (nodes_lat_long_df['Node']):
     pos[elem] = (mx[count], my[count])

nx.draw_networkx_nodes(G = graph, pos = pos, node_list = graph.nodes(),node_color = 'r', alpha = 0.8, node_size = 100)
nx.draw_networkx_edges(G = graph, pos = pos, edge_color='g', alpha=0.2, arrows = False)

m.drawcountries(linewidth = 3)
m.drawstates(linewidth = 0.2)
m.drawcoastlines(linewidth=3)
plt.tight_layout()
plt.savefig("map_unknown_removed_shit.png", format = "png", dpi = 300)