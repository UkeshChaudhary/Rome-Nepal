from rest_framework.serializers import ModelSerializer
from .models import Place, PlaceImage, Resturant, ResturantImage

#PlaceImage Serializers
class PlaceImageSerializers(ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ['id', 'image', 'description']

#Place Serializers
class PlaceSerilizers(ModelSerializer):
    images = PlaceImageSerializers(many=True, read_only=True)

    class Meta:
        model = Place
        fields = [
            'id',
            'name',
            'description',
            'place_type',
            'images'
        ]



#Resturant Image Serializers
class ResturantImageSerializers(ModelSerializer):
    class Meta:
        model = ResturantImage
        fields = [
            'id',
            'image',
            'description'
        ]

#Resturant Serializers
class ResturantSerializers(ModelSerializer):
    images = ResturantImageSerializers(many=True, read_only=True)

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
            'images'
        ]