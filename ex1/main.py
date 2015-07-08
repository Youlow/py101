# -*- coding: utf-8 -*-
from models import Field, Player
from views import View
from controllers import Controller


def main():
    player1 = Player()
    player2 = Player()
    field = Field()
    view = View()
    cont = Controller(player1, player2, field, view)
    play_again = True
    while play_again:
        cont.game_loop()
        play_again = cont.play_again()


if __name__ == "__main__":
    main()
