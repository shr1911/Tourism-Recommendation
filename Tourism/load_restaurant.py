import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tourism.settings")

import django
django.setup()

from recommendations.models import Restaurant


def save_restaurant_from_row(restaurant_row):
    restaurant = Restaurant()
    restaurant.id = restaurant_row[0]
    restaurant.rname = restaurant_row[1]
    restaurant.latitude = restaurant_row[2]
    restaurant.longitude = restaurant_row[3]
    restaurant.address = restaurant_row[4]
    restaurant.area = restaurant_row[5]
    restaurant.city = restaurant_row[6]
    restaurant.cost = restaurant_row[7]
    restaurant.rating = restaurant_row[8]
    restaurant.homedelivery = restaurant_row[9]
    restaurant.homedelivery = restaurant_row[10]
    restaurant.alcohol = restaurant_row[11]
    restaurant.wifi = restaurant_row[12]
    restaurant.valetparking = restaurant_row[13]
    restaurant.rooftop = restaurant_row[14]
    #restaurant.wine = Wine.objects.get(id=review_row[2]
    #restaurant.pub_date = datetime.datetime.now()
    restaurant.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        #recommendations_df = pd.read_csv(open(sys.argv[1],'rU'), engine='c', names=['id','rname','latitude','longitude','address','area','city','cost','rating','homedelivery','alcohol','wifi','valetparking','rooftop'])
        recommendations_df = pd.read_csv(open(sys.argv[1],'rU'), engine='c')
        print(recommendations_df)

        recommendations_df.apply(
            save_restaurant_from_row,
            axis=1
        )

        print("There are {} reviews in DB".format(Restaurant.objects.count()))
        
    else:
        print("Please, provide Reviews file path")