from django.test import override_settings
from django.http.response import Http404
from tests.utils import BaseTestCase
from drf_registration.utils import socials
from drf_registration import constants


class UtilSocialsTestCases(BaseTestCase):

    def test_is_facebook_provider(self):
        self.assertTrue(socials.is_facebook_provider(constants.FACEBOOK_PROVIDER))
        self.assertFalse(socials.is_facebook_provider('something'))

    def test_is_google_provider(self):
        self.assertTrue(socials.is_google_provider(constants.GOOGLE_PROVIDER))
        self.assertFalse(socials.is_google_provider('something'))

    def test_in_valid_provider(self):
        self.assertFalse(socials.is_valid_provider('something'))

    @override_settings(
        DRF_REGISTRATION={
            'FACEBOOK_LOGIN_ENABLED': False
        }
    )
    def test_not_enable_facebook_login(self):
        self.assertFalse(socials.is_valid_provider(constants.FACEBOOK_PROVIDER))

    @override_settings(
        DRF_REGISTRATION={
            'FACEBOOK_LOGIN_ENABLED': True
        }
    )
    def test_enable_facebook_login(self):
        self.assertTrue(socials.is_valid_provider(constants.FACEBOOK_PROVIDER))

    @override_settings(
        DRF_REGISTRATION={
            'FACEBOOK_LOGIN_ENABLED': True
        }
    )
    def test_get_facebook_user_info_invalid_access_token(self):
        self.assertEqual(socials.get_user_info(constants.FACEBOOK_PROVIDER, 'invalid-token'), None)

    @override_settings(
        DRF_REGISTRATION={
            'GOOGLE_LOGIN_ENABLED': False
        }
    )
    def test_not_enable_google_login(self):
        self.assertFalse(socials.is_valid_provider(constants.GOOGLE_PROVIDER))

    @override_settings(
        DRF_REGISTRATION={
            'GOOGLE_LOGIN_ENABLED': True
        }
    )
    def test_enable_google_login(self):
        self.assertTrue(socials.is_valid_provider(constants.GOOGLE_PROVIDER))

    @override_settings(
        DRF_REGISTRATION={
            'GOOGLE_LOGIN_ENABLED': False,
            'FACEBOOK_LOGIN_ENABLED': False,
        }
    )
    def test_not_enable_has_password(self):
        self.assertFalse(socials.enable_has_password())

    @override_settings(
        DRF_REGISTRATION={
            'GOOGLE_LOGIN_ENABLED': True,
            'FACEBOOK_LOGIN_ENABLED': False,
        }
    )
    def test_enable_has_password(self):
        self.assertTrue(socials.enable_has_password())
