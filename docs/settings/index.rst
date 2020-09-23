Settings
========

.. note::
    All setting properties in ``DRF_REGISTRATION`` object.

.. toctree::
    :maxdepth: 2

    email
    user
    register
    login
    profile
    change-password
    reset-password
    set-password
    social-login

All default settings
--------------------

.. code:: python

    DRF_REGISTRATION = {

        # General settings
        'PROJECT_NAME': 'DRF Registration',
        'PROJECT_BASE_URL': '',

        # User fields to register and response to profile
        'USER_FIELDS': (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_active',
        ),
        'USER_READ_ONLY_FIELDS': (
            'is_superuser',
            'is_staff',
            'is_active',
        ),
        'USER_WRITE_ONLY_FIELDS': (
            'password',
        ),

        'USER_SERIALIZER': 'drf_registration.api.user.UserSerializer',

        # User verify field
        'USER_VERIFY_FIELD': 'is_active',

        # Activate user by toiken sent to email
        'USER_ACTIVATE_TOKEN_ENABLED': False,
        'USER_ACTIVATE_SUCSSESS_TEMPLATE': '',
        'USER_ACTIVATE_FAILED_TEMPLATE': '',
        'USER_ACTIVATE_EMAIL_SUBJECT': 'Activate your account',
        'USER_ACTIVATE_EMAIL_TEMPLATE': '',

        # Profile
        'PROFILE_SERIALIZER': 'drf_registration.api.profile.ProfileSerializer',
        'PROFILE_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],

        # Register
        'REGISTER_SERIALIZER': 'drf_registration.api.register.RegisterSerializer',
        'REGISTER_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',
        ],
        'REGISTER_SEND_WELCOME_EMAIL_ENABLED': False,
        'REGISTER_SEND_WELCOME_EMAIL_SUBJECT': 'Welcome to the system',
        'REGISTER_SEND_WELCOME_EMAIL_TEMPLATE': '',

        # Login
        'LOGIN_SERIALIZER': 'drf_registration.api.login.LoginSerializer',
        'LOGIN_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',
        ],

        # For custom login username fields
        'LOGIN_USERNAME_FIELDS': ['username', 'email',],

        'LOGOUT_REMOVE_TOKEN': False,

        # Change password
        'CHANGE_PASSWORD_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'CHANGE_PASSWORD_SERIALIZER': 'drf_registration.api.change_password.ChangePasswordSerializer',

        # Reset password
        'RESET_PASSWORD_ENABLED': True,
        'RESET_PASSWORD_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',
        ],
        'RESET_PASSWORD_SERIALIZER': 'drf_registration.api.reset_password.ResetPasswordSerializer',
        'RESET_PASSWORD_EMAIL_SUBJECT': 'Reset Password',
        'RESET_PASSWORD_EMAIL_TEMPLATE': '',
        'RESET_PASSWORD_CONFIRM_TEMPLATE': '',
        'RESET_PASSWORD_SUCCESS_TEMPLATE': '',

        # Social register/login
        'FACEBOOK_LOGIN_ENABLED': False,
        'GOOGLE_LOGIN_ENABLED': False,

        # Set password in the case login by socials
        'SET_PASSWORD_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'SET_PASSWORD_SERIALIZER': 'drf_registration.api.set_password.SetPasswordSerializer',
    }

