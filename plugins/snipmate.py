from dragonfly import MappingRule, Text, Key, Dictation, Choice

class SnipMateRule(MappingRule):
    name = "snipmate"
    mapping = {
        "snip <text>": Text("%(text)s") + Key("tab"),
        "snip alias <alias>": Text("%(alias)s") + Key("tab"),
        # "snip letters <letter_sequence>": ...
    }
    extras = [
        Dictation("text"),
        Choice("alias", {
            # Whatever snippets become useful but hard to say?
            "fixture": "fix",
            "method": "defs",
            "function": "def",
            "class": "cl",
            "while loop": "wh",
            "for loop": "for",
            "mark code block": "codeblock",
        })
    ]
