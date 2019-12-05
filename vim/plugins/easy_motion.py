from dragonfly import MappingRule, Key, Dictation
from ..choices.letter import letterChoice
from ..choices.motion import motionChoice
from ..choices.find import findChoice
from ..choices.search import searchChoice

# TODO: Bi-directional, sneak, operator-pending modes
class EasyMotionRule(MappingRule):
    name = "gvim_EasyMotion"
    mapping = {
        "queasy <letter>": Key("backslash,backslash") + Key('%(letter)s'),
        "queasy <motion>": Key("backslash,backslash") + Key("%(motion)s"),
        "queasy <find> <letter>": Key("backslash,backslash") + Key("%(find)s,%(letter)s") + Key("enter"),
        "queasy <search> <text>": Key("backslash,backslash") + Key("%(search)s,%(text)s") + Key("enter"),
    }
    extras = [
        findChoice('find'),
        searchChoice('search'),
        # FIXME: Some of these motion choices should maybe be purged?
        motionChoice('motion'),
        letterChoice('letter'),
        Dictation("text"),
    ]
