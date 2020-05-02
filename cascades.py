import pandas as pd
import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
import matplotlib.pyplot as plt
import csv

flight_data_col = ['Source', 'Destination']
flight_data_df = pd.read_csv('flight_data.csv', names=flight_data_col, skiprows=[0])
flight_data_df['Source'] = flight_data_df['Source'].astype("string")
flight_data_df['Destination'] = flight_data_df['Destination'].astype("string")

original_data = nx.from_pandas_edgelist(flight_data_df, source = 'Source', target = 'Destination' ,create_using = nx.DiGraph())

model = ep.ThresholdModel(original_data)

config = mc.Configuration()
config.add_model_parameter('fraction_infected', 0.10)

threshold = 0.25
for i in original_data.nodes():
    config.add_node_configuration("threshold", i, threshold)

model.set_initial_status(config)

iterations = model.iteration_bunch(200)

trends = model.build_trends(iterations)

viz = DiffusionTrend(model, trends)
viz.plot("cascade_results_1.png")

