from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.bt01 = Button(self, text='ioiejrg')
        # self.bt01['text'] = 'click for flowers'
        self.bt01.pack()
        self.bt01['command'] = self.flower
        self.btquit = Button(self, text='QUIT', command=root.destroy)
        self.btquit.pack()

    def flower(self):
        messagebox.showinfo('Send Flower','✿✿✿✿✿✿✿✿✿✿✿')


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x100+200+300')
    root.title('Class GUI')
    app = Application(master=root)
    root.mainloop()