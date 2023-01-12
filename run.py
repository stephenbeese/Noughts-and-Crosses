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

    def check_cell(self, cell_y, cell_x, player):
        """
        Checks if space is free for user input
        If space is not free then user will be required to re-enter their input
        """
        if self.cells[cell_y][cell_x] == " ":
            self.update_cell(cell_y, cell_x, player)
            return True
        return False

    def swap_player(self, player):
        """
        Changes player orientation
        """
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        return player

    def player_turn(self, player, game):
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
        cell = game.check_cell(player_choice[0], player_choice[1], player)
        if cell is False:
            game.display()
            print("This space is already occupied, please try again")
            game.player_turn(player, game)

    def update_cell(self, cell_y, cell_x, player):
        """
        Appends user input to the board
        """
        self.cells[cell_y][cell_x] = player

    def check_winner(self, winner, player):
        if all([self.cells[0][0] == player, self.cells[0][1] == player, self.cells[0][2] == player]):
            winner = player
        elif all([self.cells[1][0] == player, self.cells[1][1] == player, self.cells[1][2] == player]):
            winner = player
        elif all([self.cells[2][0] == player, self.cells[2][1] == player, self.cells[2][2] == player]):
            winner = player
        elif all([self.cells[0][0] == player, self.cells[1][0] == player, self.cells[2][0] == player]):
            winner = player
        elif all([self.cells[0][1] == player, self.cells[1][1] == player, self.cells[2][1] == player]):
            winner = player
        elif all([self.cells[0][2] == player, self.cells[1][2] == player, self.cells[2][2] == player]):
            winner = player
        elif all([self.cells[0][0] == player, self.cells[1][1] == player, self.cells[2][2] == player]):
            winner = player
        elif all([self.cells[2][0] == player, self.cells[1][1] == player, self.cells[0][2] == player]):
            winner = player
        else:
            winner = None

        return winner


def main():
    """
    Main function
    """
    print("\nWelcome to the Noughts and Crosses Terminal Game")
    game = Game()
    game.display()
    player = ''
    winner = None
    while winner is None:
        player = game.swap_player(player)
        game.player_turn(player, game)
        game.display()
        winner = game.check_winner(winner, player)


main()
