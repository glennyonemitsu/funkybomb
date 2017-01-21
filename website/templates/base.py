from funkybomb import Template
from pygments.formatters import HtmlFormatter

from templates.util import row_cols


tmpl = Template()
tmpl += '<!DOCTYPE html>'
html = tmpl.html


# head
head = html.head
head.meta(charset='utf-8')

styles = (
    "https://maxcdn.bootstrapcdn.com/bootstrap/"
    "4.0.0-alpha.6/css/bootstrap.min.css",
)

for style in styles:
    head.link(rel="stylesheet", href=style, crossorigin="anonymous")
head.style += HtmlFormatter(style='colorful').get_style_defs('.highlight')
head.style += '''
.nav-links ul { margin-left: 0;}
.nav-links ul ul { margin-left: 1.2rem;}
.highlight { padding: 1.4rem; background-color: #f2f2f2; }
.highlight pre { margin: 0 }
'''

scripts = (
    "https://code.jquery.com/jquery-3.1.1.slim.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js",
    "https://maxcdn.bootstrapcdn.com/bootstrap/"
    "4.0.0-alpha.6/js/bootstrap.min.js",
)

for script in scripts:
    head.script(src=script, crossorigin="anonymous")


# body - grid layout
hb = html.body
container = hb.div(_class='container')
main = row_cols(container)
main += Template('base main')


# components - footer
footer = row_cols(main)
div = footer.div(id='footer')
div += Template('base footer')
