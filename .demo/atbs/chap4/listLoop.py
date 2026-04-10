# random_list = [1,3,4,5,2,6,"kenny", True, 8.4]

# for i in random_list:
#   print(i)


supplies = ["mouse", "flash", "headphones", "keyboard"]

for i in range(len(supplies)):
  print(f"At index {str(i)} we have {supplies[i]}")


# let's try the multiple assignment trick
ages = [40, 33, 26]

#the variables must be the exact same number as the intial list
# having x>3 or x<3 will result in a ValueError
john, phil, marc = ages

print(f"John's age is {john}")

animals = ['sheep', 'cats', 'dogs', 'badgers', 'elephants', "Baboons"]

animals.sort(reverse=False) #sort uses ASCIIbetical order rather than regular alphabetical order

letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)


