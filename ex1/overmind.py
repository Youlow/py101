# -*- coding: utf-8 -*-

class AI(object):
    """Implements bot moving in X/O game on 3x3 field
    """
    def __init__(self):
        pass

    def make_turn(self, moves_list, sign, enemy_sign):
        """Calculation of bot moves that depends on enemy's turn.
        This logic uses one-dimension coordinates:
        0|1|2
        3|4|5
        6|7|8
        """
        self.moves_list = moves_list
        if sign == "X":
            if moves_list == []:
                return self.conv(4)
            else:
                return self.x_find_turn(sign, enemy_sign)
        elif sign == "O":
            if moves_list[0] == 4:#first turn in center
                return self.o_go_corner(sign)
            elif moves_list[0] in [0, 2, 6, 8]:#first turn in corner
                if len(moves_list) == 1:
                    return self.conv(4)#second turn must be in center
                elif len(moves_list) == 3:
                    turn = -1
                    turn = self.win_turn_find(sign, True)
                    if turn == -1:
                        turn = self.win_turn_find(sign, False)
                    if turn != -1:
                        return self.conv(turn)
                    
                    if self.moves_list[0] == 0:
                        turn = 8
                    elif self.moves_list[0] == 2:
                        turn = 6
                    elif self.moves_list[0] == 6:
                        turn = 2
                    elif self.moves_list[0] == 8:
                            turn = 0
                    if turn != -1 and self.test_free(turn):
                        return self.conv(turn)
                    else:
                        return self.conv(1)#go to side!!!
                else:
                    turn = -1
                    turn = self.win_turn_find(sign, True)
                    if turn == -1:
                        turn = self.win_turn_find(sign, False)
                    if turn != -1:
                        return self.conv(turn)
                    return self.find_alternate()

            elif moves_list[0] in [1, 3, 5, 7]:#first turn on side
                if len(moves_list) == 1:
                    return self.conv(4)#second turn must be in center
                elif len(moves_list) == 3:
                    turn = -1
                    if self.moves_list[2] == 0:#corner
                        turn = 8
                    elif self.moves_list[2] == 2:
                        turn = 6
                    elif self.moves_list[2] == 6:
                        turn = 2
                    elif self.moves_list[2] == 8:
                        turn = 0
                    elif self.moves_list[0] == 7 and  self.moves_list[2] == 1:#side
                        for item in [0, 2, 6, 8]:
                            if self.test_free(item):
                                turn = item 
                    elif self.moves_list[0] == 5 and self.moves_list[2] == 3:
                        for item in [0, 2, 6, 8]:
                            if self.test_free(item):
                                turn = item 
                    elif self.moves_list[0] == 3 and self.moves_list[2] == 5:
                        for item in [0, 2, 6, 8]:
                            if self.test_free(item):
                                turn = item 
                    elif self.moves_list[0] == 7 and self.moves_list[2] == 1:
                        for item in [0, 2, 6, 8]:
                            if self.test_free(item):
                                turn = item 
                    else:
                        turn = self.moves_list[0] + self.moves_list[2] - 4

                    if turn != -1 and self.test_free(turn):
                        return self.conv(turn)
                    else:
                        return self.find_alternate()
                else:
                    turn = -1
                    turn = self.win_turn_find(sign, True)
                    if turn == -1:
                        turn = self.win_turn_find(sign, False)
                    if turn != -1:
                        return self.conv(turn)
                    return self.find_alternate()
                
    def o_go_corner(self, sign):
        """Corner turning of O-sign player when X-sign player
        has been moved to center of game field
        """
        turn = -1
        turn = self.win_turn_find(sign, True)
        if turn == -1:
            turn = self.win_turn_find(sign, False)
        if turn != -1:
            return self.conv(turn)

        for item in [0, 2, 6, 8]:
            if self.test_free(item):
                turn = item
                break
        
        if turn != -1 and self.test_free(turn):
            return self.conv(turn)
        else:
            return self.find_alternate()

    def x_find_turn(self, sign, enemy_sign):
        """Full X-sign player logic for win or draw
        """
        turn = -1
        turn = self.win_turn_find(sign, True)
        if turn == -1:
            turn = self.win_turn_find(sign, False)
        if turn != -1:
            return self.conv(turn)

        if self.moves_list[-1] == 0:
            turn = 8
        elif self.moves_list[-1] == 2:
            turn = 6
        elif self.moves_list[-1] == 6:
            turn = 2
        elif self.moves_list[-1] == 8:
            turn = 0
        elif self.moves_list[-1] == 1:
            if self.test_free(6):
                turn = 6
            else:
                turn = 8
        elif self.moves_list[-1] == 3:
            if self.test_free(2):
                turn = 2
            else:
                turn = 8
        elif self.moves_list[-1] == 5:
            if self.test_free(0):
                turn = 0
            else:
                turn = 6
        elif self.moves_list[-1] == 7:
            if self.test_free(0):
                turn = 0
            else:
                turn = 2

        if turn != -1 and self.test_free(turn):
            return self.conv(turn)
        else:
            return self.find_alternate()

    def conv(self, turn):
        """Two-dimension coords converting to one-dimension
        """
        i = turn // 3
        j = turn % 3
        return "{} {}".format(i, j)

    def test_free(self, turn):
        if turn in self.moves_list:
            return False
        else:
            return True

    def find_alternate(self):
        for i in range(9):
            if not i in self.moves_list:
                return self.conv(i)

    def win_turn_find(self, sign, win_test):
        """Test of two main rules of game:
        1. If you can win now - do it!
        2. If (1) not possible and enemy can win now - block it!

        win_test variable responsible for the testing object:
        True means that we want to test our win opportunity
        False - test enemy's opportunity

        """
        temp_list = []
        if win_test:
            if sign == "X":
                offset = 0
            elif sign == "O":
                offset = 1
        else:
            if sign == "X":
                offset = 1
            elif sign == "O":
                offset = 0
        temp_list = self.moves_list[offset: : 2]

        for i in range(9):
            if not i in self.moves_list:
                temp_list.append(i)
                if (all(item in temp_list for item in [0, 1, 2])) or \
                   (all(item in temp_list for item in [3, 4, 5])) or \
                   (all(item in temp_list for item in [6, 7, 8])) or \
                   (all(item in temp_list for item in [0, 3, 6])) or \
                   (all(item in temp_list for item in [1, 4, 7])) or \
                   (all(item in temp_list for item in [2, 5, 8])) or \
                   (all(item in temp_list for item in [0, 4, 8])) or \
                   (all(item in temp_list for item in [2, 4, 6])):
                    return i
                else:
                    temp_list.pop()
                    continue
        return -1
            

        
            

if __name__ == "__main__":
    print("AI module fo X/O game with 3x3 field")
        
