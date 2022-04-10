from django.db import models
from django.utils import timezone

# Create your models here.
class TolDiary(models.Model):

    kisan_name       = models.CharField(max_length=20)
    item_name        = models.CharField(max_length=20)
    weight           = models.IntegerField()
    rate             = models.IntegerField()
    bags             = models.IntegerField()
    extra            = models.IntegerField()
    standardBharti   = models.IntegerField()
    date_modified    = models.DateField(default=timezone.now)
    objects = models.Manager()

    def __str__(self):
        return str(self.kisan_name + " " + str(self.date_modified))

class Items (models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="emergencycontacts",null=True)
    # contact = models.EmailField()
    item_name          = models.CharField(max_length=20,primary_key = True)
    mandi_tax          = models.DecimalField(max_digits=5, decimal_places=2)
    krishikalyan_ses   = models.DecimalField(max_digits=5, decimal_places=2)
    aadat              = models.DecimalField(max_digits=5, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return str(self.item_name)

class Stock_register (models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="emergencycontacts",null=True)
    # contact = models.EmailField()
    item_name          = models.ForeignKey(Items, on_delete=models.CASCADE)
    total_amount       = models.DecimalField(max_digits=100, decimal_places=2)
    total_weight       = models.DecimalField(max_digits=100, decimal_places=2)
    average            = models.DecimalField(max_digits=100, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return str(self.item_name)
