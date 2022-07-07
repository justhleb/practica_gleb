from django.db import models
import datetime


class Image(models.Model):
    image = models.ImageField(upload_to='%d-%m-%Y/', blank=True)
