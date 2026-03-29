'''
this is a program to find the sum of the first 100 numbers 
'''
# funtion to find the sum of numbers from 1-100
def sum_of_first_100_numbers_v1(): 
  '''
  this is a basic solution that uses a for loop to solve the problem
  '''
  total = 0

  for num in range(101):
    total += num
  print(total)


'''
Young Gauss figured out that there were 50 pairs of numbers that added 
up to 100: 1 + 99, 2 + 98, 3 + 97, and so on, until 49 + 51. Since 50 × 100 is 
5,000, when you add that middle 50, the sum of all the numbers from 0 to 
100 is 5,050.
'''
