def unitOfWeight(run):
  print(run)

  if (run):
    userInput = input("Would you want to kg(1) or lbs(0)?: ")

    if (userInput == "1"):
      weightTeller(True)
    elif (userInput == "0"):
      weightTeller(False)
    else:
      print(f"Invalid input of {userInput}")
      unitOfWeight(run)
  else:
    return print("Thank you for using our program")
    

def weightTeller(kg):
  if (kg):
    try:
      kgInput = int(input("Please input kg: "))
      print(f"{kgInput}kg is {round(kgInput * 2.2)}lbs")
    except:
      weightTeller(kg)
  else:

    try:
      lbsInput = int(input("Please input lbs: "))
      print(f"{lbsInput}lbs is {round(lbsInput / 2.2)}kg")
    except:
      weightTeller(kg)
  
  print('hi')
  toRedo()

def toRedo():
  try:
    rerun = input("Would you like to rerun the program? (yes, no): ")

    if (rerun == "yes"):
      unitOfWeight(True)
    elif (rerun == "no"):
      print(rerun, 'a')
      unitOfWeight(False)
    else:
      print("Invalid response")
      toRedo()
  except:
    print('Invalid Input')
    toRedo()

unitOfWeight(True)
