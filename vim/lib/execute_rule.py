# Use in mapping of nested rules.
#
# mapping = {
#     "do <rule_a> <rule_b>": execute_rule("rule_b") + execute_rule("rule_a"),
#     "boo <rule_a> <rule_b>": execute_rule("rule_b", "rule_a"),
# }
#
# extras = [
#     RuleRef(rule = RuleA(), name = "rule_a"),
#     RuleRef(rule = RuleB(), name = "rule_b"),
# ]

from dragonfly import Function, ActionBase

def _executeRecursive(executable):
    if isinstance(executable, ActionBase):
        executable.execute()
    elif hasattr(executable, '__iter__'):
        for item in executable:
            _executeRecursive(item)
    else:
        print("Neither executable nor a list: ", executable)

def execute_rule(*rule_names):
    def _exec_function(**kwargs):
        for name in rule_names:
            executable = kwargs.get(name)
            _executeRecursive(executable)

    return Function(_exec_function)
