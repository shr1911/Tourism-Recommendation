import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tourism.settings")

import django
django.setup()

from recommendations.models import Cuisine, Restaurant


def save_cuisine_from_row(cuisine_row):
    cuisine = Cuisine()
    cuisine.id = cuisine_row[0]
    cuisine.rid = Restaurant.objects.get(id=cuisine_row[1])
    cuisine.cuisine = cuisine_row[2]
    #restaurant.wine = Wine.objects.get(id=review_row[2]
    #restaurant.pub_date = datetime.datetime.now()
    cuisine.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        #recommendations_df = pd.read_csv(open(sys.argv[1],'rU'), engine='c', names=['id','rname','latitude','longitude','address','area','city','cost','rating','homedelivery','alcohol','wifi','valetparking','rooftop'])
        cuisine_df = pd.read_csv(open(sys.argv[1],'rU'), engine='c')
        print(cuisine_df)

        cuisine_df.apply(
            save_cuisine_from_row,
            axis=1
        )

        print("There are {} reviews in DB".format(Cuisine.objects.count()))
        
    else:
        print("Please, provide Reviews file path")