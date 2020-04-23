import random
easy = random.randint (1,10)
medium = random.randint (1,20)
hard = random.randint (1,50)
guessesTaken = 0
my_name = input("Hello, What is your name? ")
difficulty = input("Well, "+ my_name + ". What dificulty would you like ? easy medium or hard? ").lower()
if difficulty == "easy":
    number = easy
    guessLen = 6
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 10")
    
if difficulty == "medium":
    number = medium
    guessLen = 4
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 20")
    
if difficulty == "hard":
    number = hard
    guessLen = 3
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 50")
    
while guessesTaken < guessLen:
    guess = int(input('Take a guess. ')) 
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print('Your guess is too low. You have' + str(guessLen - guessesTaken) + ' guess left')
        
    if guess > number:
        print('Your guess is too high. You have' + str(guessLen - guessesTaken) + ' guess left')
        
    if guess == number:
        break
    
if guess == number:
    guessesTaken = str (guessesTaken)
    print('You got it right, ' + my_name + '! You guessed my number in ' + guessesTaken + ' guesses!')
    
if guess != number:
    number = str (number)
    print('Nope. The number I was thinking of was ' + number)
