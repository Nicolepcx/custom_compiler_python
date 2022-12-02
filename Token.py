

class Token():
    public Terminal Terminal { get }
    public Location? Location { get }

    def Token(Terminal terminbal, Location? location = null):
        Terminal = terminal
        Location = location

    def override string ToString():
        return "(" + Terminal + ")"

    def override bool Equals(object? obj):
        if (obj is Token otherToken): return Terminal == otherToken.Terminal
        else: return false

    def override int GetHashCode()
        return Terminal.GetHashCode()

class StringLiteral(TokenWithAttribute<string>)
    def StringLiteral(string value, Location? location = null):
        super(Terminal.StringLiteral, value, location)

class Operator(TokenWithAttribute<Operator.OperatorType>):

        enum OperatorType:
        Less, [Symbol("<")]
        Greater, [Symbol(">")]
        LessOrEqual, [Symbol("<=")]
        GreaterOrEqual, [Symbol(">=")]
        Equal, [Symbol("=")]
        NotEqual, [Symbol("/=")]
        Plus, [Symbol("+")]
        Minus, [Symbol("-")]
        Multiplied, [Symbol("*")]
        And, [Symbol("/\\")]
        Or, [Symbol("\\/")]
        CAnd, [Symbol("/\\?")]
        COr, [Symbol("\\/?")]
        Not, [Keyword]
        DivE, [Keyword("divE")]
        DivF, [Keyword("divF")]
        DivT, [Keyword("divT")]
        ModE, [Keyword("modE")]
        ModF, [Keyword("modF")]
        ModT, [Keyword("modT")]
    
    def __init__(OperatorType type, Location? location = null)
        super(Terminal.Operator, type, location)
    }
class IntegerLiteral(TokenWithAttribute<BigInteger>, IExpression)
    public ExpressionSide? Side
    {
        get => ExpressionSide.Right
        set
        {
            if (value != Side)
            {
                throw new TypeCheckException("IntegerLiteral cannot be a left expression", Location)
            }
        }
    }
    
    public ImlComp.Parser.DataType DataType { get set }

    def __init__(BigInteger value, Location? location = null):
        super(Terminal.IntLiteral, value, location)

    def static IntegerLiteral FromToken(TokenWithAttribute<BigInteger> token):
        return new IntegerLiteral(token.Attribute, token.Location)

    def AnnotateType(Namespaces namespaces):
        AnnotateType(Parser.DataType.Any, namespaces)

    def AnnotateType(Parser.DataType targetType, Namespaces namespaces):
        if targeType.DataTypeCode == ImlComp.Scanner.DataType.DataTypeCode.Any:
            if Attribute >= int.MinValue && Attribute <= int.MaxValue: DataType = Parser.DataType.Int32,
            if Attribute >= long.MinValue && Attribute <= long.MaxValue: DataType =  Parser.DataType.Int64,
            if Attribute >= - BigInteger.Pow(2, 1023) && Attribute <= BigInteger.Pow(2, 1023): DataType =  Parser.DataType.Int1024,
        elif targetTyp.Equals(Parser.DataType.Int1024) && value >= - BigInteger.Pow(2, 1023) && Attribute <= BigInteger.Pow(2, 1023): Parser.DataType.Int1024,
        elif targetTyp.Equals(Parser.DataType.Int64) && Attribute >= long.MinValue && Attribute <= long.MaxValue: Parser.DataType.Int64,
        elif targetTyp.Equals(Parser.DataType.Int32) && Attribute >= int.MinValue && Attribute <= int.MaxValue: Parser.DataType.Int32,
        else : throw new CompilerException("Integer literal is too large", Location)
    }

    def int GenerateCode(int startLocation, Compilation compilation, string debugInfo = null)
        return GenerateCode(startLocation, compilation, null, debugInfo)
    
    def int GenerateCode(int startLocation, Compilation compilation, int? index, string debugInfo = null)
        compilation.Instructions.Add((startLocation, new LoadIm(DataType, Attribute, $"{debugInfo} Integer literal")))
        return startLocation + 1

# This class is called "ImlType" to avoid conflicts with System.Type.
# The conflicts could also be circumvented in other ways, but this is simpler to read
class DataType(TokenWithAttribute<DataType.DataTypeCode>)
    public enum DataTypeCode:
        [Keyword]
        Bool,
        
        [Keyword]
        Int32,
        
        [Keyword]
        Int64,
        
        [Keyword]
        Int1024,
        
        Any,
        CodeAddress,

    __init__ (DataTypeCode code, Location? location = null):
        super(Terminal.Type, code, location)

class TokenWithAttribute<T>(Token):
    public T Attribute { get }
    
    def __init__(Terminal terminal, T attribute, Location? location = null):
        super(terminal, location)
        Attribute = attribute

    def ToString():#TODO override python to string
        return "({}, {})".format(Terminal, Attribute)

    def override bool Equals(object? obj):
        if (obj is TokenWithAttribute<T> otherToken)
            return Terminal == otherToken.Terminal && (Attribute?.Equals(otherToken.Attribute) ?? false)
        else:  return false

    def protected bool Equals(TokenWithAttribute<T> other)
        return base.Equals(other) && EqualityComparer<T>.Default.Equals(Attribute, other.Attribute)

    def override int GetHashCode()
        return (base.GetHashCode() * 397) ^ EqualityComparer<T>.Default.GetHashCode(Attribute)
class BooleanLiteral(TokenWithAttribute<bool>, IExpression):
    public ExpressionSide? Side
    {
        get => ExpressionSide.Right
        set
        {
            if (value != Side)
            {
                throw new TypeCheckException("IntegerLiteral cannot be a left expression", Location)
            }
        }
    }
    
    public ImlComp.Parser.DataType DataType { get set }

    def BooleanLiteral(bool attribute, Location location = null):
        super(Terminal.BoolLiteral, attribute, location)
    
    def static BooleanLiteral FromToken(TokenWithAttribute<bool> token)
        return new BooleanLiteral(token.Attribute, token.Location)

    def AnnotateType(Namespaces namespaces)
        AnnotateType(Parser.DataType.Any, namespaces)

    def AnnotateType(Parser.DataType targetType, Namespaces namespaces)
        if (targetType.Equals(Parser.DataType.Bool)): DataType = new ImlComp.Parser.DataType(ImlComp.Scanner.DataType.DataTypeCode.Bool)
        else: throw new TypeCheckException($"BooleanLiteral is not assignable to type {targetType}", Location)

    def int GenerateCode(int startLocation, Compilation compilation, string debugInfo = null)
        return GenerateCode(startLocation, compilation, null, debugInfo)
    
    def int GenerateCode(int startLocation, Compilation compilation, int? index, string? debugInfo = null)
        throw new NotImplementedException()


class Identifier(TokenWithAttribute<string>, IExpression):
    ExpressionSide? Side { get set }
    Parser.DataType DataType { get set }

    def __init__(string name, Location? location = null):
        super(Terminal.Identifier, name, location)

    def AnnotateType(Namespaces namespaces)
        AnnotateType(Parser.DataType.Any, namespaces)

    def AnnotateType(Parser.DataType targetType, Namespaces namespaces)
        if !namespaces.Storages.ContainsKey(Attribute): throw new ScopeCheckException($"Use of undefined variable {Attribute}", Location)
        
        IDeclaration declaration = namespaces.Storages[Attribute]
        if declaration is StorageDeclaration storageDeclaration:
            ScopeChecker.AssertOfType(Location, targetType, storageDeclaration.TypedIdentifier.Type)
            DataType = storageDeclaration.TypedIdentifier.Type
        else if declaration is Parameter parameter:
            ScopeChecker.AssertOfType(Location, targetType, parameter.TypedIdentifier.Type)
            DataType = parameter.TypedIdentifier.Type
        else:
            throw new CompilerException("Error in TypeCheck", Location)

    def int GenerateCode(int startLocation, Compilation compilation, string debugInfo = null)
        return GenerateCode(startLocation, compilation, null, debugInfo)

    def int GenerateCode(int startLocation, Compilation compilation, int? index, string debugInfo = null):
        int nextLocation = GenerateCodeWithoutDeref(startLocation, compilation, index, debugInfo)
        
        # Dereference if right expression
        if (Side == null) throw new TypeCheckException($"Failed to check if {this} is left or right expression before Code Generation", Location)
        if (Side == ExpressionSide.Right)
            compilation.Instructions.Add((nextLocation++, new Deref($"{debugInfo} {this} on right side")))

        return nextLocation
    
    def int GenerateCodeWithoutDeref(int startLocation, Compilation compilation, int? index, string debugInfo = null):
        int nextLoc = startLocation
        # Parameters 
        if (compilation.LocalStorageAddresses?.ContainsKey(Attribute) ?? false):
            ParameterInfo info = compilation.LocalStorageAddresses[Attribute]
            if (info.StartIndex < 0):
                compilation.Instructions.Add((nextLoc++, new LoadAddrRel(info.StartIndex, $"{debugInfo} LocalIdentifier {index}")))
                
                compilation.Instructions.Add((nextLoc++, new Convert(Parser.DataType.CodeAddress, Parser.DataType.Int64)))
                compilation.Instructions.Add((nextLoc++, new Dup()))
                compilation.Instructions.Add((nextLoc++, new Convert(Parser.DataType.Int64, Parser.DataType.CodeAddress)))
                compilation.Instructions.Add((nextLoc++, new Deref()))
                compilation.Instructions.Add((nextLoc++, new LoadIm(Parser.DataType.Int64, info.Step * (index + 1) ?? 0)))
                compilation.Instructions.Add((nextLoc++, new Add(Parser.DataType.Int64)))
                compilation.Instructions.Add((nextLoc++, new Add(Parser.DataType.Int64)))
                compilation.Instructions.Add((nextLoc++, new Convert(Parser.DataType.Int64, Parser.DataType.CodeAddress)))
            else:
                compilation.Instructions.Add((nextLoc++, new LoadAddrRel(info.StartIndex + (info.Step * (index + 1) ?? 0),
                    $"{debugInfo} LocalIdentifier {index}")))
        else:
            compilation.Instructions.Add((nextLoc++, 
                new LoadIm(Parser.DataType.CodeAddress,
                    compilation.GlobalStorageAddresses[Attribute] + (index + 1 ?? 0), $"{debugInfo} Identifier")))

        return nextLoc

    def int GetArrayStep(Compilation compilation)
         return compilation.LocalStorageAddresses?[Attribute]?.Step ?? 1
