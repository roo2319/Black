# Scritch
sorry

## What? 
Yeah, Scritch is an esoteric, stack-based programming language. The programs are .png files where the RGB values represent the instruction.

R|G|B

=

OPCODE|OPERAND|EXIT DIRECTION

The opcode can range from 0 to 22, the operand 0 to 255 and the exit direction is effective at 0 to 15, but the high bits of blue are unreserved and can be used as seen fit.

## What function's are supported?

0. NOP
1. PUSH
2. POP 
3. ADD
4. SUB
5. JUMP
6. CONDJUMP
7. RET
8. CONDKILL
9. TRANSFORM
10. INP
11. DUP
12. MUL
13. EMPTYKILL
14. REVERSE 
15. ROT
16. OVER
17. SWAP
18. DROP
19. INPINT
20. WAITFOR
21. SINGLEKILL
22. RUNIFONLY

## What is exit direction?

Exit direction is the direction that the program flows. Execution starts in the top right [0,0] and the B value represents which adjacent pixels should be added to the execution queue. It is represented as a binary encoded value such that 1111 represents WSEN. 

## Doesn't this all lead to horrible concurrency issues?
Not if you program around it?

## Fine, What are the dependencies?

All that you need is a python installation with PIL or Pillow
