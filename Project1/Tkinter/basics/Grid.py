from tkinter import *
from tkinter import messagebox



class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self,text='User Name')
        self.label01.grid(row=0, column=0)
        self.entry01 = Entry(self)
        self.entry01.grid(row=0,column=1)
        Label(self, text='User name is phone number').grid(row=0,column=2)

        Label(self,text='Password').grid(row=1,column=0)
        Entry(self, show='*').grid(row=1,column=1)

        Button(self, text='Login').grid(row=2,column=1,sticky=EW)
        Button(self,text='Cancel').grid(row=2,column=2,sticky=EW)

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x400+200+300')
    app = Application(master=root)
    root.mainloop()