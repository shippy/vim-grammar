# Use in mapping of nested rules.
#
# mapping = {
#     "do <rule_a> <rule_b>": executeFactory("rule_b") + executeFactory("rule_a"),
#     "boo <rule_a> <rule_b>": multipleExecuteFactory(["rule_b", "rule_a"]),
# }
#
# extras = [
#     RuleRef(rule = RuleA(), name = "rule_a"),
#     RuleRef(rule = RuleB(), name = "rule_b"),
# ]

from dragonfly import Function, ActionBase

def executeFactory(extraName):
    def executeFunction(**kwargs):
        executable = kwargs.get(extraName)
        if isinstance(executable, ActionBase):
            executable.execute()
        else:
            # Note: Should this recurse?
            print "executeFactory cannot execute ", executable

    return Function(executeFunction)

def multipleExecuteFactory(extraNames):
    def multipleExecuteFunction(**kwargs):
        for name in extraNames:
            executable = kwargs.get(name)
            if isinstance(executable, ActionBase):
                executable.execute()
            else:
                print "multipleExecuteFactory cannot execute ", executable

    return Function(multipleExecuteFunction)
