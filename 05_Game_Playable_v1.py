from tkinter import *
import random


class Start:
    def __init__(self, parent):
        self.start_frame = Frame(parent
                                 )
        self.start_frame.grid()

        self.push_me_button = Button(self.start_frame, text="push", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)

    def to_game(self):
        starting_balance = 50
        stakes = 1

        Game(self, stakes, starting_balance)

        self.start_frame.destroy()


class Game:
    def __init__(self, partner, stakes, starting_balance):

        print(stakes)
        print(starting_balance)

        self.balance = IntVar()

        self.balance.set(starting_balance)

        # Get value of stakes (multiplier for winnings)
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # List for holding stats
        self.round_stats_list = []

        # Set up GUI
        self.game_box = Toplevel()

        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box, padx=10)
        self.game_frame.grid()

        # Play Heading row 0
        self.game_heading = Label(self.game_frame, text="Play!", font="Arial 20 bold")
        self.game_heading.grid(row=0)

        # Help text row 1
        self.game_help = Label(self.game_frame, text="Press 'enter' or 'open boxes to play!",
                               font="Arial 10 italic", fg="red")
        self.game_help.grid(row=1, pady=10)

        # The photo winnings frame row 2

        self.game_box_frame = Frame(self.game_frame)
        self.game_box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="question.gif")

        self.prize1_label = Label(self.game_box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize1_label.photo = photo
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.game_box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize2_label.photo = photo
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.game_box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize3_label.photo = photo
        self.prize3_label.grid(row=0, column=2)

        # Play button row 3

        self.game_play = Button(self.game_frame, text="Spin!", font="Arial 20 bold",
                                bg="yellow", width=13, command=self.reveal_boxes)
        self.game_play.grid(row=3)

        self.game_play.focus()
        self.game_play.bind('<Return>', lambda e: self.reveal_boxes())
        self.game_play.grid(row=3)

        # Text that shows ur starting balance. Row 4

        start_text = "Game Cost: ${} \n " "\nHow much " \
                     "will you win?".format(stakes * 5)

        self.game_balance = Label(self.game_frame, text=start_text,
                                  font="arial 15 bold", fg="green", pady=10)
        self.game_balance.grid(row=4)

        # Help and Game stats button row 5

        self.start_help_frame = Frame(self.game_frame, pady=10)
        self.start_help_frame.grid(row=5)

        # Help and statistics buttons
        self.start_help_button = Button(self.start_help_frame, text="Help",
                                        font="Arial 15 bold",
                                        command=lambda: self.to_help)
        self.start_help_button.grid(row=0, column=0)

        self.start_statistics_button = Button(self.start_help_frame, text="Statistics / Export",
                                              font="Arial 15 bold",
                                              command=lambda: self.to_stats)
        self.start_statistics_button.grid(row=0, column=1, padx=5)

        # Quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):

        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        stats_prizes = []
        for thing in range(0, 3):

            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = PhotoImage(file="gold.gif")
                prize_list = "Gold\n(${})".format(5 * stakes_multiplier)
                round_winnings += stakes_multiplier
            elif 5 < prize_num <= 25:
                # get silver if number is between 1 and 3
                prize = PhotoImage(file="silver.gif")
                prize_list = "Silver\n(${})".format(2 * stakes_multiplier)
                round_winnings += stakes_multiplier
            elif 25 < prize_num <= 65:
                prize = PhotoImage(file="copper.gif")
                prize_list = "Copper\n(${})".format(1 * stakes_multiplier)
                round_winnings += stakes_multiplier
            else:
                prize = PhotoImage(file="lead.gif")
                prize_list = "Lead\n$0"

            prizes.append(prize)
            stats_prizes.append(prize_list)

        photo1 = prizes[0]
        photo2 = prizes[1]
        photo3 = prizes[2]

        # Display prizes...
        self.prize1_label.config(image=photo1)
        self.prize1_label.photo = photo1
        self.prize2_label.config(image=photo2)
        self.prize2_label.photo = photo2
        self.prize3_label.config(image=photo3)
        self.prize3_label.photo = photo3

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balnce to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${} \nPayback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)

        # Add round results to stats list
        round_summary = "{} | {} \ {} - Cost: ${} | " \
                        "Payback: ${} | Current Balance: " \
                        "${}".format(stats_prizes[0], stats_prizes[1],
                                     stats_prizes[2],
                                     5 * stakes_multiplier, round_winnings, current_balance)
        self.round_stats_list.append(round_summary)
        print(self.round_stats_list)

        # Edit label so users can see their new balance
        self.game_balance.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.game_play.config(state=DISABLED)
            self.game_box.focus()
            self.game_play.config(text="Game Over")

            balance_statement = "Current Balance ${}\n" \
                            "Your balance is too low. You can only quit " \
                            "or view your states.".format(current_balance)
            self.game_balance.config(fg="#660000", font="Arial 10 bold",
                                  text=balance_statement)

    def to_quit(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()
