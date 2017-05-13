from dragonfly import Choice, MappingRule, Key, IntegerRef
from ..choices.motion import motionChoice
from ..choices.uncountableMotion import uncountableMotionChoice

class MotionRule(MappingRule):
    exported = True
    mapping = {
        "[<n>] <motion>": Key("%(n)d, %(motion)s"),
        "go <uncountableMotion>": Key("%(uncountableMotion)s"),
    }
    extras = [
        IntegerRef("n", 1, 10),
        motionChoice("motion"),
        uncountableMotionChoice("uncountableMotion"),
    ]
    defaults = {
        "n": 1,
    }
