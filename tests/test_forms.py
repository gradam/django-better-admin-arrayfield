from typing import Type

from django.forms import ModelForm

import pytest

from tests.testapp.models import DefaultValueNullableModel, DefaultValueRequiredModel, NullableNoDefaultModel


def form_factory(model) -> Type[ModelForm]:
    meta = type("Meta", (), {"model": model, "fields": ["array"]})
    return type("SampleForm", (ModelForm,), {"Meta": meta})


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
