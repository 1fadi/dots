from libqtile import bar, widget
from libqtile.lazy import lazy

from .qwidgets import ClickableClock, VPN, Battery
from .helpers import shorten_window_name

from utils import cpu as cpu_func

bar_1 = bar.Bar([
    widget.TextBox(
        "",
        foreground="#809fff",
        fontsize=35,
        # background="292f36",
        padding=5,
        mouse_callbacks={
            'Button3': lazy.spawn('shutdown -P +1'),
            'Button1': lazy.spawn('shutdown -c')
        }),
    widget.GroupBox(
        highlight_method="block",
        this_current_screen_border="#809fff",
        fontsize=17,
        hide_unused=False,
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
        date_format="%a, %B %d, %Y",
        fmt=" {} ",
        # background="292f36"
    ),
    widget.Spacer(length=bar.STRETCH),
    widget.Systray(),
    widget.WidgetBox(widgets=[
        VPN(
            on="VPN",
            update_interval=2,
            background="273f1e",
            fmt=" {} "
        ),
        widget.Sep(
            padding=1,
            linewidth=1,
            background="000000",
        ),
        widget.Sep(
            padding=1,
            linewidth=2,
            background="000000"
        ),
        *(
            widget.TextBox(
                "󰻠",
                background="292f36",
                fontsize=29,
                padding=7
            ),
            widget.GenPollText(
                func=cpu_func,
                fmt="{} ",
                update_interval=2,
                background="292f36",
            )
        ),
        widget.Sep(
            padding=1,
            linewidth=2,
            background="000000"
        ),
        widget.Memory(
            format=" {MemUsed:.1f}{mm}/ {MemTotal:.1f}{mm}",
            mouse_callbacks={"Button1": lazy.spawn("kitty htop")},
            measure_mem="G",
            update_interval=2,
            background="273f1e", fmt=" {} "
        ),

        widget.Sep(
            padding=1,
            linewidth=2,
            background="#000000"
        ),
    ], text_closed=" ", text_open=""),
    *(
        widget.TextBox(
            "",
            fontsize=28,
            padding=8
        ),
        widget.Volume(
            fmt="{}",
        ),
    ),
    Battery(notify=True, update_interval=10),
    # widget.Battery(
    #     charge_char='',
    #     full_char='',
    #     empty_char='',
    #     discharge_char='',
    #     unknown_char='',
    #     update_interval=30,
    #     format='{char} {percent:2.0%}',
    #     background="273f1e",
    #     fmt=" {} "
    # ),
],
    24,
    background="4d4d4d",
    border_width=[0, 1, 1, 1],
    border_color=["000000", "000000", "000000", "000000"],
)
