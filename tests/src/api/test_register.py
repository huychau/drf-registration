from django.test import override_settings
from django.core import mail
from tests.utils import BaseAPITestCase
from drf_registration.utils.users import generate_uid_and_token, set_user_verified
from drf_registration.tokens import activation_token


class RegisterAPITestCase(BaseAPITestCase):

    def setUp(self):
        super().setUp()
        self.auth = False

    def test_register_empty_params(self):
        params = {}
        resp = self.post_json_bad_request('register/', params)

        self.assertHasProps(resp.data, ['username', 'password', 'email'])

    def test_register_existed_username(self):
        params = {
            'username': self.user.username,
            'email': 'test+1@domain.com',
            'password': '123456',
        }
        resp = self.post_json_bad_request('register/', params)
        self.assertHasProps(resp.data, ['username',])
        self.assertHasErrorDetail(resp.data['username'], 'User with this username already exists.')

    def test_register_existed_email(self):
        params = {
            'username': 'testusername',
            'email': self.user.email,
            'password': '123456',
        }
        resp = self.post_json_bad_request('register/', params)

        self.assertHasProps(resp.data, ['email',])
        self.assertHasErrorDetail(resp.data['email'], 'User with this email already exists.')

    def test_register_short_password(self):
        params = {
            'username': 'testusername',
            'email': 'testuser@domain.com',
            'password': '123456',
        }
        resp = self.post_json_bad_request('register/', params)

        self.assertHasErrorDetail(resp.data['password'], 'This password is too short. It must contain at least 8 characters.')

    @override_settings(
        DRF_REGISTRATION={
            'USER_ACTIVATE_TOKEN_ENABLED': False,
            'REGISTER_SEND_WELCOME_EMAIL_ENABLED': False,
            'USER_VERIFY_CODE_ENABLED': False
        }
    )
    def test_register_normal_ok(self):
        params = {
            'username': 'testusername',
            'email': 'testuser@domain.com',
            'password': 'abcABC@123',
        }
        resp = self.post_json_created('register/', params)
        self.assertHasProps(resp.data, ['id', 'username', 'email', 'is_active', 'token'])

        self.assertTrue(resp.data['is_active'])

    @override_settings(
        DRF_REGISTRATION={
            'DEFAULT_FROM_EMAIL': 'info@testdomain.com',
            'USER_ACTIVATE_EMAIL_SUBJECT': 'Activate subject',
            'USER_ACTIVATE_TOKEN_ENABLED': True,
            'USER_VERIFY_CODE_ENABLED': False,
            'REGISTER_SEND_WELCOME_EMAIL_ENABLED': False,
        }
    )
    def test_register_activate_enabled(self):
        params = {
            'username': 'testusername',
            'email': 'testuser@domain.com',
            'password': 'abcABC@123',
        }
        resp = self.post_json_created('register/', params)

        self.assertHasProps(resp.data, ['id', 'username', 'email', 'is_active'])
        self.assertFalse(resp.data['is_active'])

        # Test email
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Activate subject')
        self.assertEqual(mail.outbox[0].to, ['testuser@domain.com'])

    @override_settings(
        DRF_REGISTRATION={
            'USER_ACTIVATE_TOKEN_ENABLED': False,
            'USER_VERIFY_CODE_ENABLED': True,
            'REGISTER_SEND_WELCOME_EMAIL_ENABLED': False,
        }
    )
    def test_register_verify_enabled(self):
        params = {
            'username': 'testusername',
            'email': 'testuser@domain.com',
            'password': 'abcABC@123',
        }
        resp = self.post_json_created('register/', params)

        self.assertHasProps(resp.data, ['id', 'username', 'email', 'is_active'])
        self.assertFalse(resp.data['is_active'])

    @override_settings(
        DRF_REGISTRATION={
            'USER_ACTIVATE_TOKEN_ENABLED': False,
            'USER_VERIFY_CODE_ENABLED': False,
            'REGISTER_SEND_WELCOME_EMAIL_ENABLED': True,
            'DEFAULT_FROM_EMAIL': 'info@testdomain.com',
            'REGISTER_SEND_WELCOME_EMAIL_SUBJECT': 'Welcome subject'
        }
    )
    def test_register_send_welcome_email_enabled(self):
        params = {
            'username': 'testusername',
            'email': 'testuser@domain.com',
            'password': 'abcABC@123',
        }
        resp = self.post_json_created('register/', params)

        self.assertHasProps(resp.data, ['id', 'username', 'email', 'is_active', 'token'])

        self.assertTrue(resp.data['is_active'])

        # Test email
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Welcome subject')
        self.assertEqual(mail.outbox[0].to, ['testuser@domain.com'])

    def test_register_activate_token_failed_views(self):
        resp = self.get_json_ok('activate/xxx/yyy/')
        self.assertContains(resp, 'Either the provided activation token is invalid or this account has already been activated.')

    def test_register_activate_token_success_views(self):
        uid_token = generate_uid_and_token(self.user, activation_token)
        uid = uid_token['uidb64']
        token = uid_token['token']
        resp = self.get_json_ok(f'activate/{uid}/{token}/')
        self.assertContains(resp, 'Your account has been activate successfully.')
