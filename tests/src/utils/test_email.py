from django.core import mail
from django.test import override_settings

from tests.utils import BaseTestCase
from drf_registration.utils.users import get_user_model
from drf_registration.utils import email



class UtilEmailTestCases(BaseTestCase):

    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create(
            username='username',
            email='test@example.com',
            password='123456',
        )

    @override_settings(
        DRF_REGISTRATION={
            'USER_ACTIVATE_TOKEN_ENABLED': True,
            'DEFAULT_FROM_EMAIL': 'info@testdomain.com',
            'USER_ACTIVATE_EMAIL_SUBJECT': 'Activate subject'
        }
    )
    def test_send_activate_token_email(self):
        email.send_verify_email(self.user, 'http://testdomain.com')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Activate subject')
        self.assertEqual(mail.outbox[0].to, [self.user.email])

    @override_settings(
        DRF_REGISTRATION={
            'USER_VERIFY_CODE_ENABLED': True,
        }
    )
    def test_send_verify_code_email(self):

        # TODO: Need to implement later
        email.send_verify_email(self.user, '')

    @override_settings(
        DRF_REGISTRATION={
            'REGISTER_SEND_WELCOME_EMAIL_ENABLED': True,
            'DEFAULT_FROM_EMAIL': 'info@testdomain.com',
            'REGISTER_SEND_WELCOME_EMAIL_SUBJECT': 'Welcome subject'
        }
    )
    def test_send_welcome_email(self):
        email.send_email_welcome(self.user)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Welcome subject')
        self.assertEqual(mail.outbox[0].to, [self.user.email])

    @override_settings(
        DRF_REGISTRATION={
            'RESET_PASSWORD_ENABLED': True,
            'DEFAULT_FROM_EMAIL': 'info@testdomain.com',
            'RESET_PASSWORD_EMAIL_SUBJECT': 'Reset password subject'
        }
    )
    def test_send_reset_password_email(self):
        email.send_reset_password_token_email(self.user, 'http://testdomain.com')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Reset password subject')
        self.assertEqual(mail.outbox[0].to, [self.user.email])
