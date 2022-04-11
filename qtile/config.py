from libqtile import bar, layout, widget
from libqtile.config import Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

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
                [mod, "control"],
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
    layout.Columns(
        margin=12, 
        border_width=0,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font="JetBrainsMono NF",
    foreground="#1E1E1E",
    fontsize=16,
    padding=5,
)
extension_defaults = widget_defaults.copy()

follow_mouse_focus = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

wmname = "qtile"

top_bar = bar.Bar(
    [
        widget.Spacer(length=20),
        widget.CPU(format="CPU {freq_current}GHz {load_percent:02.0f}%"),
        widget.ThermalZone(format="({temp}°C)", fgcolor_normal=widget_defaults["foreground"]),
        widget.TextBox("|"),
        widget.Memory(format="{MemUsed:04.0f}{mm} / {MemTotal:04.0f}{mm} ({MemPercent:02.0f}%)"),
        widget.Prompt(),
        widget.Spacer(),
        widget.GroupBox(
            hide_unused=True,

            margin_x=0,
            padding_x=8,
            highlight_method="block",

            active=widget_defaults["foreground"],
            inactive=widget_defaults["foreground"],
            block_highlight_text_color="#FFFFFF",
            this_current_screen_border="#1793D0",
        ),
        widget.Spacer(),
        widget.Clock(format="%a %-d %b | %H:%M"),
        widget.Spacer(length=20)
    ],
    50,
    #background="#1793D0", # blue
    background="#E6E6E6",
)

from libqtile import hook

@hook.subscribe.startup
def startup():
    top_bar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)

lightmode = Screen(top=top_bar, wallpaper="/home/zp4rker/media/backgrounds/archbg2.png", wallpaper_mode="fill")
darkmode = Screen(top=top_bar, wallpaper="/home/zp4rker/media/backgrounds/archbg3.png", wallpaper_mode="fill")

screens = [
    lightmode,
]
