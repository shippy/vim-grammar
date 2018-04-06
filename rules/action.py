from dragonfly import Choice, MappingRule, Key, IntegerRef, RuleRef, Text
from ..choices.verb import verbChoice
from ..choices.simple_verb import simpleVerbChoice
from ..choices.letter import letterChoice
from . import object, motion
from .letter import LetterSequenceRule
from ..lib.execute_rule import execute_rule

class ActionRule(MappingRule):
    mapping = {
        # "[<n>] <verb> <motion>": Key("%(n)s, %(verb)s") + execute_rule('motion'),
        # "[<n>] <verb> <object>": Key("%(n)s, %(verb)s") + execute_rule('object'),
        # FIXME: `select` is screwy with countable motions -- the meaning is different
        # -> disabling for now while preserving object/motion count
        "<verb> <motion>": Key("%(verb)s") + execute_rule('motion'),
        "<verb> <object>": Key("%(verb)s") + execute_rule('object'),
        "[<n>] <simple_verb>": Key("%(n)s, %(simple_verb)s"),
        "[<n>] <verb> line": Key("%(n)s, %(verb)s:2"),

        # Special cases:
        # TODO: replace sequence <letter_sequence>
        "replace spell <letter_sequence>": Key("R") + execute_rule('letter_sequence') + Key("escape"),
        "[<n>] replace <letter>": Key("%(n)s, r, %(letter)s"),
        "record <letter>": Key("q, %(letter)s"),

        # TODO: Take "select" out of "verbChoice", define it fully here
        "select line": Key("V"),
        "select last": Key("g, v"),
        "visual other": Key("o"), # switch to other end of visual selection
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
        RuleRef(rule = LetterSequenceRule(name = "action_letter_sequence"), name = "letter_sequence")
    ]
    defaults = {
        "n": 1,
    }
