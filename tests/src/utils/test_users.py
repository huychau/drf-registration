from django.contrib.auth import get_user_model
from django.test.utils import override_settings
from rest_framework.authtoken.models import Token

from drf_registration.api.user import UserSerializer
from drf_registration.utils import users
from tests.utils import BaseTestCase


class UtilUsersTestCases(BaseTestCase):

    def setUp(self):
        self.user_model = users.get_user_model()
        self.user = self.user_model.objects.create(
            username='username',
            email='test@example.com',
            password='123456',
        )

    def test_get_user_model(self):
        self.assertEqual(users.get_user_model(), get_user_model())

    @override_settings(
        DRF_REGISTRATION={
            'USER_SERIALIZER': 'drf_registration.api.user.UserSerializer'
        }
    )
    def test_get_user_serializer(self):
        self.assertEqual(users.get_user_serializer(), UserSerializer)

    def test_get_all_users(self):
        all_users = users.get_all_users()
        self.assertEqual(all_users.count(), 1)
        self.assertEqual(all_users.first(), self.user)

    def test_get_user_token(self):
        token, created = Token.objects.get_or_create(user=self.user)

        self.assertEqual(token, users.get_user_token(self.user))

    def test_remove_user_token(self):
        Token.objects.get_or_create(user=self.user)
        self.assertEqual(Token.objects.filter(user=self.user).count(), 1)

        users.remove_user_token(self.user)

        self.assertEqual(Token.objects.filter(user=self.user).count(), 0)

    def test_get_user_profile_data(self):
        data = users.get_user_profile_data(self.user)
        self.assertEqual(data['id'], self.user.id)
        self.assertEqual(data['username'], self.user.username)
        self.assertEqual(data['email'], self.user.email)

    @override_settings(
        DRF_REGISTRATION={
            'USER_VERIFY_CODE_ENABLED': False
        }
    )
    def test_no_has_user_verify_code_enabled(self):
        self.assertFalse(users.has_user_verify_code())

    @override_settings(
        DRF_REGISTRATION={
            'USER_VERIFY_CODE_ENABLED': True
        }
    )
    def test_has_user_verify_code_enabled(self):
        self.assertTrue(users.has_user_verify_code())

    @override_settings(
        DRF_REGISTRATION={
            'USER_ACTIVATE_TOKEN_ENABLED': False
        }
    )
    def test_no_has_user_activate_token_enabled(self):
        self.assertFalse(users.has_user_activate_token())

    @override_settings(
        DRF_REGISTRATION={
            'USER_ACTIVATE_TOKEN_ENABLED': True
        }
    )
    def test_has_user_activate_token_enabled(self):
        self.assertTrue(users.has_user_activate_token())

    @override_settings(
        DRF_REGISTRATION={
            'USER_VERIFY_FIELD': 'is_active'
        }
    )
    def test_not_has_user_verified(self):
        users.set_user_verified(self.user, False)
        self.assertFalse(users.has_user_verified(self.user))

    @override_settings(
        DRF_REGISTRATION={
            'USER_VERIFY_FIELD': 'is_active'
        }
    )
    def test_has_user_verified(self):
        users.set_user_verified(self.user, True)

        self.assertTrue(users.has_user_verified(self.user))

    def test_generate_uid_and_token(self):
        uid_token = users.generate_uid_and_token(self.user)
        self.assertHasProps(uid_token, ['uidb64', 'token'])

    def test_get_user_from_uid_not_found(self):
        user = users.get_user_from_uid('invalid-uid')
        self.assertEqual(user, None)

    def test_get_user_from_uid_ok(self):
        uid = users.generate_user_uid(self.user)
        user = users.get_user_from_uid(uid)
        self.assertEqual(user, self.user)
