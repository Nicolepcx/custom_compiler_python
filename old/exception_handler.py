# define Python user-defined exceptions
class SyntaxError(Exception):
    """Base class for Syntax exceptions"""
    def __init__(self, line, msg):
        super(self,msg).__init__("Syntax ERROR: at line " + line + ": \"" + msg + "\"")





def syntax_error(line, msg):
    raise SyntaxError(line,msg)
  
