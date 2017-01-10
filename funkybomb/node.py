from funkybomb.exceptions import ChildNodeError


class Node:
    """
    The building block of tree based templating.
    """

    def __init__(self):
        """
        Initialize the Node.
        """

        self._root_node = self
        self._children = []

    def __repr__(self):
        """
        String representation of the Node.
        """

        return '<BaseNode>'

    def __iter__(self):
        return iter(self._children)

    def __add__(self, *nodes):
        """
        Append nodes from the += notation.
        """

        # supports: self + ('foo', 'bar', Tag('em') + 'baz') notation
        if len(nodes) == 1 and type(nodes[0]) == tuple:
            nodes = nodes[0]
        self._append(*nodes)
        return self

    def _wash_nodes_hook(self, *nodes):
        return self._set_root_for_nodes(*self._wash_nodes(*nodes))

    def _set_root_for_nodes(self, *nodes):
        for node in nodes:
            node._root_node = self._root
            yield node

    def _wash_nodes(self, *nodes):
        for node in nodes:
            yield node

    def _append(self, *nodes):
        if len(nodes) == 1 and type(nodes[0]) is list:
            nodes = nodes[0]
        self._children.extend(list(self._wash_nodes_hook(*nodes)))

    def _prepend(self, *nodes):
        if len(nodes) == 1 and type(nodes[0]) is list:
            nodes = nodes[0]
        self._children = list(self._wash_nodes_hook(*nodes)) + self._children

    @property
    def _root(self):
        if self._root_node is self:
            return self
        return self._root_node._root


class Renderable(Node):

    def __repr__(self):
        return '<RenderableNode>'

    def __init__(self, *args, **attrs):
        super().__init__()
        self._attrs = attrs

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            self._append(value)

    def __getattr__(self, key):

        # required for a bunch of magic methods quirks like with deepcopy()
        if key.startswith('__'):
            return super().__getattr__(key)

        if hide_attribute(key):
            return None

        if key.startswith('_'):
            setattr(self, key, None)
            return super().__getattr__(key)

        n = Tag(key)
        self._append(n)
        return n

    def __call__(self, *args, **kwargs):
        self._append(*args)
        self._attrs.update(kwargs)
        return self

    @property
    def _opener(self):
        return ''

    @property
    def _closer(self):
        return ''

    def _wash_nodes(self, *nodes):
        text_types = {str, int, float}
        for node in nodes:
            if type(node) in text_types:
                yield Text(node)
            else:
                yield node


class Template(Renderable):

    def __init__(self, name=None):
        super().__init__()
        self._name = name

    def __repr__(self):
        if self._name:
            return '<TemplateNode[{name}]>'.format(name=self._name)
        else:
            return '<AnonymousTemplateNode>'

    def __setitem__(self, key, value):
        bind_template(self, key, value)


class Tag(Renderable):

    # html 5 tag categories according to
    # https://www.w3.org/TR/html5/syntax.html#void-elements
    _void_tags = {
        'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'keygen',
        'link', 'meta', 'param', 'source', 'track', 'wbr'
    }

    _raw_text_tags = {'script', 'style'}

    def __init__(self, tag=None, **attrs):
        super().__init__(**attrs)
        self._tag = tag

    def __repr__(self):
        return '<TagNode[{tag}]>'.format(tag=self._tag)

    def _wash_nodes(self, *nodes):
        if self._void and nodes:
            raise ChildNodeError()
        elif self._raw_text:
            text_types = {str, int, float}
            for node in nodes:
                if type(node) in text_types:
                    yield Text(node)
                elif type(node) is Text:
                    yield node
                else:
                    raise ChildNodeError()
        else:
            for node in super()._wash_nodes(*nodes):
                yield node

    @property
    def _void(self):
        return self._tag in self._void_tags

    @property
    def _raw_text(self):
        return self._tag in self._raw_text_tags

    @property
    def _opener(self):
        if self._tag is None:
            return ''

        if not self._attrs:
            return '<{tag}>'.format(tag=self._tag)

        attrs = build_attrs(self._attrs)
        return '<{tag} {attrs}>'.format(tag=self._tag, attrs=attrs)

    @property
    def _closer(self):
        if self._tag is None or self._void:
            return ''
        return '</{tag}>'.format(tag=self._tag)


class Text(Renderable):

    def __init__(self, content=''):
        super().__init__()
        self._content = str(content)

    def __repr__(self):
        return '<TextNode["{text}"]>'.format(text=self._content)

    @property
    def _opener(self):
        return self._content


def build_attrs(attrs):
    pairs = []
    for key, value in attrs.items():
        if key == '_class':
            key = 'class'
        pairs.append((key, value))
    attrs = ' '.join(
        '{key}="{value}"'.format(key=key, value=value)
        for key, value in pairs)
    return attrs


def hide_attribute(key):
    if is_ipython():
        if key.startswith('_ipython_'):
            return True
        if key.startswith('_repr_'):
            return True
    return False


def is_ipython():
    try:
        __IPYTHON__
    except NameError:
        return False
    else:
        return True


def bind_template(root, name, node):
    for i, child in enumerate(root):
        if isinstance(child, Template) and child._name == name:
            root._children[i] = node
            return
        else:
            bind_template(child, name, node)
