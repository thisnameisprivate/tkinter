from tkinter import *

root = Tk()
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)
listb2 = Listbox(root)
for item in li:
    listb.insert(0, item)

for item in movie:
    listb2.insert(0, item)

listb.pack()
listb2.pack()
root.mainloop()