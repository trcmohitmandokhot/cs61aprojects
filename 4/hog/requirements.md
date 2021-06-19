# Hog Project
Goal - Develop a simulator and strategies for a dice game called Hog. 

**Rules**
Two players.   
Alternate turns.  
First one to end a turn with 100 points - Wins the game.  
In each turn,  
- The player choses how many dices to roll.
	- Maximum of 10 dices.  
- Player's score = Sum of values on each dice.  
**Special rules** 
*(Choice of dice, return value on dice, # of dice now vs. prev, total score)*  
1. Pig Out - Total Turn Score = 1, if even one dice returns a unit value.
2. Free Bacon - If player choses to roll 0 dice then, Total Score = 10 - min(opposcore_tens,opposcore_units)
3. Feral Hogs - # of dice now - # of dice previous == 2, then 3 bonus points. 
4. Swine Swap - If (player1 score left)x(player1 score right) = (player2 score left)x(player2 score right): Swap scores. For single digit scores - Repeat digit. 
