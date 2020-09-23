.. _user:

User
====

.. note::
    The User model base on ``AUTH_USER_MODEL``

Field settings
--------------

.. data:: USER_FIELDS

    The fields of the User use for Register and Profile

    Default:

    .. code:: python

        (
            'id',
            'username',
            'email',
            'password',
            'is_active',
        )

    Make sure your fields include ``username``, ``email``, and ``password``.

.. data:: USER_READ_ONLY_FIELDS

    The read only fields for serializers

    Default:

    .. code:: python

        (
            'is_superuser',
            'is_staff',
            'is_active',
        )

.. data:: USER_WRITE_ONLY_FIELDS

    The write only fields for Profile serializers. Make sure those fields can not update after created.

    Default:

    .. code:: python

        (
            'password',
            'username',
        )

.. data:: USER_SERIALIZER

    The User Serializer use dotted path

    Default: ``'drf_registration.api.user.UserSerializer'``

Verify/Activate settings
------------------------

Those configurations for the Register flow.

.. data:: USER_VERIFY_FIELD

    The User verify/activate field

    Default: ``'is_active'``

.. data:: USER_ACTIVATE_TOKEN_ENABLED

    Enable verify use by token sent to email

    Default: ``False``

.. data:: USER_ACTIVATE_EMAIL_SUBJECT

    The activate email subject

    Default: ``'Activate your account'``

    .. note::
        It only works with ``USER_ACTIVATE_TOKEN_ENABLED`` is ``True``

.. data:: USER_ACTIVATE_EMAIL_TEMPLATE

    The activate email template path

    Default: ``None``

    If not set, the default template message is

    .. code:: python

        <p>By clicking on the following link, you are activating your account</p>
        <a href="{activate_link}">Activate Account</a>

    .. note::
        It only works with ``USER_ACTIVATE_TOKEN_ENABLED`` is ``True``


.. data:: USER_ACTIVATE_SUCSSESS_TEMPLATE

    The template path when activate user successfully.

    Default: ``None``

    If not set, the system will show the default message is ``Your account has been activate successfully``

    .. note::
        It only works with ``USER_ACTIVATE_TOKEN_ENABLED`` is ``True``

.. data:: USER_ACTIVATE_FAILED_TEMPLATE

    The template path when activate user failed.

    Default: ``None``

    If not set, the system will show the default message is ``Either the provided activation token is invalid or this account has already been activated.``

    .. note::
        It only works with ``USER_ACTIVATE_TOKEN_ENABLED`` is ``True``
