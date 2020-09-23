.. set-password:

Set Password
============

.. data:: set_PASSWORD_PERMISSION_CLASSES

    The set password permissions classes

    Default:

    .. code:: python

        [
            'rest_framework.permissions.IsAuthenticated',
        ]

.. data:: SET_PASSWORD_SERIALIZER

    The set password serializer

    Default: ``'drf_registration.api.set_password.SetPasswordSerializer'``
