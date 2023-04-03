from tkinter import *



def button_clicked():
    print('Hello World')
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk() # initialize new object using TK class
window.title('First GUI Program')
window.minsize(width=500, height=500)

# Label
my_label = Label(text='This is a Label', font=('Arial', 24, 'bold'))
# layout the component, place in the screen
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
# Alternative ways to change properties
# my_label['text'] = 'new text'
# my_label.config(text='new text')

# Button
button = Button(text='Click me',command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
input.grid(column=2, row=2)

window.mainloop()
