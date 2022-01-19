from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_test

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, unique=True, error_messages={'unique':'중복 금지'} ,validators=[MinLengthValidator, validate_test])
    nation = models.CharField(max_length=20)
    nation_img = models.CharField(max_length=255)
    age = models.IntegerField(validators=[validate_test])

    def __str__(self):
        return self.name