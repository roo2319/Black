from PIL import Image

condreg = 0
stack = []
callstack = []
callstack2 = []
callstack3 = []
callstack4 = []
pointers = [(0,0)]
#name = raw_input("What is the name of your image? ")
name = "test.png"
im = Image.open(name)
pix = im.load()
width, height = im.size


def operate(opcode, operand):
    pass

while pointers != []:
    x, y = pointers.pop()
    current = pix[x,y]
    print current

    operate(current[0],current[1])

    #Adds new pointers based of the B in RGB code.
    #1111 = WSEN

    if current[2] & 0b1:
        pointers.append((x,y-1))
    if current[2] >> 1 & 0b1:
        pointers.append((x+1,y))
    if current[2] >> 2 & 0b1:
        pointers.append((x,y+1))
    if current[2] >> 3 & 0b1:
        pointers.append((x-1,y))
        
    print current
