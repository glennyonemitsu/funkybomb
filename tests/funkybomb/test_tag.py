"""
Unit tests for Tag, html5 support
"""

from pytest import raises

from funkybomb.node import Tag
from funkybomb.node import Text
from funkybomb.exceptions import ChildNodeError


def test_tag():
    t = Tag('t')
    assert t._opener == '<t>'
    assert t._closer == '</t>'

    t = Tag('t', foo='bar')
    assert t._opener == '<t foo="bar">'
    assert t._closer == '</t>'

    t = Tag('t', _class='bar')
    assert t._opener == '<t class="bar">'
    assert t._closer == '</t>'

    t = Tag()
    assert t._opener == ''
    assert t._closer == ''


def test_void_tag():
    t = Tag('img')
    assert t._opener == '<img>'
    assert t._closer == ''

    t = Tag('img', foo='bar')
    assert t._opener == '<img foo="bar">'
    assert t._closer == ''

    with raises(ChildNodeError):
        t.foo


def test_raw_text_tag():
    t = Tag('style')
    assert t._opener == '<style>'
    assert t._closer == '</style>'

    t = Tag('style', foo='bar')
    assert t._opener == '<style foo="bar">'
    assert t._closer == '</style>'

    t + 'this is some text'
    t + 'this is more text'
    assert type(t._children[0]) == Text
    assert type(t._children[1]) == Text

    with raises(ChildNodeError):
        t.foo
