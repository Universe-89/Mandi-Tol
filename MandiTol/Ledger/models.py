from django.db import models
from Tol.models import *

# Create your models here.
class Ledger(models.Model):
    party_name = models.CharField(max_length=50,primary_key = True)
    party_address = models.CharField(max_length=50)
    party_pincode = models.IntegerField()
    party_city = models.CharField(max_length=20)
    party_state = models.CharField(max_length=20)
    party_opBal = models.IntegerField()
    objects = models.Manager()
    
    def __str__(self):
        return str(self.party_name)


class Entry(models.Model):
    party_name = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    item_name  = models.ForeignKey(Items, on_delete=models.CASCADE)
    amount     = models.DecimalField(max_digits=10, decimal_places=2)
    date_modified    = models.DateField(default=timezone.now)
    isCredit   = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.party_name + str(isCredit))

class TolDiaryAdat(models.Model):

    party_name       = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    item_name        = models.ForeignKey(Items, on_delete=models.CASCADE)
    weight           = models.IntegerField()
    rate             = models.IntegerField()
    bags             = models.IntegerField()
    extra            = models.IntegerField()
    standardBharti   = models.IntegerField()
    date_modified    = models.DateField(default=timezone.now)
    objects = models.Manager()

    def __str__(self):
        return str(self.party_name + " " + str(self.date_modified))

