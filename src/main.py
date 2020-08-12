import aioboto3 as aioboto3
import aiohttp

from src.service import KeyValueData
from .routes import routes

import logging
from aiohttp import web
from .config import conf


async def init(app):
    client = aioboto3.client(
        's3',
        aws_access_key_id=conf["ACCESS_KEY_ID"],
        aws_secret_access_key=conf['SECRET_KEY'],
    )
    app.add_routes(routes)
    logging.basicConfig(level=logging.DEBUG)
    app['config'] = conf
    app['s3_client'] = client
    app['KeyValueData'] = KeyValueData(client)

    app['session'] = aiohttp.ClientSession()
    yield
    await app['session'].close()


def main():
    app = web.Application()
    app.cleanup_ctx.append(init)
    web.run_app(app, port=conf['PORT'])


if __name__ == '__main__':
    main()
