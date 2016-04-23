from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings

from core.models import TimeStampedModel


class Purpose(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['-modified']

    def get_absolute_url(self):
        return reverse('purposes:list')
