from application import constants
from application.app import app


def route(u, verbs=('get',)):
    def decorator(fn):
        for verb in verbs:
            method = 'add_{verb}'.format(verb=verb)
            getattr(app.router, method)(url(u), fn)
        return fn
    return decorator


def url(u):
    return constants.url_prefix + u
