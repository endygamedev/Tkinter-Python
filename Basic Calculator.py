from tkinter import *

root = Tk()
frame_=Frame(root)

entryFirst_ = Entry(root, width=21)
entrySecond_ = Entry(root, width=21)
buttonPlus_ = Button(frame_, text="+", bg='blue', width=2, activebackground="#ea00ff")
buttonMinus_ = Button(frame_, text="-", bg='red', width=2, activebackground="#ea00ff")
buttonMulty_ = Button(frame_, text="*", bg='green', width=2, activebackground="#ea00ff")
buttonDiv_ = Button(frame_, text="/", bg='yellow', width=2, activebackground="#ea00ff")
label_ = Label(root, bg='black', fg='white', width=21, font = "Cambria 14 underline")

def noneFunction(event):
    num1 = 0
    num2 = 0
    res = 0
    label_['text'] = ""

def plusFunction(event):
    noneFunction
    num1 = int(entryFirst_.get())
    num2 = int(entrySecond_.get())
    res = num1 + num2
    label_['text'] = res

def minusFunction(event):
    noneFunction
    num1 = int(entryFirst_.get())
    num2 = int(entrySecond_.get())
    res = num1 - num2
    label_['text'] = res

def multyFunction(event):
    noneFunction
    num1 = int(entryFirst_.get())
    num2 = int(entrySecond_.get())
    res = num1 * num2
    label_['text'] = res

def divideFunction(event):
    noneFunction
    num1 = int(entryFirst_.get())
    num2 = int(entrySecond_.get())
    res = num1 / num2
    label_['text'] = res

root.title("Calculator")
root.geometry('260x120')

buttonPlus_.bind('<Button-1>', plusFunction)
buttonMinus_.bind('<Button-1>', minusFunction)
buttonMulty_.bind('<Button-1>', multyFunction)
buttonDiv_.bind('<Button-1>', divideFunction)

entryFirst_.pack()
entrySecond_.pack()
frame_.pack()
buttonPlus_.pack(side=LEFT)
buttonMinus_.pack(side=LEFT)
buttonMulty_.pack(side=LEFT)
buttonDiv_.pack(side=LEFT)
label_.pack()

root.mainloop()