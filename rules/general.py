from dragonfly import MappingRule, Key, Text

class GeneralRule(MappingRule):
    mapping = {
        "cancel": Key("escape, u"),
        "abort": Key("c-c"),
        "hide light": Text(':nohlsearch\n'),
        "local directory": Text('lcd %:h'),
    }
