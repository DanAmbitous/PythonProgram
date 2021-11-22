class UnitType:
  def __init__(self, name, inputName):
      self.name = name
      self.inputName = inputName

KG = UnitType('kilograms', '1')
LBS = UnitType('pounds', '0')

def weightUnitPickining():
  print(f"Welcome to {KG.name} to {LBS.name} converter program!")

  weightUnit = input(f"Would you like to convert from {KG.name}(1) or {LBS.name}(0)?: ")

  if (weightUnit == KG.inputName or LBS.inputName):
    weightConverter(weightUnit)
  else: 
    print('Your input is invalid')

def weightConverter(weight):
  print(weight)

  redo()

def redo():
  restart = input('Would you like to restart the program? yes(1) no(0): ')

  if (restart == '1'):
    weightUnitPickining()
  elif (restart == '0'):
    print('Thanks for using the it, and have a nice day!')
  else:
    print('Invalid input')
    redo()

weightUnitPickining()