code = [1, 1, 1, 5]
# shape = 'خ'
# o = 0

# # Method 1
for x in code:
  output = ''
  for i in range(x):
    if (x == 1):
      output += '|'
    else:
      output += '_'
  print(output)


# # Method 2
for i in code:
  print('x' * i)

# # Method 1
for i in range(code[o] + 1):
  if (i == code[o]):
    print(shape * i)
    o += 1
    for ii in range(code[o] + 1):
      if (ii == code[o]):
        print(shape * ii) 
        o += 1
        for iii in range(code[o] + 1):
          if (iii == code[o]):
            print(shape * iii) 
            o += 1
            for iv in range(code[o] + 1):
              if (iv == code[o]):
                print(shape * iv)   
                o += 1
                for v in range(code[o] + 1):
                  if (v == code[o]):
                    print(shape * v) 
                    o += 1
          