class TicTacToe:
    board = [" " for _ in range(9)]

    def __init__(self):
        self.x_win = 0
        self.o_win = 0

    def print_game(self):
        print("---------")
        print("|", " ".join(self.board[0:3]), "|", sep=" ")
        print("|", " ".join(self.board[3:6]), "|", sep=" ")
        print("|", " ".join(self.board[6:9]), "|", sep=" ")
        print("---------")

    def count_wins(self):
        horizontal_win = [self.board[0] + self.board[1] + self.board[2], self.board[3] + self.board[4] + self.board[5],\
            self.board[6] + self.board[7] + self.board[8]]
        vertical_win = [self.board[0] + self.board[3] + self.board[6], self.board[1] + self.board[4] + self.board[7],\
            self.board[2] + self.board[5] + self.board[8]]
        diagonal_win = [self.board[0] + self.board[4] + self.board[8], self.board[2] + self.board[4] + self.board[6]]

        if 'XXX' in horizontal_win or 'XXX' in diagonal_win or 'XXX' in vertical_win:
            self.x_win += 1
        elif 'OOO' in horizontal_win or 'OOO' in diagonal_win or 'OOO' in vertical_win:
            self.o_win += 1

    def play_game(self):
        move_count = 0
        coord_grid = [13, 23, 33, 12, 22, 32, 11, 21, 31]
        while self.x_win == 0 and self.o_win == 0 and move_count < 9:
            user_coord = input("Enter the coordinates:")
            remove_space = user_coord.replace(" ", "")
            if remove_space.isdigit():
                int_coord = int(remove_space)
                if int_coord == 13 or int_coord == 23 or int_coord == 33 or int_coord == 12 or\
                    int_coord == 22 or int_coord == 32 or int_coord == 11 or int_coord == 21 or\
                    int_coord == 31:
                    index = coord_grid.index(int_coord)
                    if self.board[index] == 'X'or self.board[index] == 'O':
                        print("This cell is occupied. Choose another one!")
                        continue
                    else:
                        if move_count % 2 == 0:
                            self.board[index] = 'X'
                            move_count += 1
                            self.print_game()
                            self.count_wins()
                        elif move_count % 2 == 1:
                            self.board[index] = 'O'
                            move_count += 1
                            self.print_game()
                            self.count_wins()
                        else:
                            break
                else:
                    print("Coordinates should be from 1 to 3!")
                    continue
            else:
                print("You should enter numbers!")
                continue

    def results(self):
        if self.x_win == 1:
            print("X wins")
        elif self.o_win == 1:
            print("O wins")
        else:
            print("Draw")

game = TicTacToe()
game.print_game()
game.play_game()
game.results()
