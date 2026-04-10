while True:
  try:
    result = int(input("Enter the number: "))
    def collatz(number):
      global result
      
      if number % 2 == 0:
        result = number // 2
        return result
      else:
        result = 3 * number + 1
        return result 

    while result != 1:
      print(collatz(result))
    break

  except ValueError:
    print("INVALID INPUT")
    continue 


