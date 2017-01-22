"""
Unit tests for Tag, html5 support
"""

from pytest import raises

from funkybomb.html5 import img, p, script
from funkybomb.node import Tag
from funkybomb.node import Text
from funkybomb.exceptions import ChildNodeError


def test_tag():
    t = Tag('t')
    assert t.opener == '<t>'
    assert t.closer == '</t>'

    t = Tag('t', foo='bar')
    assert t.opener == '<t foo="bar">'
    assert t.closer == '</t>'

    t = Tag('t', _class='bar')
    assert t.opener == '<t class="bar">'
    assert t.closer == '</t>'

    t = Tag()
    assert t.opener == ''
    assert t.closer == ''


def test_void_tag():
    t = Tag('img')
    assert t.opener == '<img>'
    assert t.closer == '</img>'

    t = Tag('img', foo='bar')
    assert t.opener == '<img foo="bar">'
    assert t.closer == '</img>'

    with raises(ChildNodeError):
        t.is_void = True
        t += Tag('foo')


def test_raw_text_tag():
    t = Tag('style')
    assert t.opener == '<style>'
    assert t.closer == '</style>'

    t = Tag('style', foo='bar')
    assert t.opener == '<style foo="bar">'
    assert t.closer == '</style>'

    t += 'this is some text'
    t += 'this is more text'
    assert type(t.children[0]) == Text
    assert type(t.children[1]) == Text

    with raises(ChildNodeError):
        t.is_raw_text = True
        t += Tag('foo')


def test_attrs():
    t = Tag(foo='bar')
    assert t.attrs['foo'] == 'bar'

    t += Tag('foo', level='child')
    assert t.children[0].attrs == {'level': 'child'}


def test_class_append():
    n = p()
    n += img
    n += 'hi'
    n += img
    assert n.tag == 'p'
    assert len(n.children) == 3
    assert isinstance(n.children[0], img)
    assert isinstance(n.children[1], Text)
    assert isinstance(n.children[2], img)


def test_void_restriction():
    with raises(ChildNodeError):
        n = img()
        n += 'hi'


def test_raw_text_restriction():
    n = script()
    n += 'hi'

    with raises(ChildNodeError):
        n += p
