class Node:
    """
    The building block of tree based templating.
    """

    def __init__(self):
        self.__root = self
        self._children = []

    def __iadd__(self, *nodes):
        self._append(*nodes)
        return self

    def __repr__(self):
        return '<BaseNode>'

    def __iter__(self):
        return iter(self._children)

    def _wash_nodes_hook(self, *nodes):
        return list(self._set_root_for_nodes(*self._wash_nodes(*nodes)))

    def _set_root_for_nodes(self, *nodes):
        for node in nodes:
            node.__root = self._root
            yield node

    def _wash_nodes(self, *nodes):
        for node in nodes:
            yield node

    def _append(self, *nodes):
        self._children.extend(list(self._wash_nodes_hook(*nodes)))

    def _prepend(self, *nodes):
        self._children = list(self._wash_nodes_hook(*nodes)) + self._children

    @property
    def _root(self):
        if self.__root is self:
            return self
        return self.__root._root


class Renderable(Node):

    def __repr__(self):
        return '<RenderableNode>'

    def __getattr__(self, key):
        n = Tag(key)
        self._append(n)
        return n

    def __call__(self, *args, **kwargs):
        self._append(*args)
        self._attrs = kwargs
        return self

    @property
    def _opener(self):
        return ''

    @property
    def _closer(self):
        return ''

    def _wash_nodes(self, *nodes):
        for node in nodes:
            if type(node) is str:
                yield Text(node)
            else:
                yield node


class Template(Renderable):

    def __init__(self, name=None):
        self._name = name
        self._content = {}
        super().__init__()

    def __repr__(self):
        if self._name:
            return '<TemplateNode[{name}]>'.format(name=self._name)
        else:
            return '<AnonymousTemplateNode>'

    def __setitem__(self, name, content):
        t = Template(None)
        t += content
        self._root._content[name] = t

    def __iter__(self):
        if self._name in self._root._content:
            contents = self._root._content[self._name]
        else:
            contents = self._children

        for node in contents:
            yield node


class Tag(Renderable):

    def __init__(self, tag=None):
        self._tag = tag
        self._attrs = {}
        super().__init__()

    def __repr__(self):
        return '<TagNode[{tag}]>'.format(tag=self._tag)

    @property
    def _opener(self):
        if self._tag is None:
            return ''

        if not self._attrs:
            return '<{tag}>'.format(tag=self._tag)

        attrs = ' '.join(
            '{key}="{value}"'.format(key=key, value=value)
            for key, value in self._attrs.items())
        return '<{tag} {attrs}>'.format(tag=self._tag, attrs=attrs)

    @property
    def _closer(self):
        if self._tag is None:
            return ''
        return '</{tag}>'.format(tag=self._tag)


class Text(Renderable):

    def __init__(self, content=''):
        self._content = content
        super().__init__()

    def __repr__(self):
        return '<TextNode["{text}"]>'.format(text=self._content)

    @property
    def _opener(self):
        return self._content
