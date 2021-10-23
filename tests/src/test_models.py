from drf_registration.utils.users import get_user_model
from tests.utils import BaseModelTestCase


class UserModelTestCases(BaseModelTestCase):
    def setUp(self):
        self.user_model = get_user_model()

    def test_get_user_model(self):
        user_model = get_user_model()

        self.assertHasModelFields(user_model, ['username', 'email'])
