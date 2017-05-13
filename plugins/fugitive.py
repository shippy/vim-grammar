from dragonfly import MappingRule, Key, Text, IntegerRef

class FugitiveRule(MappingRule):
    mapping = {
        # Big picture commands:
        "get status": Text(":Gstatus"),
        "get diff this": Text(":Gdiff"),
        "get commit": Text(":Gcommit"),

        # Navigating Gstatus window:
        # TODO: Should only be triggered by "get status"?
        "[<n>] get up": Key("%(n)d, c-p"),
        "[<n>] get down": Key("%(n)d, c-n"),
        "get add": Key("hyphen"),
        "get diff": Key("D"),
        "get (scratch | clean)": Key("U"),
        "get amend": Key("c, a"),
    }
    extras = [
        IntegerRef("n", 1, 10),
    ]
    defaults = {
        'n': 1,
    }
