from functools import update_wrapper

from aiohttp import web

from funkybomb import render, Template
from pygments import highlight
from pygments.lexers import HtmlLexer
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


def row_cols(node, *cols):
    row = node.div(_class='row')
    if not cols:
        return row.div(_class='col')
    divs = []
    for col in cols:
        col_class = 'col-md-{width}'.format(width=col)
        divs.append(row.div(_class=col_class))
    return divs


def nav_links(current_url, links=None):
    _links = (
        ('/', 'Funky Bomb', ()),
        ('/docs', 'Docs', (
            ('/docs/basics', 'Basics', (
                ('/docs/basics/syntax', 'Syntax', ()),
                ('/docs/basics/templating', 'Templating', ()),
                ('/docs/basics/utilities', 'Utilities', ()),
            )),
            ('/docs/patterns', 'Common Patterns', (
                ('/docs/patterns/reuseability', 'Reusability', ()),
                ('/docs/patterns/composition', 'Composition', ()),
                ('/docs/patterns/abstractions', 'Abstractions', ()),
            )),
            ('/docs/integrations', 'Integrations', (
                ('/docs/integrations/flask', 'Flask', ()),
            )),
        ))
    )
    if links is None:
        links = _links

    tmpl = Template()
    nav = tmpl.ul(_class='list-unstyled')
    for url, text, children in links:
        nav_item = nav.li()
        _class = ''
        if url == current_url:
            _class += 'active'
        nav_item.a(_class=_class, href=url) + text
        if children:
            nav_item = nav.li()
            nav_item + nav_links(current_url, children)
    return nav


def template(tmpl):
    """
    aiohttp view decorator.
    """

    def decorator(fn):
        async def wrapped(req, *args, **kwargs):
            context = await fn(req, *args, **kwargs)
            context['nav links'] = nav_links(req.url.path)
            output = render(tmpl, context=context, pretty=False)
            return web.Response(text=output, content_type='text/html')
        update_wrapper(wrapped, fn)
        return wrapped
    return decorator


def show_python(text):
    return highlight(text, PythonLexer(), HtmlFormatter(style='colorful'))


def show_html(text):
    return highlight(text, HtmlLexer(), HtmlFormatter(style='colorful'))


def source(text):
    lines = []
    indent = None
    for line in text.splitlines():
        if indent is None and line != '':
            indent = len(line) - len(line.lstrip())
        lines.append(line[indent:])
    return '\n'.join(lines).strip()