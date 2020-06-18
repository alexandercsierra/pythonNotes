'''
Stack Frames
---------------

Stack grows downward

(addresses)
701: 
700: return point 1 | 
699: return point 2 <--- SP

When you call, the return address gets pushed on the stack
When you return, the return address gets popped off the stack and stored in PC

But actually, variables local to a function are only temporary, and can be held on the stack as well

700: return point 1 |
699: a = 2          |   main()'s stack frame
698: b = ??         |

697: return point 2 |
696: x = 2          |   mult2()'s stack frame
695: y = 7          |
695: z = ??         |

700: return point 1 |
699: a = 2          |   main()'s stack frame
698: b = 14         |

697: return point 2 |
696: x = 2          |   mult2()'s stack frame
695: y = 7          |
695: z = 14         |
'''

def mult2(x,y):
    z = x * y
    return z

def main():
    a = 2
    b = mult2(a, 7)
    #return point 2
    print(b) #14
    return

main()
#return point 1
print('All done!')


'''
Recursive Stack
-----------------

701: return point 1
700: n = 4

699: return point 2
698: n = 3

697: return point 2
696: n = 2

695: return point 2
694: n = 1

693: return point 2
692: n = 0

O(n) time and space. Space because we are allocating n stack frames depending on input

tail call optimization - some languages implement an optimization that does not allocate additional stackframes for recursion

"unwinding the stack" - popping off each function call
'''

def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)
    #return point 2
    return

count(4)
#return point 1

'''
Subroutines
-------------
similar to functions in higher-level languages

CALL:
1. compute pc + 2 (the return address)
2. push the return address on the stack
3. set the pc to the value in the given register

RET:
1. pop the value off the stack (return address)
2. assign this value to the pc
'''

elif ir == CALL:
    #after function address and operand to next instruction
    return_addr = pc + 2

    #push on the stack
    register[SP] -= 1
    memory[register[SP]] = return_addr

    #set the pc to the value in the given register
    #similar to a 'jump'- calculate and address, set the pc to that address and jump there
    reg_num = memory[pc+1]
    dest_address = register[reg_num]
    pc = dest_address
    #don't increment pc since we are jumping to a specific address

elif ir == RET:
    #pop return address from stack
    return_addr = memory[register[SP]]
    register[SP] +=1

    #set the pc
    pc = return_addr

'''
In ls-8, C bit determines whether it sets the PC, but maybe does sometimes
'''

#For the sprint - jumps and conditional jumps
#conditional jumps are last thing keeping this emulator from being turing complete


'''
Interrupts
-------------

How the CPU knows that peripheral needs attention
IRET - pushes all the registers of the stack
handle the interrupt
pop the registers off the stack


Interrupt vector table stores pointers to where to go to handle certain interrupts
    -calls a driver that knows how to interact with the hardware

(for ls8)
timer interrupt - called one time per second
keyboard interrupt - stores key in F4
'''


'''
Python variables 
-----------------

variable a:
    pointer to the data -----> "hello, world" (ref count: 3)
                                     ^         
                                     |
variable b:                          |
pointer to the data -----------------+

variable c:
    pointer to the data -----> "hello, world" (ref count: 2)

a = "hello world"
b = a

id(a) = id(b)

c = "hello world"
id(c) != id(a)


sys.getrefcount(a) (adds one which is why above is 3 and 2 simply by getting the refcount)
getrecount is a function, which has a stack frame, creating a copy of the variable and adding 1 to the refcount


when reference count gets to zero it gets garbage-collected (memory gets freed up for something else)


'''