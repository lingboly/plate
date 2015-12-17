#!/usr/bin/env python
#coding=gb2312
 
#*******************************************
#更新记录
#0.1 2015-0819 create by lingboly
#. the flash will not accept the key input by normal windows apis, thus try to use the soft key instead.
#********************************************
import wx
import os
import sys

import ctypes
import win32gui
import ctypes.wintypes
sys.path.append('..\mouse_key')
import mouse_key

#import win32api
#import win32con
#import win32gui
from ctypes import *
import time
import commands
class POINT(Structure):
    _fields_ = [("x", c_ulong),
                ("y", c_ulong)]

#define the class the for number 0~9
class SOFT_KEY:
    position = POINT()
    before_time = 0.1
    keep_time = 0.4
    after_time = 0.1
    index = -1;
    name = '';
    def __init__(self, name, index):
        #1. the softkey position
        self.position = POINT()
	#2. the wait time before click key
	self.before_time = 0
	#3. the softkey pressing time
	self.keep_time = 0.3
	#4. the wait time after up key
	self.after_time = 0.1
	self.index = index;
	self.name = name;
    def input(self):
        mouse_key.mouse_up()
        time.sleep(self.before_time)
        mouse_key.mouse_down(self.position.x, self.position.y)
        time.sleep(self.keep_time)
        mouse_key.mouse_up()
	time.sleep(self.after_time)
    def save_config(self,f):
    #5. the function to save the position into config file.
        line = "SOFTKEY " + str(self.index) + " " + str(self.position.x) + " " + str(self.position.y) + "\n"
        f.write(line)
    def get_config(self, x, y):
        self.position.x = x
	self.position.y = y
    #6. the function to read the position from config file.
    def getPoint():
        print "press any key after moving mouse to the num", str(index), "\n"
        os.system("pause")
        x, y = mouse_key.get_mouse_point()
        print "current point x:" + repr(x) + " y:" + repr(y)
        self.position.x = x
	self.position.y = y


global keys
keys = []

def getScreenPoint():
    print "press any key\n"
    os.system("pause")
    x, y = mouse_key.get_mouse_point()
    print "current point x:" + repr(x) + " y:" + repr(y)
    return x,y
     
def storeConfigToFile():
    f = open('softkey.conf', 'w')
    for i in range(len(keys)):
	print "save config for ", i, keys[i].name
        keys[i].save_config(f)
    f.close

def ReadConfigFromFile():
    f = open('softkey.conf', 'r')
    for line in f:
        arguments = line.split(" ")
	if arguments[0] == "SOFTKEY":
            keys[int(arguments[1])].get_config( int(arguments[2]), int(arguments[3]) );
    f.close
def createPoints():
    for i in range(0,10):
	key = SOFT_KEY(str(i), i)
	keys.append(key)
    print "keys len", len(keys)

def initilizePoints():
    for i in range(len(keys)):
        x,y = getPoint()
        key.get_config(x, y)
    print "keys len", len(keys)

def input_nums(str=''):
    for c in str:
	key = keys[int(c)]
	key.input()

def test_input_num():
    #get the position
    authCodeInputWin = POINT()
    print "input auth code enter window\n"
    authCodeInputWin.x, authCodeInputWin.y = getScreenPoint()
    print "current authCodeInputWin ", authCodeInputWin.x, authCodeInputWin.y
    #input string.
    print "click authCodeInputWin position " + repr(authCodeInputWin.x) + "y" + repr(authCodeInputWin.y)
    mouse_key.mouse_click(authCodeInputWin.x, authCodeInputWin.y)
    input_nums("01234567890")
    mouse_key.mouse_click(authCodeInputWin.x, authCodeInputWin.y)

    

def main():
    #first get the positions and save them into config file.
    createPoints()
    #initilizePoints()
    #storeConfigToFile()
    #read positions from config file, and init all the soft keys.
    ReadConfigFromFile()
    #try input some values in the website
    test_input_num()

     
if __name__ == "__main__":
    main()
