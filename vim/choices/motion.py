from dragonfly import Choice

def motionChoice(name="motion"):
    return Choice(name, {
        "up": "k",
        "down": "j",
        "left": "h",
        "right": "l",
        "word": "w",
        "big word": "W",
        "board": "b",
        "word end": "e",
        "big end [word]": "E",
        "sent up": "lparen",
        "sent down": "rparen",
        "pare up": "lbrace",
        "pare down": "rbrace",
        "next": "n",
        "pecks": "N",
    })
