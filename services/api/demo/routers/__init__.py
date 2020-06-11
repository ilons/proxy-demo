import urllib.parse

import fastapi
import fastapi.routing


PROXY_PATH = 'api'


def get_response(message: str, request: fastapi.Request, routes: list, status_code: int = 200):
    """ Get a response dict for the given message, request and routes

    :param message:
    :param request:
    :param routes:
    :param status_code:
    :return:
    """
    return {
        'response': {
            'status_code': status_code,
            'message': message,
        },
        'request': get_request_info(request),
        '_links': get_links(request, routes),
    }


def get_router():
    """ Get the router for module

    :return:
    """
    return fastapi.APIRouter(get_routes())


def get_routes():
    """ Get all routes for this module

    :return:
    """
    return [
        fastapi.routing.APIRoute('/', endpoint=get_root, methods=['GET']),
        fastapi.routing.APIRoute('/status', get_status, methods=['GET']),
    ]


def get_links(request: fastapi.Request, routes: list):
    """ Get links to resources

    :param request:
    :param routes:
    :return:
    """
    # self_path = request.url.path[len(PROXY_PATH) + 1:]
    self_path = request.url.path

    links = {}
    for ep_path in routes:
        link_key = ep_path[1:]
        if link_key == self_path:
            link_key = 'self'
        if not link_key:
            link_key = 'root'

        links[link_key] = urllib.parse.urlunsplit((
            request.url.scheme,
            request.url.netloc,
            ep_path,
            request.url.query,
            request.url.fragment,
        ))

    return links


def get_request_info(request: fastapi.Request):
    """ Get dict with information about HTTP request

    :param request:
    :return:
    """
    return {
        'method': request.method,
        'url': {
            'fragment': request.url.fragment,
            'netloc': request.url.netloc,
            'path': request.url.path,
            'port': request.url.port,
            'query': request.url.query,
            'scheme': request.url.scheme,
            'value': request.url.__str__(),
        },
        'headers': dict(request.headers.mutablecopy()),
        'query': dict(request.query_params.items()),
        'client': dict(zip(['host', 'port'], request.client)),
    }


async def get_status(request: fastapi.Request):
    """ Healthcheck endpoint

    :param request:
    :return:
    """
    return get_response(
        'This is the service status route',
        request,
        [route.path for route in get_routes()],
    )


async def get_root(request: fastapi.Request):
    """ Root of API

    :param request:
    :return:
    """
    return get_response(
        'This is the service root route',
        request,
        [route.path for route in get_routes()],
    )
