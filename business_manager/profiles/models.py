from django.db import models
from django.conf import settings


class Firm(models.Model):
    name = models.CharField(max_length=255)
    sphere = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    vocation = models.CharField(max_length=255)
    firm = models.ForeignKey(Firm)

    def __str__(self):
        return self.user.username
