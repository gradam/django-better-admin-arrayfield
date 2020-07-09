from typing import Type

from django.forms import ModelForm, IntegerField

import pytest

from django_better_admin_arrayfield.forms.fields import DynamicArrayField
from tests.testapp.models import DefaultValueNullableModel, DefaultValueRequiredModel, NullableNoDefaultModel


def form_factory(model, **attrs) -> Type[ModelForm]:
    meta = type("Meta", (), {"model": model, "fields": ["array"]})
    return type("SampleForm", (ModelForm,), {"Meta": meta, **attrs})


class TestDefaultValue:
    @pytest.mark.parametrize(
        "model_class,init_value,expected_value",
        (
            (DefaultValueNullableModel, None, []),
            (NullableNoDefaultModel, None, None),
            (DefaultValueRequiredModel, None, []),
            (DefaultValueNullableModel, [1], [1]),
            (NullableNoDefaultModel, [1], [1]),
            (DefaultValueRequiredModel, [1], [1]),
        ),
    )
    def test_default_list(self, model_class, init_value, expected_value):
        data = {}
        if init_value is not None:
            data["array"] = init_value

        form = form_factory(model_class)(data=data)
        assert form.is_valid()
        assert form.cleaned_data["array"] == expected_value


class TestFormDefaultField:
    @pytest.mark.parametrize(
        "model_class,init_value,expected_value",
        (
            (DefaultValueNullableModel, None, [1]),
            (NullableNoDefaultModel, None, [1]),
            (DefaultValueRequiredModel, None, [1]),
            (DefaultValueNullableModel, [2], [2]),
            (NullableNoDefaultModel, [2], [2]),
            (DefaultValueRequiredModel, [2], [2]),
        ),
    )
    def test_default_different_values(self, model_class, init_value, expected_value):
        default = [1]
        data = {}
        if init_value is not None:
            data["array"] = init_value

        field = DynamicArrayField(IntegerField(), required=True, default=default)

        form = form_factory(model_class, array=field)(data=data)
        assert form.is_valid()
        assert form.cleaned_data["array"] == expected_value
