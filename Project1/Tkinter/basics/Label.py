#fg:foreground bg:background justify: 对齐方式 left center right
from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text = 'programmer', width=10,height=2,
                             bg='black', fg='white', font=('calibri',12))
        self.label01.pack()
        self.label02 = Label(self, text = 'pycharmpycharmpycharmpycharmpycharm', width=30,height=2,
                             bg='black', fg='white', font=('calibri',12))
        self.label02.pack()
        #display image
        global photo
        # 把photo变成全局变量，如果是局部变量，method执行支行，图像对象销毁，因为mainloop一直循环
        photo = PhotoImage(file='')
        self.label03 = Label(self, image=photo)
        self.label03.pack()
        #多行文本
        self.label04 = Label(self, text='awefaawefawefawefwef\nawefawef\nawefawef\nawefawef',
                             borderwidth=1,relief='solid', justify='left')#borderwidth边界，relief边界效果
        self.label04.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x400+200+300')
    app = Application(master=root)
    root.mainloop()