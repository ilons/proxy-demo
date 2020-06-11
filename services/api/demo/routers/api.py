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
        fastapi.routing.APIRoute('/', get_proxy_root, methods=['GET']),
    ]


async def get_proxy_root(request: fastapi.Request):
    """ Route used to get request information when behind a proxy

    :param request:
    :return:
    """
    return demo.routers.get_response(
        'This is the API root route',
        request,
        [route.path for route in get_routes()],
    )
