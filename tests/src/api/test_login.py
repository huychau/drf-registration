from django.test import override_settings

from drf_registration.utils.users import set_user_verified
from tests.utils import BaseAPITestCase


class LoginAPITestCase(BaseAPITestCase):

    def setUp(self):
        super().setUp()
        self.auth = False

    def test_login_empty_field(self):
        params = {}
        resp = self.post_json_bad_request('login/', params)
        self.assertHasProps(resp.data, ['username', 'password'])
        self.assertHasErrorDetail(resp.data['username'], 'This field is required.')
        self.assertHasErrorDetail(resp.data['password'], 'This field is required.')

    def test_login_invalid_credentials(self):
        params = {
            'username': 'invalid',
            'password': 'invalid'
        }
        self.post_json_unauthorized('login/', params)

    def test_login_inactivated_user(self):
        set_user_verified(self.user, False)

        params = {
            'username': self.user.username,
            'password': '123456'
        }
        resp = self.post_json_unauthorized('login/', params)
        self.assertEqual(resp.data['detail'], 'Account is not activated.')

    def test_login_ok(self):
        set_user_verified(self.user, True)
        params = {
            'username': self.user.username,
            'password': '123456',
        }
        resp = self.post_json_ok('login/', params)

        self.assertHasProps(resp.data, ['id', 'username', 'email', 'is_active', 'token'])


class SocialLoginAPITestCase(BaseAPITestCase):

    def test_login_empty_field(self):
        params = {}
        resp = self.post_json_bad_request('login/social/', params)
        self.assertHasProps(resp.data, ['provider', 'access_token'])
        self.assertHasErrorDetail(resp.data['provider'], 'This field is required.')
        self.assertHasErrorDetail(resp.data['access_token'], 'This field is required.')

    @override_settings(
        DRF_REGISTRATION={
            'FACEBOOK_LOGIN_ENABLED': False
        }
    )
    def test_invalid_provider(self):
        params = {
            'provider': 'invalid',
            'access_token': 'token'
        }
        self.post_json_bad_request('login/social/', params)

    @override_settings(
        DRF_REGISTRATION={
            'FACEBOOK_LOGIN_ENABLED': False
        }
    )
    def test_not_enable_facebook_login(self):
        params = {
            'provider': 'facebook',
            'access_token': 'token'
        }
        self.post_json_bad_request('login/social/', params)

    @override_settings(
        DRF_REGISTRATION={
            'FACEBOOK_LOGIN_ENABLED': True
        }
    )
    def test_facebook_login_invalid_access_token(self):
        params = {
            'provider': 'facebook',
            'access_token': 'invalid'
        }
        self.post_json_bad_request('login/social/', params)

    @override_settings(
        DRF_REGISTRATION={
            'GOOGLE_LOGIN_ENABLED': False
        }
    )
    def test_not_enable_google_login(self):
        params = {
            'provider': 'google',
            'access_token': 'token'
        }
        self.post_json_bad_request('login/social/', params)

    @override_settings(
        DRF_REGISTRATION={
            'GOOGLE_LOGIN_ENABLED': True
        }
    )
    def test_google_login_invalid_access_token(self):
        params = {
            'provider': 'google',
            'access_token': 'invalid'
        }
        self.post_json_bad_request('login/social/', params)
