from token import *
from scanner import *



#TODO Error Correction. This program assumes perfect input, which is unlikely.
#TODO  operators

#takes tokens and constructs a tree, with the origin node as return value
def parse(tokens):
    origin = Token()
    buffer = []
    while len(tokens) > 0:
        tok = tokens.pop(0)
        if tok.get_ttype() == TOKEN.DEF and len(buffer) > 0 :
            function_branch(origin, buffer)
            buffer.clear()
        #print(tok.get_ttype())
        #print(len(tokens))
        #print(len(origin.children))
        buffer.append(tok)
    return origin


#branch-patternb TOKEN.DEF TOKEN.VARIABLE TOKEN.(  variable_pattern TOKEN.) TOKEN : statements
def function_branch(parent, tokens): #IF function is almost identical
    ftok = tokens[0]
    parent.children.append(ftok)
    
    #ftok.children.append(tokens[1]) #function_name
    #bracket_content = get_bracket_contents(tokens[1:])
    #variable_declaration(ftok, bracket_content)
    #expression_branch(ftok, get_contents_until(tokens[len(bracket_content):], ":")) #EXPRESSION

def variable_declaration(parent,tokens):
    index = 0
    while (len(tokens) > index):
        if (tokens[index].get_ttype() == TOKEN.VARIABLE):
            parent.append(tokens[index])
            

#branch pattern VALUE OPERATOR statements
def expression_branch(parent, tokens):
#    pass
#    if is_variable(tokens[i]) and len(tokens)>1:
#        if tokens[i+1] == Token.is_operator():
#            parent.children.append(tokens[i])




def get_contents_until(tokens, symbol):
    content = []
    b_index = 0
    while b_index < len(tokens):
        token = tokens[b_index]
        if (token == symbol):
            return content
        content.append(token)
        b_index += 1
    return []


#TODO error handling everywhere
def get_bracket_contents(tokens):
    content = []
    bracket_counter = 1
    b_index = 1
    while bracket_counter > 0:
        token = tokens[b_index]
        if (token.get_ttype() == TOKEN.BRACKET_LEFT):
           context_counter += 1
        elif (token.get_ttype() == TOKEN.BRACKET_RIGHT):
           context_counter -= 1
        if bracket_counter > 0:
            return content
        content.append(token)
        b_index += 1
    return None

def get_subcontext_contents(tokens, index, indent_level):
    content = []
    indent = indent + 1
    while len(tokens) >= index and indent_level > indent:
        token = tokens[index]
        if (token == TOKEN.INDENT):
            indent = token.level
        content.append(token)
        index+=1
    return content

def print_tree(origin):
    print_branch(origin, 0)

def print_branch(node,space_count):
    print_token(node, space_count)
    if not (node.children == []):
        for child in node.children:
            print_branch(child, space_count + 0)


def print_token(tok, space_count):

    var0 = space_count*' '
    var1 = tok.get_ttype()

    # print the result
    if hasattr(tok, 'string'):
        var2 = tok.string
        print(f"{var0}{var1},{var2}")
    elif hasattr(tok, 'level'):
        var2 = tok.level
        print(f"{var0}{var1},lvl:{var2}")
    else:
        print(f"{var0}{var1}")




