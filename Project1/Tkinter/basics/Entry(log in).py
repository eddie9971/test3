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
        self.label01.pack()
        #StringVar变量绑定到指定组件
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set('admin')

        #Create input for password
        self.label02 = Label(self,text='Password')
        self.label02.pack()
        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2,show='*')
        self.entry02.pack()

        self.bt01 = Button(self, text='Login', command=self.login)
        self.bt01.pack()

    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()
        print(f'User Name: {self.entry01.get()}')
        print(f'Password: {self.entry02.get()}')
        if username == 'eddie' and pwd == '915179699':
            messagebox.showinfo('System', 'Logged In!')
        else:
            messagebox.showinfo('System', 'Failed to Log In')


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x400+200+300')
    app = Application(master=root)
    root.mainloop()