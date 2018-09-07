import numpy as np
from sklearn.neighbors import NearestNeighbors
from recommendations.models import Restaurant
import pandas as pd


def find_nearby():
    rid = Restaurant.objects.values('id')
    latitude = Restaurant.objects.values('latitude')
    longitude = Restaurant.objects.values('longitude')
        
    rid_numpy = np.array(list(rid))
    latitude_numpy = np.array(list(latitude))
    longitude_numpy = np.array(list(longitude))


    #print list(latitude)
    df_latitude = pd.DataFrame(list(latitude))
    latitude_vals = df_latitude.values
    # print "FINAL = --------------------------------------------------"
    # print latitude_vals
    df_longitude = pd.DataFrame(list(longitude))
    longitude_vals = df_longitude.values
    # print "FINAL = --------------------------------------------------"
    # print longitude_vals
    df_rid = pd.DataFrame(list(rid))
    rid_vals = df_rid.values
    # print "FINAL = --------------------------------------------------"
    # print rid_vals
        
    X_train_pos = np.hstack(( latitude_vals , longitude_vals ))
    print(X_train_pos)

    # Next we will instantiate a nearest neighbor object, and call it nbrs. Then we will fit it to dataset X.
    nbrs = NearestNeighbors(n_neighbors=500, algorithm='ball_tree').fit(X_train_pos)

    # Let's find the k-neighbors of each point in object X. To do that we call the kneighbors() function on object X.
    distances, indices = nbrs.kneighbors([[19.044497, 72.8204535]])

    # Let's print out the indices of neighbors for each record in object X.
    #print indices
    #print distances
    return indices.ravel().astype(int)

