from django.db import models
from .validators import validate_name_starting_with_a

# Create your models here.
class Entity(models.Model):
    name = models.CharField(max_length=50, validators = [validate_name_starting_with_a])