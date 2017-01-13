import asyncio

from aiohttp import web


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
