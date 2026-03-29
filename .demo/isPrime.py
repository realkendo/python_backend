input_number = input("Please type the number to check: ")

num = int(input_number)


# fizzbuzz algorithm
def fizzBuzz():
  if num % 3 == 0 and num % 5 == 0:
    print("Fizzbuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("buzz")
  else: 
    print(num)

# logic for checking even and odd numbers
def isEven():
  if num > 1:
    if num == 3 or num == 2:
      print(f'{num} is a prime number')
    else:
      for i in range(2, num):
        if num % i == 0 :
          print(f'{num} is not a prime number')
          break
        else:
          print(f'{num} is a prime number')
        break
  else:
    print("only positive integers greater than 1 are valid inputs")


def isPrime():
    
  replay = True
  
  while replay:
    isEven()
    response = input("Would you like to continue? \n Type Y for 'Yes' and N for 'No': ")
    if response.upper() == 'YES':
      continue
    elif response.upper() == 'N':
      print("Program exited sucessfully")
      replay = False

isPrime()


