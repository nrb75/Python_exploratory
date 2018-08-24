# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random


#allow user to input letters, and then check if the letters are in the word.
#we will limit the user to 10 incorrect guesses

secret='jello'

correctguesses=0
wrongguesses=0
attemptedword = ['*']*len(secret)

print('guess the letters in my ' +str(len(secret)) +' letter word' )

while wrongguesses <5:
    guess=input()
    guess = str(guess)
    if guess in secret:
        #index=secret.find(guess)
        index= [i for i, letter in enumerate(secret) if letter == guess]#this is a list of indexes that letter matches, it may be more than one
        for i in index:
            attemptedword[i]=guess
        correctguesses+=1
        print(attemptedword)
    if guess not in secret:
        wrongguesses+=1
        print('wrong guess, try again')
    if attemptedword==secret:
        break
    if attemptedword==secret:
        print('good job, you win!')
        
    