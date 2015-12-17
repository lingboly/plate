#!/usr/bin/env python
#coding=gb2312
 
#注意一下快捷方式：
#快捷键F2: 出价
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
#the flash can only accept the soft key.
import soft_key

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
                    return authCodeStr
            else:
                    time.sleep(0.3)
                    print "recognized auth code " + authCodeStr + "contains abnormal value\n"
                    continue

def setPoint():
    print "press any key\n"
    os.system("pause")
    x, y = mouse_key.get_mouse_point()
    print "current point x:" + repr(x) + "y:" + repr(y)
    return x,y
    
def setRectange():
    print ('Put the mouse at the point of the top-left of rectange\n')
    x,y = setPoint()
    print ('Put the mouse at the point of the bottom-right of rectange\n')
    u,v = setPoint();
    return x,y,u,v


def setAuthCodeRectange():
    global authCodeRec
    print "input auth code rec"
    authCodeRec.top.x, authCodeRec.top.y, authCodeRec.bottom.x, authCodeRec.bottom.y = setRectange()
    print "current authCodeRec ",authCodeRec.top.x, authCodeRec.top.y, authCodeRec.bottom.x, authCodeRec.bottom.y 

def setPriceAddBtn():
    global priceAddBtn
    print "input the price enter window0\n"
    priceAddBtn.x, priceAddBtn.y = setPoint()
    print "current priceAddBtn ",priceAddBtn.x, priceAddBtn.y

    
def setPriceInputConfimBtn():
    global priceInputConfirmBtn
    print "input the price enter confirm botton position\n"
    priceInputConfirmBtn.x, priceInputConfirmBtn.y = setPoint()
    print "current priceInputConfirmBtn ",priceInputConfirmBtn.x, priceInputConfirmBtn.y
    
def setAuthCodeInputWin():
    global authCodeInputWin
    print "input auth code enter window\n"
    authCodeInputWin.x, authCodeInputWin.y = setPoint()
    print "current authCodeInputWin ", authCodeInputWin.x, authCodeInputWin.y

def setAuthCodeConfirmBtn():
    global authCodeConfirmBtn
    print "input auth code confirm button position\n"
    authCodeConfirmBtn.x, authCodeConfirmBtn.y = setPoint()
    print "current authCodeConfirmBtn ",authCodeConfirmBtn.x, authCodeConfirmBtn.y


def minus100():
    #出价增量-100
    global priceAdd
    priceAdd -= 100     
    print "current priceAdd - 100 = " + repr(priceAdd)

def plus100():
    #出价增量+100
    global priceAdd
    priceAdd += 100     
    print "current priceAdd + 100 = " + repr(priceAdd)
     
def getCurrentMouseLocation():
    global currentMouseX
    global currentMouseY
    currentMouseX = 111
    currentMouseY = 222
    print "current x, y"
    currentMouseX, currentMouseY = mouse_key.get_mouse_point()
    print "current x y " + repr(currentMouseX) + repr(currentMouseY)
     
def commit():
    '''
    '''    
    global priceAddBtn
    global priceInputConfirmBtn
    global authCodeInputWin
    global authCodeConfirmBtn
    
    mouse_key.mouse_click(priceAddBtn.x, priceAddBtn.y)
    mouse_key.mouse_click(priceInputConfirmBtn.x, priceInputConfirmBtn.y)
    time.sleep(0.3)
    #get the authCode from the authCode rectangle
    authCodeStr = getAuthCode()
    print "click authCodeInputWin position x:" + repr(authCodeInputWin.x) + ", y:" + repr(authCodeInputWin.y)
    mouse_key.mouse_click(authCodeInputWin.x, authCodeInputWin.y)
    print "key enter " + authCodeStr
    soft_key.input_nums(authCodeStr)
    mouse_key.mouse_click(authCodeConfirmBtn.x, authCodeConfirmBtn.y)
    time.sleep(0.1)
    mouse_key.mouse_click(authCodeConfirmBtn.x, authCodeConfirmBtn.y)
    print "exit commit\n"

def ReadFromFile():
        global priceAddBtn
        global priceInputConfirmBtn
        global authCodeInputWin
        global authCodeConfirmBtn

        f = open('config_file', 'r')
        for line in f:
                arguments = line.split(" ")
                # priceAddBtn = POINT()
                if arguments[0] == "priceAddBtn":
                        priceAddBtn.x = int(arguments[1])
                        priceAddBtn.y = int(arguments[2])
        # priceInputConfirmBtn = POINT()
                elif arguments[0] == "priceInputConfirmBtn":
                        priceInputConfirmBtn.x = int(arguments[1])
                        priceInputConfirmBtn.y = int(arguments[2])
        # authCodeInputWin = POINT()
                elif arguments[0] == "authCodeInputWin":
                        authCodeInputWin.x = int(arguments[1])
                        authCodeInputWin.y = int(arguments[2])
	# authCodeConfirmBtn = POINT()
                elif arguments[0] == "authCodeConfirmBtn":
                        authCodeConfirmBtn.x = int(arguments[1])
                        authCodeConfirmBtn.y = int(arguments[2])
                # authCodeRec.top.x, authCodeRec.top.y, authCodeRec.bottom.x, authCodeRec.bottom.y = 171,279,208,294
                elif arguments[0] == "authCodeRec":
                        authCodeRec.top.x = int(arguments[1])
                        authCodeRec.top.y = int(arguments[2])
                        authCodeRec.bottom.x = int(arguments[3])
                        authCodeRec.bottom.y = int(arguments[4])
                
        f.close

 
def main():
    '''
    main function
    '''        
    hot_handle = pyhk.pyhk()
    
    print "read the soft key location from file softkey.conf\n"
    soft_key.createPoints()
    soft_key.ReadConfigFromFile()
    print "read the flash config from file\n"
    ReadFromFile()
    
    print "register commit with F2\n"
    hot_handle.addHotkey(['F2'], commit, isThread=True)

    hot_handle.start()

     
if __name__ == "__main__":
    main()
