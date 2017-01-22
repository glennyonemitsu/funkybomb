from funkybomb.html5 import html, p, h1
from funkybomb.node import Tag
from funkybomb.node import Template
from funkybomb.node import Text
from funkybomb.util import render


def test_templates():
    r = Template()
    h = html()
    h += p('this is a test')
    foo = h.foo(foo='bar')
    foo += 'this is another'
    output = render(r, pretty=False)
    expected = (
        '<html>'
        '<p>this is a test</p>'
        '<foo foo="bar">this is another</foo>'
        '</html>'
    )
    assert output == expected


def test_add_basic():
    r = Tag('p') + 'hi'
    output = render(r, pretty=False)
    assert output == '<p>hi</p>'


def test_add_magic():
    r = Template()
    h = r.html
    h.p += ('this ', 'is ', 'a ', (Tag('em') + 'test'))
    foo = h.foo(foo='bar')
    foo += 'this is another'
    bar = h.bar
    bar += 'foo'
    bar += 'bar'
    bar += 'baz'
    output = render(r, pretty=False)
    expected = (
        '<html>'
        '<p>this is a <em>test</em></p>'
        '<foo foo="bar">this is another</foo>'
        '<bar>foobarbaz</bar>'
        '</html>'
    )
    assert output == expected


def test_templates_advanced():
    r = Template()
    h = r.html
    h.p += 'this is a test'
    table = h.table
    for i in range(2):
        tr = table.tr
        for j in range(3):
            tr.td += 'row {row} col {col}'.format(row=i, col=j)
    output = render(r, pretty=False)
    expected = (
        '<html>'
        '<p>this is a test</p>'
        '<table>'
        '<tr><td>row 0 col 0</td><td>row 0 col 1</td><td>row 0 col 2</td></tr>'
        '<tr><td>row 1 col 0</td><td>row 1 col 1</td><td>row 1 col 2</td></tr>'
        '</table></html>'
    )

    assert output == expected


def test_blocks_default():
    r = Template()
    h = r.html
    foo = Template('foo')
    foo.p += 'default'
    h += foo
    output = render(r, pretty=False)
    expected = '<html><p>default</p></html>'
    assert output == expected


def test_blocks_content():
    r = Template()
    h = r.html
    foo = Template('foo')
    foo.p += 'default'
    h += foo

    data = Tag('div')
    data += 'this is overwritten'

    context = {'foo': data}
    output = render(r, context=context, pretty=False)
    expected = '<html><div>this is overwritten</div></html>'
    assert output == expected


def test_blocks_tag_content():
    r = Template()
    h = r.html
    h += Template('foo') + 'default'

    context = {'foo': Tag('p') + 'this is overwritten'}
    output = render(r, context=context, pretty=False)
    expected = '<html><p>this is overwritten</p></html>'
    assert output == expected


def test_blocks_text_content():
    r = Template()
    h = r.html
    foo = Template('foo')
    foo.p += 'default'
    h += foo

    context = {'foo': Text('this is overwritten')}
    output = render(r, context=context, pretty=False)
    expected = '<html>this is overwritten</html>'
    assert output == expected
