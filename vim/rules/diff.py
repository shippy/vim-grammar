from dragonfly import MappingRule, Key, Text

class DiffRule(MappingRule):
    mapping = {
        "put edit": Key("d, p"),
        "get edit": Key("d, o"),
    }
