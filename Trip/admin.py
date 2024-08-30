from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Place)
# admin.site.register(PlaceImage)
admin.site.register(Resturant)
admin.site.register(Activity)
admin.site.register(Trip)
admin.site.register(DayPlan)
admin.site.register(ActivityPlan)
admin.site.register(RestaurantVisit)



#Demo Model Registration
admin.site.register(Demo)
admin.site.register(Plan)