from django.contrib.auth import password_validation
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from drf_registration.settings import drfr_settings
from drf_registration.utils.common import import_string, import_string_list
from drf_registration.utils.users import get_user_profile_data, remove_user_token


class ChangePasswordSerializer(serializers.Serializer):
    """
    Change password serializer
    """

    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def validate_old_password(self, old_password):
        """
        Validate user password
        """

        user = self.context['request'].user

        if not user.check_password(old_password):
            raise serializers.ValidationError(_('Old password is not correct.'))
        return old_password

    def validate_new_password(self, new_password):
        """
        Validate user password
        """

        user = self.context['request'].user
        password_validation.validate_password(new_password, user)
        return new_password

    def save(self, **kwargs):
        password = self.validated_data['new_password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user


class ChangePasswordView(UpdateAPIView):
    """
    Change user password
    """
    
    permission_classes = import_string_list(drfr_settings.CHANGE_PASSWORD_PERMISSION_CLASSES)
    serializer_class = import_string(drfr_settings.CHANGE_PASSWORD_SERIALIZER)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Reset old token
        remove_user_token(user)

        # Response data include new token
        data = get_user_profile_data(user)

        return Response(data, status=status.HTTP_200_OK)
