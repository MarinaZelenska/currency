from time import time

from currency.models import RequestResponseLog

from django.http import HttpRequest


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def get_method(self, request):
        if request.method == 'GET':
            return "GET"
        elif request.method == 'POST':
            return "POST"

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        end = time()
        duration = end - start
        path_info = HttpRequest.get_full_path(request)
        info_method = self.get_method(request)
        RequestResponseLog.objects.create(path=path_info, request_method=info_method, time=duration)
        return response
