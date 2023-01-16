"""
Import random for computer_turn to randomly generate integers
"""
import random


class Game:
    """
    Main class that holds the main gameboard and calls methods
    to run through the game.
    """
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
        print(f"{self.cells[2][0]} | {self.cells[2][1]} | {self.cells[2][2]}")
        print()

    def choose_players(self):
        """
        Allows user to choose 1 player or 2 players
        Input will be deemed as invalid if any other value other than 
        the numbers 1 or 2 are entered.
        """
        while True:
            try:
                player_amount = input("Enter amount of players (1 or 2):\n")
                if player_amount.isdigit():
                    player_amount = int(player_amount)
                else:
                    raise ValueError()
                if 1 <= player_amount <= 2:
                    break
                raise ValueError()
            except ValueError:
                print("Please enter a value 1 or 2")
        return player_amount

    def swap_player(self, player):
        """
        Changes player orientation.
        After each turn the player variable will be changed to the opposite.
        """
        if player == "X":
            player = "O"
        else:
            player = "X"
        return player

    def check_cell(self, cell_y, cell_x, player):
        """
        Checks if space is free for user input
        If space is not free then user will be required to re-enter their input
        """
        if self.cells[cell_y][cell_x] == " ":
            self.update_cell(cell_y, cell_x, player)
            return True
        return False

    def update_cell(self, cell_y, cell_x, player):
        """
        Appends user input to the board
        """
        self.cells[cell_y][cell_x] = player

    def player_turn(self, player, game):
        """
        Takes in user input between values 1 and 3.
        The input will return invalid if any values outside of these
        parameters are entered. The user will be prompted to re-enter their
        input within the given range.
        As the paramaters are between 1 and 3 the value 1 has been taken off
        each inputted value to fit the 0 indexing of the self.cells list.
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

    def computer_turn(self, player, board):
        """
        Randomly generated computer's turn.
        The computer will generate random X and Y coordinates within
        the range of 0 and 2.
        This method also calls for a check to ensure the randomly generated 
        coordinates have not already been taken.
        """
        player_choice = []
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        player_choice = [y, x]
        cell = board.check_cell(player_choice[0], player_choice[1], player)
        if cell is False:
            board.computer_turn(player, board)

    def check_winner(self, winner, player):
        """
        Checks all possible win conditions

        If theres no win after all spaces are filled winner returns as a tie
        """
        tie = self.check_tie()
        if all(
            [
                self.cells[0][0] == player,
                self.cells[0][1] == player,
                self.cells[0][2] == player,
            ]
        ):
            winner = player
        elif all(
            [
                self.cells[1][0] == player,
                self.cells[1][1] == player,
                self.cells[1][2] == player,
            ]
        ):
            winner = player
        elif all(
            [
                self.cells[2][0] == player,
                self.cells[2][1] == player,
                self.cells[2][2] == player,
            ]
        ):
            winner = player
        elif all(
            [
                self.cells[0][0] == player,
                self.cells[1][0] == player,
                self.cells[2][0] == player,
            ]
        ):
            winner = player
        elif all(
            [
                self.cells[0][1] == player,
                self.cells[1][1] == player,
                self.cells[2][1] == player,
            ]
        ):
            winner = player
        elif all(
            [
                self.cells[0][2] == player,
                self.cells[1][2] == player,
                self.cells[2][2] == player,
            ]
        ):
            winner = player
        elif all(
            [
                self.cells[0][0] == player,
                self.cells[1][1] == player,
                self.cells[2][2] == player,
            ]
        ):
            winner = player
        elif all(
            [
                self.cells[2][0] == player,
                self.cells[1][1] == player,
                self.cells[0][2] == player,
            ]
        ):
            winner = player
        elif tie is not True:
            winner = "Tie"
        else:
            winner = None
        return winner

    def check_tie(self):
        """
        Function to check if the board is full.
        If there are no empty spaces this method will return False.
        If there are empty spaces the method will return True.
        """
        empty_space = " "
        tie = any(empty_space in sublist for sublist in self.cells)
        return tie

    def play_again(self, winner):
        """
        Function to restart the game or end the program
        after a game has been completed.
        The user is unable to enter any values except Y(y) or N(n).
        If a value is entered that isn't either Y or N the user will
        be asked to enter parameters within the conditions given.
        """
        while winner is not None:
            try:
                restart = input("\nWould you like to play again? (Y/N):\n")
                if restart.upper() == "Y":
                    return True
                if restart.upper() == "N":
                    return False
                raise ValueError()
            except ValueError:
                print("Invalid input. Please enter Y or N")
                continue


def main():
    """
    Main function
    """
    print("\nWelcome to the Noughts and Crosses Terminal Game")
    while True:
        game = Game()
        game.display()
        player = ""
        winner = None
        num_of_players = game.choose_players()
        while winner is None:
            player = game.swap_player(player)
            game.player_turn(player, game)
            game.display()
            winner = game.check_winner(winner, player)
            if winner is not None:
                break
            if num_of_players == 1:
                player = game.swap_player(player)
                print("Computer's Turn")
                game.computer_turn(player, game)
                game.display()
                winner = game.check_winner(winner, player)

        if winner == "Tie":
            print("You have tied, no winner this time!")
        else:
            print(f"Winner is player {winner}!")

        restart = game.play_again(winner)
        if restart is True:
            continue
        if restart is False:
            print("\nThanks for playing!")
            break


main()
