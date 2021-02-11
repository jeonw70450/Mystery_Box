from tkinter import *
import random


class Start:
    def __init__(self):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg="#D4E1F5")
        self.start_frame.grid()

        #background
        background="#D4E1F5"

        # Mystery box Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 16 bold", bg=background)
        self.mystery_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, text=" Please enter a dollar amount",
                                            font="Arial 8 italic", fg="red", bg=background)
        self.mystery_instructions.grid(row=1)

        # Entry box (row 2)
        self.start_amount_entry = Entry(self.start_frame,
                                        font="Arial 19")
        self.start_amount_entry.grid(row=2)

        # Buttons frame ( row 3)

        self.stakes_frame = Frame(self.start_frame, bg=background)
        self.stakes_frame.grid(row=3)

        #Button Font
        button_font = "Oswald 12 bold"

        # Low Stakes Button
        self.lowstakes_button = Button(self.stakes_frame, text="Low ($5)",
                                       font=button_font, bg="#FF9933",
                                       command=lambda: self.to_game(1))
        self.lowstakes_button.grid(row=0, column=0, pady=10)

        # Medium Stakes Button
        self.lowstakes_button = Button(self.stakes_frame, text="Medium (10$)",
                                       font=button_font, bg="#FFFF33",
                                       command=lambda: self.to_game(2))
        self.lowstakes_button.grid(row=0, column=1, pady=10, padx=5)

        # High Stakes Button
        self.lowstakes_button = Button(self.stakes_frame, text="High (15$)",
                                       font=button_font, bg="#09FF33",
                                       command=lambda: self.to_game(3))
        self.lowstakes_button.grid(row=0, column=2, pady=10, padx=5)

        #Error box (row 4)
        self.amount_error_label = Label(self.start_frame, bg=background)
        self.amount_error_label.grid(row=4)

        #Button frame for help and statistics (row 5)
        self.start_help_frame = Frame(self.start_frame, bg=background)
        self.start_help_frame.grid(row=5)

        # Help and statistics buttons
        self.start_help_button = Button(self.start_help_frame, text="Help",
                                        font="Arial 10 bold", bg="#E6E6E6",
                                        command=lambda: self.to_help)
        self.start_help_button.grid(row=0, column=0)

        self.start_statistics_button = Button(self.start_help_frame, text="Statistics / Export",
                                              font="Arial 10 bold", bg="#E6E6E6",
                                              command=lambda: self.to_stats)
        self.start_statistics_button.grid (row=0, column=1, padx=5)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()

        error_back = "#ffafaf"
        has_errors = "no"

        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")


        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the minimum amount is $5"

            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high! the maximum amount is $50" \

            elif starting_balance < 10 and (stakes == 2 or stakes == 3):
                has_errors = "yes"
                error_feedback = "Sorry, you can only afford to play low stakes."

            elif starting_balance < 15 and stakes == 3:
                has_errors = "yes"
                error_feedback = "Sorry, you can only afford to play low and Medium Stakes"


        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimal)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback, fg="red")



        else:
            Game(self, stakes, starting_balance)


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start()
    root.mainloop()
