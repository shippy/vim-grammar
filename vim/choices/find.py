from dragonfly import Choice

def findChoice(name="find"):
    return Choice(name, {
        "find": "f",
        "bind": "F",
        "(until | till)": "t",
        "bill": "T",
    })
