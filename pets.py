pets = ['dog', 'cat', 'bird', 'goldfish', 'dog', 'cat',]
print(pets)

 # Remove multiple instance of item in a list
while 'cat' in pets:
    pets.remove('cat')

print(pets)

# function using positional arguments
def describe_pet(breed, name):
    print(f'My pet is a breed of {breed}')
    print(f'His name is {name}')

describe_pet('hamster','harry')
describe_pet('dog' , 'nellie')

print('\n******************\n')

# function using keyword arguments

# **When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don’t have default values. This allows Python to
# continue interpreting positional arguments correctly. **
def describe_pet_keyword(breed, name  = 'hammysir'):
    print(f'My pet is a {breed}')
    print(f'its name is {name}')

describe_pet_keyword('hamster')
