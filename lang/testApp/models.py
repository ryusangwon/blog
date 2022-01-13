from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    nation = models.CharField(max_length=20)
    nation_img = models.CharField(max_length=255)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name