import random
import os
import time


class Board:
    def __init__(self):
        self.board = [['   ' for column in range(3)] for row in range(3)]
        self.empty = 9

    def show_board(self):
        print('---------------')
        for row in self.board:
            print(' | '.join(row))
            print('---------------')

    def check_move(self, position):
        row = int(position[0])
        column = int(position[2])

        if self.board[row-1][column-1] != '   ':
            return False
        return True

    def move(self, position, player):
        row = int(position[0])
        column = int(position[2])
        self.board[row-1][column-1] = f' {player} '
        self.empty -= 1

    def is_game_on(self):
        for check in self.board:
            if check[0] == check[1] == check[2] != '   ':
                return False

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '   ' or self.board[0][2] == self.board[1][1] == self.board[2][0] != '   ':
            return False
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != '   ':
            return False
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != '   ':
            return False
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != '   ':
            return False
        elif self.empty == 0:
            global turn
            turn = 'Draw'
            return False
        else:
            return True


class Computer:
    def select_move(self):
        return f'{random.randint(1,3)},{random.randint(1,3)}'


game = Board()
computer = Computer()


char_selected = False
while not char_selected:
    player_choose = input("Type 'X' or type 'O': ").upper()
    if player_choose == 'X':
        char_selected = True
        turn = 'player'
        computer.choose = 'O'

    elif player_choose == 'O':
        char_selected = True
        turn = 'computer'
        computer.choose = 'X'


while game.is_game_on():
    game.show_board()

    if turn == 'player':
        pos = input('Your move \'row,column\': ')
        try:
            if game.check_move(pos):
                turn = 'computer'
                game.move(pos, player_choose)
        except ValueError:
            pass

    else:
        computer_pos = computer.select_move()
        if game.check_move(computer_pos):
            time.sleep(1)
            game.move(computer_pos, computer.choose)
            turn = 'player'

    os.system('clear')


game.show_board()
if turn == 'player' or turn == 'computer':
    if turn == 'player':
        won = 'Computer'
    else:
        won = 'Player'
    print(f'{won} wins!. Game over.')
else:
    print('It\'s a draw!')
