from libqtile.config import Group

from .layouts import layouts, floating_layout
from .qwidgets import widget_defaults
from .screens import screens

groups = [Group(i) for i in "123456789"]

from .keys import keys, mouse, mod

__all__ = [
    "keys",
    "mouse",
    "mod",
    "layouts",
    "floating_layout",
    "screens",
    "groups",
    "widget_defaults"
]
