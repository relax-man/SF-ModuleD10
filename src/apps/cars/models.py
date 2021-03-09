from django.db import models
from colorfield.fields import ColorField 

from django.template.defaultfilters import slugify
from os import path


def upload_car_photo_path(instance, filename):
    return f'cars/{slugify(str(instance))}{path.splitext(filename)[1]}'


class Car(models.Model):

    TRANSMISSION_CHOICES = [
        (1, 'Mechanics'),
        (2, 'Automatic'),
        (3, 'Robot')
    ]

    producer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=upload_car_photo_path, blank=True, null=True)

    issue_year = models.IntegerField()
    transmission = models.SmallIntegerField(choices=TRANSMISSION_CHOICES)

    color = ColorField()

    def __str__(self):
        return f'{self.producer} {self.model}'
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
