from token import *


# TODO Make Code prettier.
# TODO Error handler

# takes an array of text and
def tokenize_line(line):
    tokens = []
    i = 0
    mat = ""
    line += " "
    while i < len(line) - 1:
        mat += line[i]
        tok = match(line[i+1],mat)
        if tok is not None:
            tokens.append(tok)
            mat = ""
        i+=1
    return tokens
    
def tokenize_text_array(text):
    tokens = []
    # Tokenization below
    for line in text:
        add_tok = tokenize_line(line)
        tokens += add_tok
    combine_indents(tokens)
    return tokens

def combine_indents(tokens):
    lvl = 0
    length = len(tokens)
    for x in range(len(tokens) - 1, -1, -1):
        is_context_token = tokens[x].get_ttype() == TOKEN.CONTEXT
        if is_context_token:
            next_is_context_token = tokens[x-1].get_ttype() == TOKEN.CONTEXT
            if next_is_context_token:
                lvl += tokens[x].level
                del tokens[x]
            else:
                if lvl < 1:
                    del tokens[x]
                else:
                    tokens[x].level += lvl
                    lvl = 0

def match(next_char,mat):
    curr_char = mat[len(mat)-1] 

    if curr_char.isalnum() and (len(mat) < 1 or next_char.isalnum()):
        return None
    tok_type = Token.get_token_type(mat)

    if  curr_char == "\n": 
        return None
    
    #is it a Keyword
    if  tok_type != TOKEN.NONE:
        return Token(tok_type)

    #is it a string
    if  curr_char == "\"" and mat[0] == "\"":
        return StringToken(mat[1:])
    
    if curr_char == " ":
        return IndentToken(1)

    if curr_char == "\t":
        return IndentToken(4)

    #is it a number
    #TODO answer question: do we only support integer
    if mat.isnumeric():
        return NumberToken(int(mat))

    return IdentifierToken(mat)
    #throw error

# file_content is processed by tokenize_text_array
def tokenize_file(file_path):
    with open(file_path, 'r') as file:
        return tokenize_text_array(file)


# helps with debugging
def print_tokens(tokens):
    if tokens is not None:
        for tok in tokens:
            # Assign variable var1 & var 2
            var1 = tok.get_ttype()

            # print the result
            if hasattr(tok, 'string'):
                var2 = tok.string
                print(f"{var1},{var2}")
            elif hasattr(tok, 'level'):
                var2 = tok.level
                print(f"{var1},lvl:{var2}")
            else:
                print(var1)

