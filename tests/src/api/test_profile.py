from django.test.utils import override_settings
from tests.utils import BaseAPITestCase


class ProfileAPITestCase(BaseAPITestCase):

    def test_get_profile_unauthorized(self):
        self.get_json_unauthorized('profile/')

    def test_get_profile_ok(self):
        self.client.force_authenticate(user=self.user)
        resp = self.get_json_ok('profile/')
        self.assertHasProps(resp.data, ['id', 'username', 'email', 'is_active'])

    def test_update_profile_unauthorized(self):
        self.put_json_unauthorized('profile/')

    @override_settings(
        DRF_REGISTRATION={
            'USER_WRITE_ONLY_FIELDS': (
                'password',
                'username',
            )
        }
    )
    def test_update_profile_ok(self):
        self.client.force_authenticate(user=self.user)
        params = {
            'first_name': 'Hello',
            'last_name': 'World',
            'username': 'new_username'
        }
        resp = self.put_json_ok('profile/', params)

        # Can not update write only field
        self.assertNotEqual(resp.data['username'], 'new_username')

    @override_settings(
        DRF_REGISTRATION={
            'USER_WRITE_ONLY_FIELDS': (
                'username',
            )
        }
    )
    def test_update_profile_pasword_ok(self):
        self.client.force_authenticate(user=self.user)
        old_password_hash = self.user.password
        params = {
            'password': 'abcABC@123'
        }
        self.put_json_ok('profile/', params)
        self.assertNotEqual(old_password_hash, self.user.password)
