from funkybomb.exceptions import ChildNodeError


class Node:
    """
    The building block of tree based templating.
    """

    def __init__(self):
        """
        Initialize the Node.
        """

        self._children_ = []

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        return None

    def __setattr__(self, key, value):
        if key.startswith('_') and key.endswith('_'):
            self.__dict__[key] = value
            return
        super().__setattr__(key, value)

    def __repr__(self):
        """
        String representation of the Node.
        """

        return '<BaseNode>'

    def __iter__(self):
        return iter(self._children_)

    def __add__(self, *nodes):
        """
        Append nodes from the += notation.
        """

        # supports: self + ('foo', 'bar', Tag('em') + 'baz') notation
        if len(nodes) == 1 and type(nodes[0]) == tuple:
            nodes = nodes[0]
        self._append_(*nodes)
        return self

    def _wash_nodes_(self, *nodes):
        for node in nodes:
            yield node

    def _append_(self, *nodes):
        if len(nodes) == 1 and type(nodes[0]) is list:
            nodes = nodes[0]
        self._children_.extend(list(self._wash_nodes_(*nodes)))


class Renderable(Node):

    def __repr__(self):
        return '<RenderableNode>'

    def __init__(self, **attrs):
        super().__init__()
        self._attrs_ = attrs
        self._opener_ = ''
        self._closer_ = ''

    def __setattrz__(self, key, value):
        if value is None:
            return

        if key.startswith('_') and key.endswith('_'):
            super().__setattr__(key, value)
            return

        self._append_(value)

    def __getattr__(self, key):

        # required for a bunch of magic methods quirks like with deepcopy()
        if key.startswith('_') and key.endswith('_'):
            return super().__getattr__(key)

        if hide_attribute(key):
            return None

        n = Tag(key)
        self._append_(n)
        return n

    def __call__(self, *args, **kwargs):
        self._append_(*args)
        self._attrs_.update(kwargs)
        return self

    def _wash_nodes_(self, *nodes):
        text_types = {str, int, float}
        for node in nodes:
            if type(node) in text_types:
                yield Text(node)
            else:
                yield node


class Template(Renderable):

    def __init__(self, name=None):
        super().__init__()
        self._name_ = name

    def __repr__(self):
        if self._name_:
            return '<TemplateNode[{name}]>'.format(name=self._name_)
        else:
            return '<AnonymousTemplateNode>'

    def __setitem__(self, key, value):
        bind_template(self, key, value)


class Tag(Renderable):

    # html 5 tag categories according to
    # https://www.w3.org/TR/html5/syntax.html#void-elements
    _void_tags_ = {
        'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'keygen',
        'link', 'meta', 'param', 'source', 'track', 'wbr'
    }

    _raw_text_tags_ = {'script', 'style'}

    def __init__(self, tag=None, **attrs):
        super().__init__(**attrs)
        self._tag_ = tag
        self._void_ = self._tag_ in self._void_tags_
        self._raw_text_ = self._tag_ in self._raw_text_tags_
        self._repr_ = '<TagNode[{tag}]>'.format(tag=tag)

        if self._tag_ is None:
            self._opener_ = ''
        elif not self._attrs_:
            self._opener_ = '<{tag}>'.format(tag=self._tag_)
        else:
            attrs = build_attrs(self._attrs_)
            self._opener_ = '<{tag} {attrs}>'.format(
                tag=self._tag_, attrs=attrs)

        if self._tag_ is None or self._void_:
            self._closer_ = ''
        else:
            self._closer_ = '</{tag}>'.format(tag=self._tag_)

    def __repr__(self):
        return self._repr_

    def _wash_nodes_(self, *nodes):
        if self._void_ and nodes:
            raise ChildNodeError()
        elif self._raw_text_:
            text_types = {str, int, float}
            for node in nodes:
                if type(node) in text_types:
                    yield Text(node)
                elif type(node) is Text:
                    yield node
                else:
                    raise ChildNodeError()
        else:
            for node in super()._wash_nodes_(*nodes):
                yield node


class Text(Renderable):

    def __init__(self, content=''):
        super().__init__()
        self._content_ = str(content)
        self._opener_ = str(content)

    def __repr__(self):
        return '<TextNode["{text}"]>'.format(text=self._content_)


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
        if isinstance(child, Template) and child._name_ == name:
            root._children_[i] = node
            return
        else:
            bind_template(child, name, node)
