'''Project Description:

This is a simple command-line game of "Snake, Water, Gun," a variation of the classic "Rock, Paper, Scissors" game.
In this game, both the player and the computer choose one of three options: snake (s), water (w), or gun (g).
The game determines the winner based on predefined rules:

Snake (s) drinks water (w), so snake wins.
Water (w) douses gun (g), so water wins.
Gun (g) kills snake (s), so gun wins.
If both the player and computer choose the same option, the game results in a tie.
The logic for determining the winner is implemented in the gamewin() function, which compares the choices and returns the result. 
The computer's choice is randomly generated, and the player's choice is taken as input. The game then announces the winner based on these inputs '''

import random
def gamewin(comp , you):
  if comp == you:
   return None
  elif comp == 'w':
   if you == 's':
    return True
   elif you == 'g':
    return False
  elif comp == 'g':
   if you == 'w':
    return True
   elif you == 's':
    return False
  elif comp == 's':
    if you == 'g':
        return True
    elif you == 'w':
        return False


print("Computer's turn : snake(s) water(w) gun(g)")

randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'


you = input("Your's turn : snake(s) water(w) gun(g)")

print(f"Computer chose: {comp}")
print(f"You chose: {you}")

result = gamewin(comp, you)
if result == None:
    print("this game is a tie")
elif result :
    print("you win")
else:
    print("you lose")
