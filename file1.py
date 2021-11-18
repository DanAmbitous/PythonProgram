import math

def unitOfWeight(run):
  if (run):
    userInput = input("Would you want to kg or lbs?: ")

    if (userInput == "kg"):
      weightTeller(True, True)
    elif (userInput == "lbs"):
      weightTeller(False, True)
    else:
      print(f"Invalid input of {userInput}")
      unitOfWeight(run)
  else:
    print("Thank you for using our program")

def weightTeller(kg, repeat):
  print(repeat)
  while repeat:
    try:      
      if kg:
        kg = int(input("Please input kg: "))
        lbs = int(kg * 2.2)

        print(f'{kg}kg is {lbs}lbs')

        return
      else:
        lbs = int(input("Please input lbs: "))
        kg = int(lbs / 2.2)

        print(f'{lbs}lbs is {kg}kg')

        return
    except:
      print(kg)
      weightTeller(kg, False)

    toRedo()

def toRedo():
  userInput = bool(int(input("Would you like to redo? (1, 0): ")))
  print(userInput, type(userInput), 'asdf')
  if (userInput): return

  unitOfWeight(userInput)

unitOfWeight(True)

