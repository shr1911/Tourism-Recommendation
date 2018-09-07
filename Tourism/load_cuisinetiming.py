import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tourism.settings")

import django
django.setup()

from recommendations.models import CusineTiming, Restaurant


def save_cuisinetiming_from_row(cuisinetiming_row):
    cuisinetiming = CusineTiming()
    cuisinetiming.id = cuisinetiming_row[0]
    cuisinetiming.cuisine = cuisinetiming_row[1]
    cuisinetiming.starttime = cuisinetiming_row[2]
    cuisinetiming.endtime = cuisinetiming_row[3]
    cuisinetiming.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        #recommendations_df = pd.read_csv(open(sys.argv[1],'rU'), engine='c', names=['id','rname','latitude','longitude','address','area','city','cost','rating','homedelivery','alcohol','wifi','valetparking','rooftop'])
        cuisinetiming_df = pd.read_csv(open(sys.argv[1],'rU'), engine='c')
        print(cuisinetiming_df)

        cuisinetiming_df.apply(
            save_cuisinetiming_from_row,
            axis=1
        )

        print("There are {} reviews in DB".format(CusineTiming.objects.count()))
        
    else:
        print("Please, provide Reviews file path")