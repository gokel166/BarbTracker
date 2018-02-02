from django.db import models

# Create your models here.
class CustTracker(models.Model):
    cust_id = models.Integer(primary_key=True, null=False)
    cust_email = models.CharField(max_length=120, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50)
    barber_id = models.ForeignKey(User, related_name='host_set')
