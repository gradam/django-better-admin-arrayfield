from django.db import models

from django_better_admin_arrayfield.models.fields import ArrayField


class ArrayModel(models.Model):
    sample_array = ArrayField(models.CharField(max_length=20), blank=True, null=True)
