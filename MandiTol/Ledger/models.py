from django.db import models

# Create your models here.
class Ledger(models.Model):
    party_name = models.CharField(max_length=50)
    party_address = models.CharField(max_length=50)
    party_pincode = models.IntegerField()
    party_city = models.CharField(max_length=20)
    party_state = models.CharField(max_length=20)
    party_opBal = models.IntegerField()
    
    def __str__(self):
        return str(self.party_name)

