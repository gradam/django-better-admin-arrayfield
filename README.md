# Django better admin ArrayField

[![image](https://badge.fury.io/py/django-better-admin-arrayfield.svg)](https://badge.fury.io/py/django-better-admin-arrayfield)

[![image](https://travis-ci.org/gradam/django-better-admin-arrayfield.svg?branch=master)](https://travis-ci.org/gradam/django-better-admin-arrayfield)

[![image](https://codecov.io/gh/gradam/django-better-admin-arrayfield/branch/master/graph/badge.svg)](https://codecov.io/gh/gradam/django-better-admin-arrayfield)

Better ArrayField widget for admin


## Quickstart

Install Django better admin ArrayField:

    pip install django-better-admin-arrayfield

Add it to your \`INSTALLED\_APPS\`:

``` python
INSTALLED_APPS = (
    ...
    'django_better_admin_arrayfield.apps.DjangoBetterAdminArrayfieldConfig',
    ...
)
```

Add Django better admin ArrayField's URL
patterns:

``` python
from django_better_admin_arrayfield import urls as django_better_admin_arrayfield_urls


urlpatterns = [
    ...
    url(r'^', include(django_better_admin_arrayfield_urls)),
    ...
]
```

## Features

  - TODO

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

Tools used in rendering this
    package:

  - [Cookiecutter](https://github.com/audreyr/cookiecutter)
  - [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
