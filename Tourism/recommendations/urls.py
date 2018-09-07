# accounts/urls.py
from django.conf.urls import url
from recommendations import views
#from django.contrib import admin



urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    #url(r'^mylink/$', core_views.mylinkview, name='mylink'),
    #url(r'^review_list/$', core_views.review_list, name='review_list'),
    #url(r'^add_survey/$', core_views.add_survey, name='add_survey'),
    url(r'^user/(?P<user_id>[0-9]+)/add_survey/$', views.add_survey, name='add_survey'),
    #'myproject.views'
    #url(r'^$', core_views.lastpage, name='lastpage'),
    url(r'^explore/(?P<user_id>[0-9]+)/explore/$', views.explore, name='explore'),

    # ex: restaurant/recommend/nearby
	url(r'^restaurant/recommend/(?P<algo_type>\w+)$', views.input_cuisine, name='input_cuisine'),
	
    # ex: restaurant/recommend/list/nearby
	url(r'^restaurant/recommend/list/(?P<algo_type>\w+)$', views.recommendation_list, name='recommendation_list'),
    
    # ex: restaurant/recommend/detail/867
    url(r'^restaurant/recommend/detail/(?P<resataurant_id>[0-9]+)/$', views.restaurant_detail, name='restaurant_detail'),

    url(r'^restaurant/recommend/time/$', views.timing_list, name='timing_list'),
]