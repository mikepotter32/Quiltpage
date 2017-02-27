from django.db import models

# Create your models here.
class Quilt(models.Model):
    cost = models.IntegerField()
    pic = models.ImageField(upload_to="pics/%Y/%m/%d")
    quiltID = models.CharField(max_length = 20, default="")
