"""
Erkinbek
11/13/2022
Take a number (input) from the user and guess a
randomly generated number. Provide the user with
an opportunity to guess higher or lower, depending on
the randomly generated number. Remember to use python
module(s) and nested if…else statements in your code"""

user_num = int(input("Please guess number between 1 and 100"))
import random
gen_number = random.randint(1, 100)
for i in range(1, 100):
    if user_num == gen_number:
        print("You guessed")
        break
    elif gen_number and user_num < 50:
        print("Please guess higher number")
        user_num = int(input("Please guess number between 1 and 100 "))
    elif gen_number and user_num > 50:
        print("Please guess lower")
        user_num = int(input("Please guess number between 1 and 100 "))