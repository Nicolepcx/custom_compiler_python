import Scanner
class Program:

    def compile(inStream : File, outStream  File):
        scanner = Scanner()
        tokenList = []
        with open(inStream, 'r') as stream:
            tokenList = scanner.Scan(stream)
        for t in tokenList : print(t)
        
