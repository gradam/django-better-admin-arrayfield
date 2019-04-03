import pytest

from django_better_admin_arrayfield.forms.fields import DynamicArrayField
from django.forms.fields import CharField
from django.forms import ValidationError


def test_field_not_required():
    field = DynamicArrayField(CharField(max_length=10), required=False)
    data = []
    field.clean(data)
    data = ["12", "13"]
    field.clean(data)


def test_field_required():
    field = DynamicArrayField(CharField(max_length=10), required=True)
    data = []
    with pytest.raises(ValidationError):
        field.clean(data)
    data = ["12", "13"]
    field.clean(data)
