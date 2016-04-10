from django.core.urlresolvers import reverse
from django.db import models


class Purpose(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('purposes:list')
