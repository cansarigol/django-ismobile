from django.conf import settings

from .utils import get_is_mobil


class MobileControlMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        is_mobile_attr_name = getattr(settings, "IS_MOBILE", "IS_MOBILE")
        is_mobile_value = get_is_mobil(request.META.get("HTTP_USER_AGENT"))
        setattr(request, is_mobile_attr_name, is_mobile_value)
        response = self.get_response(request)
        return response
