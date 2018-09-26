#coding:utf-8
import time
import os
from pygame import mixer
from mutagen.mp3 import MP3
import win32api
import win32console
import win32gui
from Tkinter import *
from threading import Thread
import sys

win = Tk()

width = 300
height = 300
win.configure(bg = "black")
x = (win.winfo_screenwidth() // 2) - (width // 2)
y = (win.winfo_screenheight() // 2) - (height // 2)
win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def calis():
    print "ok"
    win.destroy()
        

evet = Button(win, text="Calistir", bg="red", fg="white",command = calis)
evet.pack(fill=BOTH)
def cik():
    Thread(target = win.destroy(), args=()).start()
    sys.exit()
hayir= Button(win, text="Kapat", bg="green", fg="black",command  = cik )
hayir.pack(fill=BOTH)


helpl = Label(win,text = "Bu Program Cagri Atalar tarafından yapılmıştır\nEger Cagri Atalar'ın müzik listesinin çalınmasını istemiyorsanız Kapat butonuna tıklayın :)",fg = "yellow",bg = "blue")
helpl.pack(fill=BOTH)

mainloop()




win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

files = os.listdir(os.curdir)

liste = [i for i in files if ".mp3" in i]

for i in liste:
    mixer.init()
    mixer.music.load(i)
    mixer.music.play()
    audio = MP3(i)
    if audio.info.length >= 400:
        time.sleep(400)
    else:
        time.sleep(audio.info.length)
    
    
