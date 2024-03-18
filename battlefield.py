from tkinter import *
from tkinter import messagebox
import random

# constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ROWS = 15
COLS = 15
CELL_WIDTH = 50
CELL_HEIGHT = 50


class Battlefield:
    def __init__(self):
        self.control = None
        self.window = None
        self.form = None
        self.attack_board = None
        self.bg = ''
        self.font_name = ''
        self.label = ''
        self.button = ''
        self.user = ''
        self.row_entry = None
        self.col_entry = None
        self.ship = 0
        self.x = 0
        self.y = 0
        self.xx = 0
        self.yy = 0
        self.aix = 0
        self.aiy = 0
        self.ships = {}
        self.ai_ships = {}
        self.ship_row = 0
        self.ship_col = ''
        self.bullet = []
        self.start_warship = False
        self.end_warship = False
        self.ai_bullet = []
        self.turn = None
        self.num = 0
        self.battle = None
        self.attack_root = None
        self.count_ai_ship = []
        self.count_player_ship = []
        self.ai_hit = []
        self.cord_c = []
        self.cord_w = []
        self.cord_i = []
        self.cord_s = []
        self.hit_ship = ""

    def controls(self, window, bg, font_name, label, button, user):
        self.window = window
        self.bg = bg
        self.font_name = font_name
        self.label = label
        self.button = button
        self.user = user
        self.control = Toplevel()
        controls = self.control
        controls.geometry("625x400")
        controls.title("Battlefield Warship")
        controls.config(padx=50, pady=50, bg=bg)
        controls.resizable(width=False, height=False)

        # Warship Logo
        battle_canvas = Canvas(controls, width=200, height=145, bg=bg, highlightthickness=0)
        battle_logo = PhotoImage(file="warship.png")
        battle_logo.battle_logo = battle_logo
        battle_canvas.create_image(100, 100, image=battle_logo)
        battle_canvas.grid(row=0, column=1)

        # Labels
        battle_logo_label = Label(controls, text="Warship Battlefield", bg="#E8CBB6", font=(font_name, 20))
        battle_logo_label.grid(row=1, column=1)

        battle_dummy_label = Label(controls, text="", bg=bg, font=(font_name, 20))
        battle_dummy_label.grid(row=2, column=1)

        # Buttons
        battle_formation_button = Button(controls, text="Battlefield", bg=button, font=(font_name, 13),
                                         command=lambda: self.battle_field(0))
        battle_formation_button.grid(row=4, column=1)

        battle_attack_button = Button(controls, text="Formation", bg=button, font=(font_name, 13),
                                      command=self.formations)
        battle_attack_button.grid(row=4, column=0)

        battle_battlefield_button = Button(controls, text="Attack", bg=button, font=(font_name, 13),
                                           command=self.attack)
        battle_battlefield_button.grid(row=4, column=2)

        dummy_label2 = Label(controls, text="", bg=bg, font=(font_name, 20))
        dummy_label2.grid(row=5, column=1)

        battle_start_war_button = Button(controls, text="Start Battle", bg=button, font=(font_name, 13),
                                         command=self.start_battle)
        battle_start_war_button.grid(row=6, column=1)

    def start_battle(self):

        missing_ship = False
        missing_ai = False
        ships = ["c-ship", "w-ship", "i-ship", "s-ship"]
        for ship in ships:
            if ship not in self.ships:
                missing_ship = True

        if missing_ship:
            messagebox.showwarning(title="Oops!!, missing warship",
                                   message="All warships have not been lined up!")
        else:
            self.start_warship = True
            self.turn = "ai"

            for airship in ships:
                if airship not in self.ai_ships:
                    missing_ai = True

            while missing_ai:
                num = random.randint(2, 5)
                self.ai_order_warship(num)

                if len(self.ai_ships) == 4:
                    missing_ai = False

    def ai_order_warship(self, ai):

        xx = random.choice(NUMBERS)
        yy = random.choice(LETTERS).title()

        def get_coordinate(column, row, cell_width, cell_height, ai_ship):

            self.aix = (ord(column) - ord('A')) * cell_width + cell_width // 2
            self.aiy = (row - 1) * cell_height + cell_height // 2
            if ai_ship == 5 and (self.aix + 200) > 475:
                self.aix = 0
                self.aiy = 0
                return self.aix, self.aiy
            elif ai_ship == 4:
                if self.aiy + 150 > 475 or self.aix + 150 > 475:
                    self.aix = 0
                    self.aiy = 0
                return self.aix, self.aiy
            elif ai_ship == 3 and (self.aiy + 100) > 475:
                self.aix = 0
                self.aiy = 0
                return self.aix, self.aiy
            elif ai_ship == 2:
                if self.aiy + 50 > 475 or self.aix + 50 > 475:
                    self.aix = 0
                    self.aiy = 0
                return self.aix, self.aiy
            else:
                return self.aix, self.aiy

        self.aix, self.aiy = get_coordinate(yy, xx, CELL_WIDTH, CELL_HEIGHT, ai)

        self.ai_battle_field(ai)

    def ai_battle_field(self, ship_ai):
        if self.aix > 0 and self.aiy > 0:
            self.aix += 50
            self.aiy += 50

            ai_war_ship = []

            if ship_ai == 5 and self.aix > 0 and self.aiy > 0:
                for _ in range(ship_ai):
                    ai_war_ship.append([self.aix, self.aiy])
                    self.aix += 50
                check_for_clash = {key: value for key, value in self.ai_ships.items() if
                                   any(item in ai_war_ship for item in value)}
                if len(check_for_clash) > 0:
                    pass

                elif "c-ship" in self.ai_ships:
                    pass
                else:
                    self.ai_ships["c-ship"] = ai_war_ship
            elif ship_ai == 4 and self.aix > 0 and self.aiy > 0:
                for _ in range(ship_ai):
                    ai_war_ship.append([self.aix, self.aiy])
                    self.aix += 50
                    self.aiy += 50
                check_for_clash = {key: value for key, value in self.ai_ships.items() if
                                   any(item in ai_war_ship for item in value)}
                if len(check_for_clash) > 0:
                    pass

                elif "w-ship" in self.ai_ships:
                    pass
                else:
                    self.ai_ships["w-ship"] = ai_war_ship
            elif ship_ai == 3 and self.aix > 0 and self.aiy > 0:
                for _ in range(ship_ai):
                    ai_war_ship.append([self.aix, self.aiy])
                    self.aiy += 50
                check_for_clash = {key: value for key, value in self.ai_ships.items() if
                                   any(item in ai_war_ship for item in value)}
                if len(check_for_clash) > 0:
                    pass

                elif "i-ship" in self.ai_ships:
                    pass
                else:
                    self.ai_ships["i-ship"] = ai_war_ship
            else:
                if self.aix > 0 and self.aiy > 0:
                    for num in range(3):
                        ai_war_ship.append([self.aix, self.aiy])
                        self.aiy += 50
                        if num == 1:
                            self.aiy -= 50
                            self.aix += 50
                    check_for_clash = {key: value for key, value in self.ai_ships.items() if
                                       any(item in ai_war_ship for item in value)}
                    if len(check_for_clash) > 0:
                        pass

                    elif "s-ship" in self.ai_ships:
                        pass
                    else:
                        self.ai_ships["s-ship"] = ai_war_ship

    def get_row_column_from_coordinates(self, x, y, cell_width, cell_height):
        # Reverse the process to get row and column from pixel coordinates
        column = chr((x - cell_width // 2) // cell_width + ord('A'))
        row = (y - cell_height // 2) // cell_height + 1
        return column, int(row)

    def smart_attack(self, hit_ship):
        ship_cords = {
            "c_ship": (self.cord_c, 50, 0, 5),
            "w_ship": (self.cord_w, 50, 50, 4),
            "i_ship": (self.cord_i, 0, 50, 3),
            "s_ship": (self.cord_s, 0, 50, 3),
        }

        if hit_ship in ship_cords:
            cors, cor_x, cor_y, num = ship_cords[hit_ship]
            length = len(cors) - 1
            if num > len(cors) > 0:
                position = cors[length]
                aix = position[0] + cor_x
                aiy = position[1] + cor_y
                cl, rw = self.get_row_column_from_coordinates(aix, aiy, CELL_WIDTH, CELL_HEIGHT)
                return rw, cl

        return random.choice(NUMBERS), random.choice(LETTERS).title()

    def ai_attack_warship(self):

        while self.num < 3 and self.start_warship:

            if "hit" in self.ai_hit:
                self.xx, self.yy = self.smart_attack(self.hit_ship)
            else:
                self.xx, self.yy = random.choice(NUMBERS), random.choice(LETTERS).title()

            def get_coordinate(column, row, cell_width, cell_height):

                self.aix = (ord(column) - ord('A')) * cell_width + cell_width // 2
                self.aiy = (row - 1) * cell_height + cell_height // 2

                return self.aix + 50, self.aiy + 50

            self.aix, self.aiy = get_coordinate(self.yy, self.xx, CELL_WIDTH, CELL_HEIGHT)

            while [self.aix, self.aiy] in self.ai_bullet:
                xx = random.choice(NUMBERS)
                yy = random.choice(LETTERS).title()
                self.aix, self.aiy = get_coordinate(yy, xx, CELL_WIDTH, CELL_HEIGHT)

            cox = self.aix - 50
            coy = self.aiy - 50
            self.ai_bullet.append([self.aix, self.aiy])
            if self.hit_ship == "c_ship":
                self.cord_c.append((cox, coy))
            elif self.hit_ship == "w_ship":
                self.cord_w.append((cox, coy))
            elif self.hit_ship == "i_ship":
                self.cord_i.append((cox, coy))
            elif self.hit_ship == "s_ship":
                self.cord_s.append((cox, coy))

            if self.num == 2:
                messagebox.showinfo(title="Shots, Fired by AI", message="Check out your warships for hits!")
                self.turn = "player"
                self.battle_field(0)
                self.num = 0
                break
            self.num += 1

    def order_warship(self):

        if self.col_entry.get() == "" or self.row_entry.get() == "" or self.ship == 0:
            messagebox.showwarning(title="Oops!!, you have a missing field",
                                   message="Please don't leave any fields empty!")
        else:
            self.ship_row = int(self.row_entry.get())
            self.ship_col = self.col_entry.get().title()

            def get_coordinate(column, row, cell_width, cell_height):

                self.x = (ord(column) - ord('A')) * cell_width + cell_width // 2
                self.y = (row - 1) * cell_height + cell_height // 2
                if self.ship == 5 and (self.x + 200) > 475:
                    self.x = 0
                    self.y = 0
                    messagebox.showwarning(title="Oops!!, out of order",
                                           message="Your warship C is out of line!")
                    return self.x, self.y
                elif self.ship == 4:
                    if self.y + 150 > 475 or self.x + 150 > 475:
                        self.x = 0
                        self.y = 0
                        messagebox.showwarning(title="Oops!!, out of order",
                                               message="Your warship W is out of line!")
                    return self.x, self.y
                elif self.ship == 3 and (self.y + 100) > 475:
                    self.x = 0
                    self.y = 0
                    messagebox.showwarning(title="Oops!!, out of order",
                                           message="Your warship I is out of line!")
                    return self.x, self.y
                elif self.ship == 2:
                    if self.y + 50 > 475 or self.x + 50 > 475:
                        self.x = 0
                        self.y = 0
                        messagebox.showwarning(title="Oops!!, out of order",
                                               message="Your warship S is out of line!")
                    return self.x, self.y
                else:
                    return self.x, self.y

            self.x, self.y = get_coordinate(self.ship_col, self.ship_row, CELL_WIDTH, CELL_HEIGHT)
            self.battle_field(self.ship)

    def call_back_warship(self):

        if self.ship == 0:
            messagebox.showwarning(title="Oops!!",
                                   message="You need to pick a warship to callback!")

        else:
            if self.ship == 5:
                call = "c-ship"
            elif self.ship == 4:
                call = "w-ship"
            elif self.ship == 3:
                call = "i-ship"
            else:
                call = "s-ship"

            self.ships.pop(call)
            self.ship = 0
            self.battle_field(self.ship)

    def battle_field(self, ship):
        self.hit_ship = ""
        self.ai_hit = []
        if self.x > 0 and self.y > 0:
            self.x += 50
            self.y += 50

        def draw_grid(board, rows, cols, cell_width, cell_height):
            for i in range(rows + 1):
                y = i * cell_height
                board.create_line(0, y, cols * cell_width, y, fill="black")
                label = str(i + 1)
                board.create_text(25, y + cell_height + 25, text=label, fill="black",
                                  font=(self.font_name, self.label, "bold"))

            for j in range(cols + 1):
                x = j * cell_width
                board.create_line(x, 0, x, rows * cell_height, fill="black")
                label = chr(ord('A') + j)
                board.create_text(x + cell_width + 25, 25, text=label, fill="black",
                                  font=(self.font_name, self.label, "bold"))

        self.battle = Toplevel()
        battle_root = self.battle
        battle_root.title("Warship on battlefield")
        battle_root.resizable(width=False, height=False)

        canvas = Canvas(battle_root, width=550, height=550, bg="#f7f5dd")

        if ship > 0:
            war_ship = []
            if ship == 5 and self.x > 0 and self.y > 0:
                for _ in range(ship):
                    war_ship.append([self.x, self.y])
                    self.x += 50
                check_for_clash = {key: value for key, value in self.ships.items() if
                                   any(item in war_ship for item in value)}
                if len(check_for_clash) > 0:
                    messagebox.showwarning(title="Oops!!",
                                           message="C ships are clashing with another ship!")

                elif "c-ship" in self.ships:
                    messagebox.showwarning(title="We are ready!!",
                                           message="C ships are lined on the battlefield!")
                else:
                    self.ships["c-ship"] = war_ship
            elif ship == 4 and self.x > 0 and self.y > 0:
                for _ in range(ship):
                    war_ship.append([self.x, self.y])
                    self.x += 50
                    self.y += 50
                check_for_clash = {key: value for key, value in self.ships.items() if
                                   any(item in war_ship for item in value)}
                if len(check_for_clash) > 0:
                    messagebox.showwarning(title="Oops!!",
                                           message="W ships are clashing with another ship!")

                elif "w-ship" in self.ships:
                    messagebox.showwarning(title="We are ready!!",
                                           message="W ships are lined on the battlefield!")
                else:
                    self.ships["w-ship"] = war_ship
            elif ship == 3 and self.x > 0 and self.y > 0:
                for _ in range(ship):
                    war_ship.append([self.x, self.y])
                    self.y += 50
                check_for_clash = {key: value for key, value in self.ships.items() if
                                   any(item in war_ship for item in value)}
                if len(check_for_clash) > 0:
                    messagebox.showwarning(title="Oops!!",
                                           message="I ships are clashing with another ship!")

                elif "i-ship" in self.ships:
                    messagebox.showwarning(title="We are ready!!",
                                           message="I ships are lined on the battlefield!")
                else:
                    self.ships["i-ship"] = war_ship
            else:
                if self.x > 0 and self.y > 0:
                    for num in range(3):
                        war_ship.append([self.x, self.y])
                        self.y += 50
                        if num == 1:
                            self.y -= 50
                            self.x += 50
                    check_for_clash = {key: value for key, value in self.ships.items() if
                                       any(item in war_ship for item in value)}
                    if len(check_for_clash) > 0:
                        messagebox.showwarning(title="Oops!!",
                                               message="S ships are clashing with another ship!")

                    elif "s-ship" in self.ships:
                        messagebox.showwarning(title="We are ready!!",
                                               message="S ships are lined on the battlefield!")
                    else:
                        self.ships["s-ship"] = war_ship

        for ship, line in self.ships.items():
            for x, y in line:
                canvas.create_text(x, y, text="🚢", font=(self.font_name, self.label, "bold"))

        for ai_bullet in self.ai_bullet:
            found_match = False
            for key, value in self.ships.items():
                if ai_bullet in value:
                    canvas.create_text(ai_bullet[0], ai_bullet[1], text="💣", fill="red",
                                       font=(self.font_name, self.label, "bold"))
                    self.ai_hit.append("hit")
                    if key == "c-ship":
                        if ai_bullet in self.cord_c:
                            pass
                        else:
                            cox = ai_bullet[0] - 50
                            coy = ai_bullet[1] - 50
                            self.cord_c.append((cox, coy))
                            self.hit_ship = key
                    elif key == "w-ship":
                        if ai_bullet in self.cord_w:
                            pass
                        else:
                            cox = ai_bullet[0] - 50
                            coy = ai_bullet[1] - 50
                            self.cord_w.append((cox, coy))
                            self.hit_ship = key
                    elif key == "i-ship":
                        if ai_bullet in self.cord_i:
                            pass
                        else:
                            cox = ai_bullet[0] - 50
                            coy = ai_bullet[1] - 50
                            self.cord_i.append((cox, coy))
                            self.hit_ship = key
                    else:
                        if ai_bullet in self.cord_s:
                            pass
                        else:
                            cox = ai_bullet[0] - 50
                            coy = ai_bullet[1] - 50
                            self.cord_s.append((cox, coy))
                            self.hit_ship = key
                    if len(self.count_player_ship) == 14:
                        messagebox.showwarning(title="You Lose!!!",
                                               message="All your ships are sunk!")
                        self.end_game(value=True)
                        break
                    elif ai_bullet not in self.count_player_ship:
                        messagebox.showwarning(title="Target hit", message=f"One of {key} killed!")
                        self.count_player_ship.append(ai_bullet)
                    found_match = True
                    break

            if not found_match:
                canvas.create_text(ai_bullet[0], ai_bullet[1], text="❌", fill="red",
                                   font=(self.font_name, self.label, "bold"))
                self.ai_hit.append("miss")

        canvas.pack()
        draw_grid(canvas, ROWS, COLS, CELL_WIDTH, CELL_HEIGHT)

    def formations(self):
        self.form = Toplevel()
        formation = self.form
        formation.geometry("520x350")
        formation.title("Warship Formation")
        formation.config(padx=50, pady=50, bg=self.bg)
        formation.resizable(width=False, height=False)

        ship_label = Label(formation, text="Warship Formation", bg=self.bg, font=(self.font_name, 20))
        ship_label.grid(row=0, column=1)

        col_label = Label(formation, text="Column:", bg=self.bg, font=(self.font_name, self.label))
        col_label.grid(row=4, column=0)

        row_label = Label(formation, text="Row:", bg=self.bg, font=(self.font_name, self.label))
        row_label.grid(row=5, column=0)

        # Entry
        def radio_used():
            self.ship = int(radio_state.get())

        # Variable to hold on to which radio button value is checked.
        radio_state = IntVar()
        radiobutton1 = Radiobutton(formation, text="C warship", bg=self.bg, value="5", variable=radio_state,
                                   command=radio_used)
        radiobutton2 = Radiobutton(formation, text="W warship", bg=self.bg, value="4", variable=radio_state,
                                   command=radio_used)
        radiobutton3 = Radiobutton(formation, text="I warship", bg=self.bg, value="3", variable=radio_state,
                                   command=radio_used)
        radiobutton4 = Radiobutton(formation, text="S warship", bg=self.bg, value="2", variable=radio_state,
                                   command=radio_used)
        radiobutton1.grid(row=1, column=0)
        radiobutton2.grid(row=1, column=1)
        radiobutton3.grid(row=2, column=0)
        radiobutton4.grid(row=2, column=1)

        dummy_label3 = Label(formation, text="", bg=self.bg, font=(self.font_name, 20))
        dummy_label3.grid(row=3, column=1)

        # Entry

        self.col_entry = Entry(formation, width=30)
        self.col_entry.grid(row=4, column=1)

        self.row_entry = Entry(formation, width=30)
        self.row_entry.grid(row=5, column=1)

        # Button
        dummy_label4 = Label(formation, text="", bg=self.bg, font=(self.font_name, 20))
        dummy_label4.grid(row=6, column=1)
        create_button = Button(formation, text="Order Warship", bg="#E8C368", width=15, pady=0,
                               font=(self.font_name, self.label), command=self.order_warship)
        create_button.grid(row=7, columnspan=1, column=0)
        call_back_button = Button(formation, text="Callback Ships", bg="#E8C368", width=15, pady=0,
                                  font=(self.font_name, self.label), command=self.call_back_warship)
        call_back_button.grid(row=7, column=1)

    def attack_warship(self):

        if self.col_entry.get() == "" or self.row_entry.get() == "":
            messagebox.showwarning(title="Oops!!, you have a missing field",
                                   message="Please dont leave any fields empty!")
        else:
            self.ship_row = int(self.row_entry.get())
            self.ship_col = self.col_entry.get().title()

            def get_coordinate(column, row, cell_width, cell_height):

                self.xx = (ord(column) - ord('A')) * cell_width + cell_width // 2
                self.yy = (row - 1) * cell_height + cell_height // 2

                return self.xx, self.yy

            self.xx, self.yy = get_coordinate(self.ship_col, self.ship_row, CELL_WIDTH, CELL_HEIGHT)
            self.attack_field()

    def attack_field(self):

        if self.xx > 0 and self.yy > 0:
            self.xx += 50
            self.yy += 50

        def draw_grid(board, rows, cols, cell_width, cell_height):
            for i in range(rows + 1):
                y = i * cell_height
                board.create_line(0, y, cols * cell_width, y, fill="black")
                label = str(i + 1)
                board.create_text(25, y + cell_height + 25, text=label, fill="black", font=('courier', 10, "bold"))

            for j in range(cols + 1):
                x = j * cell_width
                board.create_line(x, 0, x, rows * cell_height, fill="black")
                label = chr(ord('A') + j)
                board.create_text(x + cell_width + 25, 25, text=label, fill="black", font=('courier', 10, "bold"))

        self.attack_root = Toplevel()
        attack_root = self.attack_root
        attack_root.title("Missiles on battlefield")
        attack_root.resizable(width=False, height=False)

        attack_canvas = Canvas(attack_root, width=550, height=550, bg="#f7f5dd")

        self.bullet.append([self.xx, self.yy])

        for bullet_coordinate in self.bullet:
            found_match = False
            for key, value in self.ai_ships.items():
                if bullet_coordinate in value:
                    attack_canvas.create_text(bullet_coordinate[0], bullet_coordinate[1], fill="green", text="💣",
                                              font=(self.font_name, self.label, "bold"))
                    if len(self.count_ai_ship) == 14:
                        messagebox.showwarning(title="You Win!!!",
                                               message="All AI ships are sunk!")
                        self.end_game(True)
                        break
                    elif bullet_coordinate not in self.count_ai_ship:
                        messagebox.showwarning(title="Target hit", message=f"One of {key} killed!")
                        self.count_ai_ship.append(bullet_coordinate)

                    found_match = True
                    break

            if not found_match:
                attack_canvas.create_text(bullet_coordinate[0], bullet_coordinate[1], fill="red", text="❌",
                                          font=(self.font_name, self.label, "bold"))

        attack_canvas.pack()
        draw_grid(attack_canvas, ROWS, COLS, CELL_WIDTH, CELL_HEIGHT)

        self.num += 1

        if self.num == 3:
            self.turn = "ai"
            self.num = 0
            self.ai_attack_warship()

    def attack(self):

        if self.start_warship and self.turn == "player":
            self.control.withdraw()
            self.attack_board = Toplevel()
            attack = self.attack_board
            attack.geometry("450x300")
            attack.title("Warship Formation")
            attack.config(padx=50, pady=50, bg=self.bg)
            attack.resizable(width=False, height=False)

            ship_label = Label(attack, text="Attack Warship", bg=self.bg, font=(self.font_name, 20))
            ship_label.grid(row=0, column=1)

            col_label = Label(attack, text="Column:", bg=self.bg, font=(self.font_name, self.label))
            col_label.grid(row=4, column=0)

            row_label = Label(attack, text="Row:", bg=self.bg, font=(self.font_name, self.label))
            row_label.grid(row=5, column=0)

            # Entry

            self.col_entry = Entry(attack, width=30)
            self.col_entry.grid(row=4, column=1)

            self.row_entry = Entry(attack, width=30)
            self.row_entry.grid(row=5, column=1)

            # Button
            dummy_label4 = Label(attack, text="", bg=self.bg, font=(self.font_name, 20))
            dummy_label4.grid(row=6, column=1)
            create_button = Button(attack, text="Attack Warship", bg="#E8C368", width=15, pady=0,
                                   font=(self.font_name, self.label), command=self.attack_warship)
            create_button.grid(row=7, columnspan=1, column=1)

        else:
            messagebox.showwarning(title="Oops!!, start battle",
                                   message="Before you attack you need to start battle!")

    def end_game(self, value):
        if value:
            self.end_warship = True
            self.form.destroy()
            self.attack_root.destroy()
            self.battle.destroy()
            self.attack_board.destroy()
            self.window.deiconify()
