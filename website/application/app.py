import asyncio

from aiohttp import web

from application import middleware


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
app.middlewares.append(middleware.funkybomb)
app.middlewares.append(middleware.nav_links)
