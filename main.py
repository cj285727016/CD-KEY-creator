from Tkinter import *
import tkMessageBox,tkFileDialog
import platform
import random

def CreateMenus():
    menubear=Menu(root)

    text=Entry(root,background ='white',width = 50)
    
    text.pack(side=TOP)

    button2=Button(root,text='enter the lenth of number\nthen create',command=lambda:createkey(text))
    button2.pack()

    playmenu=Menu(menubear,tearoff=0)
    playmenu.add_command(label='creat a cd key',command=lambda:createkey(text))
    menubear.add_cascade(label='main',menu=playmenu)

    helpmenu=Menu(menubear,tearoff=0)
    helpmenu.add_command(label='about me',command=aboutme)
    menubear.add_cascade(label='help',menu=helpmenu)

    root.config(menu=menubear)

def destroy_ui(ui):
    ui.destroy()

def aboutme():
    about=Toplevel()
    about.title('about me')
    about.geometry('200x100')
    name=Label(about,text="I AM CJAMENG")

    button=Button(about,text='return',command=lambda:destroy_ui(about))
    name.pack()
    button.pack()

def createkey(num):
    
    
    key=(1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
         't','u','v','w','x','y','z');
    i=int(num.get())
    num.delete(0, 50)
    while i:
        print random.choice(key),
        num.insert(0, random.choice(key))
        i=i-1
    print 

root=Tk()
root.title('CD-KEY creator')
root.geometry('300x200')
CreateMenus()
root.mainloop()
