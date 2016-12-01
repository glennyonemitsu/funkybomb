class Node:

    def __init__(self):
        self.__root = self
        self.__children = []

    def __iadd__(self, *nodes):
        self._append(*nodes)
        return self

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
        self.__children += list(self._wash_nodes_hook(*nodes))
        
    def _prepend(self, *nodes):
        self.__children = list(self._wash_nodes_hook(*nodes)) + self.__children

    @property
    def _children(self):
        for child in self.__children:
            yield child

    @property
    def _root(self):
        if self.__root is self:
            return self
        return self.__root._root


class Renderable(Node):

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

    def __setitem__(self, name, content):
        t = Template(None)
        t += content
        self._root._content[name] = t

    @property
    def _children(self):
        if self._name in self._root._content:
            for node in self._root._content[self._name]._children:
                yield node
        else:
            # default
            for child in self.__children:
                yield child


class Tag(Renderable):

    def __init__(self, tag=None):
        self._tag = tag
        self._attrs = {}
        super().__init__()

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

    @property
    def _opener(self):
        return self._content
