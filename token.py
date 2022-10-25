from enum import Enum

class TOKEN(Enum):
    #None enum
    NONE = 0
    CONTEXT = 1
    IDENTIFIER = 2
    STRING_LITERAL = 3
    BOOL_LITERAL = 4
    INT_LITERAL = 5

    #SYMBOLS
    EXCLAMATION = 101
    DITTO    = 102
    HASH = 103
    DOLLAR = 104
    PERCENT = 105
    AMPERSAND = 107
    BRACKET_LEFT = 108
    BRACKET_RIGHT = 109
    TIMES = 110
    PLUS = 110
    COMMA = 111
    MINUS = 112
    POINT = 113
    SLASH = 114
    COLON = 115
    SEMICOLON = 116
    LESS_THAN = 117
    EQUAL = 118
    GREATER_THAN = 219
    QUESTION_MARK = 120
    AT = 121
    SQUARE_BRACKET_LEFT = 122
    BACKSLASH = 123
    SQUARE_BRACKET_RIGHT = 124
    CIRCUMFLEX = 125
    UNDERLINE = 126
    APOSTROPHE = 156
    CURLY_BRACKET_LEFT = 130
    PIPE = 131
    CURLY_BRACKET_RIGHT = 132
    TILDE = 133
    LINEFEED = 134
    CARRIRET = 135
    COMMENT = 136

    #reserved_definitions
    BOOL = 200
    CALL  = 201
    CONST = 202
    COPY = 203
    DEBUGIN = 204
    DEBUGOUT = 205
    DIVE = 206
    DIVF = 207
    DIVT = 208
    DO = 209
    ELSE = 210
    ENDFUN = 211
    ENDIF = 212
    ENDPROC = 213
    ENDPROGRAM = 214
    ENDWHILE = 215
    FALSE = 216
    FUN = 217
    GLOBAL = 218
    IF = 219
    IN = 220
    INIT = 221
    INOUT = 222
    INT1024 = 223
    INT32 = 224
    INT64 = 225
    LOCAL = 226
    MODE = 227
    MODF = 228
    MODT = 229
    OUT = 230
    PROC = 231
    PROGRAM = 232
    REF = 233
    RETURNS = 234
    SKIP = 235
    THEN = 236
    TRUE = 237
    VAR = 238
    WHILE = 239



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
    def match(string):
        tok_type = Token.get_reserved_definitions(string) 
        if tok_type != TOKEN.NONE:
            return tok_type
        return  Token.get_symbol_type(string)
     


    @staticmethod
    def get_symbol_type(string):
        match string:
            case '!': return TOKEN.EXCLAMATION
            case '\"': return TOKEN.DITTO
            case '#': raise TOKEN.HASH
            case '$': raise TOKEN.DOLLAR
            case '%': raise TOKEN.PERCENT
            case '&': raise TOKEN.AMPERSAND
            case '(': return TOKEN.BRACKET_LEFT
            case ')': return TOKEN.BRACKET_RIGHT
            case '*': return TOKEN.TIMES
            case '+': return TOKEN.PLUS
            case ',': return TOKEN.COMMA
            case '-': return TOKEN.MINUS
            case '.': return TOKEN.POINT
            case '/': return TOKEN.SLASH
            case ':': return TOKEN.COLON
            case ';': return TOKEN.SEMICOLON
            case '<': return TOKEN.LESS_THAN
            case '=': return TOKEN.EQUAL
            case '>': return TOKEN.GREATER_THAN
            case '?': return TOKEN.QUESTION_MARK
            case '@': return TOKEN.AT
            case '[': return TOKEN.SQUARE_BRACKET_LEFT
            case '\\':return TOKEN.BACKSLASH
            case ']': return TOKEN.SQUARE_BRACKET_RIGHT
            case '^': return TOKEN.CIRCUMFLEX
            case '_': return TOKEN.UNDERLINE
            case '\'': return TOKEN.APOSTROPHE
            case '{': return TOKEN.CURLY_BRACKET_LEFT
            case '|': return TOKEN.PIPE
            case '}': return TOKEN.CURLY_BRACKET_RIGHT
            case '~': return TOKEN.TILDE
            case '~': return TOKEN.TILDE
            case '\n': return TOKEN.LINEFEED
            case '\r': return TOKEN.CARRIRET
            case '//': return TOKEN.COMMENT
        return TOKEN.NONE

    @staticmethod
    def get_reserved_definitions(string):
        match string:
            case 'bool': return TOKEN.BOOL
            case 'call': return TOKEN.CALL
            case 'const': return TOKEN.CONST
            case 'copy': return TOKEN.COPY
            case 'debugin': return TOKEN.DEBUGIN
            case 'debugout': return TOKEN.DEBUGOUT
            case 'divE': return TOKEN.DIVE
            case 'divF': return TOKEN.DIVF
            case 'divT': return TOKEN.DIVT
            case 'do': return TOKEN.DO
            case 'else': return TOKEN.ELSE
            case 'endfun': return TOKEN.ENDFUN
            case 'endif': return TOKEN.ENDIF
            case 'endproc': return TOKEN.ENDPROC
            case 'endprogram': return TOKEN.ENDPROGRAM
            case 'endwhile': return TOKEN.ENDWHILE
            case 'false': return TOKEN.FALSE
            case 'fun': return TOKEN.FUN
            case 'global': return TOKEN.GLOBAL
            case 'if': return TOKEN.IF
            case 'in': return TOKEN.IN
            case 'init': return TOKEN.INIT
            case 'inout': return TOKEN.INOUT
            case 'int1024': return TOKEN.INT1024
            case 'int32': return TOKEN.INT32
            case 'int64': return TOKEN.INT64
            case 'local': return TOKEN.LOCAL
            case 'modE': return TOKEN.MODE
            case 'modF': return TOKEN.MODF
            case 'modT': return TOKEN.MODT
            case 'out': return TOKEN.OUT
            case 'proc': return TOKEN.PROC
            case 'program': return TOKEN.PROGRAM
            case 'ref': return TOKEN.REF
            case 'returns': return TOKEN.RETURNS
            case 'skip': return TOKEN.SKIP
            case 'then': return TOKEN.THEN
            case 'true': return TOKEN.TRUE
            case 'var': return TOKEN.VAR
            case 'while': return TOKEN.WHILE
        return TOKEN.NONE


class IndentToken(Token):
    level = 0
    def __init__(self, level):
        self.keyword = TOKEN.CONTEXT
        self.level = level

class LiteralToken(Token):
    value = ""
    def __init__(self, value, keyword):
        super().__init__(keyword)
        self.value = value 

class StringLitToken(LiteralToken):
    def __init__(self, string_value):
        super().__init__(string_value, TOKEN.STRING_LITERAL)

class IntLitToken(LiteralToken):
    def __init__(self, int_value):
        super().__init__(int_value, TOKEN.INT_LITERAL)
