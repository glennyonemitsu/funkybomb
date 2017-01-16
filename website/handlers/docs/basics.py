from funkybomb import Template, Text

from application.util import route
from templates import documentation
from templates.util import template


@route('/docs/basics')
@template(documentation.tmpl)
async def docs_basics_home(req):
    tmpl = Template()
    tmpl.p + 'hi'

    return {
        'content': tmpl,
        'headline': Text('Basics')
    }


@route('/docs/basics/quick-start')
@template(documentation.tmpl)
async def docs_basics_quick_start(req):
    t = Template()

    t.h2 + 'Installation'
    t.p + 'Funky Bomb is available via PyPi and install is simple'
    t.pre.code + 'pip install funky-bomb'

    t.h2 + 'Your first HTML template'
    t.p + ''

    return {
        'content': tmpl,
        'headline': Text('Quick Start')
    }


@route('/docs/basics/syntax')
@template(documentation.tmpl)
async def docs_basics_syntax(req):
    tmpl = Template()
    tmpl.p + 'hi'

    return {
        'content': tmpl,
        'headline': Text('Syntax')
    }


@route('/docs/basics/templating')
@template(documentation.tmpl)
async def docs_basics_templating(req):
    tmpl = Template()
    tmpl.p + 'hi'

    return {
        'content': tmpl,
        'headline': Text('Templating')
    }


@route('/docs/basics/utilities')
@template(documentation.tmpl)
async def docs_basics_utilities(req):
    tmpl = Template()
    tmpl.p + 'hi'

    return {
        'content': tmpl,
        'headline': Text('Utilities')
    }
