from funkybomb import Template, Text

from application.util import route, url
from templates import documentation
from templates.util import row_cols, show_python, show_html, template


@route('/')
@template(documentation.tmpl)
async def home(req):
    followups = []
    followups.append({
        'header': 'It is easy to use',
        'content': (
            'Funky Bomb has a small set of rules to build out DOM-like '
            'structures and reusable templates with native Python.'
        ),
        'links': (
            ('Learn more:',),
            ('Syntax', '/docs/basics/syntax'),
            ('Templating', '/docs/basics/templating'),
            ('Utilities', '/docs/basics/utilities'),
        )
    })

    followups.append({
        'header': 'Use Python syntax and patterns',
        'content': (
            'Use normal programming patterns to build abstractions and '
            'construct more advanced HTML with the power of Python.'
        ),
        'links': (
            ('Common patterns:',),
            ('Abstractions', '/docs/patterns/abstractions'),
            ('Composition', '/docs/patterns/composition'),
            ('Reusability', '/docs/patterns/reusability'),
        )
    })

    followups.append({
        'header': 'Easy integration',
        'content': (
            'Any web framework that uses strings for serving HTML can have '
            'Funky Bomb integrated, since Funky Bomb outputs HTML strings '
            'itself.'
        ),
        'links': (
            ('Examples:',),
            ('Flask', '/docs/integrations/flask'),
        )
    })

    example_funky = show_python('''
    from funkybomb import render, Template
    from models import user_model

    tmpl = Template()
    table = tmpl.table

    for user in user_model.get_all():
        row = table.tr
        row.td + user.first_name
        row.td + user.last_name

    print(render(tmpl))
    ''')

    example_html = show_html('''
    <table>
        <tr>
            <td>John</td>
            <td>Doe</td>
        </tr>
        <tr>
            <td>Jane</td>
            <td>Doe</td>
        </tr>
    </table>
    ''')

    content = Template()

    pitch_python, pitch_html = row_cols(content, 6, 6)

    pitch_python.p(_class='h5') + 'Use Native Python'
    pitch_python + example_funky

    pitch_html.p(_class='h5') + 'Create HTML Pages'
    pitch_html + example_html

    fu = row_cols(content)

    fu.p(_class='lead mt-5 mb-5') + \
        'That is it! No other HTML template or code involved.'

    for item in followups:
        fu.p(_class='h4 mt-5') + item['header']
        fu.p + item['content']
        fu_links = fu.p

        for i, link in enumerate(item['links']):
            if i == 0:
                fu_links + (link[0] + ' ')
            else:
                fu_links.a(href=url(link[1])) + link[0]
                if i < (len(item['links']) - 1):
                    fu_links + ', '

    return {
        'content': content,
        'headline': Text('Funky Bomb')
    }


@route('/docs')
@template(documentation.tmpl)
async def docs_home(req):
    tmpl = Template()
    tmpl.p + 'Coming soon'

    return {
        'content': tmpl,
        'headline': Text('Docs')
    }
