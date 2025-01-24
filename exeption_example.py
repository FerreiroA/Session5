name = input("What is your name? ")
# Lets write this in a simpler way
age2 =  input(f"How old are you {name}? ")
try:
    age2 = int(age2) # Here there can be. a problem
    print(f"{name}, you were born in {2024-age2}")
except ValueError:
    print("Please enter a vaid value for age")
    print("I can also print this in case of error that I prevented")
except ZeroDivisionError:
    print("You cannot divide by 0!")
except:
    print("This is another type of error")
else: # This is for no exeption
    print("Thank you for playing as expected")
finally: # This will be excecuted no mater what at the very end
    print("Thanks for playing the game")