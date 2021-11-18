import math

def unitOfWeight(run):
  if (run):
    userInput = input("Would you want to kg or lbs?: ")

    if (userInput == "kg"):
      weightTeller(True)
    elif (userInput == "lbs"):
      weightTeller(False)
    else:
      print(f"Invalid input of {userInput}")
      unitOfWeight(run)
  else:
    print("Thank you for using our program")

def weightTeller(kg):
  if (kg):
    kgInput = int(input("Input the weight in kgs: "))

    if (math.isnan(kgInput)):
      print('hi')

    print(not isinstance(kgInput, (int, float)))
    if (not isinstance(kgInput, (int, float))):
      print('Does this run?')
      weightTeller(kg)
      return

    kgInput = int(kgInput)

    print(kgInput)
    lbs = round(kgInput * 2.2)
    print(f"The weight of {kgInput}kg is {lbs}lbs")
    toRedo()
  else:
    lbsInput = input("Input the weight in lbs: ")

    if (isinstance(lbsInput, (int, float))):
      weightTeller(kg)

    lbsInput = int(lbsInput)

    kg = round(lbsInput / 2.2)
    print(f"The weight of {lbsInput}lbs is {kg}lbs")
    toRedo()

def toRedo():
  userInput = bool(input("Would you like to redo? (True, False): "))
  unitOfWeight(userInput)

unitOfWeight(True)

