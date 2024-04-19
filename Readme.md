# Craps Game


This is a implementation of the game of Craps in Python.


## Description


Craps is a popular dice game, it involves rolling two six-sided dice and betting on the outcome.


The rules of the game are as follows:
- On the first roll:
  - If the sum of the dice is 7 or 11, the player wins.
  - If the sum is 2, 3, or 12, the player loses (this is known as "craps").
  - If the sum is any other number, that number becomes the "point".
- If the first roll doesn't immediately win or lose:
  - The player continues rolling until they either roll the point again (win) or roll a 7 (lose).


## Usage


To play the game, run the `play_craps()` function in the `main.py` file.
You can find code's functions in `Functions.py` file.


### Examples
```python


> The sum of dice is  6
You lose!


> The sum of dice is  6
Your goal_number is 6
The sum of dice is  9
You lose!


> Your goal_number is 9
The sum of dice is  7
The sum of dice is  7
The sum of dice is  10
The sum of dice is  6
The sum of dice is  12
The sum of dice is  4
The sum of dice is  5
The sum of dice is  4
The sum of dice is  7
The sum of dice is  12
You win!


```
