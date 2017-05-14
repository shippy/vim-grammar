from dragonfly import Choice, MappingRule, Key, RuleRef, Text, Dictation, IntegerRef
from . import object, motion
from ..choices.letter import letterChoice
from ..lib.execute_factory import executeFactory, multipleExecuteFactory

# Both CommandModeStartRule and CommandModeFinishRule must be wrapped in grammar
# enabling / disabling objects in the main file that dragonfly processes.
class CommandModeStartRule(CompoundRule):
    # Spoken command to enable the ExMode grammar.
    spec = "(exec | execute)"

class CommandModeFinishRule(CompoundRule):
    # spoken command to exit ex mode
    spec = "<command>"
    extras = [Choice("command", {
        "kay": "okay",
        "(cancel | oops)": "cancel",
    })]

# handles ExMode control structures
class CommandModeCommands(MappingRule):
    mapping  = {
        "read": Text("r "),
        "edit": Text("e "),
        "tab edit": Text("tabe "),
        "tab new": Text("tabnew "),

        "P. W. D.": Text("pwd "),

        "help": Text("help "),
        "sub line": Text("s/"),
        "sub file": Text("%s/"),
        "up": Key("up"),
        "down": Key("down"),
        "[<n>] left": Key("left:%(n)d"),
        "[<n>] right": Key("right:%(n)d"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
    ]
    defaults = {
        "n": 1,
    }

