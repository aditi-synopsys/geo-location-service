from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin
from .models import Location


@admin.register(Location)
class LocationAdmin(GeoModelAdmin):
    list_display = ('city', 'lat', 'lng')
