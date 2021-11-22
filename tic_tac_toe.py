import os
#TEST
# IDEA FOR SUPER FAST ALGORITHM:
# Start the game by generated every possible tic tac two board state: 3 ** 9 board states
# Add each board state to a dictionary with value as either win or lose
# Then After each move just return the value of the board from the dict
# If it returns a win, game over
# If it returns a draw, game over
# Else, keep player
# Game needs time to load, but once they are generated you can play games very fast



def clear():
    os.system('cls')


class Board:
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    @classmethod
    def update(cls, row, ele, symbol):
        cls.board[row][ele] = symbol

    @classmethod
    def reset_board(cls):
        cls.board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]


    @classmethod
    def check_board(cls):
        count = 0

        # TOP LEFT TILE CHECK (3 checks required)
        if type(cls.board[0][0]) != int:
            count += 1
            symbol = cls.board[0][0]

            if cls.board[0][1] == symbol and cls.board[0][2] == symbol:  # checks for top left horizontal win
                return symbol

            if cls.board[1][1] == symbol and cls.board[2][2] == symbol:  # checks for top left diagonal win
                return symbol

            if cls.board[0][1] == symbol and cls.board[0][2] == symbol:  # checks for top left vertical win
                return symbol

        # TOP MIDDLE TILE CHECK (1 check required, vertical down)
        if type(cls.board[0][1]) != int:
            count += 1
            symbol = cls.board[0][1]

            if cls.board[1][1] == symbol and cls.board[2][1] == symbol:  # checks for top middle vertical win
                return symbol

        # TOP RIGHT TILE CHECK  (2 check required, vertical down, top right diagonal)
        if type(cls.board[0][2]) != int:
            count += 1
            symbol = cls.board[0][2]

            if cls.board[1][2] == symbol and cls.board[2][2] == symbol:  # checks for top right vertical win
                return symbol

            if cls.board[1][1] == symbol and cls.board[0][2] == symbol:  # checks for top right diagonal win
                return symbol

        # MIDDLE LEFT TILE CHECK (1 check required, horizontal)
        if type(cls.board[1][0]) != int:
            count += 1
            symbol = cls.board[1][0]

            if cls.board[1][1] == symbol and cls.board[1][2] == symbol:  # checks for middle left horizontal win
                return symbol

        if type(cls.board[1][1]) != int:
            count += 1

        if type(cls.board[1][2]) != int:
            count += 1

        # BOTTOM LEFT TILE CHECK (1 check required, horizontal)
        if type(cls.board[2][0]) != int:
            count += 1
            symbol = cls.board[2][0]

            if cls.board[2][1] == symbol and cls.board[2][2] == symbol:  # checks for bottom left horizontal win
                return symbol

        if type(cls.board[2][1]) != int:
            count += 1

        if type(cls.board[2][2]) != int:
            count += 1

        if count == 9:
            return 'draw'

        return 'continue'


    @classmethod
    def show_board(cls):
        ele_count = 0
        row_string = ''
        for row in cls.board:
            for ele in row:
                row_string += str(ele) + '   '
                ele_count += 1
                if ele_count % 3 == 0:
                    print(row_string)
                    row_string = ''
                    ele_count = 0

    @classmethod
    def update_board(cls, num, symbol):
        pass


class Player:
    def __init__(self, symbol, name=None):
        self.name = name
        self.score = 0
        self.symbol = symbol

    def set_name(self, name):
        self.name = name

    def win_match(self):
        self.score += 1

def get_player_choice(chosen_player):
    if chosen_player.symbol == 'X':
        symbol = 'X'
    else:
        symbol = 'O'

    choices = []
    for row in Board.board:
        for ele in row:
            if type(ele) == int:
                choices.append(ele)

    Board.show_board()

    a = int(input("Select number of space to choose"))

    # Need to be able to handle user entering a string
    while a not in choices:
        a = int(input("Select number of space to choose"))


    if a == 1:
        Board.update(0, 0, symbol)

    elif a == 2:
        Board.update(0, 1, symbol)

    elif a == 3:
        Board.update(0, 2, symbol)

    elif a == 4:
        Board.update(1, 0, symbol)

    elif a == 5:
        Board.update(1, 1, symbol)

    elif a == 6:
        Board.update(1, 2, symbol)

    elif a == 7:
        Board.update(2, 0, symbol)

    elif a == 8:
        Board.update(2, 1, symbol)

    elif a == 9:
        Board.update(2, 2, symbol)

    Board.show_board()










def main():
    clear()
    # Setup the players
    player1 = Player('X')
    player2 = Player('O')

    print('Welcome to Tic Tac Tow\n')

    clear()
    player_1_name = input('Player 1, enter name\n')
    player1.set_name(player_1_name)
    player1.symbol = 'X'

    clear()
    player_2_name = input('Player 2, enter name\n')
    player2.set_name(player_2_name)
    player2.symbol = 'O'

    # Game Loop
    keep_playing = True

    while keep_playing:
        Board.reset_board()
        match_count = 0

        # Each game the other player gets to start the game
        if match_count % 2 == 0:
            first_mover = player1
        else:
            first_mover = player2

        current_mover = first_mover
        clear()
        print(f'Match Count: {match_count}')
        print(f'Player 1 wins: {player1.score}')
        print(f'Player 2 wins: {player2.score}\n')
        print('------------------\n')
        choices = ['1', '2']
        print('Choose a number')
        print(f'1 ---> "Play a game')
        print(f'2 ---> "Quit\n')

        a = input('--->')

        while a not in choices:
            a = input('--->')

        if a == '2':
            keep_playing = False
            break


        # Match loop
        while True:
            clear()
            print(f'{current_mover.name}, your turn!\n')
            get_player_choice(current_mover)
            state = Board.check_board()

            # state is either 'X', 'O', 'draw', 'continue'
            if state in ['X', 'O']:  # somebody won
                clear()
                print(f'{current_mover.name} wins!')
                print(f'+1 match point!')
                current_mover.win_match()
                match_count += 1
                a = input('Press enter to continue')
                break

            elif state == "draw":
                clear()

                print(f'Draw!')
                match_count += 1
                a = input('Press enter to continue')
                break


            if current_mover == player1:
                current_mover = player2

            else:
                current_mover = player1


if __name__ == '__main__':
    main()
