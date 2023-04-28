from libqtile import bar, widget
from libqtile.lazy import lazy

from .qwidgets import *
from .helpers import shorten_window_name
from .colors import hex_colors

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
    ClickableClock(
        name="clock2",
        time_format="%I:%M %p",
        date_format="%a, %d.%m.%Y %I:%M %p",
        fmt=" {} ",
        # background="292f36"
    ),
    widget.Spacer(length=bar.STRETCH),
    widget.Systray(),
    widget.WidgetBox(widgets=[
        *(
            widget.TextBox(
                "󰻠",
                fontsize=29,
                padding=4
            ),
            widget.GenPollText(
                func=cpu_func,
                update_interval=2,
                padding=8
            )
        ),
        widget.Sep(
            padding=1,
            linewidth=2,
        ),
        widget.Memory(
            format=" {MemUsed:.1f}{mm}/ {MemTotal:.1f}{mm}",
            mouse_callbacks={"Button1": lazy.spawn("kitty htop")},
            measure_mem="G",
            update_interval=2,
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
        charging_fg=hex_colors["light-sea-blue-2"]
    ),
],
    25,
    background="1a1a1a",
    border_width=[1, -5, 1, -5],
    border_color=hex_colors["light-sea-blue-2"],
)
