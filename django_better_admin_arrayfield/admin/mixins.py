from django.templatetags.static import static


class DynamicArrayMixin:
    class Media:
        js = (static("js/min/django_better_admin_arrayfield.min.js"),)
        css = {"all": (static("css/min/django_better_admin_arrayfield.min.css"),)}
