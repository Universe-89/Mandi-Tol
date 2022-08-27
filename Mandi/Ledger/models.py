from django.db import models

# Create your models here.
class Ledger(models.Model):
    name        = models.CharField(max_length=50,primary_key = True)
    address     = models.CharField(max_length=50)
    pincode     = models.IntegerField()
    city            = models.CharField(max_length=20)
    state        = models.CharField(max_length=20)
    opBal        = models.IntegerField()
    GSTIN        = models.CharField(max_length=15)
    phoneNumber = models.CharField(max_length=10)
    objects = models.Manager()
    
    def __str__(self):
        return str(self.name)