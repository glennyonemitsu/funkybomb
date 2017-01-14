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
