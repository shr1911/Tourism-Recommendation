import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tourism.settings")

import django
django.setup()

from recommendations.models import Timing, Restaurant


def save_timing_from_row(timing_row):
    timing = Timing()
    timing.id = timing_row[0]
    timing.rid = Restaurant.objects.get(id=timing_row[1])
    timing.day = timing_row[2]
    timing.timing = timing_row[3]
    timing.starttime = timing_row[4]
    timing.endtime = timing_row[5]
    timing.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        #recommendations_df = pd.read_csv(open(sys.argv[1],'rU'), engine='c', names=['id','rname','latitude','longitude','address','area','city','cost','rating','homedelivery','alcohol','wifi','valetparking','rooftop'])
        timing_df = pd.read_csv(open(sys.argv[1],'rU'), engine='c')
        print(timing_df)

        timing_df.apply(
            save_timing_from_row,
            axis=1
        )

        print("There are {} reviews in DB".format(Timing.objects.count()))
        
    else:
        print("Please, provide Reviews file path")