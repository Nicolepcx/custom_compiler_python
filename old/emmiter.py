
code = [] # stores the program
store = [] # stores the data
pc = 0;# program counter
sp # stack pointer, shows free stack location, stack grows from 0 upwards
ep #extreme pointer, points to first always free stack location
hp # heap pointer, shows free stack location, stack grows from length downwards 
fp # provides reference to each incarnation.

#returns remaining storage locations
def getFreeStoreCount():
    return hp - sp + 1

def emit():
    setup()
    execute(code)
    

def setup():
    pc= 0;
    sp= 0;
    ep= 0;
    hp= store.length - 1;
    fp= 0;
    code = load_program()

def load_program():
    pass

def execute():
    while (pc > -1){
        execute(code[pc]);
    }


def execute_instruction():
    pc = -1
public class SubIntExec extends SubInt implements IExecInstr {
        public void execute()
        {
            sp= sp - 1;
            store[sp-1]= Data.intSub(store[sp-1], store[sp]);
            pc= pc + 1;
    


