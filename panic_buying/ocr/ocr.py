# -*- coding: cp936 -*-
import sys
import Image
import ImageEnhance
import ImageFilter
import ImageDraw

from pytesser import *

# 二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

#由于都是数字, 对于识别成-1的修正为4
#对于识别成.的，做无效处理
rep={
     '-1':'4',
     '.':'',
     '-2':'2',
     '-3':'3',
     '-4':'4',
     '-5':'5',
     '-6':'6',
     '-7':'7',
     '-8':'8',
     '-9':'9',
     ' ':''
    };
def  clearColor(im, clColor):
    #draw = ImageDraw.Draw(im)
    newIm = Image.new("RGB", im.size, "white")
    #Image.open("newImage.jpg")
    draw = ImageDraw.Draw(newIm)
    for i in range(0,list(im.size)[0]):
        for j in range(0,list(im.size)[1]):              
            if im.mode == "RGB":
                color = list(im.getpixel((i,j)))
                if clColor == "R":
                    if color[0] >= color[1] + 50 and color[0] > color[2] + 50:
                        color[0] = 0
                        color[2] = 0
                        #print "R"
                        color[1] = 0
                        point = [i,j]
                        draw.point(point,tuple(color))
                elif clColor == "G":
                    #TODO
                    color[0] = 255
                    color[2] = 255
                    print "G"
                elif clColor == "B":
                    #TODO
                    color[1] = 255
                    color[0] = 255
                    print "B"
                else:
                    print "color type not supported!"
                    sys.exit(1)

            elif im.mode == "L":
                color = im.getpixel((i,j))
                color = color + rnd
                point = [i,j]
                draw.point(point,color)
            else:
                print "File type not supported!"
                sys.exit(1)
    del draw
    return newIm

def clearColor1(im, clColor):
    im.load()
    r,g,b = im.split()  #分割成三个通道
    r.save("r.jpg","JPEG")
    g.save("g.jpg","JPEG")
    b.save("b.jpg","JPEG")
    im = Image.merge("RGB", (g, g, b))
    return im;

def  recognize(im):
    name = "auth.jpg"
    #去除噪点
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
  
    #转化到亮度
    imgry = im.convert('L')
    imgry.save('g'+name)
    #二值化
    out = imgry.point(table,'1')
    out.save('b'+name)
    #识别
    text = image_to_string(out)
    #识别对吗
    text = text.strip()
    text = text.upper();

    for r in rep:
        text = text.replace(r,rep[r])

    #out.save(text+'.jpg')
    print text
    return text
def  recognizeAuth(im):
    #get the red color
    im = clearColor(im, "R")
    print "only RED\n"

    name = "auth.jpg"
    #im.show()
    im.save("authR.jpg","JPEG")
    return recognize(im)
    
def  recognizePrice(im):
    text = image_to_string(im)
    #识别对吗
    text = text.strip()
    text = text.upper();

 #   for r in rep:
 #       text = text.replace(r,rep[r])

    #out.save(text+'.jpg')
    print text
    return text

def  getverify1(name):    
    #open
    im = Image.open(name)
    return recognizeAuth(im)
def  getverify2(name):    
    #open
    im = Image.open(name)
    return recognize(im)

if __name__ == "__main__":
    getverify1('auth0.jpg')
    getverify1('auth1.jpg')
    getverify2('auth2.jpg')
    #getverify1('auth3.jpg')
    getverify1('auth4.jpg')
    text = "09 8 -1-2-3"
    for r in rep:
        text = text.replace(r,rep[r])
    print text
    getverify1('auth5.jpg')
    
