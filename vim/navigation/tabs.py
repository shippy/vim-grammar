from dragonfly import MappingRule, Key, Text, IntegerRef
class vimTabulatorRule(MappingRule):
    name = "gvim_tabulators"
    mapping = {
        # tabulator navigation commands
        "[<n>] tab right": Key("g,t"),
        "[<n>] tab left": Key("g,T"),
        "tab new": Key("colon") + Text("tabnew") + Key("enter"),
    }
    extras = [
        IntegerRef("n", 1, 10),
    ]
