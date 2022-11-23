# Import the required libraries
from tkinter import *
import time

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x350")

# Make the window size fixed
win.resizable(False,False)

# Create a canvas widget
canvas=Canvas(win, width=700, height=350)
canvas.pack()

# Create an oval or ball in the canvas widget
ball1=canvas.create_oval(10,10,50,50, fill="red3")
ball2=canvas.create_oval(10,10,50,50, fill="blue3")
ball3=canvas.create_oval(10,10,50,50, fill="green3")

# Move the ball

def move_ball2():
   xspeed = 5
   yspeed = 0
   canvas.move(ball2, xspeed, yspeed)
   (leftpos, toppos, rightpos, bottompos)=canvas.coords(ball2)
   if rightpos>=700:
      xspeed=0

   canvas.after(30,move_ball2)
   
def move_ball():
   xspeed=3
   yspeed=0

   canvas.move(ball1, xspeed, yspeed)
   (leftpos, toppos, rightpos, bottompos)=canvas.coords(ball1)
   if rightpos>=700:
      xspeed=0
   canvas.after(30,move_ball)

canvas.after(30, move_ball)
canvas.after(166, move_ball2)

win.mainloop()