from tkinter import *


class TempConverter:
    """
    A Simple App for conerting from Fahrenheit to Celsius
    """

    def __init__(self, parent):
        self.celsius_val = Label(parent, text="", width=20)
        self.celsius_val.grid(column=1, row=1)
        self.celsius_label  = Label(parent, text="Celsius", width=20)
        self.celsius_label.grid(column=1, row=0)

        self.fahr_input = Entry(parent)
        self.fahr_input.grid(column=0, row=1)
        self.fahr_label = Label(parent, text="Fahrenheit")
        self.fahr_label.grid(column=0, row=0)

        self.convert_button = Button(parent, text="Convert", command=self.convert)
        self.convert_button.grid(row=2, column=0)


        self.quit_button = Button(parent, text="Quit", command=parent.destroy)
        self.quit_button.grid(row=2, column=1)

    def convert(self):
        # get the fahr alie from the widget and convert it from 
        # a string to a float number
        dfahr = float(self.fahr_input.get())
        #calcularte the celsius the ceslsius value as 
        # a float
        celsius = (dfahr - 32) * 5.0/9.0
        #update the celsius widget with the celsius value
        #by
        #convertinf from a float to a string
        self.celsius_val.configure(text=str(celsius))
if __name__ == '__main__':
    root = Tk()
    app = TempConverter(root)
    root.mainloop()

