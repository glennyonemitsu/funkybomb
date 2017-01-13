from copy import deepcopy

from funkybomb import freeze, Template

from templates import base
from templates.util import row_cols


tmpl = deepcopy(base.tmpl)

content = Template()
sidebar, main = row_cols(content, 2, 10)

# components - header nav
nav = sidebar.div(_class='mt-3 nav-links')
nav + Template('nav links')

# components - content
main.h1(_class='mt-2 mb-5') + Template('headline')
main.div + Template('content')


tmpl['base main'] = content
freeze(tmpl)
