class Node:

    def __init__(self):
        self._children = []

    def __iadd__(self, *nodes):
        nodes = self._wash_nodes(*nodes)
        self._children.extend(nodes)
        return self

    def _wash_nodes(self, *nodes):
        return nodes

    @property
    def _opener(self):
        return ''

    @property
    def _closer(self):
        return ''


class Html(Node):

    def _wash_nodes(self, *nodes):
        for node in nodes:
            if type(node) is str:
                yield Text(node)
            else:
                yield node


class Tag(Html):

    def __init__(self, tag=None):
        self._tag = tag
        self._attrs = {}
        super().__init__()

    def __getattr__(self, key):
        n = Tag(key)
        self._children.append(n)
        return n

    def __call__(self, *args, **kwargs):
        self._children = list(args)
        self._attrs = kwargs
        return self

    @property
    def _opener(self):
        if self._tag is None:
            return ''

        if not self._attrs:
            return '<{tag}>'.format(tag=self._tag)

        attrs = ' '.join('{key}="{value}"'.format(key=key, value=value)
            for key, value in self._attrs.items())
        return '<{tag} {attrs}>'.format(tag=self._tag, attrs=attrs)

    @property
    def _closer(self):
        if self._tag is None:
            return ''
        return '</{tag}>'.format(tag=self._tag)


class Text(Html):

    def __init__(self, content=''):
        self._content = content
        super().__init__()

    @property
    def _opener(self):
        return self._content
