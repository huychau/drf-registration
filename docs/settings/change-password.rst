.. _change-password:

Change Password
===============

.. data:: CHANGE_PASSWORD_PERMISSION_CLASSES

    The change password permissions classes

    Default:

    .. code:: python

        [
            'rest_framework.permissions.IsAuthenticated',
        ]

.. data:: CHANGE_PASSWORD_SERIALIZER

    The change password serializer

    Default: ``'drf_registration.api.change_password.ChangePasswordSerializer'``
