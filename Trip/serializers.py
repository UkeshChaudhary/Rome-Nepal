from rest_framework.serializers import ModelSerializer
from .models import *

#PlaceImage Serializers
# class PlaceImageSerializers(ModelSerializer):
#     class Meta:
#         model = PlaceImage
#         fields = ['id', 'image', 'description']



#Resturant Serializers
class ResturantSerializers(ModelSerializer):

    class Meta:

        model = Resturant
        fields = [
            'id',
            'name',
            'description',
            'place',
            'cuisine_type',
            'opening_hours',
            'contact_info',
            'image'
        ]



# Activity Serializer
class ActivitySerializers(ModelSerializer):


    class Meta:

        model = Activity
        fields = [
            'id',
            'name',
            'place',
            'description',
            'activity_type',
            'duration',
            'cost',
            'image'
        ]


#Place Serializers
class PlaceSerilizers(ModelSerializer):
    # images = PlaceImageSerializers(many=True, read_only=True)
    activities = ActivitySerializers(many=True, read_only = True)
    resturants = ResturantSerializers(many=True, read_only=True)

    class Meta:
        model = Place
        fields = [
            'id',
            'name',
            'description',
            'place_type',
            'images',
            'activities',
            'resturants'
        ]


# Activity Plan Serializer
class ActivityPlanSerializer(ModelSerializer):
    class Meta:
        model = ActivityPlan
        fields = ['id', 'day_plan', 'activity', 'start_time', 'duration']

# Restaurant Visit Serializer
class RestaurantVisitSerializer(ModelSerializer):
    class Meta:
        model = RestaurantVisit
        fields = ['id', 'day_plan', 'restaurant', 'time']

# Day Plan Serializer
class DayPlanSerializer(ModelSerializer):
    activity_plans = ActivityPlanSerializer(many=True, read_only=True)
    restaurant_visits = RestaurantVisitSerializer(many=True, read_only=True)

    class Meta:
        model = DayPlan
        fields = ['id', 'trip', 'date', 'notes', 'activity_plans', 'restaurant_visits']

# Trip Serializer
class TripSerializer(ModelSerializer):
    day_plans = DayPlanSerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = ['id', 'user', 'name', 'place', 'start_date', 'end_date', 'day_plans']


# Demo Plan Serialzer

class DemoSerializer(ModelSerializer):

    class Meta:
        model = Demo
        fields = '__all__'


class PlanSerializer(ModelSerializer):

    class Meta:
        model = Plan
        fields = "__all__"
        