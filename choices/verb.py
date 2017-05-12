from dragonfly import Choice

def verbChoice(name="verb"):
    return Choice(name, {
        "delete": "d",
        "(copy | yank)": "y",
        "(select | visual)": "v",
        "case lower": "g,u",
        "case upper": "g,U",
        "format": "g,q",
        "comment": "g,c",
        "(indent | reindent)": "equal",
        "(flow | reflow)": "g,q",
        "shift left": "langle",
        "shift right": "rangle",
    })
