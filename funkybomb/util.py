from copy import deepcopy

from funkybomb.node import Template


def generate(node, prefix, indent, context):

    if isinstance(node, Template) and node._name_ and context and \
            node._name_ in context:
        node = context[node._name_]

    if node._opener_:
        yield prefix + node._opener_

    new_prefix = prefix
    if node._opener_ and node._closer_:
        new_prefix += indent

    for child in children(node):
        for output in generate(child, new_prefix, indent, context):
            yield output

    if node._closer_:
        yield prefix + node._closer_


def render(node, context=None, pretty=False):
    if pretty:
        return '\n'.join(generate(node, '', '    ', context))
    else:
        return ''.join(generate(node, '', '', context))


def freeze(node):
    node._children_ = tuple(node._children_)
    for child in children(node):
        freeze(child)


def children(node):
    return iter(node._children_)


def copy(node):
    return deepcopy(node)


def bind_template(node, name, value):
    for i, child in enumerate(children(node)):
        if isinstance(child, Template) and child._name_ == name:
            node._children_[i] = value
        else:
            bind_template(child, name, value)
