import random

class TicTacToe:
    board = [" " for x in range(9)]

    def __init__(self):
        self.x_win = 0
        self.o_win = 0
        self.x_count = 0
        self.o_count = 0
        self.space_count = 0
        self.move_count = 0

    def print_game(self):
        print("---------")
        print("|", " ".join(self.board[0:3]), "|", sep=" ")
        print("|", " ".join(self.board[3:6]), "|", sep=" ")
        print("|", " ".join(self.board[6:9]), "|", sep=" ")
        print("---------")

    def win(self):
        # win_list = [self.board[0] + self.board[1] + self.board[2], self.board[3] + self.board[4] + self.board[5],
        #             self.board[6] + self.board[7] + self.board[8],self.board[0] + self.board[3] + self.board[6], self.board[1] + self.board[4] + self.board[7],
        #             self.board[2] + self.board[5] + self.board[8], self.board[0] + self.board[4] + self.board[8], self.board[2] + self.board[4] + self.board[6]]
        win_list = [[0,1,2], [3,4,5], [6,7,8],[0,3,6],[1,4,7], [2,5,8], [0,4,8], [2,4,6]]

        return win_list

    def count_wins(self):
        wlist = self.win()
        string = ''
        for i in wlist:
            for j in range(3):
                string += self.board[i[j]]
            if string == 'XXX':
                self.x_win += 1
            elif string == 'OOO':
                self.o_win += 1
            string = ''

    def results(self):
        if self.x_win == 1:
            print("X wins")
        elif self.o_win == 1:
            print("O wins")
        else:
            print("Draw")


class Start(TicTacToe):
    def user_move(self):
        coord_grid = [['1','3'], ['2','3'], ['3','3'], ['1','2'], ['2','2'], ['3','2'], ['1','1'], ['2','1'], ['3','1']]
        while True:
            user_coord = input("Enter the coordinates:").split()
            if user_coord in coord_grid:
                index = coord_grid.index(user_coord)
                if self.board[index] == 'X' or self.board[index] == 'O':
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    self.x_o_move(index)
                    break
            else:
                if user_coord not in ['0','1','2','3','4','5','6','7','8','9']:
                    print("You should enter numbers!")
                    continue
                else:
                    print("Coordinates should be from 1 to 3")
                    continue
        self.print_game()
        self.count_wins()

    def ai_move_easy(self):
        print('Making move level "easy"')
        ind = self.random()
        self.x_o_move(ind)
        self.print_game()
        self.count_wins()

    def ind_two_row(self):
        for i in self.win():
            values = [self.board[j] for j in i]
            if values.count('X') == 2:
                for k in i:
                    if self.board[k] == ' ':
                        return k
            elif values.count('O') == 2:
                for k in i:
                    if self.board[k] == ' ':
                        return k
        return self.random()

    def ai_move_medium(self):
        print('Making move level "medium')
        two = self.ind_two_row()
        self.x_o_move(two)
        self.print_game()
        self.count_wins()

    def random(self):
        x = random.randrange(9)
        return x

    def x_o_move(self, ind):
        if self.move_count % 2 == 0:
            while self.board[ind] == 'X' or self.board[ind] == 'O':
                ind = self.random()
            self.board[ind] = 'X'
            self.move_count += 1
        else:
            while self.board[ind] == 'O' or self.board[ind] == 'X':
                ind = self.random()
            self.board[ind] = 'O'
            self.move_count += 1

    def menu_loop(self):
            while True:
                self.x_win = 0
                self.o_win = 0
                self.move_count = 0
                menu = input("Input Command:").split()
                if menu[0] == 'exit':
                    break
                else:
                    if len(menu) != 3:
                        print("Bad parameters")
                        continue
                    if menu[0] == 'start':
                        self.board = [" " for _ in range(9)]
                        self.print_game()
                        self.play_game(menu)
                        continue
                    else:
                        print("Bad parameters")

    def choices(self, x, o):
        while self.move_count < 9:
            if x == "user":
                self.user_move()
            elif x == "easy":
                self.ai_move_easy()
            elif x == "medium":
                self.ai_move_medium()
            if self.x_win == 1:
                break
            if self.move_count != 9:
                if o == "user":
                    self.user_move()
                elif o == "easy":
                    self.ai_move_easy()
                elif o == "medium":
                    self.ai_move_medium()
                if self.o_win == 1:
                    break
        self.results()

    def play_game(self, menu):
        if menu[1] == 'easy' and menu[2] == 'easy':
            self.choices('easy', 'easy')
        elif menu[1] == 'user' and menu[2] == 'easy':
            self.choices('user', 'easy')
        elif menu[1] == 'easy' and menu[2] == 'user':
            self.choices('easy', 'user')
        elif menu[1] == 'user' and menu[2] == 'user':
            self.choices('user', 'user')
        elif menu[1] == 'user' and menu[2] == 'medium':
            self.choices('user', 'medium')
        elif menu[1] == 'medium' and menu[2] == 'user':
            self.choices('medium', 'user')
        elif menu[1] == 'easy' and menu[2] == 'medium':
            self.choices('easy', 'medium')
        elif menu[1] == 'medium' and menu[2] == 'easy':
            self.choices('medium', 'easy')
        elif menu[1] == 'medium' and menu[2] == 'medium':
            self.choices('medium', 'medium')


game = Start()
game.menu_loop()


