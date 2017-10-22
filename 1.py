from _operator import itemgetter
from PIL import Image

im = Image.open("testcap.gif").convert("P")
his = im.histogram()
values = {}
for i in range(256):
    values[i] = his[i]
newval = []
for j, k in sorted(values.items(), key=itemgetter(1), reverse=True)[2:4]:
    newval.append(j)
im2 = Image.new("P",im.size,255)
temp = {}
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        temp[pix] = pix
        for i in newval:
            if pix == i:
                im2.putpixel((y, x), 0)
im2.save("output.gif")