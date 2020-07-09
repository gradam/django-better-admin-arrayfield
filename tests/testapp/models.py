from django.db import models

from django_better_admin_arrayfield.models.fields import ArrayField


class DefaultValueNullableModel(models.Model):
    array = ArrayField(models.IntegerField(), blank=True, null=True, default=list)


class DefaultValueRequiredModel(models.Model):
    array = ArrayField(models.IntegerField(), blank=True, default=list)


class NullableNoDefaultModel(models.Model):
    array = ArrayField(models.IntegerField(), blank=True, null=True)
