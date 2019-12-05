from dragonfly import MappingRule, Key, Text, Dictation

class QuickReplaceRule(MappingRule):
    mapping = {
        "strip <haystack>":  Text(":%%s/%(haystack)s//c") + Key('enter'),
        "replace <replace>": Text(":%%s//%(replace)s/c") + Key('enter'),
        "sub <haystack> shark <replace>": Text(":%%s/%(haystack)s/%(replace)s/c") + Key('enter'),

        # For the confirmation dialog (due to the C flag)
        "sub (this | it | yes)": Key("y"),
        "sub (no | not)": Key("y"),
        "sub all": Key("a"),
        "sub last": Key("l"),
        "sub quit": Key("q"),
    }
    extras = [
        Dictation("haystack"),
        Dictation("replace"),
    ]
