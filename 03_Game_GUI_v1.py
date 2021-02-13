from tkinter import *
import random


class Start:
    def __init__(self,partner):

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()


        self.push_me_button = Button(self.start_frame, text="push", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)


    def to_game(self):

        starting_balance = 50
        stakes = 1



        Game(self, stakes, starting_balance)

        root.withdraw()






# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()
