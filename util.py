def generate(node, prefix, indent, suffix):
    if node._opener:
        yield prefix
        yield node._opener
        yield suffix

    new_prefix = prefix
    if node._opener and node._closer:
        new_prefix += indent

    for child in node:
        for output in generate(child, new_prefix, indent, suffix):
            yield output

    if node._closer:
        yield prefix
        yield node._closer
        yield suffix


def render(node, pretty=False):
    return ''.join(generate(node, '', '    ', '\n'))
