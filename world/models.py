from __future__ import unicode_literals

from django.contrib.gis.db import models
# Create your models here.


class WorldBorder(models.Model):
	name = models.CharField(max_length = 50)
	area = models.IntegerField()
	pop2005 = models.IntegerField('Populcation 2005')
	fips = models.CharField('FIPS Code', max_length = 2)
	iso2 = models.CharField('2 Digit ISO', max_length = 2)
	iso3 = models.CharField('2 Digit ISO', max_length = 3)
	un = models.IntegerField('United Nations Code')
	region = models.IntegerField('Region Code')
	subregion = models.IntegerField('Sub-Region Code')
	lon = models.FloatField()
	lat = models.FloatField()

	mpoly = models.MultiPolygonField()

	def __str__(self):
		return self.name