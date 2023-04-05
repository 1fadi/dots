from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.extension import CommandSet

from widgets.clickable_clock import ClickableClock

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

commands = CommandSet(
    commands={
        "lock": "/usr/bin/i3lock -c 000000",
        "suspend": "systemctl suspend",
    },
    dmenu_prompt="Select a command: "
)

my_keys = [    
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset 'Master' 5%+"), desc="raise volume level"), 
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset 'Master' 5%-"), desc="lower volume level"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle"), desc="Mute sound"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+ -n 1"), desc="increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%- -n 1"), desc="descrease brightness"),
    Key([mod], "b", lazy.spawn("qutebrowser"), desc="qutebrowser"), 
    Key([mod], "p", lazy.run_extension(commands)),
    Key([], "F9", lazy.widget["clock2"].toggle_date, desc="test"),
]

for key in my_keys:
    keys.append(key)

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus="#809fff", border_normal="#00134d", border_width=2, margin=4, margin_on_single=0),
    layout.Max(),
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    layout.Matrix(),
    #layout.MonadTall(),
    #layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraCode Nerd Font Mono",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method="block",
                    this_current_screen_border="#809fff",
                    fontsize=17,
                    hide_unused=False,
                ),
                widget.Prompt(),
                widget.WindowName(format="{state}{name}"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    background="000000"
                ),
                widget.Net(
                    format=" {down} ↓↑ {up}",
                    interface="wlan0",
                    update_interval=1,
                    background="292f36", fmt=" {} "
                ),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    background="000000"
                ),
                widget.Memory(
                    format=" {MemUsed:.1f}{mm}/ {MemTotal:.1f}{mm}",
                    mouse_callbacks={"Button1": lazy.spawn("alacritty -e htop")},
                    measure_mem="M",
                    update_interval=2,
                    background="273f1e", fmt=" {} "
                ),

                widget.Sep(
                    padding=10,
                    linewidth=2,
                    background="#000000"
                ),
                *(
                    widget.TextBox(
                        " ",
                        background="292f36",
                        fontsize=20
                    ),
                    widget.Volume(
                        fmt=" {} ",
                        background="292f36",
                 ),

                ),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    background="000000"
                ),
                widget.Battery(
                    charge_char='',
                    full_char='', 
                    empty_char='',
                    discharge_char='',
                    unknown_char='', 
                    update_interval=30,
                    format='{char} {percent:2.0%}',
                    background="273f1e",
                    fmt=" {} "
                ),
                widget.Sep(
                    padding=10, 
                    linewidth=2,
                    background="000000"
                ),
                ClickableClock(
                    name="clock2",
                    time_format="%I:%M %p",
                    date_format="%a, %B %d, %Y",
                    fmt=" {} ",
                    background="292f36"
                ),
                widget.TextBox(
                    "",
                    foreground="#809fff",
                    fontsize=35,
                    background="292f36", 
                    mouse_callbacks={
                        'Button3': lazy.spawn('shutdown -P +1'),
                        'Button1': lazy.spawn('shutdown -c')
                    }),
            ],
            24,
            background="4d4d4d",
            border_width=[0, 1, 1, 1],
            border_color=["000000", "000000", "000000", "000000"]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
