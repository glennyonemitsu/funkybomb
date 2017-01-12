from aiohttp import web
from funkybomb import render

from templates import util


async def nav_links(app, handler):
    if not hasattr(handler, 'funkybomb'):
        return handler

    async def wrapped_handler(req):
        response = await handler(req)
        response['nav links'] = util.nav_links(req.url.path)
        return response

    wrapped_handler.funkybomb = handler.funkybomb
    return wrapped_handler


async def funkybomb(app, handler):
    """
    The final in the funkybomb middleware chain.
    """

    if not hasattr(handler, 'funkybomb'):
        return handler

    async def wrapped_handler(req):
        response = await handler(req)
        if isinstance(response, web.Response):
            return response
        tmpl = handler.funkybomb['template']
        text = render(tmpl, context=response, pretty=False)
        return web.Response(text=text, content_type='text/html')
    return wrapped_handler
