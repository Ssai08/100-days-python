# def add(*numbers):
#     total = 0
#     for val in numbers:
#         total += val
#     return total
#
#
# print(add(1,2,3,4,5))

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=2)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
