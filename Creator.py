from PIL import Image

im = Image.open('blank.jpg')
pix = im.load()

pix[0,0] = (127,0,2)
pix[1,0] = (0,127,4)
pix[1,1] = (64,46,8)
pix[0,1] = (46,64,1)

print pix[0,0]

im.save('test.png',quality = 95)