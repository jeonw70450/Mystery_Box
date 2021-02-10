from tkinter import *
import random


class Start:
    def __init__(self):

        # Start GUI
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        #Mystery box Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text= "Mystery Box Game",
                                       font="Arial 16 bold")
        self.mystery_box_label.grid(row=0)

        #Entry box (row 1)
        self.start_amount_entry = Entry(self.start_frame,
                                        font="Arial 19")
        self.start_amount_entry.grid(row=1)

        #Play Button (row 2)
        self.lowstakes_button = Button(text="Low ($5)",
                            command=lambda: self.to_game(1))
        self.lowstakes_button.grid(row=2, pady=10)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # Disable low stakes button
        partner.lowstakes_button.config(state=DISABLED)

        # Initialise variables





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start()
    root.mainloop()
