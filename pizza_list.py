#list in a dict

pizza = {
    'crust' : 'thick',
    'toppings': ['cheese', 'pepperoni'],
}

print(f"You ordered a {pizza['crust']} crust with" , end=" ")

for topping in pizza['toppings']:
    print(f"1x {topping}" , end=" ")