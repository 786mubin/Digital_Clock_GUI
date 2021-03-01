# getting time
import datetime

from tkinter import *

root=Tk()
root.title("Digital Clock")

def times():
    obj=datetime.datetime.now()
    time=obj.strftime("%r")
    label.config(text=time)
    label.after(1000, times)
    return time

label=Label(root,font=("ds-digital", 80), background="black", foreground="cyan" )
label.pack(anchor="center")
times()
mainloop()

