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
count_of_LAX_edges=0

# print("The flight dataset ",flight_data_df.Source.value_counts())
# print("The flight dataset ",flight_data_df.Destination.value_counts())

for index, row in flight_data_df.iterrows():
    if row['Source'] == 'LAX':
        count_of_LAX_edges+=1
        if(random.random()<=threshold):
            removed_edges_from_LAX+=1
            flight_data_df.drop(index, inplace=True)
    elif row['Destination'] == 'LAX':
        count_of_LAX_edges+=1
        if(random.random()<=threshold):
            removed_edges_from_LAX+=1
            flight_data_df.drop(index, inplace=True)

print("Total amount of edges to and from LAX is ", count_of_LAX_edges)
print("Amount of removed edges to and from LAX is ", removed_edges_from_LAX)
print("Percentage removed is ", (removed_edges_from_LAX/count_of_LAX_edges)*100, "%")

flight_data_df.to_csv(name_of_new_csv, index=None, header=True)