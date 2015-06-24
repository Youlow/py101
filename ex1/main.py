# -*- coding: utf-8 -*-
from models import *
from views import *
from controllers import *


def main():
    player1 = Player("Grisha", " X ")
    player2 = Player("Misha", " O ")
    field = Field(3)
    view = View()
    cont = Controller(player1, player2, field, view)
    cont.game_loop()


if __name__ == "__main__":
    main()
