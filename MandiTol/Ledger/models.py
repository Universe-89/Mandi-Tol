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
    party_name      = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    item_name       = models.ForeignKey(Items, on_delete=models.CASCADE)
    billId          = models.IntegerField(default=0)
    weight          = models.IntegerField(default=0)
    bags            = models.IntegerField(default=0)
    rate            = models.IntegerField(default=0)
    amount          = models.DecimalField(max_digits=10, decimal_places=2)
    extra           = models.IntegerField(default=0)
    date_modified   = models.DateField(default=timezone.now)
    standardBharti  = models.IntegerField(default=0)
    isCredit        = models.BooleanField(default=True)
    objects         = models.Manager()

    def __str__(self):
        return str(str(self.party_name) + " " + str(self.item_name))

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

class BillMetaData(models.Model):
    billId          = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    weight          = models.IntegerField(default=0)
    bags            = models.IntegerField(default=0)
    rate            = models.IntegerField(default=0)
    amount          = models.DecimalField(max_digits=10, decimal_places=2)
    extra           = models.IntegerField(default=0)
    standardBharti  = models.IntegerField(default=0)
    objects         = models.Manager()

    def __str__(self):
        return str(self.party_name)

class BillMap(models.Model):
    partyName       = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    itemName        = models.ForeignKey(Items, on_delete=models.CASCADE)
    dateModified    = models.DateField(default=timezone.now)
    billId          = models.AutoField(primary_key=True)
    objects         = models.Manager()

    def __str__(self):
        return str(str(self.billId) + " " +str(self.partyName) + " " + str(self.itemName))

