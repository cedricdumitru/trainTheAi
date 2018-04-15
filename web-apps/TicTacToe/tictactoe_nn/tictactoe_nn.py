import numpy
import random


class TicTacToeNN:
    w = []

    for number in range(9):
        w.append(random.uniform(0, 1) * .2 - .1)

    b = random.uniform(0, 1) * .2 - .1

    learning_rate = 0.2

    count = 0
    # make sure that the game itself stores the order of every step, use the method train_nn() every time after each step
    # the step stored needs to be include the list and the move by nn
    # If it has X, the value should be 2. If it has O, the value should be 1. If it has nothing, it should be 0.
    # try catch to throw out the whole thing if error occurs

    def sigmoid(self, x):
        return 1 / (1 + numpy.exp(-x))

    # do it if nn won the game
    def train_nn(self, board, nn_move):
        board_list = []
        for marker in board:
            if marker == "X":
                board_list.append(2)
            elif marker == "O":
                board_list.append(1)
            else:
                board_list.append(0)

        target = (1 + 2 * (nn_move - 1))/18.0
        z = 0
        for number in range(9):
            z += self.w[number] * board_list[number]
        z += self.b
        pred = self.sigmoid(z)

        # cost = (pred - target)**2
        dcost_dpred = 2 * (pred - target)
        dpred_dz = self.sigmoid(z) * (1 - self.sigmoid(z))

        dz_dw = []
        for number in range(9):
            dz_dw.append(board_list[number])
        dz_db = 1

        dcost_dw = []
        for number in range(9):
            dcost_dw.append(dcost_dpred * dpred_dz * dz_dw[number])
        dcost_db = dcost_dpred * dpred_dz * dz_db

        for number in range(9):
            self.w[number] -= self.learning_rate * dcost_dw[number]
        self.b -= self.learning_rate * dcost_db

        self.count += 1
        print("trained %s times" %self.count)
        w_count = 0
        for weight in self.w:
            w_count += 1
            print("w%s = %s" %(w_count, weight))
        print("b = %s" %self.b)
        print()

    # returning 1,2,3,4,5,6,7,8,9 corresponding the board
    # catch error if nothing returns
    def make_move(self, board):
        board_list = []

        for marker in board:
            if marker == "X":
                board_list.append(2)
            elif marker == "O":
                board_list.append(1)
            else:
                board_list.append(0)

        z = 0
        for number in range(9):
            z += self.w[number] * board_list[number]
        z += self.b
        pred = self.sigmoid(z)
        intended_move = int(numpy.ceil(9.0 * pred))
        if board_list[intended_move - 1] == 0:
            return intended_move
        else:
            for number in (range(1, 9)):
                if 9 >= number + intended_move >= 1 and board_list[number + intended_move - 1] == 0:
                    return number + intended_move
                if 1 <= intended_move - number <= 9 and board_list[intended_move - number - 1] == 0:
                    return intended_move - number
