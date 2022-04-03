from django.contrib import admin
from .models import *


# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('date_modified',)

admin.site.register(TolDiary) 
admin.site.register(Items) 
admin.site.register(Stock_register) 