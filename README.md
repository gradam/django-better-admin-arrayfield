# Django better admin ArrayField

[![image](https://badge.fury.io/py/django-better-admin-arrayfield.svg)](https://badge.fury.io/py/django-better-admin-arrayfield)

[![image](https://travis-ci.org/gradam/django-better-admin-arrayfield.svg?branch=master)](https://travis-ci.org/gradam/django-better-admin-arrayfield)

[![image](https://codecov.io/gh/gradam/django-better-admin-arrayfield/branch/master/graph/badge.svg)](https://codecov.io/gh/gradam/django-better-admin-arrayfield)

Better ArrayField widget for admin

Supported Python versions: 3.5, 3.6, 3.7
Supported Django versions: 1.11, 2.0, 2.1, 2.2

It changes comma separated widget to list based in admin panel.

Before:
![Alt text](readme_images/before.jpg?raw=true "Before")

After:
![Alt text](readme_images/after.png?raw=true "After")

## Quickstart

Install Django better admin ArrayField:

    pip install django-better-admin-arrayfield

Add it to your \`INSTALLED\_APPS\`:

```python
INSTALLED_APPS = (
    ...
    'django_better_admin_arrayfield.apps.DjangoBetterAdminArrayfieldConfig',
    ...
)
```


## Usage

`django_better_admin_arrayfield.models.fields.ArrayField` is a drop-in replacement for standard Django `ArrayField`.

In your admin class add `DynamicArrayMixin`:

```python
class MyModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    ...
```

That's it.

## Running Tests

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

## Pre-commit hooks

Install pre-commit black hook

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_dev.txt
    (myenv) $ pre-commit install

## Credits

Inspired by: https://stackoverflow.com/a/49370480/4638248

Tools used in rendering this
    package:

  - [Cookiecutter](https://github.com/audreyr/cookiecutter)
  - [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
