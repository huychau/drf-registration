from django.core import mail
from django.test.utils import override_settings

from tests.utils import BaseAPITestCase


class ResetPasswordAPITestCase(BaseAPITestCase):

    @override_settings(
        DRF_REGISTRATION={
            'RESET_PASSWORD_ENABLED': False
        }
    )
    def test_reset_password_is_not_enabled(self):
        self.post_json_not_found('reset-password/')

    @override_settings(
        DRF_REGISTRATION={
            'RESET_PASSWORD_ENABLED': True
        }
    )
    def test_reset_password_invalid_email(self):
        params = {
            'email': 'invalid'
        }
        self.post_json_bad_request('reset-password/', params)

    @override_settings(
        DRF_REGISTRATION={
            'RESET_PASSWORD_ENABLED': True
        }
    )
    def test_reset_password_not_found_email(self):
        params = {
            'email': 'notfoundemail@domain.com'
        }
        self.post_json_not_found('reset-password/', params)

    @override_settings(
        DRF_REGISTRATION={
            'RESET_PASSWORD_ENABLED': True,
            'RESET_PASSWORD_EMAIL_SUBJECT': 'Reset Password Subject'
        }
    )
    def test_reset_password_send_email_ok(self):
        params = {
            'email': self.user.email
        }
        self.post_json_ok('reset-password/', params)

        # Test email
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Reset Password Subject')
        self.assertEqual(mail.outbox[0].to, [self.user.email])
