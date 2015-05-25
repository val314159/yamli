"""
yaml + includes
"""
from yaml import *
_root = os.path.curdir
def _include(loader, node):
    """Include another YAML file."""
    import os.path
    global _root
    old_root = _root
    filename = os.path.join(root, loader.construct_scalar(node))
    _root = os.path.split(filename)[0]
    data = load(open(filename, 'r'))
    _root = old_root
    return data
add_constructor('!include', _include)
