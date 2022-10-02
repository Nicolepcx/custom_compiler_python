from token import *


# TODO ERROR find bug string_val' is not defined
# TODO BUG find out why there are so many indents
# TODO Subdivide functions to be smaller
# TODO Make Code prettier.

# takes an array of text and
def tokenize_text_array(text):
    tokens = []
    words = []
    for line in text:
        indents = round(len(line) - len(line.lstrip(' ')) / 4)
        # read indents
        for i in range(0, indents):
            words.append("    ")
        for word in line.split():
            words.append(word)
        words.append("EOF")

    # Tokenization below
    i = 0
    while i < len(words):
        tokens.append(Token.get_token(words, i))
        i += 1
    return tokens


# file_content is processed by tokenize_text_array
def tokenize_file(file_path):
    with open(file_path, 'r') as file:
        tokenize_text_array(file)


# helps with debugging
def print_tokens(tokens):
    for tok in tokens:
        # Assign variable var1 & var 2
        var1 = tok.get_type()
        var2 = tok.get_data()

        # print the result
        print(f"{var1},{var2}")


def main():
    # test tokenize_text_array
    text = [
        "    def fibonacci ( n ) :",
        "        if n == 0 :",
        "            return 0",
        "",
        "        elif n == 1 or n == 2 :",
        "            return 1",
        ""
        "        else:",
        "            return fibonacci ( n - 1 ) + fibonacci ( n - 2 )",
        "",
        "    def faculty ( x ) :",
        "        if ( x > 0 ) :",
        "            return x * faculty ( x - 1 )",
        "        return 1",
        "",
        "    print ( fibonacci ( 10 ) )",
        "    print ( faculty ( 10 ) )"]
    test = ["testing",
            "",
            ""]

    tokens = tokenize_text_array(test)
    print_tokens(tokens)


if __name__ == "__main__":
    main()
