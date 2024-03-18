from tkinter import *
from tkinter import messagebox
import csv


class Login:
    def __init__(self):
        self.username_entry = None
        self.password_entry = None
        self.toplevel = None
        self.window = None
        self.result = None
        self.user = ''

    def login_account(self, window, bg, font_name, label, button):
        self.window = window
        self.window.withdraw()
        self.toplevel = Toplevel()
        login_account = self.toplevel
        login_account.geometry("600x450")
        login_account.title("Login to account")
        login_account.config(padx=50, pady=50, bg=bg)
        login_account.resizable(width=False, height=False)

        go_back_button = Button(login_account, text="Go back", bg=button, font=(font_name, label),
                                command=self.go_back)
        go_back_button.grid(row=0, column=0)

        login_account_canvas = Canvas(login_account, width=200, height=145, bg=bg, highlightthickness=0)
        login_account_logo = PhotoImage(file="warship.png")
        login_account_canvas.login_account_logo = login_account_logo
        login_account_canvas.create_image(100, 100, image=login_account_logo)
        login_account_canvas.grid(row=0, column=1)

        login_account_logo_label = Label(login_account, text="Login to Warship", bg="#E8CBB6", font=(font_name, 20))
        login_account_logo_label.grid(row=1, column=1)

        dummy_label4 = Label(login_account, text="", bg=bg, font=(font_name, 20))
        dummy_label4.grid(row=2, column=1)

        username_label = Label(login_account, text="Username:", bg=bg, font=(font_name, label))
        username_label.grid(row=3, column=0)

        password_label = Label(login_account, text="Password:", bg=bg, font=(font_name, label))
        password_label.grid(row=4, column=0)

        # Entry
        self.username_entry = Entry(login_account, width=50)
        self.username_entry.grid(row=3, column=1)

        self.password_entry = Entry(login_account, width=50)
        self.password_entry.grid(row=4, column=1)

        # Button
        dummy_label3 = Label(login_account, text="", bg=bg, font=(font_name, 20))
        dummy_label3.grid(row=5, column=1)
        create_button = Button(login_account, text="Login to account", bg="#E8C368", width=30, pady=0,
                               font=(font_name, label), command=self.process_login)
        create_button.grid(row=6, column=1)

    def process_login(self):
        username = self.username_entry.get().lower()
        password = self.password_entry.get().lower()
        if len(username) == 0 or len(password) == 0:
            messagebox.showwarning(title="Oops!!, login error",
                                   message="Username or Password not found!")
        else:

            with open("users.csv") as data_file:
                data = csv.reader(data_file)
                users = [row for row in data if len(row) > 0]
                new_user = dict(users)

            found = [user for user in new_user if username in user.lower() and password in new_user[user].lower()]
            if len(found) > 0:
                self.is_successful(True, username)
            else:
                messagebox.showwarning(title="Oops!!, login error",
                                       message="Username or Password not found!")

    def is_successful(self, value, user):
        if value:
            self.result = value
            self.user = user

    def go_back(self):
        self.toplevel.withdraw()
        self.window.deiconify()
