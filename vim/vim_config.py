from dragonfly import Config, Section, Item

config            = Config("gvim")

# What words you wish to use to trigger vim's commands
config.cmd        = Section("Language")

# What custom settings does your system have?
config.system     = Section("System")
config.system.windowSwitchPrefix = Item('c-', # default: "c-w,",
                                        doc = "What prefix to use when switching windows? Relevant with vim-tmux-navigator (which can make vim windows and tmux panes inter-navigable.).")

def get_config():
    return config
