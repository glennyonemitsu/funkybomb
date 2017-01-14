from funkybomb import Template, Text

from application.util import route
from templates import documentation
from templates.util import template


@route('/docs/patterns')
@template(documentation.tmpl)
async def docs_patterns_home(req):
    tmpl = Template()
    tmpl.p + 'hi'

    return {
        'content': tmpl,
        'headline': Text('Common Patterns')
    }


@route('/docs/patterns/reusability')
@template(documentation.tmpl)
async def docs_patterns_reusability(req):
    tmpl = Template()
    tmpl.p + 'hi'

    return {
        'content': tmpl,
        'headline': Text('Reusability')
    }


@route('/docs/patterns/composition')
@template(documentation.tmpl)
async def docs_patterns_composition(req):
    tmpl = Template()
    tmpl.p + 'hi'

    return {
        'content': tmpl,
        'headline': Text('Composition')
    }


@route('/docs/patterns/abstractions')
@template(documentation.tmpl)
async def docs_patterns_abstractions(req):
    tmpl = Template()
    tmpl.p + 'hi'

    return {
        'content': tmpl,
        'headline': Text('Abstractions')
    }
