from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
        self.widget2()
    def createWidget(self):
        self.v = StringVar()
        self.v.set('F') #default choice

        self.r1 = Radiobutton(self, text='Male', value='M', variable=self.v)
        self.r2 = Radiobutton(self, text='Female', value='F', variable=self.v)

        self.r1.pack(side='left');self.r2.pack(side='left')
        Button(self, text='Enter', command=self.confirm).pack(side='left')

    def confirm(self):
        messagebox.showinfo('Message',f'Gender: {self.v.get()}')

    def widget2(self):
        self.codehobby = IntVar()
        self.videohobby = IntVar()

        self.c1 = Checkbutton(self, text='Coding', variable=self.codehobby,
                              onvalue=1, offvalue=0)
        self.c2 = Checkbutton(self, text='Watch Video', variable=self.videohobby,
                              onvalue=1, offvalue=0)
        self.c1.pack(side='left');self.c2.pack(side='left')
        Button(self, text='Enter', command=self.confirm2).pack(side='left')

    def confirm2(self):
        if self.codehobby.get() == 1:
            messagebox.showinfo('Message', 'Everyone likes coding')
        if self.videohobby.get() == 1:
            messagebox.showinfo('Message','YOUTUBE')

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x400+200+300')
    app = Application(master=root)
    root.mainloop()