from dragonfly import Choice, MappingRule, Key, IntegerRef, RuleRef
from ..choices.surround import surroundChoice
from ..rules import object, motion
from ..lib.execute_factory import executeFactory, multipleExecuteFactory

class SurroundRule(MappingRule):
    mapping = {
        # Adding surround (done separately for object and motion to avoid nesting both):
        "(Sir | wrap) <object> [in] <surround>": Key("y, s") + executeFactory('object') + Key("%(surround)s"),
        "(Sir | wrap) <motion> [in] <surround>": Key("y, s") + executeFactory('motion') + Key("%(surround)s"),
        "(Sir | wrap) now [in] <surround>": Key("S, %(surround)s"),

        # Changing and deleting surround:
        "(change Sir | strange) [from] <surround> [to] <surround_alt>": Key("c,s") + Key("%(surround)s"),
        "(delete Sir | sleet) <surround>": Key("d,s") + Key("%(surround)s"),
    }
    extras = [
        surroundChoice('surround'),
        surroundChoice('surround_alt'),
        RuleRef(rule = motion.MotionRule(name = "surround_motion"), name = "motion"),
        RuleRef(rule = object.ObjectRule(name = "surround_object"), name = "object"),
    ]
    defaults = {
        'modifier': 'inner',
    }
