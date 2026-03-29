import random, sys

for num in range(5):
  print(random.randint(1,10))


while True:
  print("Type 'exit' to quit this program ")
  response = input()

  if response.lower() == 'exit':
    sys.exit()
  print(f"You typed {response}")