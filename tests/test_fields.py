from django.forms import ValidationError
from django.forms.fields import CharField

import pytest

from django_better_admin_arrayfield.forms.fields import DynamicArrayField


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


def test_default():
    default = ["1"]
    field = DynamicArrayField(CharField(max_length=10), required=True, default=default)
    data = []
    cleaned_data = field.clean(data)
    assert cleaned_data == default


def test_callable_default():
    def default():
        return ["1", "2"]

    field = DynamicArrayField(CharField(max_length=10), required=True, default=default)
    data = []
    cleaned_data = field.clean(data)
    assert cleaned_data == default()
