from django.db import models

# Create your models here.
class CustTracker(models.Model):
    cust_id = models.Integer(null=False)
    cust_email = models.CharField(max_length=120, null=False)
