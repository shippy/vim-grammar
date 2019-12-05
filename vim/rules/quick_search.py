from dragonfly import Choice, MappingRule, Key, IntegerRef, Dictation, Text
from ..choices.find import findChoice
from ..choices.search import searchChoice
from ..choices.letter import letterChoice

class QuickSearchRule(MappingRule):
    exported = False # part of MotionRule
    mapping = {
        "[<n>] <search> <text>": Key("%(n)d, %(search)s") + Text('%(text)s') + Key('enter'),
        "[<n>] <find> <letter>": Key("%(n)d, %(find)s") + Key('%(letter)s'),
    }
    extras = [
        IntegerRef("n", 1, 10),
        letterChoice('letter'),

        findChoice('find'),
        searchChoice('search'),
        Dictation('text'),
    ]
    defaults = {
        "n": 1,
    }
