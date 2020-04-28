import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import csv

flight_data_col = ['Source', 'Destination']
flight_data_df = pd.read_csv('flight_data.csv', names=flight_data_col, skiprows=[0])
flight_data_df['Source'] = flight_data_df['Source'].astype("string")
flight_data_df['Destination'] = flight_data_df['Destination'].astype("string")

original_data = nx.from_pandas_edgelist(flight_data_df, source = 'Source', target = 'Destination' ,create_using = nx.DiGraph())

random_graph_1 = nx.erdos_renyi_graph(1259, 0.021)
random_graph_2 = nx.erdos_renyi_graph(1259, 0.021)
random_graph_3 = nx.erdos_renyi_graph(1259, 0.021)

page_rank_for_original_data = nx.pagerank(original_data)

page_rank_for_random_graph_1 = nx.pagerank(random_graph_1)
page_rank_for_random_graph_2 = nx.pagerank(random_graph_2)
page_rank_for_random_graph_3 = nx.pagerank(random_graph_3)

with open('page_rank_for_original_data.csv', 'w') as f:
    w = csv.writer(f)
    for key, value in page_rank_for_original_data.items():
        w.writerow([key,value])

with open('page_rank_for_random_graph_1.csv', 'w') as f:
    w = csv.writer(f)
    for key, value in page_rank_for_random_graph_1.items():
        w.writerow([key,value])

with open('page_rank_for_random_graph_2.csv', 'w') as f:
    w = csv.writer(f)
    for key, value in page_rank_for_random_graph_2.items():
        w.writerow([key,value])

with open('page_rank_for_random_graph_3.csv', 'w') as f:
    w = csv.writer(f)
    for key, value in page_rank_for_random_graph_3.items():
        w.writerow([key,value])

