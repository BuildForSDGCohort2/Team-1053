from django.db import models


class TimeStamps(models.Model):
    """docstring for TimeStamps."""
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
