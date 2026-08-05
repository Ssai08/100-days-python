from tkinter import *

window = Tk()
window.title("My Window")
window.minsize(height=500,width=700)
window.config(padx=100,pady=100)

# Label
my_label = Label(text="Hello",font=("Arial",40,"bold"))
my_label.grid(row=0,  column=0)
'''
There are 3 ways to show the objects on the screen
1. pack() # can label things one after another.
2. place() # needs co-ordinate where the object is required. Eg: (0,0)/(200,300)
3. grid() # divides the screen to required number of columns and rows depending upon the number of objects defined. 
        :parameters are row=0,column=0
'''

#changing the text of the label
my_label["text"] = "I'm new label"
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label.config(text="Button Got Clicked!")
    my_label.config(text=inp.get())
    print(inp.get())

button = Button(text="Click Me",command=button_clicked)
button.grid(row=1,column=1)
button2 = Button(text="New Button",command=button_clicked)
button2.grid(row=0,column=3)

#Entry

inp = Entry(width=10)
print(inp.get())
inp.grid(row=3, column=4)


window.mainloop()