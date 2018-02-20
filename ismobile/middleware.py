from .utils import get_is_mobil

class MobileControlMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.IS_MOBILE = get_is_mobil(request.META['HTTP_USER_AGENT'])
        response = self.get_response(request)
        return response