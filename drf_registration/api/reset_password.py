from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_registration.exceptions import UserNotFound
from drf_registration.settings import drfr_settings
from drf_registration.utils.common import import_string, import_string_list
from drf_registration.utils.domain import get_current_domain
from drf_registration.utils.email import send_reset_password_token_email
from drf_registration.utils.users import get_user_model


class ResetPasswordSerializer(serializers.Serializer):
    """
    Reset password serializer

    Raises:
        UserNotFound: In the case can not found user email
    """

    email = serializers.EmailField()

    def validate(self, data):

        try:
            user = get_user_model().objects.get(email=data['email'])
        except get_user_model().DoesNotExist:
            raise UserNotFound()
        # Added user model to OrderedDict that serializer is validating
        data['user'] = user

        return data


class ResetPasswordView(APIView):
    """
    Reset user password by send the link to email
    """

    permission_classes = import_string_list(drfr_settings.RESET_PASSWORD_PERMISSION_CLASSES)
    serializer_class = import_string(drfr_settings.RESET_PASSWORD_SERIALIZER)

    def post(self, request, *args, **kwargs):
        """
        Override to check reset password request

        Args:
            request (object): The request object

        Raises:
            Http404: In the case RESET_PASSWORD_ENABLED is False
        """

        # Check in the case reset password is not supported
        if not drfr_settings.RESET_PASSWORD_ENABLED:
            raise Http404()

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get user from validated data
        user = serializer.validated_data['user']

        # Send reset password link to email
        domain = get_current_domain(request)
        send_reset_password_token_email(user, domain)

        return Response(
            {'detail': _('Password reset e-mail has been sent.')},
            status=status.HTTP_200_OK
        )


class ResetPasswordConfirmView(PasswordResetConfirmView):
    """
    Custom reset password  confirm view
    """

    success_url = reverse_lazy('reset_password_complete')

    # Check in the case custom template name
    if drfr_settings.RESET_PASSWORD_CONFIRM_TEMPLATE:
        template_name = drfr_settings.RESET_PASSWORD_CONFIRM_TEMPLATE  # pragma: no cover


class ResetPasswordCompleteView(PasswordResetCompleteView):
    """
    Custom reset password complete view
    """

    # Check in the case custom template name
    if drfr_settings.RESET_PASSWORD_SUCCESS_TEMPLATE:
        template_name = drfr_settings.RESET_PASSWORD_SUCCESS_TEMPLATE  # pragma: no cover
