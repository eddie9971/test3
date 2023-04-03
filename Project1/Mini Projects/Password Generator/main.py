from tkinter import *
from tkinter import messagebox
import random
import string
import json

# Saving data to txt file


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Warning', message='Please fill all fields.')
    else:
        is_ok = messagebox.askokcancel(title='Website', message=f'Email: {email}\n'
                                                        f'Password: {password}\n'
                                                        f'Proceed to save?')
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def save_json():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    stored_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Warning', message='Please fill all fields.')
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(stored_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(stored_data)

            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            info = data[website]
            messagebox.showinfo(title=website, message=f'Email: {info["email"]}\nPassword: {info["password"]}')
    except KeyError:
        messagebox.showinfo(title='Error', message=f'No record found!')


def password_generator():
    total = string.ascii_letters + string.digits + string.punctuation
    length = 16
    password = ''.join(random.sample(total, length))
    password_entry.insert(0, password)


window = Tk()
window.title('Password Manager')
window.config(padx=200, pady=200)
# Labels
name_label = Label(text='Password Generator', font=("Arial", 36, 'normal'))
website_label = Label(text='Website')
email_label = Label(text='Email/Username')
password_label = Label(text='Password')
name_label.grid(row=0, column=1)
website_label.grid(row=1,column=0)
email_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)
# Entries
website_entry = Entry(width=50)
email_entry = Entry(width=50)
password_entry = Entry(width=32)
website_entry.grid(row=1,column=1, columnspan=2)
email_entry.grid(row=2,column=1, columnspan=2)
password_entry.grid(row=3,column=1)
website_entry.focus() # so can start typing on the first entry without click
email_entry.insert(0,'Eddie.CHL@outlook.com') # Starting value set up
# Button
generate_password_button = Button(text='Generate Password',command=password_generator)
add_button = Button(text='Add',width=36, command=save_json)
generate_password_button.grid(row=3,column=2)
add_button.grid(row=4,column=1,columnspan=2)
search_button = Button(text='Search', command=search)
search_button.grid(row=1,column=2)

window.mainloop()
