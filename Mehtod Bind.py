from tkinter import *

root = Tk()
root.title('Method Bind')
root.geometry('150x200')

projectsArray = ['Basic Calculator.py', 'Products ListBox.py', 'RadioButtons.py', 'Rainbow Buttons.py', 'TextEditor.py']

entry = Entry(root, width=20)
entry.pack(padx=5, pady=5)
listBox = Listbox(root, height=20)
listBox.pack(padx=5,pady=5, expand=1,fill=BOTH)
scrollBar = Scrollbar(listBox, command=listBox.yview)
scrollBar.pack(side=RIGHT, fill=Y)
listBox.config(yscrollcommand=scrollBar.set)

for i in projectsArray:
    listBox.insert(END, i)

def enter_event(event):
    listBox.insert(END, entry.get())
    entry.delete(0, END)

def copy_event(event):
    entry.delete(0, END)
    select = list(listBox.curselection())
    entry.insert(0, listBox.get(select))

def delete_event(event):
    select = list(listBox.curselection())
    listBox.delete(select)

entry.bind('<Return>', enter_event) # Enter
listBox.bind('<Double-Button-1>', copy_event) # Double Click ЛКМ
listBox.bind('<Double-Button-3>', delete_event) # Double Click ПКМ

root.mainloop()