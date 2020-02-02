from tkinter import *

root = Tk()
root.title('Text Editor')

menuFrame = Frame(root, bg='lightgreen')

lable = Label(menuFrame, bg='lightgreen',text='Введите имя файла с расширением: ')
lable.pack(side=LEFT, padx=5)

entry = Entry(menuFrame, width=25)
entry.pack(side=LEFT, padx=5)

btnOpen = Button(menuFrame, text='Открыть',width=10)
btnOpen.pack(side=LEFT)
btnSave = Button(menuFrame, text='Сохранить',width=10)
btnSave.pack(side=LEFT)

menuFrame.pack(padx=5,pady=5)

scrollBarX = Scrollbar(orient=HORIZONTAL)
scrollBarX.pack(side=BOTTOM, fill=X, anchor=W)

scrollBarY = Scrollbar(orient=VERTICAL)
scrollBarY.pack(side=RIGHT, fill=Y)

textBox = Text(yscrollcommand=scrollBarY.set, xscrollcommand=scrollBarX.set, wrap=WORD)
textBox.pack(side=LEFT, expand=1, fill=BOTH)

scrollBarX.config(command=textBox.xview)
scrollBarY.config(command=textBox.yview)

def btnOpen_Event():
    adress = entry.get()
    try:
        if(adress != None):
            textBox.delete(1.0, END)
            for i in open(adress):
                textBox.insert(END,i)
    except:
        textBox.delete(1.0,END)
        textBox.insert(1.0, 'Файла с таким именем не найдено в данной директории! :(')

def btnSave_Event():
    adress = entry.get()
    try:
        if(adress != None):
            text = textBox.get(1.0, END)
            file = open(adress,'w')
            file.writelines(text)
            file.close()
            textBox.delete(1.0, END)
    except:
        textBox.delete(1.0,END)
        textBox.insert(1.0, 'Файла с таким именем не найдено в данной директории! :(')

btnOpen.config(command=btnOpen_Event)
btnSave.config(command=btnSave_Event)

root.mainloop()