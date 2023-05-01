# Multiplayer Game - Galaxy Wars!!!

## Divya Podila 
## Naveen kumar Poka

### Description:

The Pygame module is being used in this code to create a game of TwoPlayer Game - Projectile Dual. The code This is a two player game that is slow turned base game and sets up the display with a defined width and height.A few variables for the game state, including the values on the board for the players - the angle is initialized by the code.The code contains numerous functions, such as drawboard1,drawboard2, gameover, which displays a "Game Over" message after the game is over, and some Events for keybooard keys press, which modifies the game's state based on a player-specified direction of throw of sword(up, down).

The Game Requirements that were met during the project are :
2 players where each player will go one after the other taking turns.
Each player will launch a sword (projectile) toward the other player, where the projectile is 2D with gravity.
The projectile is animated.( sword throw )
Collision detection between propelled object and players as well as game world
Collision between propelled object and player will result in death 
Collision between propelled object and game world will result in some minor altering of terrain - bomb with sound track of explosion.
Physics for projectile implemented -  gravity: 2D projectile
Projectile can alter the trajectory with the angle. ( keyboard inputs UP and Down arrows for Player1 and 'W' and 'S' keys for Player2)
Added gravity setting.

##  Assignments Folder
### Files
 
|   #   | Folder Link                                            | Assignment Description                                                            |
| :---: | -------------------------------------------------------| ----------------------------------------------------------------------------------|
|   1   |[Playersinfo.py](/Assignments/P03/Playersinfo.py)       |This code is attempting to build a game of 2D projectile using the Pygame library. |
|   2   |[asteroids.py](/Assignments/P03/asteroids.py)           |Sprites of the players (player1 & player2) used for Animation (During collision)   |
|   3   |[background.py](/Assignments/P03/background.py)         |Sprites of the players (player1 & player2) used for Animation (During collision)   |
|   4  |[comms.py](/Assignments/P03/comms.py)                    |Sprites of the players (player1 & player2) used for Animation (During collision)   |
|   5   |[gameClass.py](/Assignments/P03/gameClass.py)           |Sprites of the players (player1 & player2) used for Animation (During collision)   |
|   6   |[main.py](/Assignments/P03/main.py)                     |Sprites of the players (player1 & player2) used for Animation (During collision)   |
|   7   |[messages.py](/Assignments/P03/messages.py)             |Sprites of the players (player1 & player2) used for Animation (During collision)   |
|   8   |[multiplayer.py](/Assignments/P03/multiplayer.py)       |Sprites of the players (player1 & player2) used for Animation (During collision)   |
|   9   |[ship.py](/Assignments/P03/ship.py)                     |Sprites of the players (player1 & player2) used for Animation (During collision)   |
|   10   |[simple_comms.py](/Assignments/P03/simple_comms.py)    |Sprites of the players (player1 & player2) used for Animation (During collision)   |



### Instructions

- Make sure you install libraries `pygame.py` , 'Math' , 'time' & 'mixer'
- When you run the program, 
PLAYER 1 :
you'll have to use the arrow keys (UP,DOWN) to set the angle.
once angle is set, hit 'ENTER' to throw the sword at the opposite player.
If Gameover message comes up, hit the 'BACKSPACE' button to restart the game.
- Also make sure to add 'All_images' folder inside the game folder for the program to run without errors.
PLAYER 2:
you'll have to use the arrow keys ('W' & 'S') to set the angle.
once angle is set, hit 'ENTER' to throw the sword at the opposite player.
If Gameover message comes up, hit the 'BACKSPACE' button to restart the game.

-Additional instructions :
By default, always Player 1 starts the game. A horizontal line appears for player1 to set angle.
If you aim at the ground, a bomb explodes with an explosion sound.
If you aim at the wall, knife hits the wall and a knife sound is heard and its the oppposite player's turn to play.
If you aim at the player only then player dies and a Victory + Game over message is displayed.

