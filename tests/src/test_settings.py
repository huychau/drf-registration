from django.test import TestCase
from django.test.utils import override_settings

from drf_registration.utils.common import generate_settings, get_django_settings


class SettingsTestCase(TestCase):

    def setUp(self):
        self.defaults = {
            'USER_VERIFY_CODE_ENABLED': False,
        }

    def test_user_settings(self):
        user_settings = {
            'USER_VERIFY_CODE_ENABLED': True,
        }
        settings = generate_settings(user_settings, self.defaults)
        self.assertEqual(settings.USER_VERIFY_CODE_ENABLED, True)

    @override_settings(
        DRF_REGISTRATION={
            'USER_VERIFY_CODE_ENABLED': False,
        }
    )
    def test_django_settings(self):
        settings = generate_settings(get_django_settings(), self.defaults)
        self.assertEqual(settings.USER_VERIFY_CODE_ENABLED, False)
