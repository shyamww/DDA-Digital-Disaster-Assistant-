from django.db import models
from django.urls import reverse


class Camp(models.Model):
    item = models.CharField(max_length=500)
    facility = models.CharField(max_length=500)
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('camp-detail', kwargs={'pk': self.pk})

    def __self__(self):
        return self.name


class Entry(models.Model):
    type = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    local = models.CharField(max_length=50)
    discription = models.TextField(max_length=1000)
    camp = models.ManyToManyField(Camp)

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})

    def __self__(self):
        return self.type
























