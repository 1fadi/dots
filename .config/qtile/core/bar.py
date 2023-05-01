from libqtile import bar, widget, hook
from libqtile.lazy import lazy

from .qwidgets import *
from .helpers import shorten_window_name
from .colors import hex_colors
from .qwidgets.border import Border

from utils import cpu as cpu_func

bar_1 = bar.Bar([
    widget.GroupBox(
        highlight_method="block",
        this_current_screen_border=hex_colors["light-sea-blue-2"],
        fontsize=17,
        hide_unused=False,
        padding=8
    ),
    widget.Prompt(),
    widget.WindowName(
        format="{state}{name}",
        parse_text=shorten_window_name,
    ),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    widget.Spacer(length=bar.STRETCH),
    ClickableClock(
        name="clock2",
        time_format="%I:%M",
        date_format="%a %d.%m.%Y %I:%M %p",
        fmt=" {} ",
    ),
    widget.Spacer(length=bar.STRETCH),
    widget.Systray(),
    widget.WidgetBox(widgets=[
        widget.GenPollText(
            func=cpu_func,
            update_interval=2,
            fmt="CPU {}"
        ),
        widget.Sep(
            padding=1,
            linewidth=2,
        ),
        widget.Memory(
            format="{MemUsed:.1f}{mm}/ {MemTotal:.1f}{mm}",
            mouse_callbacks={"Button1": lazy.spawn("kitty htop")},
            measure_mem="G",
            update_interval=2,
            fmt="MEM {}",
            padding=8
        ),
    ],
        text_closed="{} ",
        text_open="} ",
        fontsize=14,
        close_button_location="right"
    ),
    VPN(
        on="VPN",
        update_interval=2,
        padding=6,
        fontsize=12
    ),
    Network(size=13, interfaces=["wlan0", "enp0s31f6"]),
    Volume(foreground="d5d5d5", size=18),
    Battery(
        notify=True,
        update_interval=10,
        size=(16, 32),
        charging_fg=hex_colors["light-sea-blue-2"],
        padding=2
    ),
],
    25,
    background="1a1a1a",
    border_width=[1, -5, 1, -5],
    border_color=hex_colors["light-sea-blue-2"],
)

bar_2 = bar.Bar([
    Border("left", "triangle", foreground=hex_colors["grey-1"]),
    widget.GroupBox(
        highlight_method="block",
        this_current_screen_border=hex_colors["light-sea-blue-2"],
        fontsize=17,
        hide_unused=False,
        padding=8,
        background=hex_colors["grey-1"]
    ),
    Border(side="right", shape="triangle", foreground=hex_colors["grey-1"]),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    widget.Spacer(length=bar.STRETCH),
    Border("left", "triangle", foreground=hex_colors["grey-1"]),
    ClickableClock(
        name="clock2",
        time_format="%I:%M",
        date_format="%a %d.%m.%Y %I:%M %p",
        background=hex_colors["grey-1"]
    ),
    widget.Prompt(background=hex_colors["grey-1"]),
    Border(side="right", shape="triangle", foreground=hex_colors["grey-1"]),
    widget.Spacer(length=bar.STRETCH),
    widget.Systray(),
    Border("left", "triangle", foreground=hex_colors["grey-1"]),
    widget.WidgetBox(widgets=[
        widget.GenPollText(
            func=cpu_func,
            update_interval=2,
            background=hex_colors["grey-1"],
            fmt="CPU {}"
        ),
        widget.Sep(
            padding=1,
            linewidth=2,
            background=hex_colors["grey-1"],
        ),
        widget.Memory(
            format="{MemUsed:.1f}{mm}/ {MemTotal:.1f}{mm}",
            mouse_callbacks={"Button1": lazy.spawn("kitty htop")},
            measure_mem="G",
            update_interval=2,
            fmt="MEM {}",
            background=hex_colors["grey-1"],
            padding=8
        ),
    ],
        text_closed=" {} ",
        text_open="} ",
        fontsize=14,
        close_button_location="right",
        background=hex_colors["grey-1"],
    ),
    VPN(
        on="VPN",
        update_interval=2,
        padding=6,
        fontsize=12,
        background=hex_colors["grey-1"]
    ),
    Network(size=13, interfaces=["wlan0", "enp0s31f6"], background=hex_colors["grey-1"]),
    Volume(foreground="d5d5d5", size=18, background=hex_colors["grey-1"]),
    Battery(
        notify=True,
        update_interval=10,
        size=(16, 32),
        charging_fg=hex_colors["light-sea-blue-2"],
        padding=2,
        background=hex_colors["grey-1"],
        font_color=hex_colors["grey-1"]
    ),
    Border(side="right", shape="triangle", foreground=hex_colors["grey-1"]),
],
    25,
    background="00000000",
    margin=[2, 0, 2, 0],
)

@hook.subscribe.startup
def _():
    bar_2.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)
