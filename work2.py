from tkinter import *
# from tkmessageBox import *
from tkinter import messagebox

class HelloWorld:
    """
    A hello World App With a callback
    """
    def __init__(self, parent):
        self.hello_button = Button(parent, text="Hello", command=self.say_hi)
        self.hello_button.grid(column=0, row=0)
        self.quit_button = Button(parent, text = "Quit", command=parent.destroy)
        self.quit_button.grid(column=1, row=0)
        self.greet_button = Button(parent, text = "Greet", command=self.greet) 
        self.greet_button.grid(column=3, row=0)
        self.next_button = Button(parent, text="Next",command=self.next)
        self.next_button.grid(column=0, row=1)

        #user input
        self.input = Entry(parent)
        self.input.grid(column=1, row=1)
        self.label = Label(parent, text="Enter your name: ")
        self.label.grid(column=0, row=2)
        
    def say_hi(self):
        messagebox.showinfo(message='hi There!!!')
    def greet(self):
        messagebox.showinfo(message="How Are You!!")
    
    def next(self):
        messagebox.showinfo(message="Next Button Was Clicked")


if __name__ == '__main__':
    root = Tk()
    app = HelloWorld(root)
    root.mainloop()
