from dragonfly import MappingRule, Key, Text, Dictation

class BufferRule(MappingRule):
    mapping = {
        # save = w!
        # quit = q!
        # done = x!
        "file save": Key("colon, w, exclamation, enter"),
        "file save all": Key("colon, w, a, exclamation, enter"),
        "file quit": Key("colon, q, exclamation, enter"),
        "file quit all": Key("colon, q, a, exclamation, enter"),
        "file done": Key("colon, x, exclamation, enter"),
        "file done all": Key("colon, x, a, exclamation, enter"),
        "file reload": Key("colon, e, exclamation, enter"),
        "file open [<text>]": Key("colon, e") + Text(" <text>"),
    }
    extras = [
        Dictation("text"),
    ]
    defaults = {
        "text": "",
    }
