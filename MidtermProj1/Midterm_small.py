# Elick Coval
# 00845725
# Elick_Coval@student.uml.edu
#
# I chose the coin flip simulation, I created a coin class that
# handles all of the flipping and organizes output
#
# To use the program, run it and follow the prompts
# User will be asked how many times they would like to flip
# and then be shown the resulting flip amounts and be asked
# if they would like to have another go

import random

# game loop boolean
keepFlipping = True


# class to keep track of coin flips
class Coin:

    # initialize new list every time class is created
    def __init__(self):
        self.flipResults = []

    # takes the amount of times user wants to flip and
    # randomly adds heads or tails to class list that number of times
    def flipCoin(self, times):
        for x in range(times):
            self.flipResults.append(random.choice(['Heads', 'Tails']))

    # count the number of heads or tails in the list and return a string
    def count(self):
        heads = 0
        tails = 0
        for x in self.flipResults:
            if x == 'Heads':
                heads += 1
            else:
                tails += 1
        return "There were " + str(heads) + " heads and " + str(tails) + " tails"

    # used for testing
    def print(self):
        print(self.flipResults)


# main loop
while keepFlipping:
    coin = Coin()
    results = ""

    # try block for catching invalid input
    try:
        num = int(input("How many times would you like to flip?"))
        # raise different errors for different problem scenarios
        if num < 0:
            raise TypeError
        elif num > 100000:
            raise ValueError

        # flip the coin specified amount of times
        coin.flipCoin(num)
        # store the returned string result
        results = coin.count()
        # print it
        print(results)
    except (TypeError, ValueError) as e:
        if isinstance(e, ValueError):
            print("Please enter an integer less than 100000")
        elif isinstance(e, TypeError):
            print("Please enter a positive number")

    # after flip output
    yes = {'y', 'Y', 'Yes', 'yes'}
    no = {'n', 'N', 'No', 'no'}
    again = str(input("Would you like to flip again? (Y)es (N)o"))
    if again in no:
        keepFlipping = False
        print("Thanks for flipping :)")
    else:
        pass

