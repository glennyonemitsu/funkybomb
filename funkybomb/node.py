from funkybomb.exceptions import ChildNodeError


class Node:
    """
    The building block of tree based templating.
    """

    _node_attr_keys = {
        '_children', '_tag',
        '_attrs', '_node_attrs',
        '_root', '_root_node'
        # '_wash_nodes_hook', '_wash_nodes', '_set_root_for_nodes', '_append',

    }

    def __init__(self):
        """
        Initialize the Node.
        """

        self.__dict__['attrs'] = {}
        self._root_node = self
        self._children = []

    def __add__(self, *nodes):
        """
        Append nodes from the += notation.
        """

        self._append(*nodes)

    def __repr__(self):
        """
        String representation of the object.
        """

        return '<BaseNode>'

    def __iter__(self):
        return iter(self._children)

    def __setattr__(self, key, value):
        if key.startswith('__'):
            object.__setattr__(self, key, value)
        elif key in self._node_attr_keys:
            self.__dict__['attrs'][key] = value
        else:
            self._append(value)

    def __getattr__(self, key):
        if key in self._node_attr_keys:
            return self.__dict__['attrs'][key]
        return object.__getattr__(self, key)

    @property
    def _node_attrs(self):
        if type(self) is Node:
            return self._node_attr_keys
        return self._node_attr_keys

    def _wash_nodes_hook(self, *nodes):
        return self._set_root_for_nodes(*self._wash_nodes(*nodes))

    def _set_root_for_nodes(self, *nodes):
        for node in nodes:
            if node is None:
                continue
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

    _node_attr_keys = {'_opener', '_closer', '_wash_nodes'} | \
        Node._node_attr_keys

    def __repr__(self):
        return '<RenderableNode>'

    def __init__(self, *args, **attrs):
        super().__init__(*args)
        self._attrs = attrs

    def __getattr__(self, key):
        if key in self._node_attr_keys:
            return self.__dict__['attrs'].get(key, None)
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

    _node_attr_keys = {'_content', '_name'} | Renderable._node_attr_keys

    def __init__(self, name=None):
        super().__init__()
        self._name = name
        self._content = {}

    def __repr__(self):
        if self._name:
            return '<TemplateNode[{name}]>'.format(name=self._name)
        else:
            return '<AnonymousTemplateNode>'

    def __setitem__(self, name, content):
        t = Template(None)
        t + content
        self._root._content[name] = t

    def __iter__(self):
        if self._name in self._root._content:
            contents = self._root._content[self._name]
        else:
            contents = self._children

        if contents:
            for node in contents:
                yield node


class Tag(Renderable):

    _node_attr_keys = {'_tag', '_attrs'} | Renderable._node_attr_keys

    # html 5 tag categories according to
    # https://www.w3.org/TR/html5/syntax.html#void-elements
    _void_tags = {
        'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'keygen',
        'link', 'meta', 'param', 'source', 'track', 'wbr'
    }

    _raw_text_tags = {'script', 'style'}

    def __init__(self, tag=None, **attrs):
        super().__init__()
        self._tag = tag
        self._attrs = attrs

    def __repr__(self):
        return '<TagNode[{tag}]>'.format(tag=self._tag)

    def _wash_nodes(self, *nodes):
        if self._void and nodes:
            raise ChildNodeError()
        elif self._raw_text:
            for node in nodes:
                if type(node) is str:
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

        attrs = ' '.join(
            '{key}="{value}"'.format(key=key, value=value)
            for key, value in self._attrs.items())
        return '<{tag} {attrs}>'.format(tag=self._tag, attrs=attrs)

    @property
    def _closer(self):
        if self._tag is None or self._void:
            return ''
        return '</{tag}>'.format(tag=self._tag)


class Text(Renderable):

    _node_attr_keys = {'_content'} | Renderable._node_attr_keys

    def __init__(self, content=''):
        super().__init__()
        self._content = content

    def __repr__(self):
        return '<TextNode["{text}"]>'.format(text=self._content)

    @property
    def _opener(self):
        return self._content
