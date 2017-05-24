import tkinter as tk

from struct import pack

root = tk.Tk()
choices = ('network one', 'network two', 'network three')
lb1 = tk.Listbox(root)
lb1.insert(1,*choices)
lb1.pack()
table = ('one', 'two', 'three')
def clean():
    # Reset var and delete all old options
    #for choices in lb1:
    lb1.delete(0, tk.END)
    #lb1.pack()
    #lb1.delete(i,len(lb1))

def insert(itemToInsert):

    # Insert list of new options (tk._setit hooks them up to var)
    #itemToInsert= ('one', 'two', 'three')
    for item in itemToInsert:
       lb1.insert(tk.END,item)

def mutate():
    pass
# I made this quick refresh button to demonstrate
tk.Button(root, text='Clean', command=clean).pack()
tk.Button(root, text = 'Insert',command=lambda: insert(table)).pack()
tk.Button(root, text = 'Mutate', command=clean).pack()

root.mainloop()