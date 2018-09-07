# -*- encoding='utf-8-sig' -*-
import numpy as np
from recommendations.models import Restaurant
import pandas as pd
import scipy
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances

def find_rating(nearby_rid, cuisine):
    print("I am starting to find rating algo")
    #print nearby_rid

    # First read csv files and store it in dataframe 
    # Second convert dataframe to array
    df_restaurant = pd.read_csv('data/restaurant.csv', header=0)
    array_restaurant = df_restaurant.values
    #print array_restaurant


    df_cuisine = pd.read_csv('data/cuisine.csv', header=0)
    array_cuisine = df_cuisine.values


    # # Perform natural join on cuisine and restaurant based on key 'rid' and store it in dataframe
    # # convert that dataframe into an array
    # combine = df_cuisine.set_index('rid').join(df_restaurant.set_index('id'))
    # array_combine = combine.values
    # #print array_combine

	#---------------------------------------------------------------------------   

    # Select only those restaurant from all which are nearby
    # Convert 2d numpy array to 1d array. For eg. [[1, 2, 3]] into [1, 2, 3]
    nearby_rid = nearby_rid.ravel()
    filter_nearby = df_restaurant.loc[df_restaurant['id'].isin(nearby_rid)]
    array_filter_nearby = filter_nearby.values
    #print array_filter_nearby


    filter_cuisine_id = array_cuisine[array_cuisine[:,2] == 'Italian'] 
    #print "I WANT THISSSSSSSSSS" 
    #print filter_cuisine_id
    filter_cuisine_id = filter_cuisine_id[:,1]
    #print filter_cuisine_id.astype(int)


    filter_cuisine = filter_nearby.loc[filter_nearby['id'].isin(filter_cuisine_id.astype(int))]
    print(filter_cuisine)
    filter_cuisine = filter_cuisine.values

    #---------------------------------------------------------------------------
    # Extract latitude and longitude of above filtered restaurant
    lat_long = filter_cuisine[:,2:4]
    #print lat_long


    # Apply clustering algo on filtered restaurant data
    kmeans = KMeans(n_clusters=3, random_state=0).fit(lat_long)

    # Cluster number for all the above filtered restaurant in which cluster they fall
    print(kmeans.labels_)
    #print kmeans.predict([[18.95618666,72.81199761], [18.99120402, 72.81458057]])
    print("Clustering centre")
    print(kmeans.cluster_centers_)

    #----------------------------------------------------------------------------

    # calculate distance of each cluster from user's current location
    distance = euclidean_distances([[19.044497, 72.8204535]], kmeans.cluster_centers_)
    print(np.transpose(distance))
    print(len(distance))

    # append cluster number with above distance array, for knowing which cluster distance is that 
    # because after we are sorting these distances
    distance_cluster_centre = np.insert(np.transpose(distance), 1, np.array([0, 1, 2]), axis=1)
    print(distance_cluster_centre)

    # sorted distances
    print("sorted distance")
    arr = distance_cluster_centre[distance_cluster_centre[:,0].argsort()]


    #------------------------------------------------------------------------------

    # make numpy array with columns [id, lat, long, rating, cid]
    # cid = cluster id
    id_after_cuisine = filter_cuisine[:,0]
    id_lat_long = np.insert(lat_long, 0, id_after_cuisine, axis=1)
    id_lat_long_cid = np.insert(id_lat_long, 3, kmeans.labels_ , axis=1)
    id_lat_long_rating_cid = np.insert(id_lat_long_cid, 3, filter_cuisine[:,8] , axis=1)
    print(id_lat_long_rating_cid)
 

    # convert above array to dataframe
    columns=['id','latitude','longitude','rating','cid']
    df = pd.DataFrame(id_lat_long_rating_cid ,columns=columns)

    #-----------------------------------------------------------------------------------------------

    # SORT CLUSTER ACCORDING TO CLUSTER CENTRE DISTANCES FROM USER'S LOCATION

   
    # select [[12.313, 12.375843, 24.7364],[0, 2, 1]] - [[centre distances][cluster id]]
    print(np.array(arr[:,1][0]))
    #initialize empty dataframe
    sorted_cluster =  pd.DataFrame()
    # sort cluster according to cluster centre distance
    for i in range(0, len(arr[:,1])):
    	# dataframe  of single cluster
    	single_cluster = df.loc[df['cid'].isin(np.array( arr[:,1][i] ).ravel())]
    	single_cluster = single_cluster.sort_values(by='rating', ascending=False)
    	sorted_cluster = sorted_cluster.append(single_cluster)
    print(sorted_cluster)


    #df_groupby = sorted_cluster.groupby('cid')
    #print len(df_groupby)

    #for group in  df_groupby:
    #	print group
    #print df_groupby.sort_values('rating', ascending=False)
    #print df_groupby.get_group(0)






    # convert dataframe to array and extract only rid
    sorted_cluster_rid = sorted_cluster.as_matrix(columns=None)[:,0]
    # convert long datatype of rid into int 
    return sorted_cluster_rid.astype(int)


    #df_groupby = df.groupby('cid')
    #print len(df_groupby)

    #for group in  df_groupby:
    #	print group
    #print df_groupby.sort_values('rating', ascending=False)
    #print df_groupby.get_group(0)




#--------------------------------------------------------------------------------------------------


    # featureset_all = np.delete(filter_cuisine, np.s_[2:10], axis=1)
    # print "CONVERT THIS ARRAY TO DATFRAMEEEEEEEEEEEEEE"
    # print featureset_all
    # #featureset_all = featureset_all[0:6,:]
    

    # featureset_X = np.delete(featureset_all, np.s_[0], axis=1)
    # print featureset_X

    # featureset_Y = np.delete(featureset_all, np.s_[1:], axis=1)
    # print featureset_Y



    # columns=['cuisine','homedelivery','smoking','alcohol','wifi', 'valetparking','rooftop']

    # df = pd.DataFrame(featureset_X ,columns=columns)
    # print "CONVERTEDDDDDDDDDDDDDDDDDDD"
    # print df


    # cols_to_retain = ['cuisine', 'homedelivery', 'smoking', 'alcohol', 'wifi', 'valetparking', 'rooftop']
    # #cols_to_retain = ['homedelivery', 'smoking', 'alcohol', 'wifi']
    # feature = df[cols_to_retain].to_dict( orient = 'records' )
    # print "DICTIONARYYYYYYYYY"
    # print feature


    # vec = DictVectorizer()
    # X = vec.fit_transform(feature).toarray()
    # print X

  
    # columns=['id']
    # df = pd.DataFrame(featureset_Y ,columns=columns)
    # cols_to_retain = ['id']
    # Y = df[cols_to_retain].to_dict( orient = 'records' )
    # vec = DictVectorizer()
    # Y = vec.fit_transform(Y).toarray()
    # print Y

    # X_train, X_test, Y_train_labels, Y_test_labels = train_test_split(X, Y, test_size=0.3, random_state=100)
    # print "-----------Training feature---------------"
    # print X_train
    # print "------------Testing feature--------------"
    # print X_test
    # print "------------Training label--------------"
    # print Y_train_labels
    # print "-----------Testing label---------------"
    # print Y_test_labels
    # print "--------------------------"

    # clf_entropy = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=3, min_samples_leaf=5)
    # clf_entropy.fit(X_train, Y_train_labels)

    # print "Fitting done"
    # # Make predictions
    # y_pred_en = clf_entropy.predict(X_test)
    # print y_pred_en

    # # columns=['cuisine','homedelivery','smoking','alcohol','wifi', 'valetparking','rooftop']
    # # df = pd.DataFrame([['Italian', 'yes', 'no', 'yes', 'no', 'no', 'no'], ['Italian', 'yes', 'no', 'yes', 'no', 'no', 'no']] ,columns=columns)
    # # cols_to_retain = ['cuisine', 'homedelivery', 'smoking', 'alcohol', 'wifi', 'valetparking', 'rooftop']
    # # feature = df[cols_to_retain].to_dict( orient = 'records' )
    # # print feature
    # # vec = DictVectorizer()
    # # user_input = vec.fit_transform(feature).toarray()
    # # print user_input

    # print clf_entropy.predict([[0. ,1. ,1. ,1. , 0., 0., 1., 0., 1., 0., 0., 1., 0.]])


    print("shraddha")