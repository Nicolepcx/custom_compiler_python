from scanner import * 
from token import * 

def main():
    tokens = tokenize_file("fibonnaci.iml")
    print_tokens(tokens)
    #origin = parse(tokens)
    #print_tree(origin)


if __name__ == "__main__":
    main()
