from django.db import models


class TimeStamps(object):
    """docstring for TimeStamps."""
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
