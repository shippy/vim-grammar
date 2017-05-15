from dragonfly import Choice, MappingRule, Key, IntegerRef, RuleRef
from ..choices.letter import letterChoice
# from ..lib.execute_rule import execute_rule

# FIXME: `letter` is actually all characters
# "delete to arch", "yank to sierra"
class RegisterSaveRule(MappingRule):
    exported = False
    mapping = {
        "to <letter>": Key('dquote, %(letter)s')
    }
    extras = [
        letterChoice('letter')
    ]

# "paste up from tango"
class RegisterLoadRule(MappingRule):
    exported = False
    mapping = {
        "from <letter>": Key('dquote, %(letter)s')
    }
    extras = [
        letterChoice('letter')
    ]
