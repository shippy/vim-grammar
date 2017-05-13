from dragonfly import MappingRule, Key, Text

class QuickSettingsRule(MappingRule):
    mapping = {
        "win diff": Key("colon") + Text("windo diffthis"),
        "win diff off": Key("colon") + Text("windo diffoff"),

        "win scroll": Key("colon") + Text("windo scrollbind"),
        "win scroll off": Key("colon") + Text("windo noscrollbind"),
    }
