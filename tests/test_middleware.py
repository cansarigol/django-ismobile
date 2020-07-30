from django.test import TestCase, override_settings
from django.test.client import Client


class MiddlewareTestCases(TestCase):
    def test_middleware(self):
        request = Client().get("/").wsgi_request
        assert hasattr(request, "IS_MOBILE")

    @override_settings(IS_MOBILE_ATTR_NAME="ismobile")
    def test_middleware_custom_attr(self):
        request = Client().get("/").wsgi_request
        assert hasattr(request, "ismobile")
