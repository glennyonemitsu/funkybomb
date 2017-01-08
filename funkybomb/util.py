def generate(node, prefix, indent, context):
    node_is_template = getattr(node, '_is_template', False)
    node_name = getattr(node, '_name', None)
    if node_is_template and node_name and context and node_name in context:
        node = context[node_name]

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
