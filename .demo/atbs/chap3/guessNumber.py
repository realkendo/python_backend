# this is a random secret_number guessing game
import random

secret_number = random.randint(1,20)


print("Welcome to my number guessing game...")

def replay_function():
  while True:
    try : 
      replay = input("Would you like to play the game again? Y/N: \n").strip().upper()

      if replay == "Y":
        return True
      elif replay == "N":
        print("Game exited successfully... Thanks for playing")
        return False
    except ValueError:
      print("Invalid Input: Please type 'Y' or 'N' ")
      continue

while True:
  for guesses in range(6,0,-1):
    print(f"You have a total of {guesses} guesses")
    try:
      guess = int(input("Pick a number from 1-20: "))
    
      if guess < secret_number:
        print("Your guess is low")
      elif guess > secret_number:
        print("your guess is high")
      else:
        print("Correct!!!")
        break
    except ValueError:
      print("Invalid input: only integers are allowed \n")
      continue

  if secret_number == guess:
    print("You won this round")
  else:
    print("Game Over!!!")
    print(f"The number i was thinking of was {secret_number}")

  if not replay_function():
    break
  

