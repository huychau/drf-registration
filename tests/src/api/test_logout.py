from django.test import override_settings
from rest_framework.authtoken.models import Token

from tests.utils import BaseAPITestCase


class LogoutAPITestCase(BaseAPITestCase):
    def test_logout_unauthorized(self):
        self.post_json_unauthorized('logout/')

    def test_logout_ok(self):
        self.client.force_authenticate(user=self.user)
        self.post_json_no_content('logout/')

    @override_settings(
        DRF_REGISTRATION={
            'LOGOUT_REMOVE_TOKEN': True
        }
    )
    def test_logout_remove_token_ok(self):
        self.client.force_authenticate(user=self.user)
        self.post_json_no_content('logout/')
        self.assertEqual(Token.objects.filter(user=self.user).count(), 0)
