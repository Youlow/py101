# -*- coding: utf-8 -*-
from ex1.models import Sign
from ex1.overmind import AI 
from ex1.tests import TestCase


class OvermindTests(TestCase):
    def converting_test(self):
        ai = AI()

        assert ai.conv(5) == "1 2"

    def test_free_test(self):
        ai = AI()
        ai.moves_list = [4, 1, 3]

        assert ai.test_free(2) == True
        assert ai.test_free(1) == False

    def find_alternate_test(self):
        ai = AI()
        ai.moves_list = [4, 0, 8, 1]
        turn = ai.find_alternate()

        assert turn != "1 1" and turn != "0 0" and \
               turn != "2 2" and turn != "0 1"
        assert turn == "0 2" or turn == "1 0" or turn == "1 2" or \
               turn == "2 0" or turn == "2 1"

    def win_turn_find_test(self):
        ai = AI()
        sign_x = Sign(True)
        sign_o = Sign(False)
        ai.moves_list = [2, 4, 5]

        assert ai.win_turn_find(sign_o, False) == 8

        ai.moves_list = [0, 4, 3, 5]

        assert ai.win_turn_find(sign_x, True) == 6

        ai.moves_list = [0, 4, 7, 1, 2]

        assert ai.win_turn_find(sign_o, True) == -1
        assert ai.win_turn_find(sign_o, False) == -1

    def x_find_turn_test(self):
        ai = AI()
        sign_x = Sign(True)
        ai.moves_list = [0, 1, 3, 6]

        assert ai.x_find_turn(sign_x) == "0 2"

        ai.moves_list = [0, 5, 3, 6, 2, 1]

        assert ai.x_find_turn(sign_x) == "2 2"

        ai.moves_list = [4, 2]

        assert ai.x_find_turn(sign_x) == "2 0"
        

    def o_go_corner_test(self):
        ai = AI()
        sign_o = Sign(False)
        ai.moves_list = [4, ]
        turn = ai.o_go_corner(sign_o)

        assert turn == "0 0" or turn == "0 2" or \
               turn == "2 0" or turn == "2 2"

        ai.moves_list = [4, 0, 8]
        turn = ai.o_go_corner(sign_o)

        assert turn == "0 2" or turn == "2 0"

    def make_turn_test(self):
        ai = AI()
        sign_x = Sign(True)
        sign_o = Sign(False)
        moves_list = []

        assert ai.make_turn(moves_list, sign_x) == "1 1"

        moves_list = [4, 2]

        assert ai.make_turn(moves_list, sign_x) == "2 0"

        moves_list = [4, ]
        turn = ai.make_turn(moves_list, sign_o)

        assert turn == "0 0" or turn == "0 2" or \
               turn == "2 0" or turn == "2 2"

        moves_list = [0, ]

        assert ai.make_turn(moves_list, sign_o) == "1 1"

        moves_list = [0, 4, 5]

        assert ai.make_turn(moves_list, sign_o) == "2 2"

        moves_list = [3, ]

        assert ai.make_turn(moves_list, sign_o) == "1 1"

        moves_list = [3, 4, 2]

        assert ai.make_turn(moves_list, sign_o) == "2 0"

        moves_list = [3, 4, 5]
        turn = ai.make_turn(moves_list, sign_o)

        assert turn == "0 0" or turn == "0 2" or \
               turn == "2 0" or turn == "2 2"

        moves_list = [3, 4, 7]

        assert ai.make_turn(moves_list, sign_o) == "2 0"
