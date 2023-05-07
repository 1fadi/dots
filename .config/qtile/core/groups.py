from libqtile import hook, qtile
# from libqtile.lazy import lazy
from libqtile.config import Group

groups = [Group(i) for i in "123456789"]
groups[2] = Group("3", label="~", spawn="xterm -e ranger", layout="max")


@hook.subscribe.setgroup
def on_group_change():
    current_group = qtile.current_group
    if current_group.name == "3":
        if current_group.windows:
            return
        else:
            qtile.cmd_spawn("xterm -e ranger")

