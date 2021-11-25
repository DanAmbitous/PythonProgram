from random import randint

numValues = []

while len(numValues) < 5:
  numValues.append(randint(0, 10))

# numValues.sort()

# print(numValues, numValues[-1])

# biggestNumber = max(numValues)

# print(numValues, biggestNumber)

def maxFinder(list):
  max = list[0]

  for i in list:
    if (i > max):
      max = i
  
  return max

print(maxFinder(numValues))