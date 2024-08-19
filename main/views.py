from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Place, PlaceImage, Resturant, ResturantImage
from .serializers import PlaceSerilizers, PlaceImageSerializers, ResturantSerializers, ResturantImageSerializers
from rest_framework.decorators import action





#Place Views
class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerilizers


    @action(detail=True, methods=['post'], url_path='upload-image')
    def upload_image(self, request, pk=None):
        try:
            place = Place.objects.get(pk=pk)
        except Place.DoesNotExist:
           return Response({'error': 'Place not found'}, status=status.HTTP_404_NOT_FOUND)
        
        image_serializer = PlaceImageSerializers(data=request.data)
        if image_serializer.is_valid():
            image_instance = image_serializer.save(place=place)
            return Response(PlaceImageSerializers(image_instance).data, status=status.HTTP_201_CREATED)
        return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#Resturant Views
class  ResturantViewSet(ModelViewSet):
    queryset = Resturant.objects.all()
    serializer_class = ResturantSerializers



    @action(detail=True, methods=['post'], url_path='upload-image')
    def upload_image(self, request, pk=None):
        try:
            resturant = Resturant.objects.get(pk=pk)
        except Resturant.DoesNotExist:
           return Response({'error': 'Resturant not found'}, status=status.HTTP_404_NOT_FOUND)
        
        image_serializer = ResturantImageSerializers(data=request.data)
        if image_serializer.is_valid():
            image_instance = image_serializer.save(resturant=resturant)
            return Response(ResturantImageSerializers(image_instance).data, status=status.HTTP_201_CREATED)
        return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)