from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import AbstractUser

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()

class Scooter(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    driver = models.ForeignKey(User, related_name="driven_scooter")
    in_use = models.BooleanField(default=False)

class Trip(models.Model):
    length = models.FloatField()
    minutes = models.DecimalField()
    driver = models.ForeignKey(User, related_name="trip")
    scooter = models.ForeignKey(Scooter, related_name="trip")
