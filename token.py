from enum import Enum

class TOKEN(Enum):
    #None enum
    NONE = 0
    LITERAL = 1
    IDENTIFIER = 2
    SPACE = 3
    CONTEXT = 4

    #Terminal Keyword
    #KEYWORDS
    END_OF_FILE = 101
    END_OF_LINE = 102
    CLASS = 104
    DEF = 105
    FOR = 106
    IN = 107
    IF = 108 
    RETURN = 109

    #OPERATORS
    ASSIGNMENT = 201
    SQUARE_BRACKET_LEFT = 202
    SQUARE_BRACKET_RIGHT = 203
    CURLY_BRACKET_LEFT = 204
    CURLY_BRACKET_RIGHT = 205
    BRACKET_LEFT = 206
    BRACKET_RIGHT = 207
    ADDITION = 208
    SUBTRACTION = 209
    COMMA = 210
    EQUALITY = 211


class Token:
    # On a Keyword Token this represents a TOKEN Value, if it's variable, it represents the pure string
    keyword = 0
    children = []

    def get_ttype(self):
        return self.keyword

    def get_keyword(self):
        return keyword

    def __init__(self, keyword=TOKEN.NONE):
        self.keyword = keyword

    @staticmethod
    def get_token_type(match):
        # find out if it is a keyword
        match match:
            case "class": return TOKEN.CLASS
            case "def": return TOKEN.DEF
            case "for": return TOKEN.FOR
            case "in": return TOKEN.IN
            case "if": return TOKEN.IF
            case "\"": return TOKEN.STRING
            case "=": return TOKEN.ASSIGNMENT
            case "[": return TOKEN.SQUARE_BRACKET_LEFT
            case "]": return TOKEN.SQUARE_BRACKET_RIGHT
            case "(": return TOKEN.CURLY_BRACKET_LEFT
            case ")": return TOKEN.CURLY_BRACKET_RIGHT
            case "+": return TOKEN.ADDITION
            case "-": return TOKEN.SUBTRACTION
            case "==": return TOKEN.EQUALITY
            case ",": return TOKEN.COMMA
            case "return": return TOKEN.RETURN
        # TODO return a is not a string exception.
        return TOKEN.NONE


class IndentToken(Token):
    amount = 0

    def __init__(self, level):
        self.keyword = TOKEN.CONTEXT
        self.level = level

# alphanumeric tokens
class ANToken(Token):
    string = ""
    def __init__(self, string, keyword):
        self.string = string
        self.keyword = keyword


# these classes define different Non-Keyword tokens
class StringToken(ANToken):
    def __init__(self, string):
        super().__init__(string,TOKEN.LITERAL)

class NumberToken(ANToken):
    def __init__(self, string):
        super().__init__(string, TOKEN.LITERAL)

class IdentifierToken(ANToken):
    def __init__(self, string):
        super().__init__(string, TOKEN.IDENTIFIER)


