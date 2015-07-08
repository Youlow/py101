# -*- coding: utf-8 -*-
from ex1.models import Field, Player
from ex1.tests import TestCase


class ModelTests(TestCase):
    def field_initialisation_test(self):
        field_3x3 = Field(rank=3)

        assert field_3x3.get_rank() is 3
        assert len(field_3x3.field) == 3
        assert len(field_3x3.field[0]) == 3
        for line in field_3x3.field:
            for item in line:
                assert item == " "

    def field_set_value_test(self):
        field_5x5 = Field(rank=5)
        field_5x5.set_value(2, 3, "O")
        i = 0
        for line in field_5x5.field:
            for item in line:
                if item != " ":
                    i += 1

        assert field_5x5.field[2][3] == "O"
        assert i == 1
            

    def player_test(self):
        player = Player()

        assert player.name == 'PC'
        assert player.sign == 'X' or player.sign == 'O'

    def player_set_name_sign_test(self):
        player = Player()
        player.set_name('Robert')
        player.set_sign('O')

        assert player.name == 'Robert'
        assert player.sign == 'O'
