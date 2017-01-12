from copy import deepcopy

from funkybomb import freeze, Tag, Template

from templates import base
from templates.util import row_cols, show_python, show_html


example_funky = '''
from funkybomb import render, Template
from models import user_model

tmpl = Template()
table = tmpl.table

for user in user_model.get_all():
    row = table.tr
    row.td + user.first_name
    row.td + user.last_name

print(render(tmpl))
'''

example_html = '''
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
'''

content = Template()

headline = row_cols(content)
headline.h1(_class='mt-5 mb-5') + 'Funky Bomb'

pitch_python, gutter, pitch_html = row_cols(content, 4, 1, 4)

pitch_python.p(_class='h5') + 'Use Native Python'
pitch_python.pre.code + show_python(example_funky)

gutter.p(_class='h5') + '\u2192'

pitch_html.p(_class='h5') + 'Create HTML Pages'
pitch_html.pre.code + show_html(example_html)


# follow ups
fu = row_cols(content)

fu.p(_class='lead mb-5') + \
    'That is it! No other HTML template or code involved. See how you can ' + \
    (Tag('a', href='/docs/get-started') + 'get started') + '.'

fu.p(_class='h4') + 'It is easy to use'
fu.p + (
    'Funky Bomb has a small set of rules to build out DOM-like '
    'structures and reusable templates with native Python.'
)
fu_links = fu.p
fu_links + 'Learn more: '
fu_links.a(href='/docs/basics') + 'Syntax'
fu_links + ', '
fu_links.a(href='/docs/basics') + 'Templating'
fu_links + ', '
fu_links.a(href='/docs/basics') + 'Utilities'

fu.p(_class='h4 mt-4') + 'Use Python syntax and patterns'
fu.p + (
    'Use normal programming patterns to build abstractions and construct more '
    'advanced HTML with the power of Python.'
)
fu_links = fu.p
fu_links + 'Common patterns: '
fu_links.a(href='/docs/patterns') + 'Reusability'
fu_links + ', '
fu_links.a(href='/docs/patterns') + 'Composition'
fu_links + ', '
fu_links.a(href='/docs/patterns') + 'Abstractions'

fu.p(_class='h4 mt-4') + 'Easy integration'
fu.p + (
    'Any web framework that uses strings for serving HTML can have Funky Bomb '
    'integrated, since Funky Bomb outputs HTML strings itself.'
)
fu_links = fu.p
fu_links + 'Example integrations: '
fu_links.a(href='/docs/integrations/flask') + 'Flask'


tmpl = deepcopy(base.tmpl)
tmpl['base main'] = content
freeze(tmpl)
