from tkinter import *

root = Tk()
root.title('Rainbow')
f_button = Frame(root)

hex = ['#ff0000','#ff7d00','#ffff00','#00ff00','#007dff', '#0000ff', '#7d00ff']
colors= ['красный', 'оранжевый', 'жёлтый', 'зелёный', 'голубой', 'синий', 'фиолетовый']
buttons = []

def buttonColotEvent(color, hex):
    entry.delete(0, END)
    entry.insert(0, hex)
    entry.config(bg = hex)
    label.config(text = color)

label = Label(root, text = 'Цвет', width = 20)
label.pack(padx = 5, pady = 5)

entry = Entry(root, text = "HEX цвета", width = 20)
entry.pack()

f_button.pack(padx = 5, pady = 5)

for i in range(7):
    buttons.append(Button(f_button, bg = hex[i], activebackground = hex[i], width = 1, height = 1, command = lambda index = i: buttonColotEvent(f_button, colors[index], hex[index])))
    buttons[i].pack(side = LEFT)

root.mainloop()
