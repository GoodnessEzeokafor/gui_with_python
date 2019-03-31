from tkinter import *
from tkinter import messagebox


class HelloApp:
    """
    A Simple Desktop App
    """


    def __init__(self, parent):
        #label
        self.label = Label(parent,text="Enter Name: ")
        self.label.grid(column=0, row=0)


        #input
        self.input = Entry(parent)
        self.input.grid(column=1, row=0)

        #butons
        self.greetbutton = Button(parent, text="Greet", command=self.greetbutton_func)
        self.nextbutton = Button(parent, text="Next", command=self.nextbutton_func)
        self.greetbutton.grid(column=2, row=0)
        self.nextbutton.grid(column=3, row=0)
    
    def greetbutton_func(self):
        messagebox.showinfo(message = "Hello " + self.input.get())
    
    def nextbutton_func(self):
        messagebox.showinfo("Next Button Was Clicked")
if __name__ == '__main__':
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
