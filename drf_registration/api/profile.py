from rest_framework.generics import RetrieveUpdateAPIView

from drf_registration.settings import drfr_settings
from drf_registration.utils.common import import_string, import_string_list
from drf_registration.utils.users import get_all_users, get_user_serializer


class ProfileSerializer(get_user_serializer()):
    """
    Profile serializer
    """

    def __init__(self, *args, **kwargs):
        """
        Custom to add partial=True to PUT method request to skip blank
        validations
        """

        if kwargs.get('context'):
            request = kwargs['context'].get('request', None)

            if request and getattr(request, 'method', None) == 'PUT':
                kwargs['partial'] = True

        super().__init__(*args, **kwargs)


class ProfileView(RetrieveUpdateAPIView):
    """
    Get update user profile information
    """

    permission_classes = import_string_list(drfr_settings.PROFILE_PERMISSION_CLASSES)
    serializer_class = import_string(drfr_settings.PROFILE_SERIALIZER)
    queryset = get_all_users()

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        """
        Custom update user profile
        """

        # Remove write only fields when update profile
        for field in drfr_settings.USER_WRITE_ONLY_FIELDS:

            if field in request.data.keys():
                # Make it editable
                request.data._mutable = True

                request.data.pop(field)

                # Disable editable
                request.data._mutable = False

        # Support the case user can change password in profile if
        # USER_WRITE_ONLY_FIELDS not contain password field
        if 'password' in request.data.keys():
            request.data._mutable = True
            self.request.user.set_password(request.data.pop('password')[0])
            self.request.user.save()
            request.data._mutable = False

        return super().update(request, *args, **kwargs)
