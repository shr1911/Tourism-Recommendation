from django.contrib import admin

# Register your models here.
from .models import UserSurvey, Restaurant, Cuisine, Payment, Timing, CusineTiming

class UserSurveyadmin(admin.ModelAdmin):
    model = UserSurvey
    list_display = ('user','home_delivery', 'smoking', 'alcohol', 'wifi', 'valetparking', 'rooftop')
    #list_filter = ['pub_date', 'user_name']
    #search_fields = ['comment']

class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    list_display = ('id','rname', 'latitude', 'longitude', 'address', 'area','city','price','rating','homedelivery','smoking','alcohol','wifi','valetparking','rooftop')
    list_filter = ['area', 'rating']
    #search_fields = ['comment']

class CuisineAdmin(admin.ModelAdmin):
    model = Cuisine
    list_display = ('id','rid', 'cuisine')
    list_filter = ['cuisine']

class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ('id','rid', 'payment')
    list_filter = ['payment']

class TimingAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ('id','rid', 'day', 'timing', 'starttime', 'endtime')
    list_filter = ['day']

class CusineTimingAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ('id','cuisine', 'starttime', 'endtime')
    list_filter = ['cuisine']
    
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Timing, TimingAdmin)
admin.site.register(CusineTiming, CusineTimingAdmin)
admin.site.register(UserSurvey, UserSurveyadmin)