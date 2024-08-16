from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Place, PlaceImage
from .serializers import PlaceSerilizers, PlaceImageSerializers
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