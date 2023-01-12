class Game():
    def __init__(self):
        """
        Creates the gameboard for user inputs to be placed
        """
        self.cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def display(self):
        """
        Displays the gameboard to the terminal
        """
        print()
        print(f"{self.cells[0][0]} | {self.cells[0][1]} | {self.cells[0][2]}")
        print("-- --- --")
        print(f"{self.cells[1][0]} | {self.cells[1][1]} | {self.cells[1][2]}")
        print("-- --- --")
        print(f"{self.cells[2][0]} | {self.cells[2][1]} | {self.cells[2][2]}\n")

    def player_turn(self, player):
        """
        Takes in user input between values 1 and 3
        """
        player_choice = []
        print(f"\nPlayer {player}'s turn\n")
        while True:
            try:
                x = input("Enter your X coordinate (1-3):\n")
                y = input("Enter your Y coordinate (1-3):\n")
                if x.isdigit() and y.isdigit():
                    x = int(x)
                    y = int(y)
                else:
                    raise ValueError()
                if 1 <= x <= 3 and 1 <= y <= 3:
                    break
                raise ValueError()
            except ValueError:
                print("Invalid input. Please enter values between 1 and 3")
                continue
        player_choice = [y - 1, x - 1]
        self.update_cell(player_choice[0], player_choice[1], player)
        # return player_choice

    def update_cell(self, cell_y, cell_x, player):
        """
        Appends user input to the board
        """
        self.cells[cell_y][cell_x] = player



def main():
    """
    Main function
    """
    print("\nWelcome to the Noughts and Crosses Terminal Game")
    board = Game()
    board.display()
    player = 'X'
    winner = None
    while winner is None:
        board.player_turn(player)
        board.display()
        # print(player_choice)


main()
