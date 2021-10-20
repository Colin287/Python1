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
#import time
#import random
#Create word art by using arrays and loops (loop in a loop)

#print("Here's a face")
#print()

#art = [['', '*', '', '*'],
       #[' ', '=', '', '', ''],
       #['-', '-', '-', '-', '-']]

#for i in art:
    #for j in i:
        #print(j, end=" ")
    #print()

#time.sleep(3)
#print()
#print()

#Create a coin flip

#print("Welcome to the coin flip, please enter 1 or 0:  ")

#user_input = int(input())

#if user_input != 1 | 0:
    #print("Error, please enter a 1 or 0")

#coin_state = random.randint(0, 1)

#if coin_state == user_input:
    #print("Your guess was correct!")
#else:
    #print("Your guess was incorrect")



#Programming Assignment 4
#By: Colin Campbell
#Date: 10/3/2021
import random
from random import randrange




"""
#display the board exactly as show in the example
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    #Don't know why there is a comma next to the 9 couldnt find how to remove it.
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] +   '   | '  + board[0][1] + '     |  ' + board[0][2] + '    |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1][0] + '   | ' + board[1][1] + '     |  ' + board[1][2] + '    |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[2][0] + '   | ' + board[2][1] + '     |  ' + board[2][2] + '   | ')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def enter_move(board):
    #The function accepts the board's current status, asks the user about their move,
    #checks the input, and updates the board according to the user's decision.

    while True:

        user_move = int(input("Pick a location on the board to make your move (1-9)"))
        accepted_range = range(1, 9)
        if user_move in accepted_range:
            print("")
        else:
            print("please enter a number from 1-9:  ")
        #figure out if python has switch statements for this next time
        if user_move == 1:
            board[0][0] = 'o'
        elif user_move == 2:
            board[0][1] = 'o'
        elif user_move == 3:
            board[0][2] = 'o'
        elif user_move == 4:
            board[1][0] = 'o'
        elif user_move == 5:
            board[1][1] = 'o'
        elif user_move == 6:
            board[1][2] = 'o'
        elif user_move == 7:
            board[2][0] = 'o'
        elif user_move == 8:
            board[2][1] = 'o'
        elif user_move == 9:
            board[2][2] = 'o'
        break

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_spaces
    free_spaces = [ ]

    #iterate through the whole board
    for row in range(0, 3):
        for column in range(0, 3):
            if board[row][column] == 'x' or board[row][column] == 'o':
                continue
            else:
                free_spaces.append(([row],[column]))
    #print the result
    print(free_spaces)

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    #use this for the while loop to keep runnign the turns

    #top 3 across
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        print("The user playing with ", sign, "wins the game")
        return True

    #middle 3 across
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        print("The user playing with ", sign, "wins the game")
        return True

    #bottom 3 across
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        print("The user playing with ", sign, "wins the game")
        return True

    #3 vertical left side
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        print("The user playing with ", sign, "wins the game")
        return True

    #3 down the middle
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        print("The user playing with ", sign, "wins the game")
        return True

    #3 vertical right side
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        print("The user playing with ", sign, "wins the game")
        return True

    #3 zig zag 1
    if board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        print("The user playing with ", sign, "wins the game")
        return True

    #3 zig zag 2
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        print("The user playing with ", sign, "wins the game")
        return True

def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:

        row = randrange(3)
        column = randrange(3)

        #check if it's an empty space before placing
        if ([row], [column]) not in free_spaces:
            continue
        else:
            board[row][column] = 'x'
            return


#Code for running the game / calling fucntions

#create the initial board
board = [['1', '2', '3'], ['4', 'x', '6'], ['7', '8', '9,']]
player = 'o'
computer = 'x'
print("Welcome to Python Tic-Tac-Toe")
print(display_board(board))

while victory_for(board, player) != True:
    #player move
    enter_move(board)
    #computer move
    make_list_of_free_fields(board)
    draw_move(board)
    display_board(board)
"""

import random

print("This branch will demonstrate the random module")

correct_number = random.randint(1, 5)

user_pick = int(input("Please pick a number 1-5:  "))

if user_pick != correct_number:
    print("Sorry, wrong number, try again")
    print("The correct number was: ", correct_number)

else:
    print("You chose the correct number!")

