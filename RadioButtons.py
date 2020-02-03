from tkinter import *

root = Tk()
root.title('RadioButtons')

frameButtons = Frame(root)

rVar = IntVar()
rVar.set(0)

def changeHero():
    if rVar.get() == 0:
        label.config(text='+79532206981')
    elif rVar.get() == 1:
        label.config(text='+79222003943')
    elif rVar.get() == 2:
        label.config(text='+79111954567')

btnVasya = Radiobutton(frameButtons, text='Вася', width=15, height=3, indicatoron=0, variable=rVar, value=0, command=changeHero)
btnVasya.pack(side=BOTTOM)
btnPetya = Radiobutton(frameButtons, text='Петя', width=15, height=3, indicatoron=0, variable=rVar, value=1, command=changeHero)
btnPetya.pack(side=BOTTOM)
btnMasha = Radiobutton(frameButtons, text='Маша', width=15, height=3, indicatoron=0, variable=rVar, value=2, command=changeHero)
btnMasha.pack(side=BOTTOM)

label = Label(bg='white',width=30, height=12, font='Cambria 16')
label.pack(side=RIGHT,fill=BOTH, expand=1)

frameButtons.pack(side=LEFT)

root.mainloop()