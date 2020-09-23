from django.test.utils import override_settings
from drf_registration.utils.users import get_user_model
from tests.utils import BaseAPITestCase


class SetPasswordAPITestCase(BaseAPITestCase):

    def setUp(self):
        super().setUp()

        # Assuming that no user password created by social
        self.user_1 = get_user_model().objects.create(
            username='user1',
            email='user1@example.com'
        )

    def test_set_password_unauthorized(self):
        params = {}
        self.put_json_unauthorized('set-password/', params)

    def test_set_password_invalid_new_password(self):
        self.client.force_authenticate(user=self.user_1)
        params = {
            'password': 'short'
        }
        resp = self.put_json_bad_request('set-password/', params)
        self.assertHasErrorDetail(resp.data['password'], 'This password is too short. It must contain at least 8 characters.')

    def test_set_password_existed_password(self):

        # Use user has a password
        self.client.force_authenticate(user=self.user)
        params = {
            'password': 'abcABC@123'
        }
        resp = self.put_json_bad_request('set-password/', params)
        self.assertHasErrorDetail(resp.data['password'], 'Your password is already existed.')

    def test_set_password_ok(self):
        self.client.force_authenticate(user=self.user_1)
        params = {
            'password': 'abcABC@123'
        }
        resp = self.put_json_ok('set-password/', params)
