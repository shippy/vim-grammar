from dragonfly import MappingRule, Key, Text, Dictation

class QuickSettingsRule(MappingRule):
    mapping = {
        "win diff": Key("colon") + Text("windo diffthis"),
        "win diff off": Key("colon") + Text("windo diffoff"),

        "win scroll": Key("colon") + Text("windo setl scrollbind"),
        "win scroll off": Key("colon") + Text("windo setl noscrollbind"),

        "fix exec": Key("q, colon"),
        "fix search": Key("q, slash"),

        "show registers": Text(":registers") + Key("enter"),
        "show dir": Text(":pwd") + Key("enter"),
        "show history": Text(":history") + Key("enter"),
        "show buffers": Text(":buffers") + Key("enter"),
        "show version": Text(":version") + Key("enter"),

        "show help": Text(":help ") + Key("enter"),

        # Preview windows:
        "show quick fix": Text(":copen") + Key("enter"),
        "hide quick fix": Text(":cclose") + Key("enter"),

        "show lock": Text(":lopen") + Key("enter"),
        "hide lock": Text(":lclose") + Key("enter"),

        # GUI windows:
        "system search": Text(":promptfind") + Key("enter"),
        "system sub": Text(":promptrepl") + Key("enter"),

        "show help [<text>]": Key("colon, h, space") + Text("%(text)s"),
    }
    extras = [
        Dictation('text')
    ]
    defaults = {
        'text': ''
    }
