from django.contrib import admin
from .models import Place, PlaceImage, Resturant, ResturantImage

# Register your models here.

admin.site.register(Place)
admin.site.register(PlaceImage)
admin.site.register(Resturant)
admin.site.register(ResturantImage)