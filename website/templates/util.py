import importlib

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


def nav_links(current_url):
    links = (
        ('/', 'home'),
        ('/about', 'about'),
        ('/contact', 'contact'),
    )
    nav = Template()
    for url, text in links:
        nav_item = nav.li(_class='nav-item')
        _class = 'nav-link'
        if url == current_url:
            _class += ' active'
        nav_item.a(_class=_class, href=url) + text
    return nav


def template(tmpl):
    """
    aiohttp view decorator.
    """

    def decorator(fn):
        fn.funkybomb = {'template': tmpl}
        return fn
    return decorator


def funky_pair(module, namespace='tmpl'):
    source = module.replace('.', '/')
    source += '.py'
    with open(source, 'rt') as fh:
        funky_code = fh.read()
        funky_code = highlight(
            funky_code, PythonLexer(), HtmlFormatter(style='colorful')
        )

    funky_module = importlib.import_module(module)
    target = getattr(funky_module, namespace)
    funky_output = render(target, pretty=True)
    funky_output = highlight(
        funky_output, HtmlLexer(), HtmlFormatter(style='colorful')
    )

    return funky_code, funky_output


def show_python(text):
    return highlight(text, PythonLexer(), HtmlFormatter(style='colorful'))


def show_html(text):
    return highlight(text, HtmlLexer(), HtmlFormatter(style='colorful'))
