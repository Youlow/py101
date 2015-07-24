# -*- coding: utf-8 -*-


class Field(object):
    def __init__(self, rank=3):
        self.empty = " "
        self.rank = rank
        self.field = [[self.empty, ] * rank for i in range(rank)]

    def set_value(self, x, y, sign):
        self.field[x][y] = sign.sym

    def get_rank(self):
        return self.rank

    def clear(self):
        self.field = [[self.empty, ] * self.rank for i in range(self.rank)]


class Player(object):
    def __init__(self):
        self.name = "PC"
        self.sign = Sign(True)

    def set_name(self, name):
        self.name = name

    def set_sign(self, first_turn):
        self.sign = Sign(first_turn)


class Sign(object):
    def __init__(self, first_turn):
        if first_turn:
            self.sym = "X"
        else:
            self.sym = "O"
        self.is_x = first_turn

    def __str__(self):
        return self.sym


if __name__ == "__main__":
    print("It's a model module")
