# -*- coding: utf-8 -*-

class Field(object):
    def __init__(self, rank=3):
        self.rank = rank
        self.field = [["   ",] * rank for i in range(rank)]

    def set_value(self, x, y, sym):
        self.field[x][y] = sym

    def get_rank(self):
        return self.rank
        

class Player(object):
    def __init__(self, name="Player", sign=" X "):
        self.name = name
        self.sign = sign


if __name__ == "__main__":
    print("It's a model module")
