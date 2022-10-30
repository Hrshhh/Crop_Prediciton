from django.db import models

# Create your models here.

class PredictCrop(models.Model):
    n = models.FloatField(null=True,blank=True)
    p = models.FloatField(null=True,blank=True)
    k = models.FloatField(null=True,blank=True)
    temperature = models.FloatField(null=True,blank=True)
    humidity = models.FloatField(null=True,blank=True)
    ph = models.FloatField(null=True,blank=True)
    rainfall = models.FloatField(null=True,blank=True)
    label = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.label
    