from dragonfly import Choice

def uncountableMotionChoice(name="uncountableMotion"):
    return Choice(name, {
        "start": "0",
        "front": "caret",
        "(end | rest)": "dollar",
        "match": "percent",
        "top": "g,g",
        "bottom": "G",
    })
