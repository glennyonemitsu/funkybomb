from funkybomb import Tag, Template, Text

from application.util import route
from templates import documentation
from templates import splash
# from templates.home import tmpl as home_tmpl
from templates.util import template


@route('/')
@template(splash.tmpl)
async def home(req):
    return {}


@route('/about')
@template(documentation.tmpl)
async def about(req):
    return {'content': Tag('p') + 'about'}


@route('/contact')
@template(documentation.tmpl)
async def contact(req):
    return {'content': Tag('p') + 'contact'}
