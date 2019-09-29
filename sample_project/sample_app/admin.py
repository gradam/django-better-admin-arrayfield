from django.contrib import admin

from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from sample_app.models import ArrayModel


class ArrayModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.register(ArrayModel, ArrayModelAdmin)
