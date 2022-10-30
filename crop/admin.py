from django.contrib import admin
from .models import PredictCrop

# Register your models here.

class CropModel(admin.ModelAdmin):
    list_display = ['n','k','p','temperature','humidity','ph','rainfall','label']

admin.site.register(PredictCrop,CropModel)