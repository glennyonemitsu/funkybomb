from funkybomb import Tag, Template, Text

from application.util import route
from templates import documentation
from templates.util import row_cols, show_python, show_html, source, template


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
            ('Reusability', '/docs/basics/syntax'),
            ('Composition', '/docs/basics/templating'),
            ('Abstractions', '/docs/basics/utilities'),
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
            ('Flask', '/docs/basics/syntax'),
        )
    })

    example_funky = source('''
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

    example_html = source('''
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

    pitch_python, gutter, pitch_html = row_cols(content, 5, 1, 5)

    pitch_python.p(_class='h5') + 'Use Native Python'
    pitch_python.pre.code + show_python(example_funky)

    gutter.p(_class='h5') + '\u2192'

    pitch_html.p(_class='h5') + 'Create HTML Pages'
    pitch_html.pre.code + show_html(example_html)

    fu = row_cols(content)

    fu.p(_class='lead mb-5') + \
        'That is it! No other HTML template or code involved. See how you ' + \
        'can ' + (Tag('a', href='/docs/get-started') + 'get started') + '.'

    for item in followups:
        fu.p(_class='h4 mt-5') + item['header']
        fu.p + item['content']
        fu_links = fu.p

        for i, link in enumerate(item['links']):
            if i == 0:
                fu_links + (link[0] + ' ')
            else:
                fu_links.a(href=link[1]) + link[0]
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
    tmpl.p + 'hi'

    return {
        'content': tmpl,
        'headline': Text('Docs')
    }
