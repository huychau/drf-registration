from django.contrib.auth.tokens import PasswordResetTokenGenerator

try:
    from django.utils import six
except:
    import six

from drf_registration.utils.users import get_user_verified


class CustomAccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """
    Custom account activation token generator

    Args:
        PasswordResetTokenGenerator (class): Strategy object used to generate
        and check tokens for the password reset mechanism.
    """

    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(get_user_verified(user))
        )


class CustomPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    """
    Custom password reset token generator

    Args:
        Args:
        PasswordResetTokenGenerator (class): Strategy object used to generate
        and check tokens for the password reset mechanism.
    """


activation_token = CustomAccountActivationTokenGenerator()
reset_password_token = CustomPasswordResetTokenGenerator()
