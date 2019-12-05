from dragonfly import Choice

def objectChoice(name="object"):
    return Choice(name, {
        'word': 'w',
        'big word': 'W',
        'sentence': 's',
        '(paragraph | pare)': 'p',
        'block': 'b',
        '(paren | laip)': 'rparen',
        '(brackets | rack)': 'rbracket',
        '(brace | race)': 'rbrace',
        'quote': 'dquote',
        '(post | troth)': 'apostrophe',
    })
