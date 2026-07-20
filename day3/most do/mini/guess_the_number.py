Secret = 7
while True:
    Guess = int(input("Guess the number: "))
    if Guess == Secret:
        print("You guessed it!")
        break
    else:
        print("Wrong guess!")