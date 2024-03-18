from tkinter import *


class PlayWarship:
    def __init__(self):
        self.play = None
        self.window = None
        self.ai = None
        self.user = ''

    def play_warship(self, window, bg, font_name, label, button, user):
        self.window = window
        self.user = user
        self.play = Toplevel()
        play = self.play
        play.geometry("600x450")
        play.title("Play Warship")
        play.config(padx=50, pady=50, bg=bg)
        play.resizable(width=False, height=False)

        go_back_button = Button(play, text="Go back", bg=button, font=(font_name, label),
                                command=self.go_back)
        go_back_button.grid(row=0, column=0)

        user_label = Label(play, text=f"Hi, {self.user}", bg="#E8CBB6", font=(font_name, 15))
        user_label.grid(row=0, column=2)

        play_canvas = Canvas(play, width=200, height=145, bg=bg, highlightthickness=0)
        play_logo = PhotoImage(file="warship.png")
        play_canvas.play_logo = play_logo
        play_canvas.create_image(100, 100, image=play_logo)
        play_canvas.grid(row=0, column=1)

        play_logo_label = Label(play, text="Play Warship", bg="#E8CBB6",
                                font=(font_name, 20))
        play_logo_label.grid(row=1, column=1)

        dummy_label = Label(play, text="", bg=bg, font=(font_name, 20))
        dummy_label.grid(row=2, column=1)
        dummy_label4 = Label(play, text="", bg=bg, font=(font_name, 20))
        dummy_label4.grid(row=3, column=1)

        host_account_button = Button(play, text="Play with host", bg=button, font=(font_name, 13))
        host_account_button.grid(row=4, column=0)

        ai_button = Button(play, text="Play with AI", bg=button, font=(font_name, 13), command=self.play_with_ai)
        ai_button.grid(row=4, column=2)

        friend_button = Button(play, text="Play with a friend", bg=button, font=(font_name, 13))
        friend_button.grid(row=4, column=1)

    def play_with_ai(self):
        self.ai = True

    def go_back(self):
        self.play.withdraw()
        self.window.deiconify()
