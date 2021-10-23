import requests
from rest_framework.utils import json

from drf_registration.constants import (
    FACEBOOK_PROVIDER,
    FACEBOOK_AUTH_URL,
    FACEBOOK_FIELDS,
    GOOGLE_AUTH_URL,
    GOOGLE_PROVIDER,
)
from drf_registration.settings import drfr_settings


def is_valid_provider(provider):
    """
    Check is valid provider if enabled, if not raise 404 error

    Args:
        provider (string): The provider name

    Returns:
        [bool]: Is valid provider
    """

    return (
        (is_facebook_provider(provider) and drfr_settings.FACEBOOK_LOGIN_ENABLED) or
        (is_google_provider(provider) and drfr_settings.GOOGLE_LOGIN_ENABLED)
    )


def is_facebook_provider(provider):
    """
    Check is Facebook provider

    Args:
        provider (str): The provider name

    Returns:
        [bool]: Is Facebook provider
    """

    return provider == FACEBOOK_PROVIDER


def is_google_provider(provider):
    """
    Check is Google provider

    Args:
        provider (str): The provider name

    Returns:
        [bool]: Is Google provider
    """
    return provider == GOOGLE_PROVIDER


def get_user_info(provider, access_token):
    """
    Get user information by use valid access token and request to social APIs

    Args:
        provider (str): The provider name
        access_token (str): Access token

    Returns:
        [object]: The user information
    """

    request_api = ''

    # Check is Facebook provider
    # Ref: https://developers.facebook.com/docs/graph-api/using-graph-api/
    if is_facebook_provider(provider):
        request_api = FACEBOOK_AUTH_URL
        params = {
            'access_token': access_token,
            'fields': FACEBOOK_FIELDS
        }

    # Check is Google provider
    # Ref: https://developers.google.com/identity/sign-in/web/backend-auth#calling-the-tokeninfo-endpoint
    if is_google_provider(provider):
        request_api = GOOGLE_AUTH_URL
        params = {
            'id_token': access_token
        }

    req = requests.get(request_api, params=params)
    data = json.loads(req.text)

    # Check error
    return None if 'error' in data else data


def enable_has_password():
    """
    Check to show has password field

    Returns:
        [bool]: Enable has_password field or not
    """

    return drfr_settings.FACEBOOK_LOGIN_ENABLED or drfr_settings.GOOGLE_LOGIN_ENABLED
