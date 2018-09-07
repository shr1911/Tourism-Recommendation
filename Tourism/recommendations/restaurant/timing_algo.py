import numpy as np
from recommendations.models import Restaurant
import pandas as pd
import datetime


def find_timing(nearby_rid):
    print("Shraddha")

    # Getting current time and day
    now = datetime.datetime.now()
    current_time = now.strftime('%I:%M %p')
    print(current_time)
    current_day = now.strftime('%a')
    print(current_day)


    # Load timing.csv file
    df_timing = pd.read_csv('data/timing.csv', header=0)
    print(df_timing)
    array_timing = df_timing.values


    
    # Get only those which are opened today
    # Get those whose time range include current time === time_range_rid
    day_filter = array_timing[array_timing[:,2] == current_day] 
    print(day_filter)
    print("--------------------------------------------------------------")

    columns=['id','rid','day','timing','starttime','endtime']
    df = pd.DataFrame(day_filter ,columns=columns)
    print(df)
    df = df[df.starttime != 'closed']
    df = df[df.endtime != 'closed']
    df = df[df.rid != 370]
    rows, columns = df.shape
    day_filter = df.values

    print("---------------------------------------------------------------")
    #print day_filter.size
    
    in_time = datetime.datetime.strptime(current_time, "%I:%M %p")
    current_time_24hour = datetime.datetime.strftime(in_time, "%H:%M") 

    timing_rid =  []
    for x in range(0, rows):
        start_in_time = datetime.datetime.strptime(day_filter[x,4], "%I:%M %p")
        start_out_time = datetime.datetime.strftime(start_in_time, "%H:%M")
        end_in_time = datetime.datetime.strptime(day_filter[x,5], "%I:%M %p")
        end_out_time = datetime.datetime.strftime(end_in_time, "%H:%M")
        print(str(day_filter[x,1]) + " " + start_out_time + "  " + end_out_time)
        start_hr = start_out_time.split(":")[0]
        end_hr = end_out_time.split(":")[0]
        current_hr = current_time_24hour.split(":")[0]

        print(start_hr + " " + current_hr + " " + end_hr)
        start_min = start_out_time.split(":")[1]
        end_min = end_out_time.split(":")[1]
        current_min = current_time_24hour.split(":")[1]
 
     
        if(start_hr > end_hr):
             #print("SHRADDHA")
             if((start_hr < current_hr) and (start_hr < "23")) or ((end_hr > current_hr) and (end_hr > "00")):
                #print("IN THIS LOOP")
                timing_rid.append(day_filter[x,1])
             else:
             	 if(start_min < current_min) and (current_min < end_min):
             	     #print("In loop")
                     timing_rid.append(day_filter[x,1])

        else:
             if(start_hr < current_hr) and (current_hr < end_hr):
                 #print("Sherlock")
                 timing_rid.append(day_filter[x,1])
             else:
                 if(start_min < current_min) and (current_min < end_min):
             	     #print("In loop")
                     timing_rid.append(day_filter[x,1])

    print(timing_rid)
   






    # Load timing_cuisine.csv file
    df_timing_cuisine = pd.read_csv('data/timing_cuisine.csv', header=0)
    print(df_timing_cuisine)
    array_timing_cuisine = df_timing_cuisine.values
    rows, columns = df_timing_cuisine.shape

    # Get all names of cuisines which comes under current_time ===== current_time_cuisine
    timing_cusine_id =  []
    for x in range(0, rows):
        start_in_time = datetime.datetime.strptime(array_timing_cuisine[x,2], "%I:%M %p")
        start_out_time = datetime.datetime.strftime(start_in_time, "%H:%M")
        end_in_time = datetime.datetime.strptime(array_timing_cuisine[x,3], "%I:%M %p")
        end_out_time = datetime.datetime.strftime(end_in_time, "%H:%M")
        print(start_out_time + "  " + end_out_time)
        start_hr = start_out_time.split(":")[0]
        end_hr = end_out_time.split(":")[0]
        current_hr = current_time_24hour.split(":")[0]

        print(array_timing_cuisine[x,1] + " " + start_hr + " " + current_hr + " " + end_hr)
        start_min = start_out_time.split(":")[1]
        end_min = end_out_time.split(":")[1]
        current_min = current_time_24hour.split(":")[1]
 
     
        if(start_hr >= end_hr):
             #print "SHRADDHA"
             if((start_hr <= current_hr) and (start_hr <= "23")) or ((end_hr > current_hr) and (end_hr >= "00")):
                #print "IN THIS LOOP"
                timing_cusine_id.append(array_timing_cuisine[x,1])
             else:
             	 if(start_min < current_min) and (current_min < end_min):
             	     #print "In loop"
                     timing_cusine_id.append(array_timing_cuisine[x,1])

        else:
             if(start_hr <= current_hr) and (current_hr <= end_hr):
                 print("Sherlock")
                 timing_cusine_id.append(array_timing_cuisine[x,1])
             
             else:
                 if(start_min < current_min) and (current_min < end_min):
             	     #print "In loop"
                     timing_cusine_id.append(array_timing_cuisine[x,1])

    print(timing_cusine_id)



    # Load cuisines.csv file
    df_cuisine = pd.read_csv('data/cuisine.csv', header=0)
    print(df_cuisine)
    array_cuisine = df_cuisine.values
    rows, columns = df_cuisine.shape



    # From cuisine.csv select all rid which include current_time_cuisine ====== current_time_cuisine_rid
    # timing_cusine_id = np.asarray(timing_cusine_id)
    # print timing_cusine_id
    # timing_cusine_id = timing_cusine_id.ravel()
    # df_current_time_cuisine = df_cuisine.loc[df_cuisine['cuisine'].isin(timing_cusine_id)]
    # print df_current_time_cuisine


    current_time_cuisine_rid = []
    for i in range(0, len(timing_cusine_id)):
        filter_cuisine_id = array_cuisine[array_cuisine[:,2] == timing_cusine_id[i]] 
        print(filter_cuisine_id)
        rows, columns = filter_cuisine_id.shape
        for x in range(0, rows):
            current_time_cuisine_rid.append(filter_cuisine_id[x,1])

    current_time_cuisine_rid = np.asarray(current_time_cuisine_rid)
    current_time_cuisine_rid =  current_time_cuisine_rid.astype(int)


    # remove duplicates from current_time_cuisine_rid
    current_time_cuisine_rid =  np.unique(current_time_cuisine_rid)



    # Take common rid from time_range_rid and current_time_cuisine_rid //// timing_rid == current_time_cuisine_rid
    print("Restaurant which include current time based cuisine")
    print(current_time_cuisine_rid)

    timing_rid = np.asarray(timing_rid).astype(int)
    print("Restaurnt which are currenly open")
    print(timing_rid)

    timing_based_rid = np.intersect1d(current_time_cuisine_rid, timing_rid)
    print("Final rid of time based")
    print(timing_based_rid)


    #take common from nearby and timing_based_rid 
    timing_based_rid = np.intersect1d(timing_based_rid, nearby_rid)
    print(timing_based_rid)

    # return above list of rid
    return timing_based_rid