from dragonfly import *
from vim.rules import action, motion
try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
    pass

print 'new gVim grammar accessed.'

release = Key("shift:up, ctrl:up")

normal_CCR_rules = [
    RuleRef(rule = action.ActionRule()),
    RuleRef(rule = motion.MotionRule()),
]
normal_CCR = Repetition(Alternative(normal_CCR_rules),
                        min = 1, max = 10,
                        name = "normal_mode_sequence")
class normalModeCCR(CompoundRule):
    spec     = "<normal_mode_sequence>"
    extras   = [ normal_CCR ]
    def _process_recognition(self, node, extras):
        # A sequence of actions.
        normal_mode_sequence = extras["normal_mode_sequence"]
        # An integer repeat count.
        for action in normal_mode_sequence:
            action.execute()
        release.execute()

gvim_exec_context = AppContext(executable="gvim")
vim_putty_context = AppContext(title="vim")
gvim_context = (gvim_exec_context | vim_putty_context)

normalModeGrammar = Grammar("gvim", context=gvim_context)
normalModeGrammar.add_rule(normalModeCCR())
normalModeGrammar.load()

# Unload function which will be called at unload time.
def unload():
    global normalModeGrammar
    if normalModeGrammar: normalModeGrammar.unload()
    normalModeGrammar = None
