#... python data structures 
'''lists - are ordered, indexed, allow duplicates and mutable '''
fruits = ["apple", "oranges", "banana", "cherry"]
print(fruits[1]) #output: oranges
fruits.append("grapes") #output: adds "grapes" to the end of the list
print(fruits)


'''tuples - are ordered, indexed, allow duplicates & immutable'''
my_tuple = ("wine", "soda", "milk")
print(my_tuple[1]) #output: soda


'''sets - unordered, unindexed, no duplicates'''
my_set = { "infinix", "iphone", "samsung"}
print("Samsung" in my_set) #output: False - note the case sensitivity


'''dictionaries - unordered, mutable, no duplicates and indexed, key:value pair'''
my_dict = {
  "name" : "kendo",
  "number": 8,
  "position" : "midfieled",
  "injured": False
}


### python functions

def greet(*usernames):
  return usernames

print(greet("Nani", " John", " Mike"))


# lambda functions
double = lambda x: x * 2
print(double(4)) #output: 8


# list comprehension
squares = [x**2 for x in range(10)]

# generator expression
sum_of_squares = sum(x**2 for x in range(10))


# error handling
x = "app is good"
try:
  print(x)
except NameError:
  print("variable is not defined")
except: 
  print("something else went wrong")
finally:
  print("Did u like the app?")



import unittest

class TestSum(unittest.TestCase):
  def test_sum(self):
    self.assertEqual(sum([1,2,3]), 6, "Should be 6")

    if __name__ == '__main__':
      unittest.main()


