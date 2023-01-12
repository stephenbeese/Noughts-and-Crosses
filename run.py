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


def main():
    """
    Main function
    """
    print("\nWelcome to the Noughts and Crosses Terminal Game")
    board = Game()
    board.display()


main()
