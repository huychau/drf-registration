.. _register:

Register
========

You can check the :ref:`user` for thre Register flow configurations.


.. data:: REGISTER_SERIALIZER

    Register serializer dotted path

    Default: ``'drf_registration.api.register.RegisterSerializer'``


.. data:: REGISTER_PERMISSION_CLASSES

    Register permission classes dotted paths

    Default:

    .. code:: python

        [
            'rest_framework.permissions.AllowAny',
        ]

.. data:: REGISTER_SEND_WELCOME_EMAIL_ENABLED

    Send welcome email afer register successfully

    Default: ``False``

.. data:: REGISTER_SEND_WELCOME_EMAIL_SUBJECT

    The welcome email subject

    Default: ``'Welcome to the system'``

    .. note::
        It only works with ``REGISTER_SEND_WELCOME_EMAIL_ENABLED`` is ``True``

.. data:: REGISTER_SEND_WELCOME_EMAIL_TEMPLATE

    The welcome email template path

    Default: ``None``

    If not set, the default message is

    .. code:: python

        <p>Hi,</p>
        <p>Welcome to the system!</p>

    .. note::
        It only works with ``REGISTER_SEND_WELCOME_EMAIL_ENABLED`` is ``True``
