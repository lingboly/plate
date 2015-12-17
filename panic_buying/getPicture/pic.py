#!/usr/bin/env python
#coding=gb2312

import wx
import os
import sys
sys.path.append('..\..\pyhk')
import pyhk

from PIL import ImageGrab
import ctypes
import win32gui
import ctypes.wintypes
import datetime
 
 
def capture_fullscreen():
    '''
    Function:全屏抓图
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-10
    ''' 
    #抓图  
    pic = ImageGrab.grab()
     
    #保存图片
    save_pic(pic)

 
def save_pic(pic, filename = '未命令图片.png'):
    '''
    Function:使用文件对框，保存图片
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-10
    '''    
    app = wx.PySimpleApp()
     
    wildcard = "PNG(*.png)|*.png"
    dialog = wx.FileDialog(None, "Select a place", os.getcwd(),
                           filename, wildcard, wx.SAVE)
    if dialog.ShowModal() == wx.ID_OK:
        pic.save(dialog.GetPath().encode('gb2312'))
    else:
        pass
     
    dialog.Destroy()   
     
def getPic(left, top, right, bottom):     
    class RECT(ctypes.Structure):
        _fields_ = [('left', ctypes.c_long),
                ('top', ctypes.c_long),
                ('right', ctypes.c_long),
                ('bottom', ctypes.c_long)]
        def __str__(self):
            return str((self.left, self.top, self.right, self.bottom))
     
    rect = RECT()
    rect.left = left
    rect.top = top
    rect.right = right
    rect.bottom = bottom
    print rect.left,rect.top,rect.right,rect.bottom
 
    #调整坐标
    rangle = (rect.left,rect.top,rect.right,rect.bottom)
     
    #抓图
    pic = ImageGrab.grab(rangle)
    now = datetime.datetime.now()
    fileName = now.strftime("%Y-%m-%d_%H_%M_%S") + ".jpg"
    
    pic.save(fileName,"JPEG");
    return pic
    
def main():
    '''
    Function:主函数，注册快捷键
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-10
    '''        
     
    #创建hotkey句柄
    hot_handle = pyhk.pyhk()
  
    #注册抓取全屏快捷键CTRL+F1
    hot_handle.addHotkey(['Ctrl', 'F1'], capture_fullscreen)
     
     
    hot_handle.addHotkey(['Ctrl', 'F2'], getPic)
  
    #开始运行
    hot_handle.start()
   # capture_current_windows()
     
if __name__ == "__main__":
    main()
