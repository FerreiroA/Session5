# You have 3 lives. I roll the dice. If I roll 6, you win.
# If not a 6, you lose 1 life.

from random import randint

lives = 3
while lives > 0:
    roll = randint(1, 6) # make sure to not put a: and b:1!
    if roll == 6:
        print("you rolled a 6 you win!")
        break # this exits the while even if lives still > 0
    # There is no other way to get here, unless I did not roll a 6
    print(f"You rolled a {roll}! You lose a life")
    lives -= 1
    print(f"lives left: {lives}")
else: # else from while!
    print("You lost!")