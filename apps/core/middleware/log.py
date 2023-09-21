import logging

logger = logging.getLogger('logging_mw')

# logger.info(msg)
# logger.error(msg)
# logger.critical(msg)
# logger.warning(msg)
# logger.debug(msg)


def simple_logging_middleware(get_response):
    def middleware(request):

        # PRE PROCESSING

        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers["Content-Type"]
        user_agent = request.headers["User-Agent"]

        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"
        logger.info(msg)

        response = get_response(request)
        return response
    return middleware
