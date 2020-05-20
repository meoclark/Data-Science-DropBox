single_digits = [0,1,2,3,4,5,6,7,8,9]
squares = []
for i in single_digits:
  squares.append(i**2)
  print(i)
  print(squares)
cubes = [a**3 for a in single_digits]
print(cubes)