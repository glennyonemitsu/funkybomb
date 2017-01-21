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

    for child in node:
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
    for child in node:
        freeze(child)
