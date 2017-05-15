from dragonfly import MappingRule, Key

class GeneralRule(MappingRule):
    mapping = {
        "cancel": Key("escape, u"),
        "abort": Key("escape"),
    }
