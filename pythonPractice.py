emojiMapping = {
  ':)': '😊',
  ':(': '😔',
  ':))': '😁',
  ':D': '😀',
  '<B': '❤️',
  '^': '💪'
}

def emoijGiver():
  userInput = input('Input your emotional state (or type in help): ') 

  if (userInput == 'help'):
    print(""" 
      ':)': '😊',
      ':(': '😔',
      ':))': '😁',
      ':D': '😀',
      '<B': '❤️',
      '^': '💪'
    """)
    emoijGiver()

  if (emojiMapping[userInput]):
    print(f"I'm {emojiMapping[userInput]}")

    reDo = input('Would you like to rerun the program (y/n)? ')

    if (reDo == 'y'):
      emoijGiver()
    elif (reDo == 'n'):
      return
    else:
      emoijGiver()
  else:
    print("Unknown input")
    emoijGiver()


emoijGiver()