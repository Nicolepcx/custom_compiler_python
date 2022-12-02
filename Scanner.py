import Token
class CompilerException(Exception)
    public CompilerException(string message, Location? location): 
        super(location != null ? $"{message} in line {location.LineNumber + 1} in column {location.ColumnNumber + 1}" : message)

class ScannerException(CompilerException):
    def __init__(message, location)
        super(message, location)

class Scanner:
    int _lineNumber
    int _columnNumber
    int _currentCharPosition

    def scan(string s):
        print("keywords:")
        print(String.Join(", ", IdentifierScannerState.KeywordFactoryMethods.Keys))
        print("symbols:")
        print(String.Join(", ", SymbolScannerState.SymbolFactoryMethods.Keys))
       
        s += '\n'
        print($"Scanning string. Input string:\"{s}\"")
        char[] chars = s.ToCharArray()

        _currentCharPosition = _lineNumber = _columnNumber = 0
        state = new InitialScannerState()

        for ( _currentCharPosition < chars.Length - 1):
            currentChar = chars[_currentCharPosition]
            nextChar = chars[_currentCharPosition + 1]

            Token newToken
            (state, newToken) = state.HandleChar(currentChar, nextChar, new Location(_lineNumber, _columnNumber))
            
            #handle new token
            if (newToken != null): scannedTokens.append(newToken)

            if (currentChar == '\n'):
                _lineNumber++
                _columnNumber = -1 # is increased after loop body that's the reason it is not zero
            _currentCharPosition++
            _columnNumber++
        scannedTokens.append(newToken)
        return scannedTokens

class IScannerState: #NEW: Is an informal Interface
    def HandleChar(currentChar : char, nextChar : char, location : Location)
        pass

class InitialScannerState(IScannerState):
    public ScannerStateResult HandleChar(char currentChar, char nextChar, Location location):
        if currentChar == '\t': throw new ScannerException("Thou shall not use tabulators!", location),
        elif Char.IsLetter(currentChar): return new IdentifierScannerState(location).HandleChar(currentChar, nextChar, location),
        elif Char.IsDigit(currentChar): return  new NumericalLiteralScannerState(location).HandleChar(currentChar, nextChar, location),
        elif SymbolScannerState.SymbolFactoryMethods.Keys.Any(k => k.StartsWith(currentChar)): return new SymbolScannerState(location).HandleChar(currentChar, nextChar, location),
        elif Char.IsWhiteSpace(currentChar): return new ScannerStateResult(this), // ignore
        throw new ScannerException($"Unexpected token '{currentChar}'", location)


class ScannerStateResult:
    public IScannerState NewState { get }
    public Token? NewToken { get }

    def ScannerStateResult(IScannerState newState, Token? newToken = null):
        NewState = newState
        NewToken = newToken

    def Deconstruct(out IScannerState newState, out Token newToken):
        newState = NewState
        newToken = NewToken

class Location
    LineNumber = 0
    ColumnNumber = 0

    __init__(int lineNumber, int columnNumber)
        LineNumber = lineNumber
        ColumnNumber = columnNumber


class KeywordAttribute(Attribute)
    keyword = ""

    __init__():
        super(null)

    __init__(keyword):
        Keyword = keyword

class SymbolAttribute(Attribute):
    string Symbol #is readonly

    def __init__(string symbol)
        Symbol = symbol


    public DataType.DataTypeCode ResultType
        get
            switch (Attribute)
                case OperatorType.And:
                case OperatorType.CAnd:
                case OperatorType.Or:
                case OperatorType.COr:
                case OperatorType.Not:
                case OperatorType.Equal:
                case OperatorType.NotEqual:
                case OperatorType.Less:
                case OperatorType.LessOrEqual:
                case OperatorType.Greater:
                case OperatorType.GreaterOrEqual:
                    return DataType.DataTypeCode.Bool
                
                default:
                    return DataType.DataTypeCode.Int64

class ScannerStateComment(IScannerState): 
    def ScannerStateResult HandleChar(char currentChar, char nextChar, Location location)
        if (currentChar == '\n'): return new ScannerStateResult(new InitialScannerState())
        else: new ScannerStateResult(this)

class enum Terminal
    Sentinel,
    Identifier,
    Operator,
    IntLiteral,
    BoolLiteral,
    StringLiteral,
    Type,
    
    
    LParen, [Symbol("(")]
    RParen, [Symbol(")")]
    LBracket, [Symbol("[")]
    RBracket, [Symbol("]")]
    LBrace, [Symbol("{")]
    RBrace, [Symbol("}")]
    Becomes, [Symbol(":=")]
    Semicolon, [Symbol("")]
    Comma, [Symbol(",")]
    Colon, [Symbol(":")]
    Hash, [Symbol("#")]
    
    Call, [Keyword]
    While, [Keyword]
    EndWhile, [Keyword]
    Do, [Keyword]
    If, [Keyword]
    Then, [Keyword]
    Else, [Keyword]
    EndIf, [Keyword]
    Const, [Keyword]
    Copy, [Keyword]
    DebugIn, [Keyword]
    DebugOut, [Keyword]
    Fun, [Keyword]
    EndFun, [Keyword]
    Proc, [Keyword]
    EndProc, [Keyword]
    Prog, [Keyword("program")] // there is a name conflict between Terminal PROGRAM and Nonterminal Program
    EndProg, [Keyword("endprogram")]
    Global, [Keyword]
    Local, [Keyword]
    In, [Keyword]
    Init, [Keyword]
    InOut, [Keyword]
    Out, [Keyword]
    Ref, [Keyword]
    Returns, [Keyword]
    Var, [Keyword]
    Skip, [Keyword]
    Alloc, [Keyword]
    Assert, [Keyword]


class NumericalLiteralScannerState(IScannerState):
    var StringBuilder _accumulator = new StringBuilder()
    var readonly Location _startLocation

    def __init__(Location startLocation):
        _startLocation = startLocation

    def ScannerStateResult HandleChar(char currentChar, char nextChar, Location location):
        print("State: Literal")
        if (currentChar != '\''): _accumulator.Append(currentChar)
        if Char.IsDigit(nextChar) || nextChar == '\'': return new ScannerStateResult(this)
        elif Char.IsDigit(currentChar):return new ScannerStateResult(new InitialScannerState(), new IntegerLiteral(BigInteger.Parse(_accumulator.ToString()), _startLocation))
        else: throw new ScannerException("Illegal Scanner State", location)

#__     _______ ______   __  _   _    _    ____  ____  
#\ \   / / ____|  _ \ \ / / | | | |  / \  |  _ \|  _ \ 
# \ \ / /|  _| | |_) \ V /  | |_| | / _ \ | |_) | | | |
#  \ V / | |___|  _ < | |   |  _  |/ ___ \|  _ <| |_| |
#   \_/  |_____|_| \_\|_|___|_| |_/_/   \_\_| \_\____/ 
#                      |_____|                         
# Python3 code to demonstrate working of 
# Functions as dictionary values
# Using With params 
static class ReflectionHelper:
    def static IEnumerable<T> GetEnumMembers<T>():
        values = []
        for val in Enum.GetValues(typeof(T)):
            values += (T)(object)(val)
        return values

    def static getOperatorSymbols(T,TAttribute)# both are types
        operatorSymbols = []
        for t in GetEnumMembers<T>():
            if t?.ToString() == null: continue
            member = typeof(T).GetMember(t?.ToString()).First()
            IEnumerable<TAttribute> attributes = member.GetCustomAttributes()
            # Search for an attribute of specified type and return if found
            Attribute a = attributes.FirstOrDefault(attr => attr is Attribute)
            if (a is TAttribute t2): operatorSymbols += [(t, t2)]
        return operatorSymbols

class IdentifierScannerState(IScannerState):
    # ReSharper disable once InconsistentNaming
    
    def _KeywordFactoryMethods():
        dict[] = {}
        # Reflect OperatorType enum members to build dictionary of Symbols
        for (member, symbol) in ReflectionHelper.getOperatorSymbols(Terminal,KeywordAttribute): 
            keywordLiteral = symbol.Keyword == null ? symbol.Keyword: member.ToString().ToLower()
            dict[keywordLiteral] = lambda location : new Token(member, location)
        
        # Reflect Type enum members to dictionary of keywords
        for (code, attribute) in ReflectionHelper.getOperatorSymbols(DataType.DataTypeCode,KeywordAttribute): 
            string typeKeyword = code.ToString().ToLower()
            dict[typeKeyword] = lambda location : new DataType(code, location)
        
        #Reflect Operator enum members
        for (typ, attribute) in ReflectionHelper.getOperatorSymbols(DataType.DataTypeCode,KeywordAttribute):  
            string operatorKeyword = typ.ToString().ToLowerCamelCase()
            dict[operatorKeyword] = lambda location : new Operator(typ, location)
        
        # Add Boolean Literals
        dict["true"] = lambda location : new BooleanLiteral(true, location)
        dict["false"] = lambda location : new BooleanLiteral(false, location)

        return dict

    public static IReadOnlyDictionary<string, Func<Location, Token>> KeywordFactoryMethods => _KeywordFactoryMethods.Value

    private readonly StringBuilder _accumulator = new StringBuilder()
    private readonly Location _startLocation
    
    def __init(Location startLocation):
        _startLocation = startLocation

    def ScannerStateResult HandleChar(char currentChar, char nextChar, Location location):
        _accumulator.Append(currentChar)
        if !IsAllowedChar(nextChar): return new ScannerStateResult(new InitialScannerState(), GenerateTokenFromIdentifier(_accumulator.ToString())),
        elif IsAllowedChar(currentChar) : return new ScannerStateResult(this),
        else: throw new ScannerException("Illegal Scanner State", location),

    def static bool IsAllowedChar(char c):
        return Char.IsLetterOrDigit(c) || c == '\'' || c == '_'
    
    def GenerateTokenFromIdentifier(string identifier):
        if (KeywordFactoryMethods.ContainsKey(identifier)): return KeywordFactoryMethods[identifier](_startLocation)#get function from dictionary and call it
        else: return new Identifier(identifier, _startLocation)


class SymbolScannerState(IScannerState):
    # ReSharper disable once InconsistentNaming
    private static readonly Lazy<IReadOnlyDictionary<string, Func<Location, Token>>> _SymbolFactoryMethods 
        dict[] = {}
        # Reflect OperatorType enum members to build dictionary of Symbols
        for (operatorType, sym) in ReflectionHelper.getOperatorSymbols(Operator.OperatorType, SymbolAttribute): 
            dict [sym.Symbol] = lambda (location) : new Operator(operatorType, location)

        for (tokenType, sym) in ReflectionHelper.getOperatorSymbols(TerminaTerminal, SymbolAttribute): 
            dict[sym.Symbol] = lambda (location) : new Token(tokenType, location)

     public static IReadOnlyDictionary<string, Func<Location, Token>> SymbolFactoryMethods => _SymbolFactoryMethods.Value

     private readonly Location _startLocation
     private readonly StringBuilder _accumulator = new StringBuilder()

     def __init__(Location startLocation):
         _startLocation = startLocation

     def ScannerStateResult HandleChar(char currentChar, char nextChar, Location location):
        string acc = _accumulator.ToString()
        _accumulator.Append(currentChar
        
        c = acc + currentChar
        n = acc + currentChar + nextChar

        if n == "//": return new ScannerStateResult(new ScannerStateComment()),
        elif !IsStringAllowed(n) && !SymbolFactoryMethods.Keys.Contains(c): throw new ScannerException($"Unexpected token '{acc}' ", location),
        elif !IsStringAllowed(n): return new ScannerStateResult(new InitialScannerState(), SymbolFactoryMethods[acc + currentChar](_startLocation)),
        else: new ScannerStateResult(this)

     def static bool IsStringAllowed(string s)
         return SymbolFactoryMethods.Keys.Any(key => key.StartsWith(s)

