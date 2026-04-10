'''
this file illustrates global and local variable scopes 
'''

def spam():
  eggs = 'spam local'
  print(eggs) #prints spam local

def bacon():
  eggs = 'bacon local'
  print(eggs) #prints bacon local
  spam()
  print(eggs)
  
eggs = 'global'
bacon()
print(eggs)




def tea():
  global milk
  # milk = 'local peak'
  print(milk)

milk = "global peak"
# print(milk)
tea()


