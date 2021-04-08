import random
fixedNumber = random.randint(0,101)
noOfGuesses = 0
numberGuessed = -1
while(noOfGuesses<10 or numberGuessed == fixedNumber):
    numberGuessed = int(input("Guess a number between 0-100:"))
    noOfGuesses+=1
    if(numberGuessed < fixedNumber):
        print("The number you guessed is small")
    elif(numberGuessed == fixedNumber):
        print("You guessed the correct number")
        print("Number of chances taken:",noOfGuesses)
        break;
    else:
        print("The number you guessed is larger")