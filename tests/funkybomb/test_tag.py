"""
Unit tests for Tag, html5 support
"""

from pytest import raises

from funkybomb.node import Tag
from funkybomb.node import Text
from funkybomb.exceptions import ChildNodeError


def test_tag():
    t = Tag('t')
    assert t._opener_ == '<t>'
    assert t._closer_ == '</t>'

    t = Tag('t', foo='bar')
    assert t._opener_ == '<t foo="bar">'
    assert t._closer_ == '</t>'

    t = Tag('t', _class='bar')
    assert t._opener_ == '<t class="bar">'
    assert t._closer_ == '</t>'

    t = Tag()
    assert t._opener_ == ''
    assert t._closer_ == ''


def test_void_tag():
    t = Tag('img')
    assert t._opener_ == '<img>'
    assert t._closer_ == ''

    t = Tag('img', foo='bar')
    assert t._opener_ == '<img foo="bar">'
    assert t._closer_ == ''

    with raises(ChildNodeError):
        t.foo


def test_raw_text_tag():
    t = Tag('style')
    assert t._opener_ == '<style>'
    assert t._closer_ == '</style>'

    t = Tag('style', foo='bar')
    assert t._opener_ == '<style foo="bar">'
    assert t._closer_ == '</style>'

    t += 'this is some text'
    t += 'this is more text'
    assert type(t._children_[0]) == Text
    assert type(t._children_[1]) == Text

    with raises(ChildNodeError):
        t.foo


def test_attrs():
    t = Tag(foo='bar')
    assert t._attrs_['foo'] == 'bar'

    t.foo(level='child')
    assert t._children_[0]._attrs_ == {'level': 'child'}
