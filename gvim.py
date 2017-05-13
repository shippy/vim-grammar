from dragonfly import *
from vim.rules import action, motion, navigation, buffer, quick_replace
from vim.plugins import surround, easy_motion, netrw, ctrlp
from vim.vim_config import get_config
try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
    pass

print 'new gVim grammar accessed.'

# Saving generally useful info
config = get_config()
release = Key("shift:up, ctrl:up")

# What rules go in the chainable continuous command recognition?
normal_CCR_rules = [
    RuleRef(rule = action.ActionRule()),
    RuleRef(rule = motion.MotionRule()),
    RuleRef(rule = surround.SurroundRule()),
]

normal_CCR = Repetition(Alternative(normal_CCR_rules),
                        min = 1, max = 10,
                        name = "normal_mode_sequence")

class NormalModeCCR(CompoundRule):
    spec     = "<normal_mode_sequence>"
    extras   = [ normal_CCR ]
    def _process_recognition(self, node, extras):
        # A sequence of actions.
        normal_mode_sequence = extras["normal_mode_sequence"]
        # An integer repeat count.
        for action in normal_mode_sequence:
            action.execute()
        release.execute()

normal_single_rules = [
    RuleRef(rule = easy_motion.EasyMotionRule()),
    RuleRef(rule = navigation.NavigationRule()),
    RuleRef(rule = netrw.NetrwRule()),
    RuleRef(rule = ctrlp.CtrlPRule()),
    RuleRef(rule = buffer.BufferRule()),
    RuleRef(rule = quick_replace.QuickReplaceRule()),
]
normal_single_action = Alternative(normal_single_rules, name = "normal_mode_single_action")

class NormalModeSingleAction(CompoundRule):
    spec = "<normal_mode_single_action>"
    extras = [ normal_single_action ]
    def _process_recognition(self, node, extras):
        action = extras["normal_mode_single_action"]
        action.execute()
        release.execute()

gvim_exec_context = AppContext(executable="gvim")
vim_putty_context = AppContext(title="vim")
gvim_context = (gvim_exec_context | vim_putty_context)

normalModeGrammar = Grammar("gvim", context=gvim_context)
normalModeGrammar.add_rule(NormalModeCCR())
normalModeGrammar.add_rule(NormalModeSingleAction())
normalModeGrammar.load()

# Unload function which will be called at unload time.
def unload():
    global normalModeGrammar
    if normalModeGrammar: normalModeGrammar.unload()
    normalModeGrammar = None
