from tkinter import *
from user_account import UserAccount
from play_warship import PlayWarship
from login import Login
from battlefield import Battlefield
from tkinter import messagebox

# constant used in the project
FONT_NAME = "Courier"
BG = "#f7f5dd"
LABEL_FONT = 12
BUTTON_COLOR = "#E8B468"

# Instantiating of classes
window = Tk()
user = UserAccount()
play_warship = PlayWarship()
login = Login()
battlefield = Battlefield()


# user account creation
def create_account():
    user.create_account(window, BG, FONT_NAME, LABEL_FONT, BUTTON_COLOR)

    while not user.result:
        window.update()  # Ensure the GUI updates

    # User has finished account creation, if successful, hide the account window and load the play warship
    if user.result:
        user.user_account.withdraw()
        play_warship.play_warship(window, BG, FONT_NAME, LABEL_FONT, BUTTON_COLOR, user.user)

        while not play_warship.ai:
            window.update()

        if play_warship.ai:
            play_warship.play.withdraw()
            battlefield.controls(BG, FONT_NAME, LABEL_FONT, BUTTON_COLOR, play_warship.user)


# user login
def user_login():
    login.login_account(window, BG, FONT_NAME, LABEL_FONT, BUTTON_COLOR)

    while not login.result:
        window.update()  # Ensure the GUI updates

    # User has finished account creation, if successful, hide the login window and load the play warship
    if login.result:
        login.toplevel.withdraw()
        play_warship.play_warship(window, BG, FONT_NAME, LABEL_FONT, BUTTON_COLOR, login.user)

        while not play_warship.ai:
            window.update()

        if play_warship.ai:
            play_warship.play.withdraw()
            battlefield.controls(play_warship.play, BG, FONT_NAME, LABEL_FONT, BUTTON_COLOR, play_warship.user)

        while not battlefield.start_warship:
            window.update()

            battlefield.ai_attack_warship()

        while battlefield.end_warship:
            window.update()
            play_warship.play.deiconify()
            battlefield.control.destroy()


# main warship window
window.geometry("620x430")
window.title("Warship")
window.config(padx=50, pady=50, bg=BG)
window.resizable(width=False, height=False)

# Warship Logo
canvas = Canvas(width=200, height=145, bg=BG, highlightthickness=0)
logo = PhotoImage(file="warship.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
logo_label = Label(text="Welcome to Warship", bg="#E8CBB6", font=(FONT_NAME, 20))
logo_label.grid(row=1, column=1)

dummy_label = Label(text="", bg=BG, font=(FONT_NAME, 20))
dummy_label.grid(row=2, column=1)
dummy_label2 = Label(text="", bg=BG, font=(FONT_NAME, 20))
dummy_label2.grid(row=3, column=1)

# Buttons
create_account_button = Button(text="Create account", bg=BUTTON_COLOR, font=(FONT_NAME, 13), command=create_account)
create_account_button.grid(row=4, column=1)

login_button = Button(text="Login", bg=BUTTON_COLOR, font=(FONT_NAME, 13), command=user_login)
login_button.grid(row=4, column=2)

how_to_button = Button(text="How to play", bg=BUTTON_COLOR, font=(FONT_NAME, 13))
how_to_button.grid(row=4, column=0)

window.mainloop()
