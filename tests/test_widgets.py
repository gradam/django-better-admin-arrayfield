from django.template.loader import get_template

from django_better_admin_arrayfield.forms.widgets import DynamicArrayWidget


def test_template_exists():
    get_template(DynamicArrayWidget.template_name)


def test_format_value():
    widget = DynamicArrayWidget()
    assert widget.format_value("") == []
    assert widget.format_value([1, 2, 3]) == [1, 2, 3]


def test_value_from_datadict(mocker):
    widget = DynamicArrayWidget()
    test_name = "name"

    class MockData:
        @staticmethod
        def getlist(name):
            return [name]

    mocker.spy(MockData, "getlist")

    assert widget.value_from_datadict(MockData, None, test_name) == [test_name]
    assert MockData.getlist.call_count == 1


def test_value_from_datadict_get(mocker):
    widget = DynamicArrayWidget()
    test_name = "name"

    class MockData:
        @staticmethod
        def get(name):
            return name

    mocker.spy(MockData, "get")

    assert widget.value_from_datadict(MockData, None, test_name) == test_name
    assert MockData.get.call_count == 1


def test_get_context():
    widget = DynamicArrayWidget()
    value = ["1", "2", "3"]

    context = widget.get_context("name", value, [])
    assert len(context["widget"]["subwidgets"]) == len(value)
