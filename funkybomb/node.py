from copy import deepcopy

from funkybomb.exceptions import ChildNodeError


class Node:
    """
    The building block of tree based templating.
    """

    def __init__(self, *nodes):
        """
        Initialize the Node.
        """

        self.children = []
        self.append(*nodes)

    def __repr__(self):
        return '<BaseNode>'

    def __call__(self, *args, **attrs):
        self.append(*args)
        return self

    def __add__(self, *nodes):
        cn = deepcopy(self)
        cn.append(*nodes)
        return cn

    def __iadd__(self, *nodes):
        if len(nodes) == 1 and type(nodes[0]) == tuple:
            nodes = nodes[0]
        self.append(*nodes)
        return self

    def append(self, *nodes):
        if not nodes:
            return
        if len(nodes) == 1 and type(nodes[0]) is list:
            nodes = nodes[0]
        self.children.extend(list(self.wash_nodes(*nodes)))

    def wash_nodes(self, *nodes):
        text_types = {bytes, str, int, float}
        for node in nodes:
            if type(node) in text_types:
                yield Text(node)
            elif type(node) is type:
                yield node()
            elif isinstance(node, Node):
                yield node
            else:
                raise ChildNodeError()


class Template(Node):

    def __init__(self, name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __repr__(self):
        if self.name:
            return '<TemplateNode[{name}]>'.format(name=self.name)
        else:
            return '<AnonymousTemplateNode>'


class Tag(Node):

    is_void = False
    is_raw_text = False
    tag = None
    attrs = None

    def __init__(self, tag=None, *args, **attrs):
        super().__init__(*args)
        if tag:
            self.tag = tag
        self.attrs = attrs

    def __repr__(self):
        return '<TagNode[{tag}]>'.format(tag=self.tag)

    @property
    def closer(self):
        if self.tag is None or self.is_void:
            return ''
        return '</{tag}>'.format(tag=self.tag)

    @property
    def opener(self):
        if self.tag is None:
            return ''

        if not self.attrs:
            return '<{tag}>'.format(tag=self.tag)

        pairs = []
        for key, value in self.attrs.items():
            if key == '_class':
                key = 'class'
            pairs.append((key, value))
        attrs = ' '.join(
            '{key}="{value}"'.format(key=key, value=value)
            for key, value in pairs)
        return '<{tag} {attrs}>'.format(tag=self.tag, attrs=attrs)

    def wash_nodes(self, *nodes):
        if self.is_void and nodes:
            raise ChildNodeError()
        elif self.is_raw_text:
            text_types = {bytes, str, int, float}
            for node in nodes:
                if type(node) is type:
                    node = node()
                if type(node) in text_types:
                    yield Text(node)
                elif type(node) is Text:
                    yield node
                else:
                    raise ChildNodeError()
        else:
            for node in super().wash_nodes(*nodes):
                yield node


class Text(Node):

    content = ''

    def __init__(self, content=''):
        super().__init__()
        self.content = str(content)
        self.opener = str(content)

    def __repr__(self):
        return '<TextNode["{text}"]>'.format(text=self.content)

    def wash_nodes(self, *nodes):
        raise ChildNodeError()
