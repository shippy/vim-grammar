#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
# Modified by David Gessner
# Contains some code obtained from
# https://github.com/danielgm/JarvisGrammars/blob/master/vim.py
#
# Modified by Simon Podhajsky

"""
Command-module for the vim editor
============================================================================

This module allows the user to control the vim text editor.


Discussion of this module
----------------------------------------------------------------------------

This command-module creates a powerful voice command for
editing and cursor movement.  This command's structure can
be represented by the following simplified language model:

 - *CommandRule* -- top-level rule which the user can say
    - *repetition* -- sequence of actions (name = "sequence")
       - *NormalModeKeystrokeRule* -- rule that maps a single
         spoken-form to an action
    - *optional* -- optional specification of repeat count
       - *integer* -- repeat count (name = "n")
       - *literal* -- "times"

The top-level command rule has a callback method which is
called when this voice command is recognized.  The logic
within this callback is very simple:

1. Retrieve the sequence of actions from the element with
   the name "sequence".
2. Retrieve the repeat count from the element with the name
   "n".
3. Execute the actions the specified number of times.

"""

try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
    pass

from dragonfly import *
print 'gVim grammar accessed.'

# try:
#     import sys
#     sys.path.append(r'C:\NatLink\NatLink\MacroSystem\caster')
#     from caster.lib import alphanumeric
#     letter = alphanumeric.get_alphabet_choice("letter")
#     print "Caster imported."
# except ImportError:
#     print "Caster not imported."
#     pass

#---------------------------------------------------------------------------
# Here we globally defined the release action which releases all
#  modifier-keys used within this grammar.  It is defined here
#  because this functionality is used in many different places.
#  Note that it is harmless to release ("...:up") a key multiple
#  times or when that key is not held down at all.

release = Key("shift:up, ctrl:up")

letter = Choice("letter", {
    'arch': 'a',
    'brov': 'b',
    'char': 'c',
    'delta': 'd',
    'echo': 'e',
    'foxy': 'f',
    'goof': 'g',
    'hotel': 'h',
    'india': 'i',
    'julia': 'j',
    'kilo': 'k',
    'lima': 'l',
    'mike': 'm',
    'novakeen': 'n',
    'oscar': 'o',
    'prime': 'p',
    'quebec': 'q',
    'romeo': 'r',
    'sierra': 's',
    'tango': 't',
    'uniform': 'u',
    'victor': 'v',
    'whiskey': 'w',
    'x-ray': 'x',
    'yankee': 'y',
    'zulu': 'z',

    'upper arch': 'A',
    'upper brov': 'B',
    'upper char': 'C',
    'upper delta': 'D',
    'upper echo': 'E',
    'upper foxy': 'F',
    'upper goof': 'G',
    'upper hotel': 'H',
    'upper india': 'I',
    'upper julia': 'J',
    'upper kilo': 'K',
    'upper lima': 'L',
    'upper mike': 'M',
    'upper novakeen': 'N',
    'upper oscar': 'O',
    'upper prime': 'P',
    'upper quebec': 'Q',
    'upper romeo': 'R',
    'upper sierra': 'S',
    'upper tango': 'T',
    'upper uniform': 'U',
    'upper victor': 'V',
    'upper whiskey': 'W',
    'upper x-ray': 'X',
    'upper yankee': 'Y',
    'upper zulu': 'Z',

    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',

    'ace': 'space',
    'tabby': 'tab',

    'ampersand': 'ampersand',
    '(apostrophe | post)': 'apostrophe',
    'single quote': 'squote',
    '(asterisk | starling)': 'asterisk',
    'at': 'at',
    'backslash': 'backslash',
    'backtick': 'backtick',
    'pipe': 'bar',
    'caret': 'caret',
    'deckle': 'colon',
    'boom': 'comma',
    'dollar': 'dollar',
    '(dot|period)': 'dot',
    'quote': 'dquote',
    'equal': 'equal',
    'clamor': 'exclamation',
    'hashtag': 'hash',
    'hyphen': 'hyphen',
    'minus': 'minus',
    'modulo': 'percent',
    'plus': 'plus',
    'questo': 'question',
    'semper': 'semicolon',
    'slash': 'slash',
    'tilde': 'tilde',
    '(underscore | score)': 'underscore',

    'langle': 'langle',
    'lace': 'lbrace',
    'lack': 'lbracket',
    'laip': 'lparen',
    'rangle': 'rangle',
    'race': 'rbrace',
    'rack': 'rbracket',
    'raip': 'rparen',
})
# letter = RuleRef(rule=LetterRule(), name='letter')
# letter_sequence = Repetition(letter, min=1, max=32, name='letter_sequence')

# def executeLetter(letter):
#     letter.execute()

# def executeLetterSequence(letter_sequence):
#     for letter in letter_sequence:
#         letter.execute()


def verbChoice():
    """docstring for vimVerbChoice"""
    return Choice("verb",
           {
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

def modifierChoice():
    return Choice("modifier", {
        '(in | inside | inner)': 'i',
        '(a | around | outer)': 'a',
    })

def objectChoice():
    return Choice("object",{
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

def motionChoice():
    """docstring for motionChoice"""
    return Choice("motion", {
        "up": "k",
        "down": "j",
        "left": "h",
        "right": "l",
        "word": "w",
        "big word": "W",
        "bored": "b",
        "end word": "e",
        "big end [word]": "E",
        "sent up": "lparen",
        "sent down": "rparen",
        "pare up": "rparen",
        "pare down": "lparen",
        "next": "n",
        "pecks": "N",
    }),

def uncountableMotionChoice():
    return Choice("uncountableMotion", {
        "start": "0",
        "front": "caret",
        "(end | rest)": "dollar",
        "match": "percent",
        "top": "g,g",
        "bottom": "G",
    })

def findChoice():
    return Choice("find", {
        "find": "f",
        "bind": "F",
        "(until | till)": "t",
        "bill": "T",
    })

def searchChoice():
    return Choice("search", {
        "search": "slash",
        "birch": "question",
    })

def surroundChoice(name):
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
#---------------------------------------------------------------------------
# Set up this module's configuration.

# This defines a configuration object with the name "gvim".
config            = Config("gvim")
config.cmd        = Section("Language section")


# This searches for a file with the same name as this file (gvim.py), but with
# the extension ".py" replaced by ".txt". In other words, it loads the
# configuration specified in the file gvim.txt
namespace = config.load()

#---------------------------------------------------------------------------
# Here we prepare the list of formatting functions from the config file.

# Retrieve text-formatting functions from this module's config file.
#  Each of these functions must have a name that starts with "format_".
format_functions = {}
if namespace:
    for name, function in namespace.items():
     if name.startswith("format_") and callable(function):
        spoken_form = function.__doc__.strip()

        # We wrap generation of the Function action in a function so
        #  that its *function* variable will be local.  Otherwise it
        #  would change during the next iteration of the namespace loop.
        def wrap_function(function):
            def _function(dictation):
                formatted_text = function(dictation)
                Text(formatted_text).execute()
            return Function(_function)

        action = wrap_function(function)
        format_functions[spoken_form] = action


# Here we define the text formatting rule.
# The contents of this rule were built up from the "format_*"
#  functions in this module's config file.
if format_functions:
    class FormatRule(MappingRule):
        mapping  = format_functions
        extras   = [Dictation("dictation")]

else:
    FormatRule = None


#---------------------------------------------------------------------------
# Here we define the keystroke rule.

# This rule maps spoken-forms to actions.  Some of these
#  include special elements like the number with name "n"
#  or the dictation with name "text".  This rule is not
#  exported, but is referenced by other elements later on.
#  It is derived from MappingRule, so that its "value" when
#  processing a recognition will be the right side of the
#  mapping: an action.
# Note that this rule does not execute these actions, it
#  simply returns them when it's value() method is called.
#  For example "up 4" will give the value Key("up:4").
# More information about Key() actions can be found here:
#  http://dragonfly.googlecode.com/svn/trunk/dragonfly/documentation/actionkey.html

class NormalModeKeystrokeRule(MappingRule):
    exported = False
    mapping = {
        # Motions
        # "[<n>] <motion>": Key("%(n)s, %(motion)s"),
        "[<n>] up": Key("k:%(n)d"),
        "[<n>] down": Key("j:%(n)d"),
        "[<n>] left": Key("h:%(n)d"),
        "[<n>] right": Key("l:%(n)d"),

        "go start": Key("caret"),
        "go end": Key("dollar"),

        "go line <line>": Key("colon") + Text("%(n)d") + Key("enter"),
        "match": Key("percent"),

        "[<n>] next": Key("n:%(n)d"),
        "[<n>] pecks": Key("N:%(n)d"),
        "[<n>] back": Key("b:%(n)d"),
        "[<n>] whiskey": Key("w:%(n)d"),
        "[<n>] end": Key("e:%(n)d"),

        "Center": Key("z,dot"),
        "format": Key("g,q"),
        "comment": Key("g,c"),

        "[<n>] sent down": Key("rparen"),
        "[<n>] sent up": Key("lparen"),

        "[<n>] pare down": Key("rbrace"),
        "[<n>] pare up": Key("lbrace"),

        # Search (which is also a motion)
        '[<n>] find <letter>': Text('%(n)df%(letter)s') + Key('%(letter)s'),
        '[<n>] bind <letter>': Text('%(n)dF') + Key('%(letter)s'),

        '[<n>] (until | tell) <letter>': Text('%(n)dt') + Key('%(letter)s'),
        '[<n>] (bill | bell) <letter>': Text('%(n)dT') + Key('%(letter)s'),

        # '[<n>] again': Text('%(n)d;'),
        # '[<n>] shift again': Text('%(n)d,'),
        # Count-only verbs
        "[<n>] case (swap | toggle)": Key("tilde"),

        "[<n>] X.": Key("x:%(n)d"),
        "[<n>] Pete macro": Key("at,at:%(n)d"),
        "record [macro] <letter>": Key("q") + Key('%(letter)s'),
        "[<n>] macro <letter>": Key("%(n)s,at") + Key('%(letter)s'),

        "[<n>] join": Key("J:%(n)d"),

        "[<n>] (increment|increase)": Key("c-a:%(n)d"),
        "[<n>] (decrement|decrease)": Key("c-x:%(n)d"),

        "[<n>] undo": Key("u:%(n)d"),
        "[<n>] redo": Key("c-r:%(n)d"),

        "[<n>] paste [down]": Key("p"),
        "[<n>] paste up": Key("P"),

        "[<n>] replace <letter>": Key("r"),
        # "shift replace <letter_sequence>": Key("R"),

        # Pete is shorthand for repeat
        "[<n>] Pete": Key("dot:%(n)d"),

        # Verbs
        "<verb> (now | visual)": Key("%(verb)s"),
        "(visual | select) block": Key("c-v"),

        "<verb> <modifier> <object>": Key("%(verb)s, %(modifier)s, %(object)s"),
        # "<verb> [<n>] <motion>": Key("%(verb)s, %(n)s, %(motion)s"),
        # In absence of the above, poor man's solution is "<verb> now <motion>"

        # Line operations
        "<verb> line": Key("%(verb)s:2"),
        "select line": Key("%(verb)s:2"),
        "duplicate line": Key("y,y,p"),
        "shackle": Key("s-v"), # for consistency with caster

        # Rest-of-line operations
        "<verb> rest": Key("%(verb)s,dollar"),

        # Misc
        "mimic <text>": release + Mimic(extra="text"),
    }
    extras   = [
        verbChoice(),
        modifierChoice(),
        objectChoice(),
        letter,
        IntegerRef("n", 1, 100),
        IntegerRef("line", 1, 500),
        Dictation("text"),
    ]
    defaults = {
        "n": 1,
    }
    # Note: when processing a recognition, the *value* of
    #  this rule will be an action object from the right side
    #  of the mapping given above.  This is default behavior
    #  of the MappingRule class' value() method.  It also
    #  substitutes any "%(...)." within the action spec
    #  with the appropriate spoken values.


#---------------------------------------------------------------------------
# Here we create an element which is the sequence of keystrokes.

# First we create an element that references the keystroke rule.
#  Note: when processing a recognition, the *value* of this element
#  will be the value of the referenced rule: an action.
normal_mode_alternatives = []
normal_mode_alternatives.append(RuleRef(rule=NormalModeKeystrokeRule()))
if FormatRule:
    normal_mode_alternatives.append(RuleRef(rule=FormatRule()))
normal_mode_single_action = Alternative(normal_mode_alternatives)

# Second we create a repetition of keystroke elements.
#  This element will match anywhere between 1 and 16 repetitions
#  of the keystroke elements.  Note that we give this element
#  the name "sequence" so that it can be used as an extra in
#  the rule definition below.
# Note: when processing a recognition, the *value* of this element
#  will be a sequence of the contained elements: a sequence of
#  actions.
normal_mode_sequence = Repetition(normal_mode_single_action,
    min=1, max=10, name="normal_mode_sequence")


#---------------------------------------------------------------------------
# Here we define the top-level rule which the user can say.

# This is the rule that actually handles recognitions.
#  When a recognition occurs, it's _process_recognition()
#  method will be called.  It receives information about the
#  recognition in the "extras" argument: the sequence of
#  actions and the number of times to repeat them.
class NormalModeRepeatRule(CompoundRule):

    # Here we define this rule's spoken-form and special elements.
    spec     = "<normal_mode_sequence> [[[and] repeat [that]] <n> times]"
    extras   = [
            # Sequence of actions defined above.
            normal_mode_sequence,
            # Times to repeat the sequence.
            IntegerRef("n", 1, 100),
        ]
    defaults = {
            # Default repeat count.
            "n": 1,
        }

    # This method gets called when this rule is recognized.
    # Arguments:
    #  - node -- root node of the recognition parse tree.
    #  - extras -- dict of the "extras" special elements:
    #     . extras["sequence"] gives the sequence of actions.
    #     . extras["n"] gives the repeat count.
    def _process_recognition(self, node, extras):
        # A sequence of actions.
        normal_mode_sequence = extras["normal_mode_sequence"]
        # An integer repeat count.
        count = extras["n"]
        for i in range(count):
            for action in normal_mode_sequence:
                action.execute()
        release.execute()

#---------------------------------------------------------------------------

# NOTE: Unused
caster_consistency_rule = MappingRule(
    name = "caster_consistency",
    mapping = {
        "stoosh": Key("y"),
        "cut": Key("d"),
        "spark": Key("p"),
        "fly": Key("W"),
        "shin <direction_small>": Key("v,%(direction_small)s"),
        "queue <direction_big>": Key("v,%(direction_big)s"),
        "fly <direction_big>": Key("%(direction_big)s"),
    },
    extras = [
        Choice("direction_small",
               {"lease": "h",
                "ross": "l",
                "sauce": "j",
                "dunce": "k",
                }),
        Choice("direction_big",
               {"lease": "b",
                "ross": "w",
                "sauce": "lbrace",
                "dunce": "rbrace",
                })
    ]
)

#---------------------------------------------------------------------------

gvim_window_rule = MappingRule(
    name = "gvim_window",
    mapping = {
        # window navigation commands
        "win west": Key("c-w,h"),
        "win east": Key("c-w,l"),
        "win north": Key("c-w,k"),
        "win south": Key("c-w,j"),
        "win switch": Key("c-w,c-w"),

        # window creation commands
        "win split": Key("c-w,s"),
        "win (vault | fault)": Key("c-w,v"),
        },
    extras = [
        ]
)

#---------------------------------------------------------------------------

gvim_tabulator_rule = MappingRule(
    name = "gvim_tabulators",
    mapping = {
        # tabulator navigation commands
        "[<n>] tab right": Key("g,t"),
        "[<n>] tab left": Key("g,T"),
        "tab new": Key("colon") + Text("tabnew") + Key("enter"),
        },
    extras = [
        IntegerRef("n", 1, 10),
        ]
)

#---------------------------------------------------------------------------

gvim_general_rule = MappingRule(
    name = "gvim_general",
    mapping = {
        "cancel": Key("escape,u"),
        "last visual": Key("g,v"),
        },
    extras = [
        ]
)

#---------------------------------------------------------------------------

gvim_navigation_rule = MappingRule(
    name = "gvim_navigation",
    mapping = {
        "go top": Key("g,g"),
        "go bottom": Key("G"),
        "go old": Key("c-o"),
        "go new": Key("c-i"),

        "cursor top": Key("s-h"),
        "cursor middle": Key("s-m"),
        "cursor (low | bottom)": Key("s-l"),

        # line navigation
        "go line <line>": Key("colon") + Text("%(line)s\n"),

        # searching
        "search <text>": Key("slash") + Text("%(text)s\n"),
        "search this": Key("asterisk"),
        "(birch | Burch | perch) <text>": Key("question") + Text("%(text)s\n"), # search before / search previous
        "wide search": Key("colon") + Text('Ack! \"\"') + Key("left"),
        "wide search <text>": Key("colon") + Text('Ack! \"%(text)s\"') + Key("left"),
        },
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
        IntegerRef("line", 1, 100)
        ]
)


#---------------------------------------------------------------------------
# SP: Extracted from ex mode
gvim_config_rule = MappingRule(
    name = "gvim_config",
    mapping = {
        # "them" is how DNS recognizes "vim"
        "them set number": Text("set number "),
        "them set relative number": Text("set relativenumber "),
        "them set ignore case": Text("set ignorecase "),
        "them set no ignore case": Text("set noignorecase "),
        "them set file format UNIX": Text("set fileformat=unix "),
        "them set file format DOS": Text("set fileformat=dos "),
        "them set file type Python": Text("set filetype=python"),
        "them set file type tex": Text("set filetype=tex"),
        },
    extras = [
        Dictation("text"),
        Choice("format",
               {"DOS": "dos",
                "UNIX": "unix"}),
        Choice("language",
               {"Python": "python",
                "tex": "tex"}),
        ]
)

gvim_file_operation_rule = MappingRule(
    name = "gvim_file_operation",
    mapping = {
        # save = w!
        # quit = q!
        # done = x!
        "file save": Key("colon,w,exclamation,enter"),
        "file save all": Key("colon,w,a,exclamation,enter"),
        "file quit": Key("colon,q,exclamation,enter"),
        "file quit all": Key("colon,q,a,exclamation,enter"),
        "file done": Key("colon,x,exclamation,enter"),
        "file done all": Key("colon,x,a,exclamation,enter"),
        "file reload": Key("colon,e,exclamation,enter"),
        "file open": Key("colon,e") + Text(" <text>"),
    },
    extras = [
        Dictation("text")
        # Dictation, Choice, ...
    ]
)

gvim_quick_replace_rule = MappingRule(
    name = "gvim_quick_replace",
    mapping = {
        "strip line <haystack>": Key("colon") + Text("s/%(haystack)s/c") + Key('enter'),
        "strip all <haystack>": Key("colon") + Text("%s/%(haystack)s/c") + Key('enter'),
        "replace line <replace>": Key("colon") + Text("s//%(replace)s/c") + Key('enter'),
        "replace all <replace>": Key("colon") + Text("s//%(replace)s/c") + Key('enter'),
        "sub line <haystack> shark <replace>": Key("colon") + Text("s/%(haystack)s/%(replace)s/c") + Key('enter'),
        "sub all <haystack> shark <replace>": Key("colon") + Text("%s/%(haystack)s/%(replace)s/c") + Key('enter'),
        },
    extras = [
        Dictation("haystack"),
        Dictation("replace"),
        ]
)

gvim_CtrlP_rule = MappingRule(
    name = "gvim_CtrlP",
    mapping = {
        "switch file": Key("colon") + Text("CtrlPMixed") + Key("enter"),
        "switch fault": Key("c-v"),
        "switch tab": Key("c-t"),
        "explore here": Text(":Explore") + Key("enter"),
        "explore fault": Text(":Vexplore") + Key("enter"),
        "explore split": Text(":Sexplore") + Key("enter"),
        "explore tab": Text(":Texplore") + Key("enter"),
        "explore back": Text(":Rexplore") + Key("enter"),
        },
    extras = []
)

gvim_surround_rule = MappingRule(
    name = "gvim_surround",
    mapping = {
        "put (Sir | surrounding) <surround> [to] <modifier> <object>": Key("y,s,%(modifier)s,%(object)s,%(surround)s"),
        "change (Sir | surrounding) [from] <surround> [to] <surround_alt>": Key("c,s") + Key("%(surround)s"),
        "delete (Sir | surrounding) <surround>": Key("d,s") + Key("%(surround)s"),
        "(sir | surround) now <surround>": Key("s-s, %(surround)s"),
    },
    extras = [
        modifierChoice(),
        objectChoice(),
        surroundChoice('surround'),
        surroundChoice('surround_alt'),
    ],
    defaults = {
        'modifier': 'inner',
    }
)

gvim_EasyMotion_rule = MappingRule(
    name = "gvim_EasyMotion",
    mapping = {
        "queasy <letter>": Key("backslash,backslash") + Key('%(letter)s'),
        "queasy <motion>": Key("backslash,backslash") + Key("%(motion)s"),
        "queasy <find> <letter>": Key("backslash,backslash") + Key("%(find)s,%(letter)s") + Key("enter"),
        "queasy <search> <text>": Key("backslash,backslash") + Key("%(search)s,%(text)s") + Key("enter")
    },
    extras = [
        letter,
        Choice("find",
               {"find": "f",
                "bind": "F",
                "tell": "t",
                "bell": "T",
                }),
        Choice("motion",
               {"up": "k",
                "down": "j",
                "word": "w",
                "big word": "W",
                "bored": "b",
                "pare up": "rparen",
                "pare down": "lparen",
                }),
        Choice("search",
               {
                "search": "slash",
                "(birch | Burch | perch)": "question"
               }),
        Dictation("text")
    ]
)
#---------------------------------------------------------------------------

snipmate_rule = MappingRule(
    name = "snipmate",
    mapping = {
        "snip <text>": Text("text") + Key("tab"),
        "snip alias <alias>": Text("alias") + Key("tab"),
    },
    extras = [
        Dictation("text"),
        Choice("alias", {
            # Whatever snippets become useful but hard to say?
        })
    ]
)


class ExModeEnabler(CompoundRule):
    # Spoken command to enable the ExMode grammar.
    spec = "(exec | execute)"

    # Callback when command is spoken.
    def _process_recognition(self, node, extras):
        exModeBootstrap.disable()
        normalModeGrammar.disable()
        ExModeGrammar.enable()
        Key("colon").execute()
        print "ExMode grammar enabled"
        print "Available commands:"
        print '  \n'.join(ExModeCommands.mapping.keys())
        print "\n(EX MODE)"

class ExModeDisabler(CompoundRule):
    # spoken command to exit ex mode
    spec = "<command>"
    extras = [Choice("command", {
        "kay": "okay",
        "(cancel | oops)": "cancel",
    })]

    def _process_recognition(self, node, extras):
        ExModeGrammar.disable()
        exModeBootstrap.enable()
        normalModeGrammar.enable()
        if extras["command"] == "cancel":
            print "ex mode command canceled"
            Key("escape").execute()
        else:
            print "ex mode command accepted"
            Key("enter").execute()
        print "\n(NORMAL)"

# handles ExMode control structures
class ExModeCommands(MappingRule):
    mapping  = {
        "read": Text("r "),
        "(write|save) file": Text("w "),
        "quit": Text("q "),
        "(write|save) and quit": Text("wq "),
        "edit": Text("e "),
        "tab edit": Text("tabe "),
        "tab new": Text("tabnew "),

        "P. W. D.": Text("pwd "),

        "help": Text("help"),
        "sub line": Text("s/"),
        "sub file": Text("%s/"),
        "up": Key("up"),
        "down": Key("down"),
        "[<n>] left": Key("left:%(n)d"),
        "[<n>] right": Key("right:%(n)d"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
    ]
    defaults = {
        "n": 1,
    }


#---------------------------------------------------------------------------
class InsertModeEnabler(MappingRule):
    exported = True
    mapping = {
        "change <modifier> <object>": Key("c, %(modifier)s, %(object)s"),
        "change line": Key("c,c"),
        "change rest": Key("C"),

        "insert": Key("i"),
        "prepend": Key("I"),
        "after": Key("a"),
        "append": Key("A"),
        "oh": Key("o"),
        "bo": Key("O"),
    }
    extras = [
        modifierChoice(),
        objectChoice(),
              ]

    def _process_recognition(self, node, extras):
        InsertModeBootstrap.disable()
        normalModeGrammar.disable()
        InsertModeGrammar.enable()
        super(InsertModeEnabler, self)._process_recognition(node, extras)
        print "\n(INSERT)"

class InsertModeDisabler(CompoundRule):
    # spoken command to exit InsertMode
    spec = "<command>"
    extras = [Choice("command", {
        "kay": "okay",
        "( cancel | oops )": "cancel",
    })]

    def _process_recognition(self, node, extras):
        InsertModeGrammar.disable()
        InsertModeBootstrap.enable()
        normalModeGrammar.enable()
        Key("escape").execute()
        if extras["command"] == "cancel":
            Key("u").execute()
            print "Insert command canceled"
        else:
            print "Insert command accepted"
        print "\n(NORMAL)"

# handles InsertMode control structures
class InsertModeCommands(MappingRule):
    mapping  = {
        "<text>": Text("%(text)s"),
        "[<n>] (scratch|delete)": Key("c-w:%(n)d"),
        "[<n>] slap": Key("enter:%(n)d"),
        "[<n>] tab": Key("tab:%(n)d"),
        "[<n>] clear": Key("backspace:%(n)d"),
        "(scratch|delete) line": Key("c-u"),
        "[<n>] left": Key("left:%(n)d"),
        "[<n>] right": Key("right:%(n)d"),

	"assign": Key("space,equal,space"),
	"plus": Key("space,plus,space"),
	"minus": Key("space,minus,space"),
	"times": Key("space,asterisk,space"),
	"equals": Key("space,equal,equal,space"),
	"not equals": Key("space,exclamation,equal,space"),
	"triple quote": Key("dquote,dquote,dquote"),

	# snippets for snipmate
	"new fixture": Key("f,i,x,tab"),
	"new method": Key("d,e,f,s,tab"),
	"new class": Key("c,l,tab"),
	"new function": Key("d,e,f,tab"),
	"new while loop": Key("w,h,tab"),
	"new for loop": Key("f,o,r,tab"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
    ]
    defaults = {
        "n": 1,
    }

#---------------------------------------------------------------------------

gvim_exec_context = AppContext(executable="gvim")
# set the window title to vim in the putty session for the following context to
# work.
vim_putty_context = AppContext(title="vim")
gvim_context = (gvim_exec_context | vim_putty_context)

# set up the grammar for vim's ex mode
exModeBootstrap = Grammar("ExMode bootstrap", context=gvim_context)
exModeBootstrap.add_rule(ExModeEnabler())
exModeBootstrap.load()
ExModeGrammar = Grammar("ExMode grammar", context=gvim_context)
ExModeGrammar.add_rule(ExModeCommands())
ExModeGrammar.add_rule(ExModeDisabler())
ExModeGrammar.load()
ExModeGrammar.disable()

# set up the grammar for vim's insert mode
InsertModeBootstrap = Grammar("InsertMode bootstrap", context=gvim_context)
InsertModeBootstrap.add_rule(InsertModeEnabler())
InsertModeBootstrap.load()
InsertModeGrammar = Grammar("InsertMode grammar", context=gvim_context)
InsertModeGrammar.add_rule(InsertModeCommands())
InsertModeGrammar.add_rule(InsertModeDisabler())
InsertModeGrammar.load()
InsertModeGrammar.disable()

# set up the grammar for vim's normal mode and start normal mode
normalModeGrammar = Grammar("gvim", context=gvim_context)
normalModeGrammar.add_rule(NormalModeRepeatRule())
normalModeGrammar.add_rule(gvim_window_rule)
normalModeGrammar.add_rule(gvim_tabulator_rule)
normalModeGrammar.add_rule(gvim_general_rule)
normalModeGrammar.add_rule(gvim_navigation_rule)
normalModeGrammar.add_rule(gvim_config_rule)
normalModeGrammar.add_rule(gvim_quick_replace_rule)
normalModeGrammar.add_rule(gvim_CtrlP_rule)
normalModeGrammar.add_rule(gvim_EasyMotion_rule)
normalModeGrammar.add_rule(gvim_file_operation_rule)
normalModeGrammar.add_rule(gvim_surround_rule)
normalModeGrammar.add_rule(snipmate_rule)
# normalModeGrammar.add_rule(caster_consistency_rule)
normalModeGrammar.load()

# Unload function which will be called at unload time.
def unload():
    global normalModeGrammar
    if normalModeGrammar: normalModeGrammar.unload()
    normalModeGrammar = None

    global ExModeGrammar
    if ExModeGrammar: ExModeGrammar.unload()
    ExModeGrammar = None

    global InsertModeGrammar
    if InsertModeGrammar: InsertModeGrammar.unload()
    InsertModeGrammar = None
