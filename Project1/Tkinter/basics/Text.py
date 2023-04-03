from tkinter import *
from tkinter import messagebox
import webbrowser


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.w1 = Text(root, width=40, height=12, bg='gray')
        self.w1.pack()
        self.w1.insert(1.0,'aeorigjaoeirjgh\naergaoerjig') #1.0 第一行第0列
        self.w1.insert(2.3,'034953840304985\n23049230498')

        Button(self, text='Insert text', command=self.insertText).pack(side='left')
        Button(self, text='Return text', command=self.returnText).pack(side='left')
        Button(self, text='Add Image', command=self.addImage).pack(side='left')
        Button(self, text='Add Widget', command=self.addWidget).pack(side='left')
        Button(self, text='Delete All', command=self.Deleteall).pack(side='left')
        # Button(self, text='test tag', command=self.testtag).pack(side='left')
    def insertText(self):
        #Insert表示在光标处插入
        self.w1.insert(INSERT, 'aaaaa')
        #END表示在最后插入
        self.w1.insert(END,'sererg')

    def returnText(self):
        print(f'All text: {self.w1.get(1.0, END)}')

    def addImage(self):
        self.photo = PhotoImage(file='')
        self.w1.image_create(INSERT, image=self.photo)

    def addWidget(self):
        b1 = Button(self.w1,text='123123',command=self.webshow())
        self.w1.window_create(INSERT,window=b1)

    # def testtag(self):
    #     self.w1.tag_add('Bing', 4.0, 4.2)
    #     self.w1.tag_config('Bing', underline=True)
    #     self.w1.tag_bind('Bing', self.webshow)
    #
    def webshow(self):
        webbrowser.open('https://cn.bing.com/')

    def Deleteall(self):
        self.w1.delete(1.0, END)

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x400+200+300')
    app = Application(master=root)
    root.mainloop()