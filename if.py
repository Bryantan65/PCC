pizza = ['mushrooms', 'cheese']

# if 'cheese' in pizza:
  #  print("cheese added")
# if 'mushrooms' in pizza:
  #  print('mushroom added')

for ingredients in pizza:
    print(f'Your {ingredients} has been added')

emptylist = []

# If list is empty, python will evaluate as False
# this If statement runs if True
if emptylist:
    print("list is running!!")
else:
    print("ARE U SURE U WANT AN EMPTY PIZZA??!!")