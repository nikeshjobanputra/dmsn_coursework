import random
import pandas as pd

flight_data_col = ['Source', 'Destination']
flight_data_df = pd.read_csv('flight_data.csv', names=flight_data_col, skiprows=[0])
flight_data_df['Source'] = flight_data_df['Source'].astype("string")
flight_data_df['Destination'] = flight_data_df['Destination'].astype("string")

#threshold param to change
threshold=0.4

#name of file---update when changing threshold
name_of_new_csv = "fourty_percentage_threshold.csv"

removed_edges_from_LAX=0

for index, row in flight_data_df.iterrows():
    if(random.random()<=threshold):
        if row['Source'] == 'LAX':
            removed_edges_from_LAX+=1
            flight_data_df.drop(index, inplace=True)
        elif row['Destination'] == 'LAX':
            removed_edges_from_LAX+=1
            flight_data_df.drop(index, inplace=True)


print("Amount of removed edges to and from LAX is ", removed_edges_from_LAX)

flight_data_df.to_csv(name_of_new_csv, index=None, header=True)