class UnitType:
  def __init__(self, name, inputName):
      self.name = name
      self.inputName = inputName

KG = UnitType('kilograms', '1')
LBS = UnitType('pounds', '0')

def strIntConversion(strInput):
  try:
    return int(strInput)
  except:
    pass


def weightUnitPickining(initialRun):
  if (initialRun):
    print(f"Welcome to {KG.name} and {LBS.name} converter program!")

  weightUnit = input(f"Would you like to convert from {KG.name}(1) or {LBS.name}(0)?: ")

  if (weightUnit == KG.inputName or LBS.inputName):
    weightConverter(weightUnit)
  else: 
    print('Your input is invalid')

def weightConverter(weight):
  if (weight == "1"):
    print(f"You've chosen to convert from {KG.name} to {LBS.name}")
  
    while True:
      try:
        fromKg = int(input(f"Input the {KG.name} you'd like to convert from: "))
        print(f"{fromKg} {KG.name} is {round(fromKg*2.2)} {LBS.name}")
        redo()
        break
      except:
        print('Invalid input')
        pass
  else:
    print(f"You've chosen to convert from {LBS.name} to {KG.name}")
  
    while True:
      try:
        fromLBS = int(input(f"Input the {LBS.name} you'd like to convert from: "))
        print(f"{fromLBS} {LBS.name} is {round(fromLBS/2.2)} {KG.name}")
        redo()
        break
      except:
        print('Invalid input')
        pass

def redo():
  restart = input('Would you like to restart the program? yes(1) no(0): ')

  if (restart == '1'):
    weightUnitPickining(False)
  elif (restart == '0'):
    print('Thanks for using the it, and have a nice day!')
    return
  else:
    print('Invalid input')
    redo()

weightUnitPickining(True)