from typing import Any
from django.conf import settings
from apps.core.logging import Logging
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


logging = Logging(str(settings.BASE_DIR / "logs" / "req_res_logs.txt"))


def simple_logging_middleware(get_response):
    def middleware(request):

        # PRE PROCESSING

        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers["Content-Type"]
        user_agent = request.headers["User-Agent"]

        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"
        logging.info(msg)

        response = get_response(request)

        # POST PROCESSING

        content = response.content
        status_code = response.status_code

        msg = f"{status_code} | {content}"
        logging.info(msg)

        return response

    return middleware


class ViewExecutionTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = timezone.now()

        response = self.get_response(request)

        total_time = timezone.now() - start_time
        http_method = request.method
        host = request.get_host()
        url = request.get_full_path()

        msg = f"EXECUTION TIME: {total_time}. {http_method} | {host}{url}"

        logging.info(msg)


class ViewExecutionTime2Middleware(MiddlewareMixin):

    def process_request(self, request):
        request.start_time = timezone.now()

    def process_response(self, request, response):
        total_time = timezone.now() - request.start_time
        http_method = request.method
        host = request.get_host()
        url = request.get_full_path()
        msg = f"EXECUTION TIME: {total_time}. {http_method} | {host}{url}"
        logging.info(msg)

        return response
