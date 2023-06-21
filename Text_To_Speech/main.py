from tkinter import *
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()
win=Tk()
win.title("Text-to-Speech")
win.configure(bg="orange")
win.geometry("500x250")

def speak():
    t=entry1.get()
    engine.say(t)
    engine.runAndWait()
    engine.stop()
    if(t==""):
        messagebox.showerror("Error","Please enter the text")

# Label Frame

lf=LabelFrame(win,text="Text to Speech",font="30" ,bd=5,bg="green")
lf.pack(fill="both",expand="yes",padx=10,pady=10)

Label(lf,text="Text",font="30",padx=15).pack(side=LEFT)

# Entry Widget (User enter his text)

text=StringVar()
entry1=Entry(lf,width=25,bd=5,font=20,textvariable=text)
entry1.pack(side=LEFT,padx=10)

# Button

Button(lf,text="Speech",font=15,command=speak).pack(side=LEFT)
mainloop()