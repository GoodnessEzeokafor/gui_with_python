from tkinter import *
class HelloWorld:
    """ A Helo World App"""
    def __init__(self, parent):
        self.label = Label(parent, text="Hello World")
        self.label.grid(column=1, row=10)


if __name__ == '__main__':
    root = Tk()
    # create the application
    app = HelloWorld(root)
    root.mainloop()
    
'''
class EventLoop:
    """
    A non-gui simulated event loop class
    """
    def __init__(self):
        self.text = ""


    def draw_screen(self):
        for i in range(10):
            print()
        print(self.text)

    def get_event(self):
        return input()

    def process_event(self, event):
        if(event == 'quit'):
            quit()
        elif (event == "hello"):
            self.text = "Hello to you too"
        elif (event == "Goodbye"):
            self.text = "Goodbye"
            self.draw_screen()
            self.process_event("quit")
        else:
            self.text = "I don't know that event"


    def mainloop(self):
        # start the event loop
        while True:
            event = self.get_event()
            self.process_event(event)
            self.draw_screen()



if __name__ == '__main__':
    event = EventLoop()
    event.mainloop()
    # # print(event)


'''

