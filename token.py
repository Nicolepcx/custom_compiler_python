from enum import Enum


class TOKEN(Enum):
    NONE = 0
    END_OF_FILE = 1
    END_OF_LINE = 2
    INDENT = 3
    CLASS = 4
    DEF = 5
    FOR = 6
    IN = 7
    IF = 8
    ASSIGNMENT_OPERATOR = 9
    SQUARE_BRACKET_LEFT = 10
    SQUARE_BRACKET_RIGHT = 11
    CURLY_BRACKET_LEFT = 12
    CURLY_BRACKET_RIGHT = 13
    ADDITION_OPERATOR = 14
    SUBTRACTION_OPERATOR = 15
    COMMA_SEPERATOR = 16
    EQUALITY_OPERATOR = 17
    RETURN = 18
    LITERAL = 19
    IDENTIFIER = 20


class Token:
    # On a Keyword Token this represents a TOKEN Value, if it's variable, it represents the pure string
    # TODO does this make sense? shouldn't I add a 2 variable? Does the TOKEN Enum make sense?
    string_val = TOKEN.NONE

    def get_type(self):
        print('string value:', self.string_val)
        return self.string_val

    def get_data(self):
        return ""

    def __init__(self, string_val):
        self.string_val = string_val

    @staticmethod
    def get_token(token_list, index):
        token = token_list[index]
        # find out if it is a keyword
        match token:
            case "class": return Token(TOKEN.CLASS)
            case "def": return Token(TOKEN.DEF)
            case "for": return Token(TOKEN.FOR)
            case "    ": return Token(TOKEN.INDENT)
            case "in": return Token(TOKEN.IN)
            case "if": return Token(TOKEN.IF)
            case "=": return Token(TOKEN.ASSIGNMENT_OPERATOR)
            case "[": return Token(TOKEN.SQUARE_BRACKET_LEFT)
            case "]": return Token(TOKEN.SQUARE_BRACKET_RIGHT)
            case "(": return Token(TOKEN.CURLY_BRACKET_LEFT)
            case ")": return Token(TOKEN.CURLY_BRACKET_RIGHT)
            case "+": return Token(TOKEN.ADDITION_OPERATOR)
            case "-": return Token(TOKEN.SUBTRACTION_OPERATOR)
            case "==": return Token(TOKEN.EQUALITY_OPERATOR)
            case ",": return Token(TOKEN.COMMA_SEPERATOR)
            case "return": return Token(TOKEN.COMMA_SEPERATOR)

        # is it an Identifier
        if (len(token) > index) and (token_list[index + 1] == TOKEN.ASSIGNMENT_OPERATOR):
            return IdentifierToken(token_list[index])
        # is it  a function
        elif (index > 0) and (token_list[index - 1] == TOKEN.DEF):
            return FunctionToken(token_list[index])
        # if (token_list[index] == None):
        #    return Token(TOKEN.NONE)

        # Nothing else matches so it must be a literal
        return LiteralToken(token_list[index])


# generic Non-Keyword-Class
class NKToken(Token):
    def get_data(self, string_val=None):
        return string_val


# these classes define different Non-Keyword tokens
class LiteralToken(NKToken):
    def get_type(self):
        return TOKEN.LITERAL


class FunctionToken(NKToken):
    def get_type(self):
        return TOKEN.LITERAL


class IdentifierToken(NKToken):
    def get_type(self):
        return TOKEN.IDENTIFIER 
