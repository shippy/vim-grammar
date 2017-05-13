from dragonfly import MappingRule, Key, IntegerRef, Text
# FIXME: Just import config
from ..vim_config import get_config

c = get_config()

class NavigationRule(MappingRule):
    mapping = {
        # Jump list:
        "go old": Key("c-o"),
        "go new": Key("c-i"),

        # Cursor:
        "cursor top": Key("s-h"),
        "cursor middle": Key("s-m"),
        "cursor (low | bottom)": Key("s-l"),

        # Windows/viewports:
        "win west": Key(c.system.windowSwitchPrefix + "h"),
        "win east": Key(c.system.windowSwitchPrefix + "l"),
        "win north": Key(c.system.windowSwitchPrefix + "k"),
        "win south": Key(c.system.windowSwitchPrefix + "j"),
        "win switch": Key("c-w, c-w"),

        "win split": Key("c-w, s"),
        "win (vault | fault)": Key("c-w, v"),

        "win equal": Key("c-w, equal"),

        # Tabs:
        "[<n>] tab right": Key("g, t"),
        "[<n>] tab left": Key("g, T"),
        "tab new": Key("colon") + Text("tabnew") + Key("enter"),
    }
    extras = [
        IntegerRef("n", 1, 10),
    ]
    defaults = {
        "n": 1,
    }
