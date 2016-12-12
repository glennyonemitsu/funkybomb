"""
Unit tests for Renderable, where trees grow rapidly.
"""

from funkybomb.node import Renderable as R
from funkybomb.node import Text


def test_auto_append():
    """
    Test the attr append magicness.

    ex. foo.bar results in foo with bar child.
    """
    r = R()
    r.foo
    assert len(r._children) == 1

    # this makes another foo child, not append to it
    r.foo.bar
    assert len(r._children) == 2
    assert len(r._children[1]._children) == 1


def test_text_wash():
    """
    String appends are converted to Text nodes.
    """
    r = R()
    r + 'this is a text node'
    assert type(r._children[0]) == Text
    r + 'this is another text node'
    assert type(r._children[1]) == Text


def test_attrs():
    r = R(foo='bar')
    assert r._attrs['foo'] == 'bar'

    r.foo(level='child')
    assert r._children[0]._attrs == {'level': 'child'}
