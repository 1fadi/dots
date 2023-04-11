from libqtile.extension import CommandSet


def shorten_window_name(name):
    if name.endswith("Mozilla Firefox"):
        return name[-len("Mozilla Firefox"):]
    else:
        return name


commands = CommandSet(
    commands={
        "lock": "/usr/bin/i3lock -c 000000",
        "suspend": "systemctl suspend",
    },
    dmenu_prompt="Select a command: "
)
