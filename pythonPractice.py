class Options:
  def __init__(self, toStart, toStop, toHelp, toQuit):
      self.toStart = toStart,
      self.toStop = toStop,
      self.toHelp = toHelp,
      self.toQuit = toQuit,

cmds = Options('start', 'stop', 'help', 'quit')
print(cmds.toStart)
status = cmds.toStop

print(cmds)

def gameInit(): 
  print(f"""The car's current status is {status}""")

  userAction = input('> ')

  if (userAction == 'stop'):
    userAction = cmds.toStop
  elif (userAction == 'start'):
    userAction = cmds.toStart
  elif (userAction == 'help'):
    userAction = cmds.toHelp
  elif (userAction == 'quit'):
    userAction = cmds.toQuit

  if (status and userAction == cmds.toStop):
    print(""" Car's already stopped """)
  elif (status and userAction == cmds.toStart):
    print(""" Car's already started """)
  elif (status and userAction == cmds.toStop):
    print(""" Car's halted """)
  elif (status and userAction == cmds.toStart):
    print(""" Car's started """)
  else: 
    print(status, userAction)

  if (userAction == cmds.toHelp):
    print('help')
  elif (userAction == cmds.toQuit):
    print('quit')

gameInit()