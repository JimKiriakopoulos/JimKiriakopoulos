from tkinter import *
from api import d,h
import Person as greeting


def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return motion

a=greeting.Person["name"]
m=greeting.Person["age"]

master = Tk()
whatever_you_do = h,d,a,m
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 100, 'italic'))
msg.bind('<Motion>',motion)
msg.pack()
mainloop()
