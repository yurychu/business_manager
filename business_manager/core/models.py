from django.db import models


class TimeStampedModel(models.Model):
    """
    Абстрактный класс для добавления автообновляющихся полей
    даты создания и даты обновления в модель
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
