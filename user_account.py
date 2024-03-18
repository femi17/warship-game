from tkinter import *
from tkinter import messagebox
import csv


class UserAccount:
    def __init__(self):
        self.username_entry = None
        self.password_entry = None
        self.user_account = None
        self.window = None
        self.result = None
        self.user = ''

    def create_account(self, window, bg, font_name, label, button):
        self.window = window
        self.window.withdraw()
        self.user_account = Toplevel()
        user_account = self.user_account
        user_account.geometry("600x500")
        user_account.title("Create account")
        user_account.config(padx=50, pady=50, bg=bg)
        user_account.resizable(width=False, height=False)

        go_back_button = Button(user_account, text="Go back", bg=button, font=(font_name, label),
                                command=self.go_back)
        go_back_button.grid(row=0, column=0)

        user_account_canvas = Canvas(user_account, width=200, height=145, bg=bg, highlightthickness=0)
        user_account_logo = PhotoImage(file="warship.png")
        user_account_canvas.user_account_logo = user_account_logo
        user_account_canvas.create_image(100, 100, image=user_account_logo)
        user_account_canvas.grid(row=0, column=1)

        user_account_logo_label = Label(user_account, text="Create Warship Account", bg="#E8CBB6",
                                        font=(font_name, 20))
        user_account_logo_label.grid(row=1, column=1)

        dummy_label4 = Label(user_account, text="", bg=bg, font=(font_name, 20))
        dummy_label4.grid(row=2, column=1)

        username_label = Label(user_account, text="Username:", bg=bg, font=(font_name, label))
        username_label.grid(row=3, column=0)

        password_label = Label(user_account, text="Password:", bg=bg, font=(font_name, label))
        password_label.grid(row=4, column=0)

        # Entry
        self.username_entry = Entry(user_account, width=50)
        self.username_entry.grid(row=3, column=1)

        self.password_entry = Entry(user_account, width=50)
        self.password_entry.grid(row=4, column=1)

        # Button
        dummy_label3 = Label(user_account, text="", bg=bg, font=(font_name, 20))
        dummy_label3.grid(row=5, column=1)
        create_button = Button(user_account, text="Create Account", bg="#E8C368", width=30, pady=0,
                               font=(font_name, label), command=self.create_user)
        create_button.grid(row=6, column=1)

    def create_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if len(username) == 0 or len(password) == 0:
            messagebox.showwarning(title="Oops!!, you have a missing field",
                                   message="Please dont leave any fields empty!")
        else:
            is_ok = messagebox.askokcancel(title="Account Creation", message=f"These are the data entered: \n"
                                                                             f"Username: {username}\nPassword: {password} "
                                                                             f"\nIs it ok to save?"
                                           )
            self.is_successful(is_ok, username)

            if is_ok:
                with open("users.csv", 'a', newline='') as data:
                    fieldnames = ['user_name', 'password']
                    writer = csv.DictWriter(data, fieldnames=fieldnames)
                    writer.writerow({'user_name': username, 'password': password})

    def is_successful(self, value, user):
        if value:
            self.result = value
            self.user = user

    def go_back(self):
        self.user_account.withdraw()
        self.window.deiconify()
