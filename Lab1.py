from random import *

##Heather Anne Amo
##used https://www.codementor.io/kaushikpal/user-defined-functions-in-python-8s7wyc8k2 to help me remember how to write functions
##used https://pythonspot.com/en/random-numbers/ to remind me how to use the random number generator
##used https://www.cyberciti.biz/faq/python-convert-string-to-int-functions/ because I forgot how to convert string to int



def randInt():
    return randint(1,10) #here's our random integer

def respond(guess1, r):
    #while(numTest(guess1)):
        guess = numTest(guess1)
        while (guess != r & numTest(guess)):
            if (guess>r):
                userIn=input("Too high, guess again.")
                guess=numTest(userIn)
            elif (guess<r):
                userIn=input("Too Low, guess again.")
                guess=numTest(userIn)

        print(" Good Job! You got it!")


def main():
    play=input("Would you like to play a number guessing game?  Type y to play.")
    play=play.lower()

    while play=='y':
        ra=randInt() #get random integer
        stGuess=input("Guess a number between 1 and 10.")
        respond(stGuess,ra)
        play=input("Type y if you want to play again.")

def numTest(strGuess):
    try:
        i=int(strGuess)
        return i
    except ValueError: ##Error if wrong answer is entered repeatedly and then correct answer is entered.
        t = input("Guess must be a number. Please try again.")
        if(numTest(t)):
            return int(t)

main()

