from django.contrib import admin
from .models import TolDiary

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('date_modified',)

admin.site.register(TolDiary) 