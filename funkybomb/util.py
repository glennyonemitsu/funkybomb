def generate(node, prefix, indent):
    if node._opener:
        yield prefix + node._opener

    new_prefix = prefix
    if node._opener and node._closer:
        new_prefix += indent

    for child in node:
        for output in generate(child, new_prefix, indent):
            yield output

    if node._closer:
        yield prefix + node._closer


def render(node, pretty=False):
    if pretty:
        return '\n'.join(generate(node, '', '    '))
    else:
        return ''.join(generate(node, '', ''))


def freeze(node):
    node._children = tuple(node._children)
    for child in node:
        freeze(child)
