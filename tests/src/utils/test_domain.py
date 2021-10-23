from django.test.utils import override_settings

from drf_registration.utils.domain import get_current_domain
from tests.utils import BaseTestCase


class UtilDomainTestCases(BaseTestCase):

    @override_settings(
        DRF_REGISTRATION={
            'PROJECT_BASE_URL': 'https://testdomain.com'
        }
    )
    def test_get_current_domain_from_settings(self):
        domain = get_current_domain({})

        self.assertEqual(domain, 'https://testdomain.com')
