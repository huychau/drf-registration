.. _login:

Login
=====

.. data:: LOGIN_SERIALIZER

    Login serializer dotted path

    Default: ``'drf_registration.api.login.LoginSerializer'``

.. data:: LOGIN_PERMISSION_CLASSES

    Login permission classes dotted paths

    Default:

    .. code:: python

        [
            'rest_framework.permissions.AllowAny',
        ],

.. data:: LOGIN_USERNAME_FIELDS:

    Custom multiple login username fields.

    Default: ``['username', 'email',]``
