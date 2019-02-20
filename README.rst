================================
Django better admin ArrayField
================================

.. image:: https://badge.fury.io/py/django-better-admin-arrayfield.svg
    :target: https://badge.fury.io/py/django-better-admin-arrayfield

.. image:: https://travis-ci.org/gradam/django-better-admin-arrayfield.svg?branch=master
    :target: https://travis-ci.org/gradam/django-better-admin-arrayfield

.. image:: https://codecov.io/gh/gradam/django-better-admin-arrayfield/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/gradam/django-better-admin-arrayfield

Better ArrayFied widget for admin

Documentation
-------------

The full documentation is at https://django-better-admin-arrayfield.readthedocs.io.

Quickstart
----------

Install Django better admin ArrayField::

    pip install django-better-admin-arrayfield

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_better_admin_arrayfield.apps.DjangoBetterAdminArrayfieldConfig',
        ...
    )

Add Django better admin ArrayField's URL patterns:

.. code-block:: python

    from django_better_admin_arrayfield import urls as django_better_admin_arrayfield_urls


    urlpatterns = [
        ...
        url(r'^', include(django_better_admin_arrayfield_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
