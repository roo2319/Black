from PIL import Image

#functions = {0: nop, 1: push, 2: pop, 3: add, 4: sub,
#             5: jump, 6: condjump, 7: ret, 8: condkill,
#             9: transform, 10: inp, 11: dup, 12: mul,
#             13: emptykill, 14: reverse, 15: rot, 16: over,
#             17: swap, 18: drop, 19: inpint, 20: waitfor,
#             21: singlekill, 22:runifonly}
# 1111 = WSEN

im = Image.open('blank.png')
pix = im.load()


pix[0,0] = (1,32,2)
pix[1,0] = (1,32,2)
pix[2,0] = (5,0,2)
pix[3,0] = (22,0,2)
pix[4,0] = (0,0,6)
pix[4,1] = (22,0,4)
pix[4,2] = (2,0,0)
pix[5,0] = (21,0,2)
pix[6,0] = (12,0,4)
pix[6,1] = (0,0,8)
pix[5,1] = (0,0,1)

pix[32,32] = (0,0,4)
pix[32,33] = (19,0,14)

pix[31,33] = (0,0,8)
pix[30,33] = (11,0,8)
pix[29,33] = (4,1,8)
pix[28,33] = (11,0,4)
pix[28,34] = (8,0,2)
pix[29,34] = (11,0,2)
pix[30,34] = (8,1,2)
pix[31,34] = (0,0,1)

pix[33,33] = (11,0,2)
pix[34,33] = (4,1,2)
pix[35,33] = (0,0,2)
pix[36,33] = (11,0,4)
pix[36,34] = (8,0,8)
pix[35,34] = (11,0,8)
pix[34,34] = (8,1,8)
pix[33,34] = (0,0,1)



pix[32,34] = (20,1,4)
pix[32,35] = (0,0,4)
pix[32,36] = (0,0,4)
pix[32,37] = (0,0,4)
pix[32,38] = (18,0,0)






im.save('test.png',quality = 95)

''' Hello World
pix[1,3] = (1,ord('h'),4)
pix[2,2] = (1,ord('e'),0)
pix[1,2] = (1,ord('l'),6)
pix[2,1] = (1,ord('l'),0)
pix[0,2] = (1,ord('o'),2)
pix[1,1] = (1,ord('w'),2)
pix[2,0] = (1,ord('o'),0)
pix[0,1] = (1,ord('r'),6)
pix[1,0] = (1,ord('l'),2)
pix[0,0] = (1,ord('d'),6)

pix[1,4] = (2,1,14)
pix[0,4] = (2,20,0)
pix[2,4] = (2,20,0)
pix[1,5] = (2,20,14)
pix[0,5] = (2,30,4)
pix[2,5] = (2,30,6)
pix[1,6] = (2,30,0)
pix[0,6] = (2,40,0)
pix[2,6] = (2,40,0)
pix[3,5] = (2,40,0)
'''

'''
#Repeats users string back to them
pix[0,0] = (10,255,2)
pix[1,0] = (11,0,2)
pix[2,0] = (11,0,2)
pix[3,0] = (1,5,4)
pix[3,1] = (1,0,8)
pix[2,1] = (15,255,8)
pix[1,1] = (6,ord(' '),8)
pix[0,1] = (8,ord(' '),1)

pix[0,5] = (0,0,2)
pix[1,5] = (14,0,2)
pix[2,5] = (2,255,2)
pix[3,5] = (13,0,4)
pix[3,6] = (0,0,8)
pix[2,6] = (0,0,1)
'''
