# -*- coding: utf-8 -*-
from ex1.models import Field, Player
from ex1.views import View
from ex1.controllers import Controller
from ex1.tests import TestCase


class ControllerTests(TestCase):
    def controller_initialization_test(self):
        field_3x3 = Field(rank=3)
        view = View()
        player1 = Player()
        player2 = Player()
        cont = Controller(player1, player2, field_3x3, view)

        assert cont.player1 is player1
        assert cont.player2 is player2
        assert cont.view is view
        assert cont.field is field_3x3

    def winner_determination_test(self):
        field_3x3 = Field(rank=3)
        view = View()
        player1 = Player()
        player2 = Player()
        cont = Controller(player1, player2, field_3x3, view)

        win_raw = [["O", " ", " "], \
                   ["X", "X", "X"], \
                   ["O", " ", " "]]
        win_col = [["O", "O", " "], \
                   ["X", "O", "X"], \
                   ["X", "O", "X"]]
        win_diag = [["O", "O", " "], \
                    ["X", "O", "X"], \
                    ["X", "O", "X"]]
        no_one_wins = [["O", "X", "O"], \
                       ["X", "O", "X"], \
                       ["X", "O", "X"]]

        cont.field.field = win_raw
        assert cont.is_win() == True

        cont.field.field = win_col
        assert cont.is_win() == True

        cont.field.field = win_diag
        assert cont.is_win() == True

        cont.field.field = no_one_wins
        assert cont.is_win() == False
        assert cont.no_one_wins() == True

        
        
        
