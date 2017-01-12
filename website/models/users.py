from collections import namedtuple


user = namedtuple('User', ('name', 'age'))


def get_all():
    return (
        user('John', 43),
        user('Jane', 32),
        user('Bill', 21)
    )
