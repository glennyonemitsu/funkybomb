from application.app import app


def route(url, verbs=('get',)):
    def decorator(fn):
        for verb in verbs:
            method = 'add_{verb}'.format(verb=verb)
            getattr(app.router, method)(url, fn)
        return fn
    return decorator
