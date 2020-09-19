from tkinter import *

root = Tk()
root.title('Events')
menuFrame = Frame(root)

def changeTextBoxSize(event):
    try:
        if entryHeight.get() != '' and entryWidth.get() != '':
            textBox.config(height=entryHeight.get(), width=entryWidth.get())
    except Exception as e:
        print(e)

def changeTextBoxBg(event, color):
    textBox.config(bg=color)

entryWidth = Entry(menuFrame, width=3)
entryHeight = Entry(menuFrame, width=3)
button = Button(menuFrame,text='Изменить')
textBox = Text(bg='lightgrey')

menuFrame.pack()
button.pack(side=RIGHT, padx=5)
entryWidth.pack(side=BOTTOM)
entryHeight.pack(side=BOTTOM)
textBox.pack(fill=BOTH, pady=5)

button.bind('<Button-1>', changeTextBoxSize) #ЛКМ
entryWidth.bind('<Return>', changeTextBoxSize) #Enter
entryHeight.bind('<Return>', changeTextBoxSize) #Enter

textBox.bind('<FocusIn>', lambda event, color='white': changeTextBoxBg(event, color))
textBox.bind('<FocusOut>', lambda event, color='lightgrey': changeTextBoxBg(event, color))

root.mainloop()
