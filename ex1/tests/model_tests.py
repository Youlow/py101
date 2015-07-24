# -*- coding: utf-8 -*-
from ex1.models import Field, Player, Sign
from ex1.tests import TestCase


class ModelTests(TestCase):
    def field_initialisation_test(self):
        field_3x3 = Field(rank=3)

        assert field_3x3.get_rank() is 3
        assert field_3x3.empty == " "
        assert len(field_3x3.field) == 3
        assert len(field_3x3.field[0]) == 3
        for line in field_3x3.field:
            for item in line:
                assert item == field_3x3.empty

    def field_set_value_test(self):
        field_5x5 = Field(rank=5)
        sign = Sign(False)
        field_5x5.set_value(2, 3, sign)
        i = 0
        for line in field_5x5.field:
            for item in line:
                if item != field_5x5.empty:
                    i += 1

        assert field_5x5.field[2][3] == sign.sym
        assert i == 1

    def player_test(self):
        player = Player()
        sign = Sign(True)

        assert player.name == 'PC'
        assert player.sign.sym == sign.sym

    def player_set_name_sign_test(self):
        player = Player()
        player.set_name('Robert')
        player.set_sign(False)
        sign = Sign(False)

        assert player.name == 'Robert'
        assert player.sign.sym == sign.sym

    def sign_test(self):
        sign = Sign(True)

        assert sign.sym == "X"
        assert str(sign) == sign.sym
        assert str(sign) == "X"
        assert sign.is_x
