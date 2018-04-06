from dragonfly import Choice, MappingRule, Key, IntegerRef, RuleRef
from .quick_search import QuickSearchRule
from .marks import MarkMotionRule
from ..choices.motion import motionChoice
from ..choices.uncountableMotion import uncountableMotionChoice
from ..lib.execute_rule import execute_rule

class MotionRule(MappingRule):
    exported = True
    mapping = {
        "[<n>] <motion>": Key("%(n)d, %(motion)s"),
        "<quick_search>": execute_rule('quick_search'),
        "<mark>": execute_rule('mark'),
        "go <uncountableMotion>": Key("%(uncountableMotion)s"),
    }
    extras = [
        IntegerRef("n", 1, 10),
        motionChoice("motion"),
        uncountableMotionChoice("uncountableMotion"),
        RuleRef(rule = QuickSearchRule(name = "motion_qsearch"), name = "quick_search"),
        RuleRef(rule = MarkMotionRule(name = "motion_mark"), name = "mark"),
    ]
    defaults = {
        "n": 1,
    }
