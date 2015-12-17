#!/usr/bin/env python
#coding=gb2312
 

#*******************************************
#********************************************
import wx
import os
import sys
sys.path.append('..\..\pyhk')
import pyhk

from PIL import ImageGrab
import ctypes
import win32gui
import ctypes.wintypes
sys.path.append('..\mouse_key')
import mouse_key

sys.path.append('..\ocr')
import ocr
sys.path.append('..\getPicture')
import pic


import win32api
import win32con
import win32gui
from ctypes import *
import time
import commands

class POINT(Structure):
    _fields_ = [("x", c_ulong),
                ("y", c_ulong)]
class RECTANGE(Structure):
    _fields_ = [("top", POINT),
                ("bottom", POINT)]
authCodeRec = RECTANGE()
global priceAddBtn
global priceInputConfirmBtn
global authCodeInputWin
global authCodeConfirmBtn
priceAddBtn = POINT()
priceInputConfirmBtn = POINT()
authCodeInputWin = POINT()
authCodeConfirmBtn = POINT()

authCodeRec.top.x, authCodeRec.top.y, authCodeRec.bottom.x, authCodeRec.bottom.y = 171,279,208,294

global currentMouseX
global currentMouseY

def getAuthCode():
    global authCodeRec
    while 1:
            im = pic.getPic(authCodeRec.top.x, authCodeRec.top.y, authCodeRec.bottom.x, authCodeRec.bottom.y)
            authCodeStr = ocr.recognizeAuth(im) 
            print "current auth code " + repr(authCodeStr)
            # if the authCodeStr contains not number, return to get again.
            if authCodeStr.isdigit():
                    #if the color is no longer read, then strp 1:4.
                    return authCodeStr[1:4]
                    #return authCodeStr
            else:
                    print "识别到的验证码" + authCodeStr + "包含非法数字\n"
                    continue

def setPoint():
    print "按任意键\n"
    os.system("pause")
    x, y = mouse_key.get_mouse_point()
    print "获取的鼠标位置 x:" + repr(x) + "y:" + repr(y)
    return x,y
    
def setRectange():
    print ('将鼠标放置到截图区域的左上角，然后按回车\n')
    x,y = setPoint()
    print ('将鼠标防止到截图区域的右下角，然后按回车\n')
    u,v = setPoint();
    return x,y,u,v


def setAuthCodeRectange():
    global authCodeRec
    print "设置验证码截图区域"
    authCodeRec.top.x, authCodeRec.top.y, authCodeRec.bottom.x, authCodeRec.bottom.y = setRectange()
    print "得到验证码截图区域的坐标： ",authCodeRec.top.x, authCodeRec.top.y, authCodeRec.bottom.x, authCodeRec.bottom.y 

def setPriceAddBtn():
    global priceAddBtn
    print "将鼠标放置到加价按钮上\n"
    priceAddBtn.x, priceAddBtn.y = setPoint()
    print "得到加价按钮的坐标： ",priceAddBtn.x, priceAddBtn.y

    
def setPriceInputConfimBtn():
    global priceInputConfirmBtn
    print "将鼠标放置到出价按钮上\n"
    priceInputConfirmBtn.x, priceInputConfirmBtn.y = setPoint()
    print "current priceInputConfirmBtn ",priceInputConfirmBtn.x, priceInputConfirmBtn.y
    
def setAuthCodeInputWin():
    global authCodeInputWin
    print "将鼠标放置到输入验证码的窗口上\n"
    authCodeInputWin.x, authCodeInputWin.y = setPoint()
    print "current authCodeInputWin ", authCodeInputWin.x, authCodeInputWin.y

def setAuthCodeConfirmBtn():
    global authCodeConfirmBtn
    print "将鼠标放置到验证码输入后的确认按钮上\n"
    authCodeConfirmBtn.x, authCodeConfirmBtn.y = setPoint()
    print "current authCodeConfirmBtn ",authCodeConfirmBtn.x, authCodeConfirmBtn.y


def getCurrentMouseLocation():
    global currentMouseX
    global currentMouseY
    currentMouseX = 111
    currentMouseY = 222
    print "current x, y"
    currentMouseX, currentMouseY = mouse_key.get_mouse_point()
    print "current x y " + repr(currentMouseX) + repr(currentMouseY)
          
 
def setConfig():

    setAuthCodeRectange()
    setPriceAddBtn()
    setPriceInputConfimBtn()    
    setAuthCodeInputWin()
    setAuthCodeConfirmBtn()

def WriteToFile():
    global priceAddBtn
    global priceInputConfirmBtn
    global authCodeInputWin
    global authCodeConfirmBtn
    f = open('config_file', 'w')
# priceAddBtn = POINT()
    line = "priceAddBtn " + str(priceAddBtn.x) + " " + str(priceAddBtn.y) +"\n"
# priceInputConfirmBtn = POINT()
    line += "priceInputConfirmBtn " + str(priceInputConfirmBtn.x) + " " + str(priceInputConfirmBtn.y) + "\n"
# authCodeInputWin = POINT()
    line += "authCodeInputWin " + str(authCodeInputWin.x) + " " + str(authCodeInputWin.y) + "\n"
# authCodeConfirmBtn = POINT()
    line += "authCodeConfirmBtn " + str(authCodeConfirmBtn.x) + " " + str(authCodeConfirmBtn.y) + "\n"
# authCodeRec.top.x, authCodeRec.top.y, authCodeRec.bottom.x, authCodeRec.bottom.y = 171,279,208,294
    line += "authCodeRec " + str(authCodeRec.top.x) + " " + str(authCodeRec.top.y) + " " + str(authCodeRec.bottom.x) + " " + str(authCodeRec.bottom.y) + "\n"
    f.write(line)
    f.close



     
if __name__ == "__main__":
    setConfig()
    WriteToFile()
