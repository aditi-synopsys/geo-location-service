from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('locations', views.LocationView)

urlpatterns = [
    path('', include(router.urls))
]

