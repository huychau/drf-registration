from django.contrib.auth import get_user_model as django_get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.authtoken.models import Token

from drf_registration.settings import drfr_settings
from drf_registration.utils.common import import_string


def get_user_model():
    """
    Get user model base on AUTH_USER_MODEL
    """

    return django_get_user_model()


def get_all_users():
    """
    Get all users  queryset
    """

    return get_user_model().objects.all()


def get_user_serializer():
    """
    Get user serializer from settings
    """

    return import_string(drfr_settings.USER_SERIALIZER)


def get_user_token(user):
    """
    Get or create token for user

    Args:
        user (dict): The user instance

    Returns:
        [str]: The user token
    """

    token, created = Token.objects.get_or_create(user=user)

    return token


def remove_user_token(user):
    """
    Remove user token

    Args:
        user (dict): The user instance

    """

    # Remove old token
    Token.objects.filter(user=user).delete()


def get_user_profile_data(user):
    """
    Get user refresh token and access token

    Args:
        user (dict): The user instance

    Returns:
        [dict]: The data response include the token
    """

    serializer = import_string(drfr_settings.USER_SERIALIZER)
    data = serializer(user).data

    # Add tokens to data
    if has_user_verified(user):
        data['token'] = get_user_token(user).key

    return data


def has_user_activate_token():
    """
    Check to has user verify token from settings

    Returns:
        [bool]: True if USER_ACTIVATE_TOKEN_ENABLED is True, else is False
    """

    return drfr_settings.USER_ACTIVATE_TOKEN_ENABLED


def has_user_verify_code():
    """
    Check to has user verify code from settings

    Returns:
        [bool]: True if USER_VERIFY_CODE_ENABLED is True, else is False
    """

    return drfr_settings.USER_VERIFY_CODE_ENABLED


def has_user_verified(user):
    """
    Check user verify or not

    Args:
        user (object): The user instance

    Returns:
        [bool]: The verified value
    """

    return get_user_verified(user)


def get_user_verified(user):
    """
    Get user verified value

    Args:
        user (object): The user instance

    Returns:
        [bool]: The verified value
    """

    return getattr(user, drfr_settings.USER_VERIFY_FIELD)


def set_user_verified(user, verified=True):
    """
    Set user verified

    Args:
        user (object): The user instance
        verified (bool): The verified value
    """

    setattr(user, drfr_settings.USER_VERIFY_FIELD, verified)
    user.save()


def generate_user_uid(user):
    """
    Generate user UID from user pk

    Args:
        user (object): The user object

    Returns:
        [str]: The UID
    """

    return urlsafe_base64_encode(force_bytes(user.pk))


def generate_uid_and_token(user, token_generator=None):
    """
    Generate UID and token from user information

    Args:
        user (object): The user object
        token_generator (optional): The token generator class. Defaults to None.

    Returns:
        [object]: The object of uid and token
    """

    token_generator = token_generator or default_token_generator

    return {
        'uidb64': generate_user_uid(user),
        'token': token_generator.make_token(user)
    }


def get_user_from_uid(uidb64):
    """
    Get user from uidb64

    Args:
        uidb64 (string): The uidb64

    Returns:
        [optional]: The user object or None
    """

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
        return user
    except (DjangoUnicodeDecodeError, get_user_model().DoesNotExist):
        return None
