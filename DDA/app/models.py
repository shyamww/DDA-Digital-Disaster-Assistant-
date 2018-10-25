from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Camp(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    items = models.CharField(max_length=500)
    facility = models.CharField(max_length=500)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('camp-detail', kwargs={'pk': self.pk})

    def __self__(self):
        return self.name


class Entry(models.Model):
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2020), MinValueValidator(1800)])
    type = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    local = models.CharField(max_length=50)
    discription = models.TextField(max_length=5000)
    photo = models.ImageField(upload_to='image/', verbose_name='insert_image', null=False, blank=True)
    camp = models.ManyToManyField('Camp')

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})

    def __self__(self):
        return self.type























