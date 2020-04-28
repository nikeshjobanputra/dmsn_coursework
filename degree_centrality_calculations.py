import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import csv

flight_data_col = ['Source', 'Destination']
flight_data_df = pd.read_csv('flight_data.csv', names=flight_data_col, skiprows=[0])
flight_data_df['Source'] = flight_data_df['Source'].astype("string")
flight_data_df['Destination'] = flight_data_df['Destination'].astype("string")

original_data = nx.from_pandas_edgelist(flight_data_df, source = 'Source', target = 'Destination' ,create_using = nx.DiGraph())

degree_centrality_dict = nx.degree_centrality(original_data)

with open('degree_centrality_results.csv', 'w') as f:
    w = csv.writer(f)
    for key, value in degree_centrality_dict.items():
        w.writerow([key,value])