def spam(divideBy):
  try:
    return 42 // divideBy
  except ZeroDivisionError:
    print("Error: Invalid Arguement")

print(spam(0))