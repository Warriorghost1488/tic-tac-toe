X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    print(""" Числа соотвествуют полям так, как показано ниже:
 1 | 2 | 3
 4 | 5 | 6
 7 | 8 | 9""")


def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question)) - 1
    return response


def pieces():
    go_first = ask_yes_no("Начнешь игру? (y, n): ")
    if go_first == "y":
        print("Играй крестиком.")
        human = X
        computer = O
    else:
        print("Начну я .")
        computer = X
        human = O
    return computer, human


def new_board():
    # board = [EMPTY] * NUM_SQUARES

    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    # print(f'{board[0]} | {board[1]} | {board[2]}')
    # print("----------")
    # print(f'{board[0]} | {board[1]} | {board[2]}')
    # print("----------")
    # print(f'{board[0]} | {board[1]} | {board[2]}')
    # print("----------")
    #
    print(board[0], "|", board[1], "|", board[2])
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])


def legal_moves(board):
    # moves = [move for move in board if move == EMPTY]

    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (6, 4, 2))
    for row in WAYS_TO_WIN:
        strategy_has_same_point = board[row[0]] == board[row[1]] == board[row[2]]
        user_to_check = board[row[0]]
        if strategy_has_same_point and user_to_check != EMPTY:
            return user_to_check
        if EMPTY not in board:
            return TIE
    return None


def human_move(board):
    legal = legal_moves(board)
    move = None
    # your_turn_phrase = f'Твой ход. Выбери одно из полей  {", ".join(legal)}'
    #
    # a = 'a'
    # str_ = 'qwe'
    #
    # str_ = 'qwe %s' % a
    #
    # str_ = 'qwe {}'.format(a)
    #
    # str_ = f'qwe {a}'
    while move is None:
        next_move = ask_number("Твой ход. Выбери одно из полей (1 - 9):", 0, NUM_SQUARES)
        if next_move in legal:
            move = next_move
        # if move not in legal:
        #     print("Это поле уже занято. Выбери другое.")
    print("Хорошо")

    return move


def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    moves = legal_moves(board)
    # phrase = 'Я выберу поле номер {}'
    # print(phrase.format(move))

    print("Я выберу поле номер", end=" ")
    for move in moves:
        board[move] = computer
        if winner(board) == computer:
            print(move+1)
            return move
        board[move] = EMPTY

    for move in moves:
        board[move] = human
        if winner(board) == human:
            print(move+1)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in moves:
            print(move+1)
            return move


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

    # return O if turn == X else X


def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!")
    else:
        print("Ничья!")
    if the_winner == computer:
        print("Ты проиграл!!!")
    elif the_winner == human:
        print("Ты выйграл!!!")
    elif the_winner == TIE:
        print("Жму руку! У нас ничья!!!")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while len(legal_moves(board)):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        the_winner = winner(board)
        if the_winner:
            congrat_winner(the_winner, computer, human)
            return

main()
# input("Нажмите Enter, чтобы выйти.")