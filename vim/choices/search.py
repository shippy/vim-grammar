from dragonfly import Choice

def searchChoice(name="search"):
    return Choice(name, {
        "search": "slash",
        "birch": "question",
    })
