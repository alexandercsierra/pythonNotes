'''
The Elements of Computing Systems - good book to read
https://www.nand2tetris.org/
'''

'''
Number Bases
-------------
Binary - Base 2
Octal - Base 8
Decimal - Base 10
Hexadecimal - Base 16

Base 64 uses 0-9 A-Z a-z + /

Base is the number of digits
Think about bases as different human languages for describing the same things

Counting and Places 
--------------------
when we run out of digits we add a new place that is the next power of the base


10^0 = 1
10^1 = 10
10^2 = 100
10^3 = 1000


Base 2:
    0
    1
   10
   11
  100

2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16

bit = 1 binary digit
Byte = 8 bits

11111111 == 255 decimal


In python we can tell python we want a number to be binary we can add 0b to the beginning for example: 0b1000 == 8
For hexadecimal  0x1000 == 4096
For octal 0o1000 == 512

Each of these will print out in decimal. To print in binary you can use bin(num) or for hex you can use hex(num)
You can also use a formatted string f'{8:b}' => 1000 which will output a str of that number in binary. Can make it 8 bit by using f'{8:08b}' => 00001000

int(str) can take a base as an argument int(str, 2) for base 2 or binary

Hexadecimal colors in CSS
RR GG BB
FF 00 AB

Hex is used also when you want to write binary, but binary is too verbose


0b0011 => decimal => 3 hex => 0x3

since binary and hexadecimal both have bases that are powers of two (2 and 16) you can convert between them

ob1111 => deicmal => 15 => hex => F

four bits is equal to one hex digit

ob0001001011011110010111010101 => hex - break it down in groups of four
0b 0001 0010 1101 1110 0101 1101 0101
0x   1    2    D    E    5    D    5
0x12DE5D5

77 to 0b. 77 has a 64, so put a 1 in 64s place, 77-64 = 13, there's an 8 then a 4 then a 1
0b1001101

binary => hex
0x  1    2     3   A    B     C
0b 0001 0010 0011 1010 1011 1100
0b000100100011101010111100

1 wire per bit. Under the hood a bit represents a single wire connection
'''


'''
Computer Emulator
software that pretends to be hardware

Turing Complete => it can solve any problem for which there is an algorithm*
*will be limited by memory

can think of memory as a big array of numbers
    you have indexes and values
index into the memory array == 'address' == 'pointer'
'''

# memory = [0] * 256 #RAM

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3  #SAVE_REG R1, 37  =>  R1 = 37 => register[1] = 37
PRINT_REG = 4 #PRINT_REG R1  => print(register[1])
memory_1 = [
    PRINT_BEEJ,
    PRINT_BEEJ,
    PRINT_BEEJ,
    HALT,
]

memory = [
    SAVE_REG, #SAVE_REG R1, 37
    1,
    37,
    SAVE_REG,
    2,
    11,
    ADD,
    1,
    2,
    PRINT_REG, #PRINT_REG R1
    1,
    PRINT_BEEJ,
    HALT
]

#this is okay but we should keep track of instructions we are running
for v in memory:
    if v == PRINT_BEEJ:
        print('Beej!')
    elif v == HALT:
        break

import sys

register = [0] * 8 #8 registers, like variables - with fixed names R0, R1, R2 .. R7. Registers are fixed, you cannot make more because they are physical hardware components. These are general purpose registers





pc = 0 #program counter, index of the current instruction. This is a special purpose register
while running:
    ir = memory[pc] #instruction register
    if ir == PRINT_BEEJ:
        print('Beej!')
        pc +=1
    elif ir == SAVE_REG:
        reg_num = memory[pc+1]
        value = memory[pc+2]
        register[reg_num] == value
        pc +=3
    elif ir == PRINT_REG:
        reg_num = memory[pc + 1]
        print(register[reg_num])
        pc+=2
    elif ir == ADD:
        num1 = memory[pc + 1]
        num2 = memory[pc + 2]
        print(memory[num1]+memory[num2])
        pc+=3
    elif ir == HALT:
        running = False
        pc +=1
    else:
        print(f'Unkown instruction {ir} at address {pc}')
        sys.exit(1)


'''
asm directory can be ignored - talking about interrupts can be ignored


ls8 where the code is 
    readme has more detail (not split by day)
ls8-spec - has all the details that you need to know
main readme - high level overview of what we want to do
examples directory contains programs that your emulator will be able to run
'''