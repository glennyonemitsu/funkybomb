from funkybomb.node import Node


def test_adding_children():
    root = Node()
    assert len(root._children) == 0

    n = Node()
    root += n
    assert len(root._children) == 1

    n += Node()
    assert len(root._children) == 1

    root._append(Node())
    assert len(root._children) == 2


def test_root():
    root = Node()
    n = Node()
    root += n
    assert n._root == root

    n._append(Node(), Node(), Node())
    for child in n._children:
        assert child._root == root


def test_children_iteration():
    children = [Node() for i in range(5)]
    root = Node()
    root._append(*children)
    for i, node in enumerate(root):
        assert node is children[i]
