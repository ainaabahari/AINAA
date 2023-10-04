#!/usr/bin/env python

import random

def musicgenre():
    """Start a music genre guessing game."""
    print("Guess music genre!")
          
music =[
     "rock",
     "hip hop",
     "metal",
     "pop",
     "reggae",
     "classical",
     "jazz",
    ]

x = random.choice(music)
guess = None
print(x)

for trial in range(4):
    score=0
    while x!=guess:

     guess=str(input("what music genre am I thinking: "))

    if guess == x:
        
        print("correct! ".format (guess))
        score +=3
        break
        
    else:
        print("Incorrect.. try again".format(guess))
        
    

print (" ur score :",score)

musicgenre()

