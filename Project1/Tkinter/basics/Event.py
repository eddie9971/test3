from tkinter import  *

root = Tk();root.geometry('530x300')

c1 = Canvas(root,width=200,height=200,bg='green')
c1.pack()


def mouseTest(event):
    print(f'Left click location(Relative to Widget):{event.x}, {event.y}')
    print(f'Left click location(on screen):{event.x_root}, {event.y_root}')
    print(f'Event binding widget: {event.widget}')


def testDrag(event):
    c1.create_oval(event.x,event.y,event.x+1,event.y+1)


def keyboardTest(event):
    print(f'keycode: {event.keycode} char: {event.char} Keysym:{event.keysym}')


def press_a_test(event):
    print('press a')


def releaseAtest(event):
    print('release a')

c1.bind('<Button-1>', mouseTest)
c1.bind('<B1-Motion>', testDrag)

root.bind('<KeyPress>', keyboardTest)
root.bind('<KeyPress-a>', press_a_test)
root.bind('<KeyRelease-a>', releaseAtest)


root.mainloop()