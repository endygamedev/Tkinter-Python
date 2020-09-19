from tkinter import *

root = Tk()
root.title('Product List')

# Frames
frameButtons = Frame(root)
frameListBoxProducts = LabelFrame(root, text='Список покупок')
frameListBoxBought = LabelFrame(root, text='Купленные товары')
frameAdditionalButtons = Frame(root)

frameListBoxProducts.pack(side=LEFT, expand=1, fill=BOTH, padx=5,pady=5)
frameButtons.pack(side=LEFT)
frameAdditionalButtons.pack(side=RIGHT, padx=5)
frameListBoxBought.pack(side=RIGHT, expand=1, fill=BOTH,padx=5,pady=5)

products = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple', 'milk', 'tomato']

def btnProductsBought_Event(_listBoxGet, _listBoxInsert):
    select = list(_listBoxGet.curselection())
    select.reverse()
    for i in select:
        _listBoxInsert.insert(END,_listBoxGet.get(i))
        _listBoxGet.delete(i)

def btnAdd_Event():
    try:
        if entryProductName.get()!= '':
            listBoxProducts.insert(END,entryProductName.get())
            entryProductName.delete(0,END)
    except:
        None

def btnDelete_Event():
    select = list(listBoxProducts.curselection())
    select.reverse()
    for i in select:
        listBoxProducts.delete(i)

# ListBoxes
listBoxProducts = Listbox(frameListBoxProducts, selectmode=EXTENDED)
listBoxProducts.pack(side=LEFT, expand=1, fill=BOTH)
scrollListBoxProducts = Scrollbar(frameListBoxProducts, command = listBoxProducts.yview)
scrollListBoxProducts.pack(side=RIGHT, fill=Y)
listBoxProducts.config(yscrollcommand=scrollListBoxProducts.set)

listBoxBoughtProducts = Listbox(frameListBoxBought, selectmode=EXTENDED)
listBoxBoughtProducts.pack(side=LEFT, expand=1, fill=BOTH)
scrollListBoxBought = Scrollbar(frameListBoxBought, command = listBoxBoughtProducts.yview)
scrollListBoxBought.pack(side=RIGHT, fill=Y, anchor=E)
listBoxBoughtProducts.config(yscrollcommand=scrollListBoxBought.set)

# Buttons Frame
btnBougth = Button(frameButtons, text='>>>', width=3, height=1, command=lambda: btnProductsBought_Event(listBoxProducts,listBoxBoughtProducts))
btnBougth.pack()
btnProducts = Button(frameButtons, text='<<<', width=3, height=1, command=lambda: btnProductsBought_Event(listBoxBoughtProducts,listBoxProducts))
btnProducts.pack()

# Additional Frame
entryProductName = Entry(frameAdditionalButtons, width=23)
entryProductName.pack()
btnAdd = Button(frameAdditionalButtons, text='Добавить новый товар', command=btnAdd_Event)
btnAdd.pack()
btnDelete = Button(frameAdditionalButtons, text='Удалить товар', command=btnDelete_Event)
btnDelete.pack()


for i in products:
    listBoxProducts.insert(END,i)

root.mainloop()
