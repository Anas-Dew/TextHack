from ast import Import
import hashlib
from tkinter import *
from cgitb import text
from turtle import color
import pyperclip as pc


# INITALIZATION HERE
root = Tk()
# root.geometry("700x350")
root.title("Text Hack - Do more with texts")
operator = ""
text_Input = StringVar()
find_input = StringVar()
text_display = Entry(root, font=('serif', 17), textvariable=text_Input, bd=8, width=37, cursor="plus", insertwidth=5,
                     bg="white", justify='left').grid(row=0, columnspan=6)

# find = Entry(root,font=('serif', 17),textvariable=find_input,bd=8, width=5,cursor="plus", insertwidth=5,
#                      bg="white", justify='left').grid(row=1,column=0, columnspan=6)
# reple = Entry(root,font=('serif', 17),textvariable=find_input,bd=8, width=5,cursor="plus", insertwidth=5,
#                      bg="white", justify='left').grid(row=1,column=1, columnspan=6)



# TITLE UPDATING HERE


def word_details(event):

    global operator
    operator = text_Input.get()
    words = str(len(operator.split()))
    charecters = str(len(operator))
    title_masala = "Text Hack - Do more with texts - " + \
        words+" Words and "+charecters+" Charecters"
    root.title(title_masala)


root.bind('<space>', word_details)
root.bind('<BackSpace>', word_details)

# BUTTONS HERE WITH THIER RESPECTIVE FUNCTIONS


def btnclickup():
    global operator
    operator = text_Input.get()
    text_Input.set(operator.upper())


Uppercase_button = Button(root, padx=14, pady=8, font=('serif', 10), bg="grey", text=(
    "Uppercase"), command=lambda: btnclickup()).grid(row=2, column=0)


def btnclicklow():
    global operator
    operator = text_Input.get()
    text_Input.set(operator.lower())


Lowercase_button = Button(root, padx=14, pady=8, font=('serif', 10), bg="grey", text=(
    "Lowercase"), command=lambda: btnclicklow()).grid(row=2, column=1)


def btnclickcopy():
    global operator
    operator = text_Input.get()
    pc.copy(operator)


Copy_button = Button(root, padx=14, pady=8, font=('serif', 10), bg="grey", text=(
    "Copy"), command=lambda: btnclickcopy()).grid(row=2, column=2)


def btnclickpaste():
    text_Input.set(pc.paste())
    word_details(None)


Paste_button = Button(root, padx=14, pady=8, font=('serif', 10), bg="grey", text=(
    "Paste"), command=lambda: btnclickpaste()).grid(row=2, column=3)


def btnclickENC():
    global operator
    operator = text_Input.get()
    if operator == "":
        pass
    else:

        operator = hashlib.md5(operator.encode())
        text_Input.set(operator.hexdigest())
        word_details(None)

Encrpyt_button = Button(root, padx=14, pady=8, font=('serif', 10), bg="grey", text=(
    "Encrypt MD5"), command=lambda: btnclickENC()).grid(row=2, column=4)


def btnclickclear():
    global operator
    operator = ""
    text_Input.set("")
    word_details(None)

clear_button = Button(root, padx=14, pady=8, font=('serif', 10), bg="dark red", text=(
    "Clear"), command=lambda: btnclickclear()).grid(row=2, column=5)


def btnclickstd():  # UNDER DEVELOPED !!!
    global operator
    operator = text_Input.get()
    dot = "."
    res = [i for i in range(len(operator)) if operator.startswith(dot, i)]
    for dots in range(operator.count(dot)):
        replaced = operator[res[dots]+1]
        new = replaced.capitalize()
        out = ["'new'"]
        out = list(eval('+'.join(out)))
        for resa in range(len(res)):
            operator = operator.replace(operator[res[dots]+1], new)
    text_Input.set(operator)
    

#Std_button = Button(root,padx=14,pady=8,font=('serif',10),bg="grey",text=("Standard Case"),command=lambda:btnclickstd()).grid(row=3,column=0)



root.mainloop()
