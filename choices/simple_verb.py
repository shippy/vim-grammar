from dragonfly import Choice

def simpleVerbChoice(name="simple_verb"):
    return Choice(name, {
        "case (swap | toggle)": "tilde",
        "X.": "x",

        "Pete macro": "at,at",
        "Pete": "dot",

        "join": "J",

        "paste up": "P",
        "paste down": "p",

        "(increment|increase)": "c-a",
        "(decrement|decrease)": "c-x",

        "undo": "u",
        "redo": "c-r",
    })
