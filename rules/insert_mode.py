from dragonfly import Choice, MappingRule, Key, RuleRef, Text, Dictation, IntegerRef
from . import object, motion
from ..choices.letter import letterChoice
from ..lib.execute_rule import execute_rule

# Both InsertModeStartRule and InsertModeFinishRule must be wrapped in grammar
# enabling / disabling objects in the main file that dragonfly processes.
class InsertModeStartRule(MappingRule):
    exported = True
    mapping = {
        "change <motion> [<text>]": Key("c") + execute_rule('motion') + Text('%(text)s'),
        "change <object> [<text>]": Key("c") + execute_rule('object') + Text('%(text)s'),
        "change line [<text>]": Key("c,c") + Text('%(text)s'),

        "insert [<text>]": Key("i") + Text('%(text)s'),
        "prepend [<text>]": Key("I") + Text('%(text)s'),
        "after [<text>]": Key("a") + Text('%(text)s'),
        "append [<text>]": Key("A") + Text('%(text)s'),
        "oh [<text>]": Key("o") + Text('%(text)s'),
        "bo [<text>]": Key("O") + Text('%(text)s'),

        "insert last [<text>]": Key("g, i") + Text('%(text)s'),
    }
    extras = [
        RuleRef(rule = motion.MotionRule(name = "insert_motion"), name = "motion"),
        RuleRef(rule = object.ObjectRule(name = "insert_object"), name = "object"),
        Dictation("text"),
    ]
    defaults = {
        "text": "",
    }

class InsertModeFinishRule(MappingRule):
    mapping = {
        "okay | kay | abort": Key("escape"),
        "cancel | oops": Key("escape, u"),
    }

class InsertModeCommands(MappingRule):
    mapping = {
        # Insertion
        "<text>": Key('c-g, u') + Text("%(text)s"), # create undo point
        # "complete": Key("tab"), # "tabby" should do the trick
        "comp line": Key("c-x, c-l"),
        "comp file": Key("c-x, c-f"),
        "shark paste <letter>": Key("c-r, %(letter)s"),
        "shark paste literal <letter>": Key("c-r:2, %(letter)s"),
        "shark paste sys": Key("c-r, asterisk"),
        "shark paste file": Key("c-r, percent"),
        "shark paste search": Key("c-r, slash"),
        "shark shift left": Key("c-t"),
        "shark shift right": Key("c-d"),

        # Deletion
        "scratch [last]": Key("escape, u, i"), # undo last utterance & re-enter insert mode
        "[<n>] scratch word": Key("c-w:%(n)d"),
        "[<n>] scratch line": Key("c-u:%(n)d"),
        "[<n>] scratch back": Key("c-h:%(n)d"),

        # Motion
        "[<n>] up": Key("up:%(n)d"),
        "[<n>] down": Key("down:%(n)d"),
        "[<n>] left": Key("left:%(n)d"),
        "[<n>] right": Key("right:%(n)d"),
        "go end": Key("c-e"),
        "go start": Key("escape, I"), # avoiding c-a because of tmux conflict

        "breathe <letter>": Key("space, %(letter)s, space"),
	"assign": Key("space, equal, space"),
    }
    extras = [
        letterChoice("letter"),
        Dictation("text"),
        IntegerRef("n", 1, 50),
    ]
    defaults = {
        "n": 1,
    }
