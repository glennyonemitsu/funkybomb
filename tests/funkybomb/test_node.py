from funkybomb.node import Node


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


def test_root():
    root = Node()
    n = Node()
    root += n
    # assert n._root_ == root

    n._append_(Node(), Node(), Node())
    for child in n._children_:
        # assert child._root_ == root
        pass


def test_children_iteration():
    children = [Node() for i in range(5)]
    root = Node()
    root._append_(*children)
    for i, node in enumerate(root):
        assert node is children[i]
