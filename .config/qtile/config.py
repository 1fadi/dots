from core import (
    keys,
    mouse,
    mod,
    widget_defaults,
    groups,
    screens,
    layouts,
    floating_layout
)

extension_defaults = widget_defaults.copy()
dgroups_key_binder = None
dgroups_app_rules: list = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
