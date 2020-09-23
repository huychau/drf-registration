.. email:

Email
=====

.. note::

    We are using the ``django.core.mail`` module and default configurations of SMTP server.

    You just need config email if you enabled send email in the Registration flow such as ``USER_ACTIVATE_TOKEN_ENABLED``, ``REGISTER_SEND_WELCOME_EMAIL_ENABLED`` and ``RESET_PASSWORD_ENABLED``.

Default settings
-----------------

Add the SMTP configurations in your settings

.. code:: python

    # Default configurations
    EMAIL_HOST = 'smtp.mailserver.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'username'
    EMAIL_HOST_PASSWORD = 'hostpassword'
    EMAIL_USE_TLS = True

    # Default from email
    DEFAULT_FROM_EMAIL = 'info@testingdomain.com'

Template settings
-----------------

The settings in ``DRF_REGISTRATION`` object, to custom activate email template, make sure you have set ``USER_ACTIVATE_TOKEN_ENABLED`` is ``True``.

Context support:
    - ``activate_link``: The activate link
    - ``domain``: Current domain

.. data:: USER_ACTIVATE_EMAIL_SUBJECT

    The activate email subject

    Default: ``'Activate your account'``


.. data:: USER_ACTIVATE_EMAIL_TEMPLATE

    The activate email template path

    Default: ``None``

    If not set, the default template message is

    .. code:: python

        <p>By clicking on the following link, you are activating your account</p>
        <a href="{activate_link}">Activate Account</a>

Custom welcome email template, make sure you have set ``REGISTER_SEND_WELCOME_EMAIL_ENABLED`` is ``True``.

Context support:
    - ``user``: the user information object.

.. data:: REGISTER_SEND_WELCOME_EMAIL_SUBJECT

    The welcome email subject

    Default: ``'Welcome to the system'``


.. data:: REGISTER_SEND_WELCOME_EMAIL_TEMPLATE

    The welcome email template path

    Default: ``None``

    If not set, the default template message is

    .. code:: python

        <p>Hi,</p>
        <p>Welcome to the system!</p>

Custom reset password email template, make sure you have set ``RESET_PASSWORD_ENABLED``.

Context support:
    - ``reset_password_link``: The reset password link
    - ``domain``: Current domain

.. data:: RESET_PASSWORD_EMAIL_SUBJECT

    The welcome email subject

    Default: ``'Reset Password'``


.. data:: RESET_PASSWORD_EMAIL_TEMPLATE

    The reset password email body template path

    Default: ``None``

    If not set, the default template message is

    .. code:: python

        <p>Please go to the following page and choose a new password:</p>
        <a href="{reset_password_link}">Reset Password</a>
