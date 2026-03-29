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


# function definition for checking if a user is underage
def checkAge():
    reload = True
    while reload:

      # ask the user's age
      askAge = input("What is your age? _")
      if int(askAge) < 18:
        print("Access denied, user is underage") #deny access if underage
      else:
        print("Access granted") #grant access if eligible
      
      # logic to rerun program or exit based on the user's preference 
      recheckForAnotherUser = input("Would you like to recheck for another user? type 'Y' for yes & 'N' for no _ ")
      if recheckForAnotherUser.upper() == "N":
        #setting loop condition to false so it doesn't rerun
        reload = False 
        print("Program exited successfully")
        break
      elif recheckForAnotherUser.upper() == "Y":
        reload = True #setting loop condition to rerun
      else:
        reload = True #setting loop condition to rerun
        print("invalid response")

#age checker function call 
checkAge()
    




