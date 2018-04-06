from dragonfly import MappingRule, CompoundRule, Key, IntegerRef, RuleRef, Text, Repetition, Alternative
from ..choices.letter import letterChoice

class LetterRule(MappingRule):
    mapping = {
        "<letter>": Key("%(letter)s"),
    }
    extras = [
        letterChoice("letter"),
    ]

letter_sequence = Repetition(
    Alternative([RuleRef(rule = LetterRule())]),
    min = 1, max = 6, name = "letter_sequence")

class LetterSequenceRule(CompoundRule):
    spec     = "<letter_sequence>"
    extras   = [ letter_sequence ]
    def _process_recognition(self, node, extras):
        # A sequence of actions.
        letter_sequence = extras["letter_sequence"]
        # An integer repeat count.
        for letter in letter_sequence:
            letter.execute()
        Key("shift:up, ctrl:up").execute()
