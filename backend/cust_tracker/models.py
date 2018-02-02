from django.db import models
from cities.models import *

# Create your models here.





class CustTracker(models.Model):
    cust_id = models.Integer(primary_key=True, null=False)
    cust_email = models.CharField(max_length=120, null=False)
    first_name = models.CharField(max_length=50, default="John", null=False)
    last_name = models.CharField(max_length=50, null=True)

class BizCities(models.Model):
    biz_city = models.CharField(max_length=80, default="Add City")
    biz_state = models.ForeignKey('BizStates', null=False, default="MO")

    def __str__(self):
        return "%s the City" % (self.biz_city, self.biz_state)


class BarberLoc(models.Model):
    barber_id = models.OneToOneField(CustTracker, related_name='host_set')
    barb_street = models.CharField(max_length=200)
    barb_city = models.CharField(max_length=100, default="Select")
    barb_state = models.CharField(max_length=2, default="MO", )
    barb_zipcode = models.SmallIntegerField()

    def __str__(self):
        return "%s the Barber location at %s" % (self.barb_city, self.barb_state)

class BizStates(models.Model):
    biz_state = models.CharField(max_length=2, null=False)