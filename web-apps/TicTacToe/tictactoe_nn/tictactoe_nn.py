import numpy


class TicTacToeNN:
    w1 = numpy.random * .2 - .1
    w2 = numpy.random * .2 - .1
    w3 = numpy.random * .2 - .1
    w4 = numpy.random * .2 - .1
    w5 = numpy.random * .2 - .1
    w6 = numpy.random * .2 - .1
    w7 = numpy.random * .2 - .1
    w8 = numpy.random * .2 - .1
    w9 = numpy.random * .2 - .1
    b = numpy.random * .2 - .1

    learning_rate = 0.2

    # make sure that the game itself stores the order of every step, use the method train_nn() every time after each step
    # the step stored needs to be inlcude the list and the move by nn
    # If it has X, the value should be 2. If it has O, the value should be 1. If it has nothing, it should be 0.

    def sigmoid(self, x):
        return 1 / (1 + numpy.exp(-x))

    # do it if nn won the game
    def train_nn(self, board_list, nn_move):
        target = nn_move

        z = TicTacToeNN.w1 * board_list[0] + TicTacToeNN.w2 * board_list[1] + TicTacToeNN.w3 * board_list[2] + \
            TicTacToeNN.w4 * board_list[3] + TicTacToeNN.w5 * board_list[4] + \
            TicTacToeNN.w6 * board_list[5] + TicTacToeNN.w7 * board_list[6] + \
            TicTacToeNN.w8 * board_list[7] + TicTacToeNN.w9 * board_list[8] + TicTacToeNN.b
        pred = TicTacToeNN.sigmoid(z)

        cost = (pred - target)**2
        dcost_dpred = 2*(pred-target)
        dpred_dz = TicTacToeNN.sigmoid(z) * (1-TicTacToeNN.sigmoid(z))

        dz_dw1 = board_list[0]
        dz_dw2 = board_list[1]
        dz_dw3 = board_list[2]
        dz_dw4 = board_list[3]
        dz_dw5 = board_list[4]
        dz_dw6 = board_list[5]
        dz_dw7 = board_list[6]
        dz_dw8 = board_list[7]
        dz_dw9 = board_list[8]
        dz_db = 1

        dcost_dw1 = dcost_dpred * dpred_dz * dz_dw1
        dcost_dw2 = dcost_dpred * dpred_dz * dz_dw2
        dcost_dw3 = dcost_dpred * dpred_dz * dz_dw3
        dcost_dw4 = dcost_dpred * dpred_dz * dz_dw4
        dcost_dw5 = dcost_dpred * dpred_dz * dz_dw5
        dcost_dw6 = dcost_dpred * dpred_dz * dz_dw6
        dcost_dw7 = dcost_dpred * dpred_dz * dz_dw7
        dcost_dw8 = dcost_dpred * dpred_dz * dz_dw8
        dcost_dw9 = dcost_dpred * dpred_dz * dz_dw9
        dcost_db = dcost_dpred * dpred_dz * dz_db

        TicTacToeNN.w1 -= TicTacToeNN.learning_rate * dcost_dw1
        TicTacToeNN.w2 -= TicTacToeNN.learning_rate * dcost_dw2
        TicTacToeNN.w3 -= TicTacToeNN.learning_rate * dcost_dw3
        TicTacToeNN.w4 -= TicTacToeNN.learning_rate * dcost_dw4
        TicTacToeNN.w5 -= TicTacToeNN.learning_rate * dcost_dw5
        TicTacToeNN.w6 -= TicTacToeNN.learning_rate * dcost_dw6
        TicTacToeNN.w7 -= TicTacToeNN.learning_rate * dcost_dw7
        TicTacToeNN.w8 -= TicTacToeNN.learning_rate * dcost_dw8
        TicTacToeNN.w9 -= TicTacToeNN.learning_rate * dcost_dw9
        TicTacToeNN.b -= TicTacToeNN * dcost_db



