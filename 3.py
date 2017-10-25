import os
from veccom import  VectorCompare

def buildvector(im):
  d1 = {}
  count = 0
  for i in im.getdata():
    d1[count] = i
    count += 1
  return d1

v = VectorCompare()

iconset =  ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

imageset = []

for letter in iconset:
  for img in os.listdir('./iconset/%s/'%(letter)):
    temp = []
    if img != "Thumbs.db":
      temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
    imageset.append({letter:temp})