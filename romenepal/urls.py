from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import PlaceViewSet
from django.conf import settings    
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)



urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

