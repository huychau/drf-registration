from django.core.exceptions import FieldDoesNotExist
from django.test import TestCase
from rest_framework.test import APIClient

from drf_registration.utils.users import get_user_model


class BaseTestCase(TestCase):

    def assertHasProp(self, obj, prop):
        self.assertTrue(True if prop in obj else False)

    def assertHasProps(self, obj, props):
        for prop in props:
            self.assertHasProp(obj, prop)


class BaseModelTestCase(BaseTestCase):

    def hasModelField(self, model, field):
        """
        Check model has field or not

        Args:
            model (class): The model instance
            field (str): The field in model

        Returns:
            [bool]: Has field in model or not
        """

        try:
            model._meta.get_field(field)
            return True
        except FieldDoesNotExist:
            return False

    def assertHasModelFields(self, model, fields=[]):
        for field in fields:
            self.assertTrue(self.hasModelField(model, field))


class BaseAPITestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.client = APIClient()
        self.auth = False
        self.resource = 'accounts'
        self.endpoint = '/api'

        self.user_model = get_user_model()
        self.user = self.user_model.objects.create(
            username='username',
            email='test@example.com',
        )

        self.user.set_password('123456')
        self.user.save()

    def request_config(self):
        if self.auth:
            self.client.force_authenticate(user=self.user)

            self.client.login(user=self.user)

    def assertHttpOK(self, resp):
        self.assertEqual(resp.status_code, 200)

    def assertHttpCreated(self, resp):
        self.assertEqual(resp.status_code, 201)

    def assertHttpNoContent(self, resp):
        self.assertEqual(resp.status_code, 204)

    def assertHttpBadRequest(self, resp):
        self.assertEqual(resp.status_code, 400)

    def assertHttpUnauthorized(self, resp):
        self.assertEqual(resp.status_code, 401)

    def assertHttpNotFound(self, resp):
        self.assertEqual(resp.status_code, 404)

    def assertHasErrorDetail(self, element, msg):
        self.assertEqual(element[0], msg)

    def build_api_url(self, fragment='', **params):
        uri = ''

        if self.resource:
            uri = f'{uri}/{self.resource}'

        if fragment:
            uri = f'{uri}/{fragment}'

        # TODO: Create url from params
        if params:
            pass

        return f'{self.endpoint}{uri}'

    # GET JSON
    # ---------------------------------------#
    def get_json(self, fragment='', **params):
        self.request_config()

        url = self.build_api_url(fragment)

        return self.client.get(url, **params)

    def get_json_ok(self, fragment='', **params):
        resp = self.get_json(fragment, **params)
        self.assertHttpOK(resp)
        return resp

    def get_json_unauthorized(self, fragment='', **params):
        resp = self.get_json(fragment, **params)
        self.assertHttpUnauthorized(resp)
        return resp

    # POST JSON
    # ---------------------------------------#
    def post_json(self, fragment='', data=None, **params):
        self.request_config()

        url = self.build_api_url(fragment)
        return self.client.post(url, data, **params)

    def post_json_ok(self, fragment='', data=None, **params):
        resp = self.post_json(fragment, data, **params)
        self.assertHttpOK(resp)
        return resp

    def post_json_created(self, fragment='', data=None, **params):
        resp = self.post_json(fragment, data, **params)
        self.assertHttpCreated(resp)
        return resp

    def post_json_no_content(self, fragment='', data=None, **params):
        resp = self.post_json(fragment, data, **params)
        self.assertHttpNoContent(resp)
        return resp

    def post_json_bad_request(self, fragment='', data=None, **params):
        resp = self.post_json(fragment, data, **params)
        self.assertHttpBadRequest(resp)
        return resp

    def post_json_unauthorized(self, fragment='', data=None, **params):
        resp = self.post_json(fragment, data, **params)
        self.assertHttpUnauthorized(resp)
        return resp

    def post_json_not_found(self, fragment='', data=None, **params):
        resp = self.post_json(fragment, data, **params)
        self.assertHttpNotFound(resp)

    # PUT JSON
    # ---------------------------------------#
    def put_json(self, fragment='', data=None, **params):
        self.request_config()

        url = self.build_api_url(fragment)
        return self.client.put(url, data, **params)

    def put_json_ok(self, fragment='', data=None, **params):
        resp = self.put_json(fragment, data, **params)
        self.assertHttpOK(resp)
        return resp

    def put_json_bad_request(self, fragment='', data=None, **params):
        resp = self.put_json(fragment, data, **params)
        self.assertHttpBadRequest(resp)
        return resp

    def put_json_unauthorized(self, fragment='', data=None, **params):
        resp = self.put_json(fragment, data, **params)
        self.assertHttpUnauthorized(resp)
        return resp

    def put_json_not_found(self, fragment='', data=None, **params):
        resp = self.put_json(fragment, data, **params)
        self.assertHttpNotFound(resp)
