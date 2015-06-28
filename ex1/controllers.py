# -*- coding: utf-8 -*-
import random


class Controller(object):
    def __init__(self, player1, player2, field, view):
        self.player1 = player1
        self.player2 = player2
        self.field = field
        self.view = view

    def game_loop(self):
#        show_menu()
        player_one_turn = bool(random.randint(0, 1))
        game_over = False
        while not game_over:
            self.view.clear_screen()
            self.view.draw(self.field)
            if player_one_turn:
                str_values = self.view.input_values(self.player1)
                sym = self.player1.sign
            else:
                str_values = self.view.input_values(self.player2)
                sym = self.player2.sign
            error = self.test_values(str_values)
            if error:
                self.view.show_message(error)
                continue
            a, b = str_values.split()
            a, b = int(a), int(b)
            self.field.set_value(a, b, sym)
            if self.no_one_wins(self.field):
                self.view.clear_screen()
                self.view.draw(self.field)
                self.view.show_message("Round draw")
                break
            if self.is_win():
                self.view.clear_screen()
                self.view.draw(self.field)
                if player_one_turn:
                    self.view.show_message(self.player1.name + self.player1.sign + "wins")
                else:
                    self.view.show_message(self.player2.name + self.player2.sign + "wins")
                break
            player_one_turn = not player_one_turn

    def test_values(self, str_values):
        try:
            a, b = str_values.split()
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

    def is_win(self):
        for line in self.field.field:
            win = True
            raw_item = line[0]
            for item in line:
                if raw_item == "   " or (win and raw_item != item):
                    win = False
            if win:
                return True
        col_list = self.field.field[0]
        for i in range(self.field.get_rank()):
            win = True
            for line in self.field.field:
                if col_list[i] == "   " or (win and col_list[i] != line[i]):
                    win = False
            if win:
                return True
        diag_item = self.field.field[0][0]
        win = True
        for i in range(self.field.get_rank()):
            if diag_item == "   " or (win and diag_item != self.field.field[i][i]):
                win = False
        if win:
            return True
        diag_item = self.field.field[0][self.field.get_rank() - 1]
        win = True
        for i in range(self.field.get_rank()):
            if diag_item == "   " or (win and diag_item != self.field.field[i][self.field.get_rank() - 1 - i]):
                win = False
        if win:
            return True
        else:
            return False

    def no_one_wins(self, field):
        for line in field.field:
            for item in line:
                if item == "   ":
                    return False
        return True


if __name__ == "__main__":
    print("It's a controller module")
