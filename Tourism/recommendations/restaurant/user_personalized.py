import numpy as np
from sklearn.neighbors import NearestNeighbors
from recommendations.models import Restaurant
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer




def find_personalized(nearby_rid, cuisine):
    df_restaurant = pd.read_csv('data/restaurant.csv', header=0)
    array_restaurant = df_restaurant.values


    df_cuisine = pd.read_csv('data/cuisine.csv', header=0)
    array_cuisine = df_cuisine.values


    nearby_rid = nearby_rid.ravel()
    filter_nearby = df_restaurant.loc[df_restaurant['id'].isin(nearby_rid)]
    array_filter_nearby = filter_nearby.values
    #print array_filter_nearby


    filter_cuisine_id = array_cuisine[array_cuisine[:,2] == 'Italian'] 
    #print "I WANT THISSSSSSSSSS" 
    #print filter_cuisine_id
    filter_cuisine_id = filter_cuisine_id[:,1]
    #print filter_cuisine_id.astype(int)


    filter_cuisine_nearby = filter_nearby.loc[filter_nearby['id'].isin(filter_cuisine_id.astype(int))]
    print(filter_cuisine_nearby)
    filter_cuisine_nearby_array = filter_cuisine_nearby.values




    featureset_all = filter_cuisine_nearby_array
    #featureset_all = np.delete(filter_cuisine_nearby, np.s_[2:10], axis=1)
    print("CONVERT THIS ARRAY TO DATFRAMEEEEEEEEEEEEEE")
    print(featureset_all)
    #featureset_all = featureset_all[0:6,:]
    

    featureset_X = np.delete(featureset_all, np.s_[0:9], axis=1)
    print(featureset_X)

    featureset_Y = np.delete(featureset_all, np.s_[1:], axis=1)
    print(featureset_Y)



    columns=['homedelivery','smoking','alcohol','wifi', 'valetparking','rooftop']

    df_X = pd.DataFrame(featureset_X ,columns=columns)
    print("CONVERTEDDDDDDDDDDDDDDDDDDD")
    print(df_X)


    cols_to_retain = ['homedelivery', 'smoking', 'alcohol', 'wifi', 'valetparking', 'rooftop']
    #cols_to_retain = ['homedelivery', 'smoking', 'alcohol', 'wifi']
    feature = df_X[cols_to_retain].to_dict( orient = 'records' )
    print("DICTIONARYYYYYYYYY")
    print(feature)


    vec = DictVectorizer()
    X = vec.fit_transform(feature).toarray()
    print(X)

  
    columns=['id']
    df_Y = pd.DataFrame(featureset_Y ,columns=columns)
    cols_to_retain = ['id']
    Y = df_Y[cols_to_retain].to_dict( orient = 'records' )
    vec = DictVectorizer()
    Y = vec.fit_transform(Y).toarray()
    print(Y)

    X_train, X_test, Y_train_labels, Y_test_labels = train_test_split(X, Y, test_size=0.3, random_state=100)
    print("-----------Training feature---------------")
    print(X_train)
    print("------------Testing feature---------------")
    print(X_test)
    print("------------Training label----------------")
    print(Y_train_labels)
    print("-----------Testing label------------------")
    print(Y_test_labels)
    print("------------------------------------------")

    clf_entropy = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=3, min_samples_leaf=5)
    clf_entropy.fit(X_train, Y_train_labels)

    print("Fitting done")
    # Make predictions
    y_pred_en = clf_entropy.predict(X_test)
    print(y_pred_en)

    # columns=['cuisine','homedelivery','smoking','alcohol','wifi', 'valetparking','rooftop']
    # df = pd.DataFrame([['Italian', 'yes', 'no', 'yes', 'no', 'no', 'no'], ['Italian', 'yes', 'no', 'yes', 'no', 'no', 'no']] ,columns=columns)
    # cols_to_retain = ['cuisine', 'homedelivery', 'smoking', 'alcohol', 'wifi', 'valetparking', 'rooftop']
    # feature = df[cols_to_retain].to_dict( orient = 'records' )
    # print feature
    # vec = DictVectorizer()
    # user_input = vec.fit_transform(feature).toarray()
    # print user_input

    personalized_rid = clf_entropy.predict([[0. ,1. ,1. , 0., 0., 1., 0., 1., 1., 0., 1., 0.]])
    return personalized_rid.astype(int)

