import tkinter 
from tkinter import scrolledtext
from tkinter import filedialog

class TextEdit:
    """
    A simple text editor using a ScrolledText widet
    """
    def __init__(self, parent):
        self.parent = parent
        self.textWidget = scrolledtext.ScrolledText(parent, width=80, height=50)
        self.textWidget.pack()


        self.menuBar = tkinter.Menu(parent, tearoff=0)
        self.fileMenu = tkinter.Menu(self.menuBar,tearoff=0)
        self.fileMenu.add_command(label="Open", command=self.open_command)
        self.fileMenu.add_command(label="Save", command=self.save_command)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Quit", command=self.exit_program)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        parent.config(menu=self.menuBar)


    def open_command(self):
        file = filedialog.askopenfile()
        if file != None:
            contents = file.read()
            self.textWidget.delete("1.0", tkinter.END)
            self.textWidget.insert(tkinter.END, contents)
    def save_command(self):
        file = filedialog.asksaveasfile()
        if file != None:
            #slice off the ast character from get
            # as an extra return is added
            contents = self.textWidget.get("1.0", tkinter.END)[:-1]
            file.write(contents)
            file.close()
    
    def exit_program(self):
        self.parent.destroy()
if __name__ == '__main__':
    root = tkinter.Tk()
    textApp = TextEdit(root)
    root.mainloop()