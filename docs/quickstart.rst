.. _quickstart:

Quickstart
==========

All configurations in your ``settings.py``

.. note::
    We use authentication scheme uses a simple token-based HTTP Authentication scheme. Token authentication is appropriate for client-server setups, such as native desktop and mobile clients.


Add ``drf_registration`` to ``INSTALLED_APPS``. You also have to add ``rest_framework`` and ``rest_framework.authtoken`` too.

.. code:: python

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'rest_framework.authtoken',
        'drf_registration',
        ...
    ]

Configure the user model

.. code:: python

    AUTH_USER_MODEL = 'accounts.User' # You can set valid value of current system

Include urls of ``drf_registration`` in ``urls.py``

.. code:: python

    urlpatterns = [
        ...
        path('/api/accounts/', include('drf_registration.urls')),
        ...
    ]

.. note::
    Add ``path('admin/', admin.site.urls),`` to ``urlpatterns`` if ``RESET_PASSWORD_ENABLED`` is ``True`` and use default Django reset password templates.


Set ``AUTHENTICATION_BACKEND`` for support login by multiple custom fields and check inactivate user when login

.. code:: python

    AUTHENTICATION_BACKENDS = [
        'drf_registration.auth.MultiFieldsModelBackend',
    ]

You can update login username fields by change ``LOGIN_USERNAME_FIELDS`` in ``DRF_REGISTRATION`` object. Default to ``['username, email,]``.

Set ``DEFAULT_AUTHENTICATION_CLASSES`` in ``REST_FRAMEWORK`` configuration

.. code:: python

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
        ],
    }
