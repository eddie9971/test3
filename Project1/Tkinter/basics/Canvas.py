from tkinter import *
from tkinter import messagebox
import random


# noinspection PyTypeChecker
class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.canvas = Canvas(self, width=300, height=200, bg='green')
        self.canvas.pack()
        # draw straight line
        line = self.canvas.create_line(10, 10, 30, 20, 40, 50) # three set of coordinate(10,10)(30,20)
        # draw rectangle
        rect = self.canvas.create_rectangle(50,50,100,100) # coordinate (50,50)(100,100)
        # draw oval
        oval = self.canvas.create_oval(50,50,100,100)

        global photo
        photo = PhotoImage(file='')
        self.canvas.create_image(150, 170, image=photo)

        Button(self, text='Draw', command=self.draw).pack(side='left')

    def draw(self):
        for i in range (10):
            x1 = random.randrange(int(self.canvas['width'])/2)
            y1 = random.randrange(int(self.canvas['heigh']) / 2)
            x2 = random.randrange(int(self.canvas['width']) / 2)
            y2 = random.randrange(int(self.canvas['height']) / 2)
            self.canvas.create_rectangle(x1,y1,x2,y2)


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x400+200+300')
    app = Application(master=root)
    root.mainloop()