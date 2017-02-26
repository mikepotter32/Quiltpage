from django.db import models

# Create your models here.
class Quilt(models.Model):
    cost = models.IntegerField()
    pic = models.ImageField(upload_to="media/")
    quiltID = models.CharField(max_length = 20, default="")
