# spam = 0

# while spam < 5:
#   print("Hello, world")
#   spam +=1


# name = ""
# print("WELCOME TO MY CONSOLE PROGRAM: type 'exit'  to close the program at any point ")

# while name != "Ken".lower():
#   print("What is your name? ")
#   name = input()

#   if name == "exit".lower():
#     print("program closed")
#     print("Goodbye dear, user")
#     break
#   elif name == "ken":
#     print(f"Goodbye dear, {name}")

# function to rerun program or exit based on the user's preference 
def program_rerun_function():
  while True:
    choice = input("Would you like to recheck for another user? type 'Y' for yes & 'N' for no:  ").strip().upper()
    if choice == "N":
      print("Program exited successfully")
      return False  #setting loop condition to false so it doesn't rerun
    elif choice.upper() == "Y":
      return True #setting loop condition to rerun
    else:
      print("invalid response, type either 'Y' or 'N' ")


# function definition for checking if a user is underage
def check_age():
    # reload = True
    while True:

      # ask the user's age
      age_input = input("What is your age? _")

      try:
        age = int(age_input)
      except ValueError:
          print("INVALID INPUT : Please enter integers only \n")
          continue

      if age < 18:
        print("Access denied, user is underage") #deny access if underage
      else:
        print("Access granted") #grant access if eligible
      
      if not program_rerun_function():
        break 

#age checker function call 
check_age()