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
