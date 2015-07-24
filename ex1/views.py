# -*- coding: utf-8 -*-
import os
import sys


class View(object):
    def __init__(self):
        pass

    def input_values(self, player):
        try:
            return raw_input(player.name + "'s (" + str(player.sign) + ") turn\n")
        except NameError:
            return input(player.name + "'s turn\n")

    def draw(self, field):
        i = 0
        for line in field.field:
            i += 1
            print(" " + " | ".join(line))
            if i != field.get_rank():
                print("---|---|---")

    def clear_screen(self):
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

    def show_message(self, message):
        print(message)
        try:
            raw_input("Press Enter")
        except NameError:
            input("Press Enter")

    def show_menu(self, input_data):
        try:
            data = raw_input(input_data + "\n")
        except NameError:
            data = input(input_data + "\n")
        return data


if __name__ == "__main__":
    print("It's a view module")
