from django.test.utils import override_settings
from tests.utils import BaseAPITestCase


class ChangePasswordAPITestCase(BaseAPITestCase):

    def test_change_password_unauthorized(self):
        params = {}
        self.put_json_unauthorized('change-password/', params)

    def test_change_password_invalid_old_password(self):
        self.client.force_authenticate(user=self.user)
        params = {
            'old_password': 'invalid',
            'new_password': 'abcABC@123'
        }
        resp = self.put_json_bad_request('change-password/', params)
        self.assertHasErrorDetail(resp.data['old_password'], 'Old password is not correct.')

    def test_change_password_invalid_new_password(self):
        self.client.force_authenticate(user=self.user)
        params = {
            'old_password': '123456',
            'new_password': 'short'
        }
        resp = self.put_json_bad_request('change-password/', params)
        self.assertHasErrorDetail(resp.data['new_password'], 'This password is too short. It must contain at least 8 characters.')

    def test_change_password_ok(self):
        self.client.force_authenticate(user=self.user)
        old_password_hash = self.user.password
        params = {
            'old_password': '123456',
            'new_password': 'abcABC@123'
        }
        self.put_json_ok('change-password/', params)
        self.assertNotEqual(old_password_hash, self.user.password)
