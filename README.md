# DRF Registration

[![Downloads](https://static.pepy.tech/personalized-badge/drf-registration?period=total&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/drf-registration)

Simple user registration package based on Django Rest Framework. DRF Registration - The easy way to generate registration RESTful APIs.

Check the document at https://drf-registration.readthedocs.io/


## Requirements
- Django (>=2.0)
- Django REST Framework (>=3.8.2)
- Python (>=3.6)


## Features
- Register
- Verify/activate account by token sent to email
- Login use token
- Logout
- User profile
- Change password
- Reset password
- Login by socials (Facebook, Google)
- Set password when login by social
- Sync user account with socials
- HTML email configuration
- Test coverage (98%)


## Installation & Configuration
Install by use `pip`:
```
pip install drf-registration
```

Add `drf_registration` in `INSTALLED_APPS`
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'drf_registration',
    ...
]
```

Include urls of `drf_registration` in `urls.py`
```
urlpatterns = [
    ...
    path('/api/accounts/', include('drf_registration.urls')),
    ...
]
```


## Settings
Set `AUTHENTICATION_BACKEND` for support login by multiple custom fields and check inactivate user when login:

```
AUTHENTICATION_BACKENDS = [
    'drf_registration.auth.MultiFieldsModelBackend',
]
```

You can update login username fields by change `LOGIN_USERNAME_FIELDS` in `DRF_REGISTRATION` object. Default to `['username', 'email',]`.

- Set `DEFAULT_AUTHENTICATION_CLASSES` in `REST_FRAMEWORK` configuration

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

### Design settings
```
DRF_REGISTRATION = {

}
```

Check default settings [here](https://drf-registration.readthedocs.io/en/latest/settings/index.html).


## Base APIs Design

Assuming that base resource is `/api/v1/accounts/`

- `POST: /register/`: Register new user
- `POST: /verify/`: Verify account by email
- `POST: /login/`: Login to the system use username/email and password
- `POST: /logout/`: Logout of the system
- `GET: /profile/`: Get user profile
- `PUT: /profile/`: Update user profile
- `PUT: /change-password/`: Change user password
- `PUT: /set-password/`: Set user password when login with social account

Check more APIs Design at [here](https://drf-registration.readthedocs.io/en/latest/apis.html).

## Command line

Unit Test
```
make test
```
*You can add `ARGS="specific_folder/"` or `ARGS="specific_file.py"` to run specific test cases.*

Run pylint
```
make pylint
```

Build & run docs local server
```
make docs
```
Access docs server at http://localhost:8080

Clean
```
make clean
```
