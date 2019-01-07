from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager
#from django.contrib.auth.models import AbstractUser

'''
class User(AbstractUser):
    location = gis_models.PointField("longitude/latitude",
                                     geography=True, blank=False, null=True)
'''

class Location(gis_models.Model):
    city = gis_models.CharField(max_length=64)
    lat = gis_models.FloatField(max_length=20)
    lng = gis_models.FloatField(max_length=20)
    country = gis_models.CharField(max_length=45)
    coords = gis_models.PointField(null=False, blank=False, srid=4326, verbose_name="loc", default=False)

    objects = GeoManager()


'''
    def __unicode__(self):
        return "%s, %s (%s)" % (self.city, self.country)
'''