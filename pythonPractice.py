import random

def gameReplay():
  replay = input('You are out of tries would like to start over? (y/n)?: ')

  if (replay == "y"):
    print("Good luck!")
    guessingGame()
  elif (replay == 'no'):
    print("Thanks for playing see you later!")
    return False
  else: 
    print("Didn't understand the input")
    gameReplay()

def guessingGame():
  secret_number = str(random.randint(0, 10))
  tries = 3

  print(secret_number)

  print("Welcome to the guessing game")

  while tries != -1:
    print(f"You currently have {tries} tries, left")
    
    guessedNumber = input("Guess a number: ")

    if (guessedNumber == secret_number):
      print(f"Success you've guessed the secret number which is {guessedNumber}!")
      break
    elif (tries != 0):
      print(f"The secret number isn't {guessedNumber}!")
    else: 
      replay = gameReplay()

      if (not replay):
        break

    tries = tries - 1
    
guessingGame()