class TicTacToe:
    def __init__(self):
        print(" WELCOME TO TIC-TAC-TOE ")
        print("Player 1 :'X' | Player 2 :'O'")
        self.map = {i: str(i) for i in range(1, 10)}
        self.game_board()
        print()
        while True:
            self.take_input_p1()
            self.game_board()
            if self.is_over():
                print(" Player 1 is WINNER! ")
                self.map.clear()
                break
            if self.is_draw():
                print("The game is DRAW ")
                self.map.clear()
                break
            self.take_input_p2()
            self.game_board()
            if self.is_over():
                print("Player 2 is WINNER!")
                self.map.clear()
                break
            if self.is_draw():
                print("The game is DRAW ")
                self.map.clear()
                break

    def game_board(self):
        print("\t\t     |     |     ")
        print("\t\t   {} |  {}  |  {} ".format(self.map[1], self.map[2], self.map[3]))
        print("\t\t_____|_____|_____")
        print("\t\t     |     |     ")
        print("\t\t   {} |  {}  |  {} ".format(self.map[4], self.map[5], self.map[6]))
        print("\t\t_____|_____|_____")
        print("\t\t     |     |     ")
        print("\t\t   {} |  {}  |  {} ".format(self.map[7], self.map[8], self.map[9]))
        print("\t\t     |     |     ")

    def take_input_p1(self):
        print("Player 1's turn: ")
        input1 = int(input())
        if input1 not in self.map or self.map[input1] in ['O', 'X']:
            print("Invalid input or box already filled. Choose another one!")
            self.take_input_p1()
        else:
            self.map[input1] = 'X'

    def take_input_p2(self):
        print("Player 2's turn: ")
        input2 = int(input())
        if input2 not in self.map or self.map[input2] in ['O', 'X']:
            print("Invalid input or box already filled. Choose another one!")
            self.take_input_p2()
        else:
            self.map[input2] = 'O'

    def is_over(self):
        for i in range(1, 10, 3):
            if self.map[i] == self.map[i+1] == self.map[i+2]:
                return True
        for i in range(1, 4):
            if self.map[i] == self.map[i+3] == self.map[i+6]:
                return True
        if self.map[1] == self.map[5] == self.map[9] or self.map[3] == self.map[5] == self.map[7]:
            return True
        return False

    def is_draw(self):
        return all(self.map[i] in ['O', 'X'] for i in range(1, 10))


while True:
    t = TicTacToe()