# -*- coding: utf-8 -*-
import random


class Controller:
    def __init__(self, p1, p2, f, v):
        self.player1 = p1
        self.player2 = p2
        self.field = f
        self.view = v

    def game_loop(self):
#        show_menu()
        playerOneTurn = bool(random.randint(0, 1))
        gameOver = False
        while not gameOver:
            self.view.clear_screen()
            self.view.draw(self.field)
            if playerOneTurn:
                strValues = self.view.input_values(self.player1)
                sym = self.player1.sign
            else:
                strValues = self.view.input_values(self.player2)
                sym = self.player2.sign
            error = self.test_values(strValues)
            if error:
                self.view.show_message(error)
                continue
            a, b = strValues.split()
            a, b = int(a), int(b)
            self.field.set_value(a, b, sym)
            self.who_win(playerOneTurn)
            playerOneTurn = not playerOneTurn

    def test_values(self, strValues):
        try:
            a, b = strValues.split()
        except:
            return "Enter two numbers with space delimiter"
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            return "Only integer coordinates!"
        if not (0 <= a < self.field.get_rank() and 0 <= b < self.field.get_rank()):
            return "Enter coords in range [0;{})".format(self.field.get_rank())
        elif self.field.field[a][b] != "   ":
            return "Coordinates are occupied!"
        else:
            return ""

    def who_win(self, playerOneTurn):
        if playerOneTurn:
            signComb = self.player1.sign * 3
        else:
            signComb = self.player2.sign * 3
        for line in self.field.field:
            for j in self.field.field:
                j
                



if __name__ == "__main__":
    print("It's controller module")
