.. reset-password:

Reset Password
==============

.. note::
    The reset password views use custom of ``PasswordResetConfirmView`` and ``PasswordResetCompleteView`` from ``django.contrib.auth.views``. The default templates from Django registration. All configurations just work if ``RESET_PASSWORD_ENABLED`` is ``True``.

.. data:: RESET_PASSWORD_ENABLED

    Enable reset password API

    Default: ``True``

.. data:: RESET_PASSWORD_PERMISSION_CLASSES

    The reset password permissions classes

    Default:

    .. code:: python

        [
            'rest_framework.permissions.AllowAny',
        ]

.. data:: RESET_PASSWORD_SERIALIZER

    The reset password serializer

    Default: ``'drf_registration.api.reset_password.ResetPasswordSerializer'``

.. data:: RESET_PASSWORD_EMAIL_SUBJECT

    The reset password email subject

    Default: ``'Reset Password'``

.. data:: RESET_PASSWORD_EMAIL_TEMPLATE

    The reset password email body template

    Default: ``None``

    If not set, it will use default email template message:

    .. code:: python

        <p>Please go to the following page and choose a new password:</p>
        <a href="{reset_password_link}">Reset Password</a>

.. data:: RESET_PASSWORD_CONFIRM_TEMPLATE

    The reset password confirm template

    Default: ``None``

    If not set, it will use the Django default registration template

.. data:: RESET_PASSWORD_SUCCESS_TEMPLATE

    The reset password success template

    Default: ``None``

    If not set, it will use the Django default registration template
