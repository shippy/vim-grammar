from dragonfly import Choice

def modifierChoice(name="modifier"):
    return Choice(name, {
        '(in | inside | inner)': 'i',
        '(a | around | outer)': 'a',
    })
