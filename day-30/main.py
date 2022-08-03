import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_produce():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number = range(0, 10)
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    nr_letters = 6
    nr_symbol = 2
    nr_numbers = 3
    letters_final = []
    letters_final = [random.choice(letters) for _ in
                     range(0, nr_letters)]
    letters_final += [random.choice(number) for item in
                      range(0, nr_numbers)]  # item not care
    letters_final += [random.choice(symbols) for item in
                      range(0, nr_symbol)]
    random.shuffle(letters_final)
    return ''.join(map(str,
                       letters_final))  # use map  beacause  int convert to str


def pass_gen():
    password_i.delete(0, END)
    password_i.insert(0, password_produce())
    pyperclip.copy(password_i.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_i.get()
    email = email_i.get()
    password = password_i.get()
    data_json = {website: {"Email": email, "Password": password}}
    if website and email and password:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"these are details entered : website:{website}\n Email:{email} \n Password : {password} \n is it ok for save ?")
        if is_ok:
            try:
                with open("./data-pass.json", mode="r") as pass_list:
                    data = json.load(pass_list)
                    data.update(data_json)
            except FileNotFoundError:
                with open("./data-pass.json", mode="w") as pass_list:
                    json.dump(data_json,pass_list)
            else:
                with open("./data-pass.json", mode="w") as pass_list_r:
                    json.dump(data, pass_list_r, indent=4)
            finally:
                website_i.delete(0, END)
                password_i.delete(0, END)
    else:
        messagebox.showinfo(title="warning",
                            message="please make sure haven't left any field empty !")


# ---------------------------- UI SETUP ------------------------------- #

tk = Tk()
tk.config(pady=50, padx=50)
tk.title("password manager")
canv = Canvas(width=200, height=200)
image = PhotoImage(file="./logo.png")
canv.create_image(100, 100, image=image)
canv.grid(row=0, column=1)

website_l = Label(text="Website :")
website_l.grid(row=1, column=0)

website_i = Entry(width=52)
website_i.grid(row=1, column=1, columnspan=2, sticky="w", padx=10)
website_i.focus()
email_l = Label(text="Email/Useraname :")
email_l.grid(row=2, column=0)

email_i = Entry(width=52)
email_i.grid(row=2, column=1, columnspan=2, sticky="w", padx=10)
email_i.focus()
email_i.insert(0, "scarlettJohansson@Gmail.com")
password_l = Label(text="Password :")
password_l.grid(row=3, column=0)

password_i = Entry(width=21)
password_i.grid(row=3, column=1, sticky="w", padx=10)
password_i.focus()
button_g = Button(text="Generate Password", command=pass_gen)
button_g.grid(row=3, column=2, sticky="w")

add_b = Button(text="add", width=44, command=save_pass)
add_b.grid(row=4, column=1, columnspan=2, sticky="w", padx=10)
tk.mainloop()
