class Game():
    def __init__(self):
        self.cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def display(self):
        print()
        print(f"{self.cells[0][0]} | {self.cells[0][1]} | {self.cells[0][2]}")
        print("-- --- --")
        print(f"{self.cells[1][0]} | {self.cells[1][1]} | {self.cells[1][2]}")
        print("-- --- --")
        print(f"{self.cells[2][0]} | {self.cells[2][1]} | {self.cells[2][2]}\n")

    def player_turn(self, player):
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
        return player_choice


def main():
    """
    Main function
    """
    print("\nWelcome to the Noughts and Crosses Terminal Game")
    board = Game()
    board.display()
    player = ''
    winner = None
    while winner is None:
        player_choice = board.player_turn(player)
        print(player_choice)




main()
