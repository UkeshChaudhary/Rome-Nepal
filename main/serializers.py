from rest_framework.serializers import ModelSerializer
from .models import Place, PlaceImage

#PlaceImage Serializers
class PlaceImageSerializers(ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ['id', 'image']

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

    