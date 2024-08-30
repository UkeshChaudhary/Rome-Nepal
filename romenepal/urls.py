from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Trip.views import *
from django.conf import settings    
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'trips', TripViewSet, basename='trip')
router.register(r'day-plans', DayPlanViewSet, basename='dayplan')
router.register(r'activity-plans', ActivityPlanViewSet, basename='activityplan')
router.register(r'restaurant-visits', RestaurantVisitViewSet, basename='restaurantvisit')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')
router.register(r'demo', DemoViewSet, basename='demo')
router.register(r'plan', PlanViewSet, basename='plan')


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

