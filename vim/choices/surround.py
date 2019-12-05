from dragonfly import Choice

def surroundChoice(name="surround"):
    return Choice(name, {
        "tag": "t",
        'ampersand': 'ampersand',
        '( post | apostrophe )': 'apostrophe',
        '( starling | asterisk )': 'asterisk',
        'backtick': 'backtick',
        '( bar | pipe )': 'bar',
        'dollar': 'dollar',
        'quote': 'dquote',
        'hashtag': 'hash',
        'modulo': 'percent',
        'single quote': 'squote',
        '(tilde | strike)': 'tilde',
        '(underscore | score)': 'underscore',

        'langle': 'langle',
        'lace': 'lbrace',
        'lack': 'lbracket',
        'laip': 'lparen',

        'rangle': 'rangle',
        '(race | brace | curly)': 'rbrace',
        '(rack | bracket)': 'rbracket',
        '(raip | paren)': 'rparen',
    })
