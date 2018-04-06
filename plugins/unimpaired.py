from dragonfly import MappingRule, Key, Text, IntegerRef, Choice

class UnimpairedRule(MappingRule):
    mapping = {
        "edit <dir>": Key("%(dir)s, c"),
        "space <dir>": Key("%(dir)s, space"),
        "file <dir>": Key("%(dir)s, f"),
        "(lint | lock) <dir>": Key("%(dir)s, l"),
        "(quick | bug) <dir>": Key("%(dir)s, q"),

        # Ack puts search results in quickfixlist, so it should follow search
        "big <ack>": Key("%(ack)s, q"),
    }
    extras = [
        IntegerRef("n", 1, 10),
        Choice("dir", {
            "up": "lbracket",
            "down": "rbracket",
        }),
        Choice("ack", {
            "pecks": "lbracket",
            "next": "rbracket",
        })
    ]
    defaults = {
        'n': 1,
    }
