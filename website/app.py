from aiohttp import web

from application.app import app
import handlers  # noqa


web.run_app(app, host='0.0.0.0', port=8080)
