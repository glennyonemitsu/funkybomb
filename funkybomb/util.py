from funkybomb.node import Template


def generate(node, prefix, indent, context):

    if isinstance(node, Template) and node._name and context and \
            node._name in context:
        node = context[node._name]

    if node._opener:
        yield prefix + node._opener

    new_prefix = prefix
    if node._opener and node._closer:
        new_prefix += indent

    for child in node:
        for output in generate(child, new_prefix, indent, context):
            yield output

    if node._closer:
        yield prefix + node._closer


def render(node, context=None, pretty=False):
    if pretty:
        return '\n'.join(generate(node, '', '    ', context))
    else:
        return ''.join(generate(node, '', '', context))


def freeze(node):
    node._children = tuple(node._children)
    for child in node:
        freeze(child)
