# -*- coding: utf-8 -*-
from models import Field, Player
from views import View
from controllers import Controller


def main():
    player1 = Player("Grisha", " X ")
    player2 = Player("Misha", " O ")
    field = Field()
    view = View()
    cont = Controller(player1, player2, field, view)
    cont.game_loop()


if __name__ == "__main__":
    main()
