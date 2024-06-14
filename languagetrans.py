from tkinter import *

# used for combobox
from tkinter import ttk

import gtts

from playsound import playsound

import googletrans

from googletrans import LANGUAGES,Translator

root= Tk()
root['bg']='white'

def trans():
    translator = Translator()
    translated=translator.translate(text=input.get(1.0,END),src=src_input.get(),dest=opt_lan.get())
    output.delete(1.0,END)
    output.insert(END,translated.text)
    
    def audio():
        print(googletrans.LANGUAGES)
a = gtts.gTTS("namste, kya hal chal hain",lang='hi')

a.save('myfile.mp3')
playsound("myfile.mp3")

frame= Frame(root,width=800,height=600,bg="brown")
frame.place(x=270,y=50)

l_title= Label(frame,text=" Language Translator",font="arial 25 bold underline",bg="brown",fg="white")
l_title.place(x=230,y=30)

# combo box:- for dropdown list in input :-
src_lan= list(LANGUAGES.values())
src_input=ttk.Combobox(frame,values=src_lan,width=30,font='arial 13 bold')
src_input.place(x=70,y=120)
src_input.set('choose input language')

#  for output:- 
lang= list(LANGUAGES.values())
opt_lan=ttk.Combobox(frame,values=lang,width=30,font='arial 13 bold')
opt_lan.place(x=450,y=120)
opt_lan.set('choose output language')


# typing text box for input:-
input = Text(frame,height=15,width=40)
input.place(x=60,y=220)

# typing text box for output:-
output = Text(frame,height=15,width=40)
output.place(x=430,y=220)

# button:-
btn=Button(frame,text="Translate",font="arial 10 bold",padx=10,pady=2,bd=6,background="black",fg="white",command=trans)
btn.place(x=360,y=500)

btn=Button(frame,text="Translate",font="arial 10 bold",padx=10,pady=2,bd=6,background="black",fg="white",command=trans)
btn.place(x=280,y=500)

mainloop()