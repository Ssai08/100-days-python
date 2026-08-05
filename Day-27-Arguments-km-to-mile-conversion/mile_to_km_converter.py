from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(height=100,width=300)
window.config(padx=30,pady=10)

inp = Entry(width=10)
inp.grid(row=0, column=1)

def button_clicked():
    mile_val = float(inp.get())
    km_val = round(mile_val * 1.609344,2)
    km_value.config(text=km_val)

miles_label = Label(text="Miles",font=("Arial",14,"bold"))
miles_label.grid(row=0,  column=2)

equals_label = Label(text="is equal to ",font=("Arial",14,"bold"))
equals_label.grid(row=1,  column=0)

button = Button(text="Calculate",command=button_clicked)
button.grid(row=2,column=1)

km_value = Label(text="0",font=("Arial",14,"bold"))
km_value.grid(row=1,  column=1)

km_label = Label(text="KM",font=("Arial",14,"bold"))
km_label.grid(row=1,  column=2)


window.mainloop()