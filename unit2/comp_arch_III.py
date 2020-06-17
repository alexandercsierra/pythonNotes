'''
(stretch hint - registers get pushed onto the stack when an interrupt happens)

Stack
-----------
methods - push, pop, seek, is_empty

built into hardware: 
push - put something on the stack
pop - take something off the stack

programmers can add:
peek - look at item on the top of the stack
is_empty - is the stack empty or not

Need these to implement a stack:
*list - a place to store the data that we push (RAM or registers)
*location of top of the stack (aka pointer/address)


Let's:
*Store the stack data in RAM
*R7 for the LS-8 project will hold the SP
    *gets initialized to 0xf4 when the machine boots up

SP is the stack pointer, or the thing at the top of the stack
V
0 1 2 3 4 5 6 7 8 index
0 0 0 0 0 0 0 0 0 value

PUSH 5
V
0 1 2 3 4 5 6 7 8 index
5 0 0 0 0 0 0 0 0 value
PUSH 7
  V
0 1 2 3 4 5 6 7 8 index
5 7 0 0 0 0 0 0 0 value
PUSH 2
    V
0 1 2 3 4 5 6 7 8 index
5 7 2 0 0 0 0 0 0 value
POP 2
  V
0 1 2 3 4 5 6 7 8 index
5 7 2 0 0 0 0 0 0 value

program counter is also a pointer (for program)

LS-8 Stack
-------------
Register contains F4 which is the address in memory that the SP is pointing at. R7: F4 ram[F4] = the value that the SP is pointing at

R7 does not contain the value that the SP is pointing to, but the address in memory

ram[reg[7]] = value


When Pushing:
-decrement the SP
-copy the value in the given register to the address point to by the SP


When Popping:
-copy the value from the address point to by SP to the given register
-increment SP


stack overflow is when the stack 'overflows' and overwrites where the program is stored in memory
'''

#power on state - r7 is set to 0XF4
SP = 7
register[SP] = 0xf4


elif ir == PUSH: # PUSH R2
    #decrement SP
    register[SP] -= 1

    #get value we want to store from the register
    reg_num = memory[pc + 1]
    value = register[reg_num]

    #figure out where to store it
    top_of_stac_addr = register[SP]
    
    #store it
    memory[top_of_stac_addr] = value

    pc +=2