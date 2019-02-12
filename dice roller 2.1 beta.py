#the goal of the python dice roll calculator is to build a random number generator that can add bonuses, subtract debuffs, and display advantages and disadvantages
print("what is your stat in this skill?")
y = int(input())
stat = y
print('What die shall you cast?')
z = int(input())
from random import *
roll = randint(1,z)
print(roll, '+', stat, '=', roll + stat)
input()
