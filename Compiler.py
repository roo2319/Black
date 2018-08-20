from PIL import Image

condreg = 0
stack = []

# single callstack so you really should have functions terminate in call order
# or v bad
callstack = []

pointers = [(0, 0)]
#name = raw_input("What is the name of your code? ")
name = "test.png"
im = Image.open(name)
pix = im.load()
width, height = im.size

# No operation


def nop(operand):
    pass

# Pushes operand to the stack


def push(operand):
    stack.insert(0, operand)

# Pops and prints the first element of the stack, Prints as ascii char if non-zero operand


def pop(operand):
    out = stack.pop(0)
    if operand != 0:
        print chr(out)
    else:
        print out

# Adds top elements of stack unless given non zero arg


def add(operand):
    if operand == 0:
        stack.insert(0, stack.pop(0) + stack.pop(0))
    else:
        stack.insert(0, stack.pop(0) + operand)

# Subtracts top elements of stack, unless given non zero arg


def sub(operand):
    if operand == 0:
        stack.insert(0, stack.pop(0) - stack.pop(0))
    else:
        stack.insert(0, stack.pop(0) - operand)

# Jumps to (stack[0],stack[1])


def jump(operand):
    try:
        coords = (stack.pop(0), stack.pop(0))
        pointers.append(coords)
        callstack.append(coords)
    except IndexError:
        print "Tried to pop empty stack"
        exit(1)

# Returns to top of callstack, Should be used in pixel with no outgoing pointers


def ret(operand):
    try:
        pointers.append(callstack.pop(0))
    except IndexError:
        print "Tried to pop an empty call stack"
        exit(1)


# Transforms current coordinates to have opcode operrand and operand stack.pop()


def transform(operand):
    pix[(x, y)] = (operand, stack.pop(0), pix[(x, y)][3])


functions = {0: nop, 1: push, 2: pop, 3: add, 4: sub, 5: jump, 6: ret, 7: transform}


def operate(opcode, operand):
    try:
        functions[opcode](operand)
    except KeyError:
        print "R value not valid!"
        exit(1)


while pointers != []:
    global x, y
    x, y = pointers.pop(0)
    current = pix[x, y]
    operate(current[0], current[1])

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
