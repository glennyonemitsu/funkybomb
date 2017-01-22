from copy import deepcopy

from funkybomb.node import Template


def generate(node, prefix, indent, context):

    if isinstance(node, Template) and node.name and context and \
            node._name_ in context:
        node = context[node.name]

    if node.opener:
        yield prefix + node.opener

    new_prefix = prefix
    if node.opener and node.closer:
        new_prefix += indent

    for child in node.children:
        for output in generate(child, new_prefix, indent, context):
            yield output

    if node.closer:
        yield prefix + node.closer


def render(node, context=None, pretty=False):
    if pretty:
        return '\n'.join(generate(node, '', '    ', context))
    else:
        return ''.join(generate(node, '', '', context))


def freeze(node):
    node.children = tuple(node.children)
    for child in node.children:
        freeze(child)


def copy(node):
    return deepcopy(node)


def bind_template(node, name, value):
    for i, child in enumerate(node.children):
        if isinstance(child, Template) and child.name == name:
            node.children[i] = value
        else:
            bind_template(child, name, value)
