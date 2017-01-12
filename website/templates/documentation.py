from copy import deepcopy

from funkybomb import freeze, Template

from templates import base
from templates.util import row_cols


tmpl = deepcopy(base.tmpl)

content = Template()
sidebar, main = row_cols(content, 2, 10)

# components - header nav
sidebar.p + 'Funky Bomb'
nav = sidebar.ul(_class='nav flex-column')
nav + Template('nav links')

# components - content
main.h1() + Template('headline')
main.div + Template('content')


tmpl['base main'] = content
freeze(tmpl)
