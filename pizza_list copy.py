pizzas = ['pepperoni' , '4-cheese', 'spicy']

friends_pizzas = pizzas[:]

pizzas.append('clam')

friends_pizzas.append('pineapple')

#both variables can be the same because the variable pizza is declared and run one at a time?

for pizza in pizzas:
    print(f"My fav pizzas are {pizza}")

for pizza in friends_pizzas:
    print(f"My friends fav pizzas are {pizza}")
