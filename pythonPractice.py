def replay():
  userInput = input('Thanks for playing do you want to play again? (y/n): ')
  if (userInput == 'y'):
    carFunctionalities()
  elif(userInput == 'n'):
    print('Thanks for playing have a great day!')
  else:
    print('Did not understand')
    replay()


def carFunctionalities():
  userInput = input('> ')

  if (userInput == "start"):
    print("The car has been started!")
    replay()
  elif(userInput == 'stop'):
    print("The car has been stopped")
    replay()
  elif(userInput == 'quit'):
    replay()
  else:
    print(f'Did not understand the command of {userInput}')
    replay()
  
carFunctionalities()