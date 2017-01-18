from funkybomb import Template, Text

from application.util import route
from templates import documentation
from templates.util import template


@route('/docs/integrations')
@template(documentation.tmpl)
async def docs_integrations_home(req):
    tmpl = Template()
    tmpl.p + 'Coming soon.'

    return {
        'content': tmpl,
        'headline': Text('Integrations')
    }


@route('/docs/integrations/flask')
@template(documentation.tmpl)
async def docs_integrations_flask(req):
    tmpl = Template()
    tmpl.p + 'Coming soon.'

    return {
        'content': tmpl,
        'headline': Text('Integrating with Flask')
    }
