import pandas as pd
import numpy as np

data = pd.read_csv("shit_ones.csv")
# data = pd.read_csv("test.csv")
data2 = pd.read_csv("nodes_lat_long.csv")

# print(data)
data = data.set_index('Code')
# print(data)

data2 = data2.set_index("Node")
# print(data2)

# for index in data2.index:
#     print(data2.loc[index, "Node"])
counter = 0
for index in data2.index:
    try:
        #  realLon = int(data.loc[index, "Lon"])
        #  ogLon = int(data2.loc[index, "Lon"])

        #  realLat = int(data.loc[index, "Lat"])
        #  ogLat = int(data2.loc[index, "Lat"])


        #  if(ogLon != realLon or realLat != ogLat):
            # print(index, og, real)
        data2.loc[index,"Lon"] = data.loc[index, "Lon"]
        data2.loc[index,"Lat"] = data.loc[index, "Lat"]
            # print(data2.loc[index,"Lon"])

    except:
        counter+=1
        print(index, data2.loc[index,"Airport Name"])
        # data2.drop(labels)
        # data2.loc[index,"Lat"] = np.nan
        pass
    
print(counter)

# data2.dropna()

data2.to_csv(r'data.csv')