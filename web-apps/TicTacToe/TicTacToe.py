def introduce_game():
    print("\n" * 100)
    print("****************\nTic Tac Toe Game\n****************\n")
    print("Instructions:\nTo place an X or O at a spot, enter that spot's corresponding number.")
    print("\t\t|\t\t|")
    print("\t1\t|\t2\t|\t3\t")
    print("\t\t|\t\t|")
    print(" -------|-------|------- ")
    print("\t\t|\t\t|")
    print("\t4\t|\t5\t|\t6\t")
    print("\t\t|\t\t|")
    print(" -------|-------|------- ")
    print("\t\t|\t\t|")
    print("\t7\t|\t8\t|\t9\t")
    print("\t\t|\t\t|\n")


def print_board(positions):
    print("\t\t|\t\t|")
    print(f"\t{positions[0]}\t|\t{positions[1]}\t|\t{positions[2]}\t")
    print("\t\t|\t\t|")
    print(" -------|-------|------- ")
    print("\t\t|\t\t|")
    print(f"\t{positions[3]}\t|\t{positions[4]}\t|\t{positions[5]}\t")
    print("\t\t|\t\t|")
    print(" -------|-------|------- ")
    print("\t\t|\t\t|")
    print(f"\t{positions[6]}\t|\t{positions[7]}\t|\t{positions[8]}\t")
    print("\t\t|\t\t|\n")


def has_x_won(board):
    if "".join(board[:3]) == "XXX" or "".join(board[3:6]) == "XXX" or "".join(board[6:9]) == "XXX" or "".join(
            [board[0], board[3], board[6]]) == "XXX" or "".join([board[1], board[4], board[7]]) == "XXX" or "".join(
        [board[2], board[5], board[8]]) == "XXX" or "".join([board[0], board[4], board[8]]) == "XXX" or "".join(
        [board[2], board[4], board[6]]) == "XXX":
        return True
    return False


def has_o_won(board):
    if "".join(board[:3]) == "OOO" or "".join(board[3:6]) == "OOO" or "".join(board[6:9]) == "OOO" or "".join(
            [board[0], board[3], board[6]]) == "OOO" or "".join([board[1], board[4], board[7]]) == "OOO" or "".join(
        [board[2], board[5], board[8]]) == "OOO" or "".join([board[0], board[4], board[8]]) == "OOO" or "".join(
        [board[2], board[4], board[6]]) == "OOO":
        return True
    return False


def is_tie(board):
    return "" not in board


def two_together_ai(board, xo):
    if board[0] == xo and board[1] == xo and board[2] == "":
        return 2
    if board[3] == xo and board[4] == xo and board[5] == "":
        return 5
    if board[6] == xo and board[7] == xo and board[8] == "":
        return 8
    if board[1] == xo and board[2] == xo and board[0] == "":
        return 0
    if board[4] == xo and board[5] == xo and board[3] == "":
        return 3
    if board[7] == xo and board[8] == xo and board[6] == "":
        return 6
    if board[0] == xo and board[3] == xo and board[6] == "":
        return 6
    if board[1] == xo and board[4] == xo and board[7] == "":
        return 7
    if board[2] == xo and board[5] == xo and board[8] == "":
        return 8
    if board[3] == xo and board[6] == xo and board[0] == "":
        return 0
    if board[4] == xo and board[7] == xo and board[1] == "":
        return 1
    if board[5] == xo and board[8] == xo and board[2] == "":
        return 2
    if board[0] == xo and board[4] == xo and board[8] == "":
        return 8
    if board[2] == xo and board[4] == xo and board[6] == "":
        return 6
    if board[4] == xo and board[6] == xo and board[2] == "":
        return 2
    if board[4] == xo and board[8] == xo and board[0] == "":
        return 0
    if board[0] == xo and board[6] == xo and board[3] == "":
        return 3
    if board[2] == xo and board[8] == xo and board[5] == "":
        return 5
    if board[0] == xo and board[2] == xo and board[1] == "":
        return 1
    if board[6] == xo and board[8] == xo and board[7] == "":
        return 7
    else:
        return -1


def two_together_player(board, xo):
    if board[0] == xo and board[1] == xo and board[2] == "":
        return 2
    if board[3] == xo and board[4] == xo and board[5] == "":
        return 5
    if board[6] == xo and board[7] == xo and board[8] == "":
        return 8
    if board[1] == xo and board[2] == xo and board[0] == "":
        return 0
    if board[4] == xo and board[5] == xo and board[3] == "":
        return 3
    if board[7] == xo and board[8] == xo and board[6] == "":
        return 6
    if board[0] == xo and board[3] == xo and board[6] == "":
        return 6
    if board[1] == xo and board[4] == xo and board[7] == "":
        return 7
    if board[2] == xo and board[5] == xo and board[8] == "":
        return 8
    if board[3] == xo and board[6] == xo and board[0] == "":
        return 0
    if board[4] == xo and board[7] == xo and board[1] == "":
        return 1
    if board[5] == xo and board[8] == xo and board[2] == "":
        return 2
    if board[0] == xo and board[4] == xo and board[8] == "":
        return 8
    if board[2] == xo and board[4] == xo and board[6] == "":
        return 6
    if board[4] == xo and board[6] == xo and board[2] == "":
        return 2
    if board[4] == xo and board[8] == xo and board[0] == "":
        return 0
    if board[0] == xo and board[6] == xo and board[3] == "":
        return 3
    if board[2] == xo and board[8] == xo and board[5] == "":
        return 5
    if board[0] == xo and board[2] == xo and board[1] == "":
        return 1
    if board[6] == xo and board[8] == xo and board[7] == "":
        return 7
    else:
        return -1


def can_make_tricks(board, xo):
    if board[0] == xo and board[1] == "" and board[2] == "" and board[6] == "":
        return 2
    if board[0] == xo and board[2] == "" and board[3] == "" and board[6] == "":
        return 6
    if board[2] == xo and board[0] == "" and board[1] == "" and board[8] == "":
        return 0
    if board[2] == xo and board[0] == "" and board[5] == "" and board[8] == "":
        return 8
    if board[6] == xo and board[0] == "" and board[3] == "" and board[8] == "":
        return 0
    if board[6] == xo and board[0] == "" and board[7] == "" and board[8] == "":
        return 8
    if board[8] == xo and board[2] == "" and board[5] == "" and board[6] == "":
        return 2
    if board[8] == xo and board[2] == "" and board[6] == "" and board[7] == "":
        return 6
    else:
        return -1


def run_game():
    introduce_game()
    # if count is even, it's player 1's turn, if it's odd, it's player 2's turn
    count = 0
    board = [""] * 9
    second_player_marker = input("Do you want to be X or O? ").upper()
    while second_player_marker != "X" and second_player_marker != "O":
        second_player_marker = input("Please enter either \"X\" or \"O\": ").upper()
    first_player_marker = "X" if second_player_marker == "O" else "O"
    while True:
        if has_x_won(board):
            print(f"{'The AI' if first_player_marker == 'X' else 'You'} (X) won.")
            break
        elif has_o_won(board):
            print(f"{'The AI' if second_player_marker == 'X' else 'You'} (O) won.")
            break
        elif is_tie(board):
            print("It is a tie, no one wins.")
            break
        else:
            is_input_error = False
            if count % 2 == 0:
                if two_together_ai(board, first_player_marker) != -1:
                    position = two_together_ai(board, first_player_marker)
                elif two_together_player(board, second_player_marker) != -1:
                    position = two_together_player(board, second_player_marker)
                elif can_make_tricks(board, first_player_marker) != -1:
                    position = can_make_tricks(board, first_player_marker)
                else:
                    if board[4] == "":
                        position = 4
                    elif board[6] == "":
                        position = 6
                    elif board[8] == "":
                        position = 8
                    elif board[0] == "":
                        position = 0
                    elif board[2] == "":
                        position = 2
                    elif board[1] == "":
                        position = 1
                    elif board[3] == "":
                        position = 3
                    elif board[7] == "":
                        position = 7
                    else:
                        position = 5
            else:
                try:
                    position = int(input(
                        f"Player ({second_player_marker}), choose your position (1 through 9): ")) - 1
                except ValueError:
                    print("The position you enter must be an integer.")
                    is_input_error = True
            if not is_input_error:
                if position < 0 or position > 8:
                    print("Please enter a position from 1 through 9.")
                elif board[position] != "":
                    print("That position is already taken. Please choose a different position.")
                else:
                    while board[position] == "":
                        if count % 2 == 0:
                            board[position] = first_player_marker
                        else:
                            board[position] = second_player_marker
                        print("{} moved to position {}.".format("The AI" if count % 2 == 0 else "You", position + 1))
                        print_board(board)
                        count += 1


while True:
    run_game()
    play_again = input("Do you want to play again? Enter \"yes\" or \"no\": ").lower()
    while play_again != "yes" and play_again != "no":
        play_again = input("Please enter either \"yes\" or \"no\": ").lower()
    if play_again == "no":
        break
