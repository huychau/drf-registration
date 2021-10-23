from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status


class NotActivated(APIException):
    """
    Custom not activate exception when user is not activated

    Args:
        APIException (class): Base class for exceptions
    """
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Account is not activated.')
    default_code = 'not-activated'


class LoginFailed(APIException):
    """
    Custom login failure exception when the credentials are invalid

    Args:
        APIException (class): Base class for exceptions
    """
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Login failed wrong user credentials.')
    default_code = 'login-failed'


class UserNotFound(APIException):
    """
    Custom user not found exception when user is not found

    Args:
        APIException (class): Base class for exceptions
    """
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('User not found.')
    default_code = 'user-not-found'


class InvalidProvider(APIException):
    """
    Custom provider invalid exception

    Args:
        APIException (class): Base class for exceptions
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Provider is invalid or you forgot enable social login.')
    default_code = 'invalid-provider'


class InvalidAccessToken(APIException):
    """
    Custom invalid access token exception

    Args:
        APIException (class): Base class for exceptions
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('This access token is invalid or is already expired.')
    default_code = 'invalid-access-token'


class MissingEmail(APIException):
    """
    Custom missing email exception

    Args:
        APIException (class): Base class for exceptions
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Missing email address.')
    default_code = 'missing-email'
