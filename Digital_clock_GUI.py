# getting time
import datetime

from tkinter import *

root=Tk()
root.title("Digital Clock")

def times():
    obj=datetime.datetime.now()
    time=obj.strftime('%H : %M : %S : %p')
    label.config(text=time)
    label.after(1000, times)
    return time

# Label(root, text="Welcome to the digital clock").pack()
label=Label(root,font=("ds-digital", 80), background="black", foreground="cyan" )
label.pack(anchor="center")
times()
mainloop()

