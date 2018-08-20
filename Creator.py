from PIL import Image

#functions = {0: nop, 1: push, 2: pop, 3: add, 4: sub, 5: jump, 6: transform}
# 1111 = WSEN

im = Image.open('blank.jpg')
pix = im.load()

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



im.save('test.png',quality = 95)