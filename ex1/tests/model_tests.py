# -*- coding: utf-8 -*-
from ex1.models import Field, Player
from ex1.tests import TestCase


class ModelTests(TestCase):
    def field_initialisation_test(self):
        field_3x3 = Field(rank=3)

        assert field_3x3.get_rank() is 3
        assert len(field_3x3.field) == 3
        assert len(field_3x3.field[0]) == 3

    #     add your model tests

    def player_test(self):
        player = Player(name='Tom', sign=['x', 'y', 'z'])

        assert player.name == 'Tom'

        # This assert will fail! You should repair model to pass this test
        assert player.sign == ' X ' or player.sign == ' 0 '

    #     add your model tests
