# -*- coding: utf-8 -*-

class Field:
    def __init__(self, x):
        self.rank = x
        self.field = [["   ",] * x for i in range(x)]

    def set_value(self, x, y, sym):
        self.field[x][y] = sym

    def get_rank(self):
        return self.rank
        

class Player:
    def __init__(self, n, s):
        self.name = n
        self.sign = s


if __name__ == "__main__":
    print("It's model module")
