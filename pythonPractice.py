numbers = [5, 10, 5, 12, 1, 23]
uniqueNumbers = []

for number in numbers:
  if (number not in uniqueNumbers):
    uniqueNumbers.append(number)

print(uniqueNumbers)