# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from recommendations.forms import SignUpForm, UserSurveyForm

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render_to_response, get_object_or_404
#import models, forms
from .models import UserSurvey
import numpy as np



from .models import Restaurant
from recommendations.restaurant.forms import CuisineForm

from recommendations.restaurant.nearby import find_nearby
from recommendations.restaurant.rating_algo import find_rating
from recommendations.restaurant.price_algo import find_price
from recommendations.restaurant.user_personalized import find_personalized
from recommendations.restaurant.timing_algo import find_timing
import pandas as pd


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('add_survey', user_id=user.id)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def add_survey(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    #print(np.array(list(user)))
    form = UserSurveyForm()
    return render(request, 'add_survey.html', {'user': user, 'form': form})

def explore(request, user_id):
    print(user_id)
    user = get_object_or_404(User, pk=user_id)
    form = UserSurveyForm(request.POST)
    if form.is_valid():
            #user_name = form.cleaned_data['username']
        home_delivery = form.cleaned_data['home_delivery']
        smoking = form.cleaned_data['smoking']
        alcohol = form.cleaned_data['alcohol']
        wifi = form.cleaned_data['wifi']
        valetparking = form.cleaned_data['valetparking']
        rooftop = form.cleaned_data['rooftop']
        usersurvey = UserSurvey()
        #sersurvey = UserSurvey.save(commit=False)
        #usersurvey.user = request.user
        #usersurvey = f.save(commit=False)
        #usersurvey.user = user_id
            #usersurvey.user_name = user_name
        usersurvey.user = user
        usersurvey.home_delivery = home_delivery
        usersurvey.smoking = smoking
        usersurvey.alcohol = alcohol
        usersurvey.wifi = wifi
        usersurvey.valetparking = valetparking
        usersurvey.rooftop = rooftop
        usersurvey.save()
        return render(request, 'explore.html', {'user': user})
        #return HttpResponseRedirect(reverse('lastpage.html', args=(user.id,)))
        #return render(request, 'add_survey.html', {'user': user, 'usersurvey' : usersurvey})
        #return redirect('lastpage', user_id=user.id)

    else:
        form = UserSurveyForm()
        return render(request, 'add_survey.html', {'user': user, 'form': form})
 

 ##############################################################

 # Takes input from user about the cuisine they want to have
def input_cuisine(request, algo_type):
    if algo_type == 'timing':
        print("####### IN timing")
        return redirect(reverse('recommendations/timing_list'))
    else:
        print("####### NOT IN timing")
        form = CuisineForm()
        return render(request, 'restaurant/input_cuisine.html', {'form': form, 'algo_type': algo_type})

# Displays list of restaurants to be recommended based on what type of recommedation user wants
def recommendation_list(request, algo_type):
    # Get form which was submitted in input_cuisine.html
    form = CuisineForm(request.POST)
    if form.is_valid():
        cuisine = request.POST['cuisine']
        
        # Call find_nearby() function for recommending near by restaurants
        if algo_type == 'nearby':
            nearby_rid = find_nearby()
            # recommend_rid = np.delete(nearby_rid, 883)
            recommend_rid = nearby_rid

        
        # First call find_nearby() function to find near by restaurants
        # Second call find_rating() for recommending rating wise recommendation
        if algo_type == 'rating':
            nearby_rid = find_nearby()
            rating_based = find_rating(nearby_rid, cuisine)
            recommend_rid = rating_based


        if algo_type == 'price':
            nearby_rid = find_nearby()
            price_based = find_price(nearby_rid, cuisine)
            recommend_rid = price_based


        if algo_type == 'personalized':
            nearby_rid = find_nearby()
            user_personalized_based = find_personalized(nearby_rid, cuisine)
            recommend_rid = user_personalized_based


        # Above recommend_rid stores id of restaurnts that has to be display
        # Below code gets Restaurant objects for that all ids stored in recommend_rid
        # We store all those Restaurant objects in restaurant_list
        restaurants = Restaurant.objects.filter(id__in=recommend_rid)
        restaurants = dict([(obj.id, obj) for obj in restaurants])
        restaurant_list = [restaurants.get(ids, 0) for ids in recommend_rid]
        restaurant_list = filter(lambda a: a != 0, restaurant_list)
        #print restaurant_list

        # Send recommended restaurant list to recommendation_list.html template for displaying
        return render(request, 'restaurant/recommendation_list.html', {'cuisine' : cuisine, 'restaurant_list' : restaurant_list})
    else:
        # if form is not valid render same page
        form = CuisineForm()
        return render(request, 'restaurant/input_cuisine.html', {'form': form})


def timing_list(request):
    nearby_rid = find_nearby()
    timing_based = find_timing(nearby_rid)
    recommend_rid = timing_based

    restaurants = Restaurant.objects.filter(id__in=recommend_rid)
    restaurants = dict([(obj.id, obj) for obj in restaurants])
    restaurant_list = [restaurants.get(ids, 0) for ids in recommend_rid]
    restaurant_list = filter(lambda a: a != 0, restaurant_list)
        #print restaurant_list

    # Send recommended restaurant list to recommendation_list.html template for displaying
    return render(request, 'restaurant/timing_list.html', {'restaurant_list' : restaurant_list})


# when clicks on any restaurant from list it shows detail of that restaurant
def restaurant_detail(request, resataurant_id):
    restaurant = get_object_or_404(Restaurant, pk=resataurant_id)
    return render(request, 'restaurant/restaurant_detail.html', {'restaurant': restaurant})





    