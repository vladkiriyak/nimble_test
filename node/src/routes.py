from aiohttp import web
from aiohttp.web_request import Request

from node.src.service import KeyValueData

routes = web.RouteTableDef()


@routes.get('/{key}')
async def get_data(request: Request):
    kvd: KeyValueData = request.app['KeyValueData']
    value = await kvd.get_item(request.match_info['key'])
    return web.Response(body=value)


@routes.put('/{key}')
async def put_data(request: Request):
    data = (await request.json())['value']
    kvd: KeyValueData = request.app['KeyValueData']
    await kvd.set_item(request.match_info['key'], data)
    return web.Response(status=200)

