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
    Function:ȫ��ץͼ
    Input��NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-10
    ''' 
    #ץͼ  
    pic = ImageGrab.grab()
     
    #����ͼƬ
    save_pic(pic)

 
def save_pic(pic, filename = 'δ����ͼƬ.png'):
    '''
    Function:ʹ���ļ��Կ򣬱���ͼƬ
    Input��NONE
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
 
    #��������
    rangle = (rect.left,rect.top,rect.right,rect.bottom)
     
    #ץͼ
    pic = ImageGrab.grab(rangle)
    now = datetime.datetime.now()
    fileName = now.strftime("%Y-%m-%d_%H_%M_%S") + ".jpg"
    
    pic.save(fileName,"JPEG");
    return pic
    
def main():
    '''
    Function:��������ע���ݼ�
    Input��NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-10
    '''        
     
    #����hotkey���
    hot_handle = pyhk.pyhk()
  
    #ע��ץȡȫ����ݼ�CTRL+F1
    hot_handle.addHotkey(['Ctrl', 'F1'], capture_fullscreen)
     
     
    hot_handle.addHotkey(['Ctrl', 'F2'], getPic)
  
    #��ʼ����
    hot_handle.start()
   # capture_current_windows()
     
if __name__ == "__main__":
    main()
