from copy import deepcopy

from funkybomb import freeze, Tag, Template

from templates import base
from templates.util import funky_pair, row_cols
from templates.util import show_python, show_html


content = Template()

headline = row_cols(content)
headline.h1(_class='display-4 mt-5') + (
    'Funky Bomb is an HTML template framework powered by native Python syntax'
)

example_funky = '''
from funkybomb import render, Template
from models import users

tmpl = Template()
headline = Template('headline')
headline + 'This is a default headline'

tmpl.h1 + headline
table = tmpl.table

for user in users.get_all():
    row = table.tr
    row.td + user.first_name
    row.td + user.last_name

ctx = {'headline': 'Here are some names'}
print(render(tmpl, context=ctx))
'''

example_html = '''
<h1>Here are some names</h1>
<table>
    <tr>
        <td>John</td>
        <td>Doe</td>
    </tr>
    <tr>
        <td>Jane</td>
        <td>Doe</td>
    </tr>
    <tr>
        <td>George</td>
        <td>Washington</td>
    </tr>
</table>
'''

pitch_python, gutter, pitch_html = row_cols(content, 4, 1, 4)

pitch_python.p(_class='h4 mt-5 mb-4') + 'Use Native Python'
pitch_python.pre.code + show_python(example_funky)

gutter.p(_class='h4 mt-5 mb-4') + '\u2192'

pitch_html.p(_class='h4 mt-5 mb-4') + 'Create HTML Pages'
pitch_html.pre.code + show_html(example_html)

pitch_close = row_cols(content)
pitch_close.p(_class='lead') + \
    'That is it! No other HTML template or code involved. See how you can ' + \
    (Tag('a', href='/docs/get-started') + 'get started') + '.'

# second row - native python benefits
followups = content.div(_class='mt-5')
basics, patterns, integrations = row_cols(followups, 4, 4, 4)

basics.h4 + 'The Basics'
basics.p + (
    'Funky Bomb has a small set of rules to build out DOM-like structures '
    'with native Python.'
)
basics_links = basics.p
basics_links.a(href='/docs/basics') + 'Syntax'
basics_links + ', '
basics_links.a(href='/docs/basics') + 'Templating'
basics_links + ', '
basics_links.a(href='/docs/basics') + 'Utilities'

patterns.h4 + 'Common Patterns'
patterns.p + (
    'Use normal programming patterns to build abstractions and construct more '
    'advanced HTML easily.'
)
patterns_links = patterns.p
patterns_links.a(href='/docs/patterns') + 'Reusability'
patterns_links + ', '
patterns_links.a(href='/docs/patterns') + 'Composition'
patterns_links + ', '
patterns_links.a(href='/docs/patterns') + 'Abstractions'

integrations.h4 + 'Integrate with frameworks'
integrations.p + (
    'Easily slip in Funky Bomb into your application.'
)
integrations_links = integrations.p
integrations_links.a(href='/docs/integrations/flask') + 'Flask'


tmpl = deepcopy(base.tmpl)
tmpl['base main'] = content
freeze(tmpl)
