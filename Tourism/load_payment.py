import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tourism.settings")

import django
django.setup()

from recommendations.models import Payment, Restaurant


def save_payment_from_row(payment_row):
    payment = Payment()
    payment.id = payment_row[0]
    payment.rid = Restaurant.objects.get(id=payment_row[1])
    payment.payment = payment_row[2]
    #restaurant.wine = Wine.objects.get(id=review_row[2]
    #restaurant.pub_date = datetime.datetime.now()
    payment.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        #recommendations_df = pd.read_csv(open(sys.argv[1],'rU'), engine='c', names=['id','rname','latitude','longitude','address','area','city','cost','rating','homedelivery','alcohol','wifi','valetparking','rooftop'])
        payment_df = pd.read_csv(open(sys.argv[1],'rU'), engine='c')
        print(payment_df)

        payment_df.apply(
            save_payment_from_row,
            axis=1
        )

        print("There are {} reviews in DB".format(Payment.objects.count()))
        
    else:
        print("Please, provide Reviews file path")