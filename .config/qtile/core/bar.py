from libqtile import bar, widget
from libqtile.lazy import lazy

from .qwidgets import *
from .helpers import shorten_window_name

from utils import cpu as cpu_func

bar_1 = bar.Bar([
    # widget.TextBox(
    #     "",
    #     foreground="#809fff",
    #     fontsize=35,
    #     # background="292f36",
    #     padding=5,
    #     mouse_callbacks={
    #         'Button3': lazy.spawn('shutdown -P +1'),
    #         'Button1': lazy.spawn('shutdown -c')
    #     }),
    widget.GroupBox(
        highlight_method="block",
        this_current_screen_border="#809fff",
        fontsize=17,
        hide_unused=False,
        fmt="{}",
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
        # widget.Sep(
        #     padding=1,
        #     linewidth=1,
        # ),
        *(
            widget.TextBox(
                "󰻠",
                fontsize=29,
                padding=7
            ),
            widget.GenPollText(
                func=cpu_func,
                fmt="{} ",
                update_interval=2,
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
            fmt=" {} "
        ),
    ],
        text_closed="",
        text_open="",
        fontsize=25,
        close_button_location="right"
    ),
    VPN(
        on="VPN",
        update_interval=2,
        padding=6,
        fontsize=12
    ),
    Volume(foreground="d5d5d5", size=18),
    Network(size=13, interfaces=["wlan0", "enp0s31f6"]),
    Battery(
        notify=True,
        update_interval=10,
        size=(16, 32)
    ),
],
    25,
    background="1a1a1a",
    border_width=[0, 1, 1, 1],
    border_color=["000000", "000000", "000000", "000000"],
)
