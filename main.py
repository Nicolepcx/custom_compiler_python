from scanner import * 
from parser import * 
from token import * 

def main():
    tokens = tokenize_file("test.py")
    #print_tokens(tokens)
    origin = parse(tokens)
    print_tree(origin)


if __name__ == "__main__":
    main()
