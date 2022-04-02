from django.db import models

# Create your models here.
class TolDiary(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="emergencycontacts",null=True)
    # contact = models.EmailField()
    kisan_name       = models.CharField(max_length=20)
    item_name        = models.CharField(max_length=20)
    weight           = models.IntegerField()
    rate             = models.IntegerField()
    bags             = models.IntegerField()
    extra            = models.IntegerField()
    standardBharti   = models.IntegerField()
    date_modified    = models.DateTimeField(auto_now_add=True)
    # phone = PhoneField()
    objects = models.Manager()

    def __str__(self):
        return str(self.kisan_name + " " + str(self.date_modified))
