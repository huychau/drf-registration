from django.utils.translation import gettext as _

from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from drf_registration.settings import drfr_settings
from drf_registration.utils.users import get_user_model, get_all_users
from drf_registration.utils.socials import enable_has_password


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """

    if 'email' in drfr_settings.USER_FIELDS:
        email = serializers.EmailField(validators=[UniqueValidator(
            queryset=get_all_users(),
            message=_('User with this email already exists.')
        )])

    if 'username' in drfr_settings.USER_FIELDS:
        username = serializers.CharField(validators=[UniqueValidator(
            queryset=get_all_users(),
            message=_('User with this username already exists.')
        )])

    if enable_has_password():
        has_password = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()

        # Check to response has password field in the case enable Facebook or Google login
        fields = drfr_settings.USER_FIELDS + ('has_password',) if enable_has_password() else drfr_settings.USER_FIELDS
        read_only_fields = drfr_settings.USER_READ_ONLY_FIELDS
        extra_kwargs = {'password': {'write_only': True}}

    def get_has_password(self, user):
        """
        Custom response field to check user has password or not
        """

        return bool(user.password)
