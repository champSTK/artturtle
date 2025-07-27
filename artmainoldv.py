from tkinter import *
from turtle import *
import turtle
import time
color("grey")
speed(20)
title("Art with Aroow")


from PIL import ImageGrab
from PIL import Image

name = ("1")

def exitart():
    exit()

def saveas():
    img=Tk()
    f = Entry(img)
    f.pack()
    f.focus_set()
    
    def savename():
        name =f.get()
        if isinstance(name,str) :
           saveart()

    b = Button(img, text = "OK", width = 10,command=savename)
    b.pack()



def saveart():
    fileart = ImageGrab.grab()
    #filename= input('Save as :\n')
    filename= name  
    fileart.save(filename +".png")
    fileart.close() 

savebtn = Button(text='Save' ,command= saveart).pack()

exitbtn = Button(text='Exit' , command=exitart).pack(side='right')

saveasbtn = Button(text='Save As' , command=saveas).pack()

screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)


#turle operations
def fr():
    forward(20)
def up():
    setheading(90)
    forward(20)
def down():
    setheading(270)
    forward(20)
def left():
    setheading(180)
    forward(20)
def right():
    setheading(0)
    forward(20)
def uleftv():
    lt(45)
    forward(20)
def urightv():
    rt(45)
    forward(20)
def dleftv():
    lt(135)
    forward(20)
def drightv():
    rt(135)
    forward(20)
# def leftu():
#     setheading(90)                  #still working on curve turning of the turtle
#     circle(20,90)
# def rightu():
#     setheading(270)
#     circle(20,-90)       
def clickleft(x,y):
    penup()
def clickmiddle(x,y):
    color("grey")
def clickright(x,y):
    pendown()

def ccb():
    color("blue")
def ccg():
    color("green")
def ccr():
    color("red")
def ccbl():
    color("black")
def ccy():
    color("yellow")
def cco():
    color("orange")

listen()

#mouse keys
onscreenclick(clickleft, 1)
onscreenclick(clickmiddle, 2)     #1 is for left click button     #2 is for the middle click button
onscreenclick(clickright, 3)      #3 is for right click button

#colour changes
onkey(ccb, "b")
onkey(ccg, "g")
onkey(ccr, "r")
onkey(ccbl, "l")
onkey(ccy, "y")
onkey(cco, "o")


#movement
onkey(fr, "Up")
onkey(up, "w")
onkey(down, "s")
onkey(left, "a")
onkey(right, "d") 
onkey(uleftv, "q")
onkey(urightv, "e")
onkey(dleftv, "z")
onkey(drightv, "c")


mainloop()  

#done()    