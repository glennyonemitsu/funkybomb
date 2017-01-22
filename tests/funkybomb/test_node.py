from funkybomb.node import Node, Text


def test_adding_children():
    root = Node()
    assert len(root.children) == 0

    n = Node()
    root += n
    assert len(root.children) == 1

    n += Node()
    assert len(root.children) == 1

    root.append(Node())
    assert len(root.children) == 2

    children = [Node() for i in range(5)]
    root += children
    assert len(root.children) == 7


def test_children_iteration():
    node_children = [Node() for i in range(5)]
    root = Node()
    root.append(*node_children)
    for i, node in enumerate(root.children):
        assert node is node_children[i]


def test_text_wash():
    """
    String appends are converted to Text nodes.
    """
    r = Node()
    r += 'this is a text node'
    assert type(r.children[0]) == Text
    r += 'this is another text node'
    assert type(r.children[1]) == Text
