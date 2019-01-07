from django.shortcuts import render
from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance


from django.contrib.gis.geos import Point


class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        """ This view shouldn't return a list of all the purchases. Currently for the authenticated user"""
        #obj = Location.objects.filter(city="chandigarh").values()
            #('-country','lat', 'lng')
        cit = 'chandigarh'
        obj = Location.objects.filter(city__startswith=cit)

        distance_m = 2000



        #res = Location.objects.filter(pt__distance_lte=(origin, D(m=distance_m))).distance(ref_location).order_by('pt__distance')


        point = Location.objects.get(city='Chandigarh')


        for chapter in Location.objects.filter(id=point.id):
            lt = chapter.lat
            lng = chapter.lng
            print(lt, chapter.coords.distance)

        origin = Point(lt, lng)
        # print(origin)

        res = Location.objects.filter(coords__distance_lte=(origin, D(m=distance_m))).distance(origin).order_by('coords__distance')[:1][0]

        #closest_spot = Location.objects.filter(coords__distance_lte=(origin, D(m=distance_m))).distance(origin).order_by('coords__distance')[:1][0]

        #res = Location.objects.filter(coords__distance_lte=(origin, D(m=distance_m))).distance(origin).order_by('coords__distance')[:1][0]

        print("element = ", res)

        '''
        for cur in obj:
            lat = cur['lat']
            lng = cur['lng']

        

        pnt = GEOSGeometry('POINT(%s %s)' % (lat, lng))
        qs = Location.objects.filter(point__distance_lte=(pnt, D(km=20)))
        print("qs", qs)
        '''
        return obj