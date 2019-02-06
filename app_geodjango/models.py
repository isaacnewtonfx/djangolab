from django.contrib.gis.db import models
from elasticsearch_dsl import DocType, Text, Float



class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class places(models.Model):
    place_type = models.CharField(max_length=255, blank=True, null=True)
    place_name = models.CharField(max_length=255, blank=True, null=True)
    admin1 = models.CharField(max_length=255, blank=True, null=True)
    admin2 = models.CharField(max_length=255, blank=True, null=True)
    admin3 = models.CharField(max_length=255, blank=True, null=True)
    floor = models.CharField(max_length=255, blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    # GeoDjango-specific: a geometry field (MultiPointField) SRID = 4326 by default
    geom = models.MultiPointField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.address


# class PlacesIndex(DocType):
#     place_type = Text()
#     place_name = Text()
#     admin1 = Text()
#     admin2 = Text()
#     admin3 = Text()
#     floor = Text()
#     room =Text()
#     lon = Float()
#     lat = Float()
#     address = Text()
#     geom = Text()
    

#     class Meta:
#         index = 'places2'