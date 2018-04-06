from dragonfly import MappingRule, Key, Text, IntegerRef

class FugitiveRule(MappingRule):
    mapping = {
        # Big picture commands:
        "get status": Text(":Gstatus") + Key("enter"),
        "get diff this": Text(":Gdiff") + Key("enter"),
        "get commit": Text(":Gcommit") + Key("enter"),

        # Navigating Gstatus window:
        # TODO: Own grammar with AppContext "vim - index"
        "[<n>] get up": Key("%(n)d, c-p"),
        "[<n>] get down": Key("%(n)d, c-n"),
        "get pick": Key("hyphen"), # add on unstaged/untracked, remove on staged files
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
