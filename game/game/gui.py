import tkinter as tk


class GUI(tk.Frame):

    Winner_BG = "#ffcc00"
    Loser_BG = "#a39489"

    def message(self, message, win):
        background = ""
        if win:
            background = self.Winner_BG
        else:
            background = self.Loser_BG

        print(message)
