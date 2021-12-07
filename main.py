#This is Branch "strings1" for Programming Assignment 6
import sys

def encase(): #wraps commands in double backslashes
    args = str(sys.argv)
    print(args.join("//"))

def clean(): #remove single quotes
    args = str(sys.argv)
    print(args.replace("'", ""))


print ('Arguments: ', len(sys.argv))
print ("Your arguments are: , ", str(sys.argv))

print("Here they are wrapped in backslashes: ")
print(encase())

print("Here they are with all single quotes removed: ")
print(clean())


