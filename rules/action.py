from dragonfly import Choice, MappingRule, Key, IntegerRef, RuleRef, Text
from ..choices.verb import verbChoice
from ..choices.simple_verb import simpleVerbChoice
from ..choices.letter import letterChoice
from . import object, motion
from ..lib.execute_factory import executeFactory, multipleExecuteFactory

class ActionRule(MappingRule):
    exported = True
    mapping = {
        "[<n>] <verb> <motion>": Key("%(n)s, %(verb)s") + executeFactory('motion'),
        "[<n>] <verb> <object>": Key("%(n)s, %(verb)s") + executeFactory('object'),
        "[<n>] <simple_verb>": Key("%(n)s, %(simple_verb)s"),
        "[<n>] <verb> line": Key("%(n)s, %(verb)s:2"),

        # Special cases:
        # TODO: replace sequence <letter_sequence>
        "[<n>] replace <letter>": Key("%(n)s, r, %(letter)s"),
        "record <letter>": Key("q, %(letter)s"),

        "select line": Key("V"),
        "select last": Key("g, v"),
        "(visual | select) block": Key("c-v"),
        "duplicate line": Key("y, y, p"),
    }
    extras = [
        IntegerRef("n", 1, 10),
        verbChoice("verb"),
        simpleVerbChoice("simple_verb"),
        letterChoice("letter"),
        RuleRef(rule = motion.MotionRule(name = "action_motion"), name = "motion"),
        RuleRef(rule = object.ObjectRule(name = "action_object"), name = "object"),
    ]
    defaults = {
        "n": 1,
    }
