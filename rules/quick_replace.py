from dragonfly import MappingRule, Key, Text, Dictation

class QuickReplaceRule(MappingRule):
    mapping = {
        "strip line <haystack>": Key("colon") + Text("s/%(haystack)s/c") + Key('enter'),
        "strip all <haystack>": Key("colon") + Text("%s/%(haystack)s/c") + Key('enter'),
        "replace line <replace>": Key("colon") + Text("s//%(replace)s/c") + Key('enter'),
        "replace all <replace>": Key("colon") + Text("s//%(replace)s/c") + Key('enter'),
        "sub line <haystack> shark <replace>": Key("colon") + Text("s/%(haystack)s/%(replace)s/c") + Key('enter'),
        "sub all <haystack> shark <replace>": Key("colon") + Text("%s/%(haystack)s/%(replace)s/c") + Key('enter'),
    }
    extras = [
        Dictation("haystack"),
        Dictation("replace"),
    ]
