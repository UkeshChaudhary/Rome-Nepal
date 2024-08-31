from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Place, Resturant, Activity
from .serializers import *
from rest_framework.decorators import action





#Place Views
class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerilizers


    # @action(detail=True, methods=['post'], url_path='upload-image')
    # def upload_image(self, request, pk=None):
    #     try:
    #         place = Place.objects.get(pk=pk)
    #     except Place.DoesNotExist:
    #        return Response({'error': 'Place not found'}, status=status.HTTP_404_NOT_FOUND)
        
    #     image_serializer = PlaceImageSerializers(data=request.data)
    #     if image_serializer.is_valid():
    #         image_instance = image_serializer.save(place=place)
    #         return Response(PlaceImageSerializers(image_instance).data, status=status.HTTP_201_CREATED)
    #     return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Trip ViewSet
class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

# Day Plan ViewSet
class DayPlanViewSet(viewsets.ModelViewSet):
    queryset = DayPlan.objects.all()
    serializer_class = DayPlanSerializer

# Activity Plan ViewSet
class ActivityPlanViewSet(viewsets.ModelViewSet):
    serializer_class = ActivityPlanSerializer

    def get_queryset(self):
        trip_id = self.request.query_params.get('trip')
        if trip_id:
            trip = Trip.objects.get(id=trip_id)
            return ActivityPlan.objects.filter(day_plan__trip=trip, activity__place=trip.place)
        return ActivityPlan.objects.all()

# Restaurant Visit ViewSet
class RestaurantVisitViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantVisitSerializer

    def get_queryset(self):
        trip_id = self.request.query_params.get('trip')
        if trip_id:
            trip = Trip.objects.get(id=trip_id)
            return RestaurantVisit.objects.filter(day_plan__trip=trip, restaurant__place=trip.place)
        return RestaurantVisit.objects.all()

# Activity ViewSet (For Adding Activities)
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers

    def get_queryset(self):
        place_id = self.request.query_params.get('place', None)
        if place_id:
            return self.queryset.filter(place=place_id)
        return self.queryset

# Restaurant ViewSet (For Adding Restaurants)
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Resturant.objects.all()
    serializer_class = ResturantSerializers

    def get_queryset(self):
        place_id = self.request.query_params.get('place', None)
        if place_id:
            return self.queryset.filter(place=place_id)
        return self.queryset

class DemoViewSet(ModelViewSet):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer


class PlanViewSet(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer