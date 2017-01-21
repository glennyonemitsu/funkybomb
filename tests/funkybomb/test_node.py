from funkybomb.node import Node
from funkybomb.util import children


def test_adding_children():
    root = Node()
    assert len(root._children_) == 0

    n = Node()
    root += n
    assert len(root._children_) == 1

    n += Node()
    assert len(root._children_) == 1

    root._append_(Node())
    assert len(root._children_) == 2

    children = [Node() for i in range(5)]
    root += children
    assert len(root._children_) == 7


def test_children_iteration():
    node_children = [Node() for i in range(5)]
    root = Node()
    root._append_(*node_children)
    for i, node in enumerate(children(root)):
        assert node is node_children[i]
