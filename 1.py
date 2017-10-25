from _operator import itemgetter
from PIL import Image
import hashlib
import time
import os
from veccom import  VectorCompare


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
#im2.save("output.gif")
inletter = False
foundletter = False
start = 0
end = 0

letters = []

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y, x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y
    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start, end))
    inletter = False

count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
    b = ("%s%s" % (time.time(),count)).encode('utf-8')
    m.update(b)
    im3.save("./%s.gif" % (m.hexdigest()))
    count += 1

def buildvector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1

v = VectorCompare()

iconset =  ['1','2','3','4','5','6','7','8','9']
imageset = []

for letter in iconset:
    for img in os.listdir('./icontest/%s/'%(letter)):
        temp = []
        if img != "Thumbs.db":
            temp.append(buildvector(Image.open("./icontest/%s/%s"%(letter,img))))
        imageset.append({letter:temp})
