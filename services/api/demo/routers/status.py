import fastapi
import fastapi.routing

import demo.routers


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
        fastapi.routing.APIRoute('', get_status, methods=['GET']),
        fastapi.routing.APIRoute('/health', get_health, methods=['GET']),
    ]


async def get_status(request: fastapi.Request):
    """ Status endpoint

    :param request:
    :return:
    """
    return demo.routers.get_response(
        'This is the status root route',
        request,
        [route.path for route in get_routes()],
    )


async def get_health(request: fastapi.Request):
    """ Healthcheck endpoint

    :param request:
    :return:
    """
    return demo.routers.get_response(
        'This is the status /health route',
        request,
        [route.path for route in get_routes()],
    )
