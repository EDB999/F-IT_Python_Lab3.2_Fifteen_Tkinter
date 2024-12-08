from tkinter import Tk, Canvas

from random import shuffle

BOARD_SIZE = 4
SQUARE_SIZE = 80

EMPTY_SQUARE = BOARD_SIZE ** 2


def draw_board():
    c.delete('all')

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            index = str(board[BOARD_SIZE * i + j])

            if index != str(EMPTY_SQUARE):
                c.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE,
                                   j * SQUARE_SIZE + SQUARE_SIZE,
                                   i * SQUARE_SIZE + SQUARE_SIZE,
                                   fill='#21DBAD',
                                   outline='#000')

                c.create_text(j * SQUARE_SIZE + SQUARE_SIZE / 2,
                              i * SQUARE_SIZE + SQUARE_SIZE / 2,
                              text=index,
                              font="Arial {}".format(int(SQUARE_SIZE / 4)),
                              fill='#FFFFFF')


def click(event):
    x, y = event.x, event.y

    x = x // SQUARE_SIZE
    y = y // SQUARE_SIZE

    board_index = x + (y * BOARD_SIZE)
    empty_index = get_empty_neighbor(board_index)

    board[board_index], board[empty_index] = board[empty_index], board[board_index]

    draw_board()

    if board == correct_board:
        show_victory_plate()


def get_empty_neighbor(index):
    empty_index = board.index(EMPTY_SQUARE)

    abs_value = abs(empty_index - index)
    if abs_value == BOARD_SIZE:

        return empty_index
    elif abs_value == 1:

        max_index = max(index, empty_index)
        if max_index % BOARD_SIZE != 0:
            return empty_index
    return index


def show_victory_plate():
    c.create_rectangle(SQUARE_SIZE / 5,

                       SQUARE_SIZE * BOARD_SIZE / 2 - 10 * BOARD_SIZE,

                       BOARD_SIZE * SQUARE_SIZE - SQUARE_SIZE / 5,

                       SQUARE_SIZE * BOARD_SIZE / 2 + 10 * BOARD_SIZE,

                       fill='#FFFFFF',

                       outline='#000000')

    c.create_text(SQUARE_SIZE * BOARD_SIZE / 2, SQUARE_SIZE * BOARD_SIZE / 1.9,

                  text="ПОБЕДА!", font="Times New Roman {} bold".format(int(10 * BOARD_SIZE)), fill='#21DBAD')


def get_inv_count():
    inversions = 0
    inversion_board = board[:]
    inversion_board.remove(EMPTY_SQUARE)

    for i in range(len(inversion_board)):
        first_item = inversion_board[i]
        for j in range(i + 1, len(inversion_board)):
            second_item = inversion_board[j]

            if first_item > second_item:
                inversions += 1
    return inversions


def is_solvable():
    num_inversions = get_inv_count()

    if BOARD_SIZE % 2 != 0:
        return num_inversions % 2 == 0
    else:
        empty_square_row = BOARD_SIZE - (board.index(EMPTY_SQUARE) // BOARD_SIZE)
        if empty_square_row % 2 == 0:
            return num_inversions % 2 != 0
        else:
            return num_inversions % 2 == 0


if __name__ == '__main__':
    root = Tk()
    root.title("Fifteen Puzzle")

    c = Canvas(root, width=BOARD_SIZE * SQUARE_SIZE,
               height=BOARD_SIZE * SQUARE_SIZE, bg='#808080')

    c.bind('<Button-1>', click)
    c.pack()

    board = list(range(1, EMPTY_SQUARE + 1))
    correct_board = board[:]

    shuffle(board)

    while not is_solvable():
        shuffle(board)

    draw_board()

    root.mainloop()
