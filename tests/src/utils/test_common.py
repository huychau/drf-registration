from rest_framework.permissions import AllowAny

from drf_registration.api.user import UserSerializer
from drf_registration.utils.common import import_string, import_string_list
from tests.utils import BaseTestCase


class UtilCommonTestCases(BaseTestCase):

    def test_import_string(self):
        user_serializer = import_string('drf_registration.api.user.UserSerializer')

        self.assertTrue(user_serializer, UserSerializer)

    def test_import_string_list(self):
        permission_classes = import_string_list([
            'rest_framework.permissions.AllowAny',
        ])

        self.assertEqual(permission_classes, [AllowAny, ])
