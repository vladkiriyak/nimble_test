from aiohttp import web
from aiohttp.web_request import Request

from controller.src.utils import get_node_ip, get_value_from_node, put_value_in_node

routes = web.RouteTableDef()


@routes.get('/{key}')
async def get_data(request: Request):
    node_ip = get_node_ip(request.match_info['key'])
    value = await get_value_from_node(node_ip, request.match_info['key'])
    return web.Response(body=value)


@routes.put('/{key}')
async def put_data(request: Request):
    node_ip = get_node_ip(request.match_info['key'])
    await put_value_in_node(node_ip, request.match_info['key'], (await request.json())['value'])
    return web.Response(status=200)
