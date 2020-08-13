from aiohttp import web
from aiohttp.web_request import Request


routes = web.RouteTableDef()


@routes.get('/{key}')
async def get_data(request: Request):
    return web.Response()


@routes.put('/{key}')
async def put_data(request: Request):
    return web.Response(status=200)

