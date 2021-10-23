from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from drf_registration.settings import drfr_settings
from drf_registration.utils.common import import_string, import_string_list
from drf_registration.utils.users import (
    get_user_model,
    get_user_profile_data,
    has_user_verified,
    set_user_verified,
)
from drf_registration.utils import socials
from drf_registration.exceptions import (
    NotActivated,
    LoginFailed,
    InvalidProvider,
    MissingEmail,
    InvalidAccessToken,
)


class LoginSerializer(serializers.ModelSerializer):
    """
    User login serializer
    """

    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    def validate(self, data):
        user = authenticate(**data)
        if user:

            # Check user is activated or not
            if has_user_verified(user):

                # added user model to OrderedDict that serializer is validating
                data['user'] = user

                return data
            raise NotActivated()
        raise LoginFailed()


class LoginView(CreateAPIView):
    """
    This is used to Login into system.
    """

    permission_classes = import_string_list(drfr_settings.LOGIN_PERMISSION_CLASSES)
    serializer_class = import_string(drfr_settings.LOGIN_SERIALIZER)

    def post(self, request, *args, **kwargs):
        """
        Override to check user login

        Args:
            request (object): The request object

        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        # Update last logged in
        update_last_login(None, user)
        data = get_user_profile_data(user)

        return Response(data, status=status.HTTP_200_OK)


class SocialLoginSerializer(serializers.Serializer):
    """
    User social login serializer
    """

    provider = serializers.CharField()
    access_token = serializers.CharField()

    class Meta:
        fields = ('provider', 'access_token',)


class SocialLoginView(CreateAPIView):
    """
    This is used to Social Login into system.
    """

    permission_classes = import_string_list(
        drfr_settings.LOGIN_PERMISSION_CLASSES)
    serializer_class = SocialLoginSerializer

    def post(self, request, *args, **kwargs):
        """
        Authenticate user through the provider and access_token
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        provider = serializer.data.get('provider', None)

        # Check is invalid provider
        if not socials.is_valid_provider(provider):
            raise InvalidProvider()

        # Check valid token
        access_token = serializer.data.get('access_token', None)

        user_data = socials.get_user_info(provider, access_token)

        # None value mean the access token is not valid
        if not user_data:
            raise InvalidAccessToken()

        # Check the case can not get user email address
        if not user_data.get('email'):
            raise MissingEmail()

        # Create user if not exist
        User = get_user_model()
        try:
            user = User.objects.get(email=user_data['email'])
        except User.DoesNotExist:
            user = User.objects.create(
                username=user_data['email'],
                email=user_data['email'],
                first_name=user_data.get('first_name'),
                last_name=user_data.get('last_name'),
            )

            # Always verified user if they using Google or Facebook
            set_user_verified(user)

        # Update last logged in
        update_last_login(None, user)
        data = get_user_profile_data(user)

        return Response(data, status=status.HTTP_200_OK)
