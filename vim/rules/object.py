from dragonfly import Choice, MappingRule, Key, IntegerRef
from ..choices import object, modifier

class ObjectRule(MappingRule):
    exported = False
    mapping = {
        "[<n>] <modifier> <object>": Key("%(n)d, %(modifier)s, %(object)s")
    }
    extras = [
        IntegerRef("n", 1, 10),
        modifier.modifierChoice("modifier"),
        object.objectChoice("object"),
    ]
    defaults = {
        "n": 1,
    }
