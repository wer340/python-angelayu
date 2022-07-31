from tkinter import *

list_fill = []


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_i.get()
    email = email_i.get()
    password = password_i.get()
    with open("./data-pass.txt", mode="a") as pass_list:
        pass_list.write(f"{website}|{email}|{password}\n")


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
button_g = Button(text="Generate Password")
button_g.grid(row=3, column=2, sticky="w")

add_b = Button(text="add", width=44,command=save_pass)
add_b.grid(row=4, column=1, columnspan=2, sticky="w", padx=10)
tk.mainloop()
