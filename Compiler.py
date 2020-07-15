from __future__ import print_function
from PIL import Image

stack = []

# single callstack so you really should have functions terminate in call order
# or v bad
callstack = []

pointers = [(0, 0)]
#name = raw_input("What is the name of your program? ")
name = 'test.png'
im = Image.open(name)
pix = im.load()

# No operation


def nop(operand):
    getpointers()

# Pushes operand to the stack


def push(operand):
    stack.append(operand)
    getpointers()

# Pops and prints the first element of the stack, Prints as ascii char if non-zero operand


def pop(operand):
    out = stack.pop()
    if operand != 0:
        try:
            print (chr(out), end='')
            getpointers()
        except:
            print ("Conversion error from int to char in pop")
            exit(1)
    else:
        print (out, end='')
        getpointers()

# Adds top elements of stack unless given non zero arg


def add(operand):
    if operand == 0:
        stack.append(stack.pop() + stack.pop())
        getpointers()
    else:
        stack.append(stack.pop() + operand)
        getpointers()

# Subtracts top elements of stack, unless given non zero arg


def sub(operand):
    if operand == 0:
        stack.append(stack.pop() - stack.pop())
        getpointers()
    else:
        stack.append(stack.pop() - operand)
        getpointers()

# Unconditional jump to (stack[0],stack[1]), destroys top 2 elements of stack


def jump(operand):
    try:
        coords = (stack.pop(), stack.pop())
        pointers.append(coords)
        callstack.append(coords)
        getpointers()
    except IndexError:
        print ("Tried to pop empty stack")
        exit(1)

# Jumps if stack.pop() == operand, destroys top 3 elements of stack


def condjump(operand):
    try:
        if stack.pop() == operand:
            coords = (stack.pop(), stack.pop())
            pointers.append(coords)
            callstack.append(coords)
            getpointers()
        else:
            stack.pop()
            stack.pop()
            getpointers()
    except IndexError:
        print ("Tried to pop empty stack")
        exit(1)


# Functions like getpointers, But takes operand as B and top of call stack as location.


def ret(operand):
    try:
        location = callstack.pop()
        if operand & 0b1:
            pointers.append((location[0], location[1]-1))
        if operand >> 1 & 0b1:
            pointers.append((location[0]+1, location[1]))
        if operand >> 2 & 0b1:
            pointers.append((location[0], location[1]+1))
        if operand >> 3 & 0b1:
            pointers.append((location[0]-1, location[1]))
            
    except IndexError:
        print ("Tried to pop an empty call stack")
        exit(1)

# Kills pointer if stack.pop() == operand, Destroys top of stack


def condkill(operand):
    try:
        if stack.pop() == operand:
            pass
        else:
            getpointers()
    except IndexError:
        print ("Tried to pop empty stack")
        exit(1)

# Transforms current coordinates to have opcode operand and operand stack.pop()


def transform(operand):
    pix[(x, y)] = (operand, stack.pop(), pix[(x, y)][2])
    getpointers()

# Reads input from user and pushes to stack


def inpchar(operand):
    userin = ord(input("? ")[0])
    if type(userin) != int:
        print ("INVALID INPUT! Please input an ascii character")
        exit(1)
    else:
        stack.append(userin)
        getpointers()

# Reads input from user as an integer and pushes to stack


def inpint(operand):
    userin = int(input("? "))
    if type(userin) != int:
        print ("INVALID INPUT! Please input an integer")
        exit(1)
    else:
        stack.append(userin)
        getpointers()


# Duplicates top element of stack


def dup(operand):
    last = stack.pop()
    stack.extend([last, last])
    getpointers()

# Multiplies top elements of stack unless given a non-zero operand


def mul(operand):
    if operand == 0:
        stack.append(stack.pop() * stack.pop())
        getpointers()
    else:
        stack.append(stack.pop() * operand)
        getpointers()

# Removes outgoing pointers if the stack is empty


def emptykill(operand):
    if stack == []:
        pass
    else:
        getpointers()

# Reverses the stack


def reverse(operand):
    stack.reverse()
    getpointers()

# Rotates stack such that n1     n3
#                         n2  -> n1
#                         n3     n2


def rot(operand):
    try:
        n1 = stack.pop()
        n2 = stack.pop()
        n3 = stack.pop()
        stack.extend([n2, n1, n3])
        getpointers()
    except:
        print ("Rotate Error on stack {0}, at {1},{2}".format(stack, x, y))
        exit(1)

# Makes a copy of the second item and pushes it to the top


def over(operand):
    try:
        n1 = stack.pop()
        n2 = stack.pop()
        stack.extend([n2, n1, n2])
        getpointers()
    except:
        print ("Over Error")
        exit(1)

# Swaps the top two elements of the stack


def swap(operand):
    try:
        n1 = stack.pop()
        n2 = stack.pop()
        stack.extend([n1, n2])
        getpointers()
    except:
        print ("Swap Error")
        exit(1)

# Removes the top of the stack


def drop(operand):
    try:
        stack.pop()
        getpointers()
    except IndexError:
        print ("Tried to drop empty stack")
        exit(1)

# Waits for stack to equal operand before proceeding


def waitfor(operand):
    try:
        top = stack.pop()
        if top == operand:
            getpointers()
        else:
            pointers.append((x, y))
        stack.append(top)

    except IndexError:
        print ("Tried to wait on an empty stack")
        exit(1)

# Kills if stack has one element


def singlekill(operand):
    if len(stack) == 1:
        pass
    else:
        getpointers()

# Runs if it is the last pointer


def runifonly(operand):
    if len(pointers) == 0:
        getpointers()
    else:
        pointers.append((x, y))


functions = {0: nop, 1: push, 2: pop, 3: add, 4: sub,
             5: jump, 6: condjump, 7: ret, 8: condkill,
             9: transform, 10: inpchar, 11: dup, 12: mul,
             13: emptykill, 14: reverse, 15: rot, 16: over,
             17: swap, 18: drop, 19: inpint, 20: waitfor,
             21: singlekill, 22: runifonly}


def operate(opcode, operand):
    try:
        functions[opcode](operand)
    except KeyError:

        print ("R value {0} not valid! (instruction at {1},{2})".format(
            opcode, x, y))
        exit(1)


def getpointers():
    # refresh current in case changed by kill
    current = pix[x, y]
    # Adds new pointers based of the B in RGB code.
    # 1111 = WSEN

    if current[2] & 0b1:
        pointers.append((x, y-1))
    if current[2] >> 1 & 0b1:
        pointers.append((x+1, y))
    if current[2] >> 2 & 0b1:
        pointers.append((x, y+1))
    if current[2] >> 3 & 0b1:
        pointers.append((x-1, y))


while pointers != []:
    x, y = pointers.pop(0)
    try:
        current = pix[x, y]
    except IndexError:
        print ("Coords out of range ({0},{1})".format(x,y))
        exit(1)
    operate(current[0], current[1])
