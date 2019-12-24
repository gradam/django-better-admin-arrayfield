from itertools import chain

from django import forms
from django.contrib.postgres.utils import prefix_validation_error
from django_better_admin_arrayfield.forms.widgets import DynamicArrayWidget


class DynamicArrayField(forms.Field):

    default_error_messages = {"item_invalid": "Item %(nth)s in the array did not validate: "}

    def __init__(self, base_field, **kwargs):
        self.base_field = base_field
        self.max_length = kwargs.pop("max_length", None)
        kwargs.setdefault("widget", DynamicArrayWidget)
        super().__init__(**kwargs)

    def clean(self, value):
        cleaned_data = []
        errors = []
        value = list(filter(None, value))
        if not value:
            cleaned_data = None
        for index, item in enumerate(value):
            try:
                cleaned_data.append(self.base_field.clean(item))
            except forms.ValidationError as error:
                errors.append(
                    prefix_validation_error(
                        error, self.error_messages["item_invalid"], code="item_invalid", params={"nth": index}
                    )
                )
        if errors:
            raise forms.ValidationError(list(chain.from_iterable(errors)))
        if not cleaned_data and self.required:
            raise forms.ValidationError(self.error_messages["required"])
        return cleaned_data

    def has_changed(self, initial, data):
        if not data and not initial:
            return False
        return super().has_changed(initial, data)
