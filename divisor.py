import sys

number = int(sys.argv[1])

for i in range(1, 101):
  if number % i == 0:
    print(i, end= " ")

print()
