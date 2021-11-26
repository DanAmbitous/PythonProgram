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
  else:
    print("Unknown input")
    emoijGiver()


emoijGiver()