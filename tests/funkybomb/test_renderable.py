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
    assert len(r._children_) == 1

    # this makes another foo child, not append to it
    r.foo.bar
    assert len(r._children_) == 2
    assert len(r._children_[1]._children_) == 1


def test_text_wash():
    """
    String appends are converted to Text nodes.
    """
    r = R()
    r += 'this is a text node'
    assert type(r._children_[0]) == Text
    r += 'this is another text node'
    assert type(r._children_[1]) == Text
