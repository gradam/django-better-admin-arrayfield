=====
Usage
=====

To use Django better admin ArrayField in a project, add it to your `INSTALLED_APPS`:

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
