from functools import update_wrapper
import html

from aiohttp import web
from funkybomb import render, Tag, Template
from pygments import highlight
from pygments.lexers import HtmlLexer, PythonLexer, TextLexer
from pygments.formatters import HtmlFormatter

from application import constants
from application.util import url


def row_cols(node, *cols):
    row = node.div(_class='row')
    if not cols:
        return row.div(_class='col')
    divs = []
    for col in cols:
        col_class = 'col-md-{width}'.format(width=col)
        divs.append(row.div(_class=col_class))
    return divs


def nav_links(current_url, links):
    tmpl = Template()
    nav = tmpl.ul(_class='list-unstyled')
    for href, text, children in links:
        nav_item = nav.li()
        _class = ''
        if url == current_url:
            _class += 'active'
        nav_item.a(_class=_class, href=url(href)) + text
        if children:
            nav_item = nav.li()
            nav_item + nav_links(current_url, children)
    return nav


def nav_links_new():
    nav_groups = (
        (
            'Basics',
            (
                ('/docs/basics/installation', 'Installation'),
                ('/docs/basics/syntax', 'Syntax'),
                ('/docs/basics/templating', 'Templating'),
                ('/docs/basics/utilities', 'Utilities'),
            )
        ),
        (
            'Common Patterns',
            (
                ('/docs/patterns/abstraction', 'Abstractions'),
                ('/docs/patterns/composition', 'Composition'),
                ('/docs/patterns/reusability', 'Reusability'),
            )
        ),
        (
            'Integrations',
            (
                ('/docs/integrations/flask', 'Flask'),
            )
        ),
    )

    tmpl = Template()
    nav = tmpl.ul(_class='list-unstyled')
    nav.li.a(href=url('/')) + 'Funky Bomb'

    for name, links in nav_groups:
        nav.li.p(_class='mt-3 mb-1') + name
        for u, text in links:
            nav.li.a(href=url(u)) + text

    return tmpl


def template(tmpl):
    """
    aiohttp view decorator.
    """

    def decorator(fn):
        async def wrapped(req, *args, **kwargs):
            context = await fn(req, *args, **kwargs)
            context['nav links'] = nav_links_new()
            output = render(tmpl, context=context, pretty=False)
            return web.Response(text=output, content_type='text/html')
        update_wrapper(wrapped, fn)
        return wrapped
    return decorator


def show_python(text):
    return highlight(
        source(text), PythonLexer(), HtmlFormatter(style='colorful'))


def show_html(text):
    return highlight(source(text), HtmlLexer(), HtmlFormatter(style='colorful'))


def show_text(text):
    return highlight(source(text), TextLexer(), HtmlFormatter(style='colorful'))


def source(text):
    lines = []
    indent = None
    for line in text.splitlines():
        if indent is None and line != '':
            indent = len(line) - len(line.lstrip())
        lines.append(line[indent:])
    return '\n'.join(lines).strip()


def header(text, level=2):
    attr = text.lower().replace(' ', '-')
    t = 'h' + str(level)
    return Tag(t, id=attr, _class='mt-5') + text


def p(*texts):
    tmpl = Template()
    for p in texts:
        tmpl.p + html.escape(p)
    return tmpl
