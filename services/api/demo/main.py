import fastapi
import starlette.exceptions

import demo.routers
import demo.routers.api

PROXY_PATH = 'api'


app = fastapi.FastAPI()
app.include_router(demo.routers.get_router())
# app.include_router(demo.routers.api.get_router(), prefix=f'/{PROXY_PATH}')


@app.exception_handler(starlette.exceptions.HTTPException)
async def unicorn_exception_handler(request: fastapi.Request, exc: starlette.exceptions.HTTPException):
    return fastapi.responses.JSONResponse(
        status_code=exc.status_code,
        content=demo.routers.get_response(
            f"Unable to serve request: {request.url}",
            request,
            [route.path for route in demo.routers.get_routes()],
            exc.status_code,
        ),
    )
