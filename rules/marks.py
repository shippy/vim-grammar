from dragonfly import Choice, MappingRule, Key, IntegerRef, RuleRef, Text
from ..choices.letter import letterChoice
from ..lib.execute_rule import execute_rule

class MarkMotionRule(MappingRule):
    exported = False
    mapping = {
        "go <letter>": Key('apostrophe, %(letter)s'),
        "go line <letter>": Key('backtick, %(letter)s'),
    }
    extras = [
        letterChoice('letter'),
    ]

# Non-chainable op
class MarkOpRule(MappingRule):
    exported = False
    mapping = {
        "mark <letter>": Key("m, %(letter)s"),
        "show marks": Text(":marks") + Key("enter"),
        "clear mark <letter>": Text(':delmark %(letter)s'),
        # "clear marks <letter_sequence>": Text(':delmark ') + execute_rule('letter_sequence'),
    }
    extras = [
        letterChoice('letter')
    ]
