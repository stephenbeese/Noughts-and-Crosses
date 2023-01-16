# Noughts and Crosses Terminal Game
 
![Responsive](/assets/images/responsive.png)
 
## How To Play
<hr>
Noughts and Crosses is an in-terminal version of a classic pen-and-paper game Tic-Tac-Toe, more commonly known in the UK as Noughts and Crosses.
 
The aim of the game is to match 3 of your pieces, horizontally, vertically or diagonally.
 
In this version, a user will enter the number of players (1 or 2), determining whether they will be playing with a friend or the randomly generated computer.
 
The player 'X' will then be asked to input an X coordinate and then a Y coordinate of where they wish to place their piece.
 
The player will then switch to 'O' and will be asked for an X and Y coordinate. This pattern alternates until either a player has matched 3 of their pieces or all the spaces have been filled resulting in a tie.
 
## Features
<hr>
 
### Existing Features
 
#### 1 and 2 player modes
- The user has a choice to play one or two players.
- In one-player mode, the user plays against a randomly generated computer as 'O'.
- In two-player mode both X and O require user input allowing the user to play with a friend
 
![Players](/assets/images/players.png)
 
#### Random computer-generated turns
- If a user selects 1 player mode they will play against a randomly generated computer turn.
- The computer turn uses the random library to generate these numbers. The numbers being generated are integers between 0 and 2 to fit the indexing of the game board.
- I decided to add a computer turn so users can play on their own. 
 
![Computer Turn](/assets/images/computer-turn.png)
 
#### Accepts user input
This program accepts user input to find:
- How many players there are
- What space the player would like to fill
- Whether they would like to play again after a game has been completed.
 
![User Input](/assets/images/user-input.png)
 
#### Input validation and error checking
- The user is unable to:
   - Enter coordinates outside of the grid
   - Enter letters when asking for numbers
   - Enter numbers when asking for letters
   - Enter the same space twice
   - Enter the number of players outside of 1 or 2
 
Trying any of these will print error messages to the user asking them to retry within the parameters given.
Here are some examples:
 
![Amount of Players Validation](/assets/images/players-validation.png)
 
![Taken Space Validation](/assets/images/input-validation.png)

![Player Input Validation](/assets/images/input-validation-2.png)
 
 
#### Play Again
- After the user has played the game they will be asked if they want to start again. If a user enters 'Y' the program’s main loop will start again. Starting the loop again, will reset the game board and then carry on with a new game.
- If the user selects No the program will end.
 
![Play Again](/assets/images/play-again.png)
 
### Future Features
- Play against a harder computer that can foresee moves
- Allow player to choose 'X' or 'O'
 
## Data Model
<hr>
I decided to use a Game class model. The game creates an instance of Game class to store the gameboard.
 
The class has methods that are used to play the game. Such as:
- <code>display</code> method to print out the current board after each turn.
- <code>choose_players</code> method receives user input for 1 or 2 players. This is called at the start of each game.
- <code>swap_player</code> method changes player <code>X</code> to <code>O</code>. The method is called after each turn.
- <code>check_cell</code> method checks if the space inputted by the user or randomly generated computer has already been taken. If the space is free the method will call the <code>update_cell</code> method and return <code>True</code>. Otherwise, it will return <code>False</code>. When <code>False</code> has been returned it will recall either <code>player_turn</code> or <code>computer_turn</code> depending on the turn to retry the input.
- <code>update_cell</code> method will be called if it has passed the <code>check_cell</code> method. This means the cell won't update if it's already taken.
- <code>player_turn</code> method to receive user input. The method then creates an empty <code>player_choice</code> list to hold the X and Y coordinates which are used to determine the place in the game board list. The user will only be able to input numbers 1-3 for both the X and Y coordinates. If the user tries inputting values outside of this range it will raise a <code>ValueError</code> and ask the user to input values within that range. If the user inputs a value that has already been taken, the <code>check_cell</code> method will return <code>False</code> and execute a <code>display</code> method and <code>print</code> to inform the user and then recall the <code>player_turn</code> to retake their input. This will loop until their input is valid.
- <code>computer_turn</code> method to recieve randomly generated input. The input is checked through the <code>check_cell</code> and appends through the <code>update_cell</code> method if it returns <code>True</code>. If <code>check_cell</code> returns <code>False</code>, the computer will regenerate random numbers and check again. This will loop until it returns <code>True</code>.
- <code>check_winner</code> method checks through 8 possible win conditions. It will check for various wins vertically, horizontally and diagonally to see if these spaces are equal to the player that has just had their turn (X or O). If a win condition is met the method will return the player (X or O) as the winner.
- <code>check_tie</code> method to check if there are any empty spaces on the board. If there are empty spaces this method will return <code>True</code>. If not, it will return <code>False</code>. This method is called through the <code>check_winner</code> method. If no win conditions are true and <code>check_tie</code> is <code>check_winner</code> will return the winner as <code>"Tie"</code>
- <code>play_again</code> method asks the user if they would like to play again after a game has been completed. If the user enters Y, the main() function while loop will restart. If the user enters N the program will close and thank them for playing.

![Flow Chart](/assets/images/flow-chart.png)
 
## Testing
<hr>
 
### Bugs
#### Solved Bugs
- When writing this project, I encountered a bug where after a player wins in 1-player mode, the computer would still be able to take their go despite the user winning previously. To fix this I added breaks in the <code>while winner is None:</code> loop in the main() function. The break comes after the win state has been checked which <code>if winner is not None:</code> the code will break out of the loop and announce the winner.
#### Remaining Bugs
- No bugs remaining
### Validator Testing
- PEP8
   - No errors were returned through [CI Python Linter](https://pep8ci.herokuapp.com/)
 
![PEP8 Validator](/assets/images/pep8.png)
 
## Deployment
<hr>

Steps for deployment:
- Add requirements to requirements.txt file by typing into the terminal <code>pip3 freeze > requirements.txt</code> and pressing Enter.
- Once the .txt file has been updated, create a new app on your Heroku.
- Navigate to settings and find the buildbacks section. Once in the buildbacks section add <code>Python</code> and <code>NodeJS</code> in that order.
- After the buildbacks have been done, navigate to the deployment tab. Scroll down until you see 'Deployment method' and link the GitHub repository to the Heroku app.
- Once these are linked you are ready to click 'Deploy Branch' and the app will start being built.
- Once the app has been built you are then able to view the site.
 
 
You can find the live link here: [Noughts and Crosses](https://noughts-and-crosses1.herokuapp.com/)
 
## Credits
<hr>
- Code Institute for the deployment terminal