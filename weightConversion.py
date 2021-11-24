cmds = 'start stop quit help'
cmds = cmds.split(' ')



def commandRunning():
  carStatus = 'stop'

  while True:
    userCmd = input('> ')
    
    match userCmd:
      case 'start':
        if (carStatus == 'stop'):
          print('Starting the car')
          carStatus = 'start'
        else:
          print('Car is already running')
      case 'stop':
        if (carStatus == 'start'):
          print('Stopping the car')
          carStatus = 'stop'
        else:
          print('Car is already stopped')
      case 'quit':
        print('Thanks for playing')
        playAgain(False)
        return
      case 'help':
        print('The commands are start, stop, help, and quit')
      case _:
        print('Did not understand the command')

def playAgain(remessage):
  if (remessage):
    print('Did not understand')

  toReplay = input('Would you like to replay? (y/n): ')
  print(toReplay)
  match toReplay:
    case 'y':
      commandRunning()
    case 'n':
      return
    case _:
      playAgain(True)

commandRunning()
