import random
def NumberGuessingGame():   
        chances = 0
        randomnumber=random.randint(1,10)
        while chances<5:
            guess = int(input("Enter the guessed number: "))
            if guess == randomnumber:
                print("Hurray! You got it!")
                break
            elif guess < randomnumber:
                print(" Your number is less than the random number")
            else:
                print(" Your number is greater than the random number")
            chances += 1
        if not chances<5:
            print("You loose!!! The number is", randomnumber)

NumberGuessingGame()
