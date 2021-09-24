#Programming Assignment 2
# By: Colin Campbell
# Date: 9/16/2021

# Part 1
# name = input("Please enter your name: ")
# print(name)

# Part 2
# user_num = int(input("Please enter a number: "))
# num_multi = user_num ** 2
# print(num_multi)

# Part 3
#user_word = str(input("Please enter a single word: "))
#user_word_length = len(user_word)
# print("Your word has")
# print(user_word_length)
# print("letters")

# Had to print it weird like that it kept throwing an error i didn't understand





# Coding Assignment 3
# By: Colin Campbell
# Date: 9/24/2021
import time
import random
#Create word art by using arrays and loops (loop in a loop)

print("Here's a face")
print()

art = [['', '*', '', '*'],
       [' ', '=', '', '', ''],
       ['-', '-', '-', '-', '-']]

for i in art:
    for j in i:
        print(j, end=" ")
    print()

time.sleep(3)
print()
print()

#Create a coin flip

print("Welcome to the coin flip, please enter 1 or 0:  ")

user_input = int(input())

if user_input != 1 | 0:
    print("Error, please enter a 1 or 0")

coin_state = random.randint(0, 1)

if coin_state == user_input:
    print("Your guess was correct!")
else:
    print("Your guess was incorrect")
